#!/usr/bin/env node
// qmd-prover protocol adapter. It never changes a verdict or a proof.
import { readFile, mkdir, writeFile, rename } from 'node:fs/promises';
import { existsSync, realpathSync, rmSync } from 'node:fs';
import { homedir } from 'node:os';
import { join, dirname, resolve, delimiter } from 'node:path';
import { execFileSync } from 'node:child_process';
import { pathToFileURL } from 'node:url';
// Set QMD_PROVER_ROOT to the installed package directory if npm -g is not used.
const engineCandidates=[];
try { engineCandidates.push(join(execFileSync('npm',['root','-g'],{encoding:'utf8'}).trim(),'qmd-prover')); } catch {}
for (const directory of (process.env.PATH ?? '').split(delimiter)) {
  const executable=join(directory,'qmd-prover');
  if (existsSync(executable)) engineCandidates.push(resolve(dirname(realpathSync(executable)),'../../..'));
}
const engineRoot=process.env.QMD_PROVER_ROOT || engineCandidates.find(directory=>existsSync(join(directory,'skills/qmd-prover/scripts/verifiers/lib.js')));
if (!engineRoot) throw new Error('Cannot locate qmd-prover. Set QMD_PROVER_ROOT to its installed package directory.');
const engineImport=p=>import(pathToFileURL(join(engineRoot,'skills/qmd-prover/scripts',p)).href);
const {readPacket,buildPrompt,findVerdict}=await engineImport('verifiers/lib.js');
const {verificationKey}=await engineImport('core/verification/protocol.js');
const {stableJson}=await engineImport('core/infrastructure/files.js');

const BASE = 'http://100.95.50.98:8219/v1';
const packet = await readPacket();
const contract = packet.checker_contract;
const model = contract.model;
if (model !== 'gpt-6.1-sol' || contract.effort !== 'xhigh') {
  throw new Error('This project requires the user-selected gpt-6.1-sol / xhigh checker.');
}
if (!model || contract.citations !== 'strict' || contract.rigor !== 'strict' || contract.rigor_disprove !== 'strict') {
  throw new Error('This adapter requires an explicit model and all three strict settings.');
}
if ((contract.tools ?? []).length) throw new Error('This adapter has no tool-execution loop: tools must be empty.');
// Reuse only an actual independent API response to an identical full packet.
// The native engine still validates the verdict and current source freshness.
const preparedPath=join(process.cwd(),'reports/api-prepared',verificationKey(packet)+'.json');
try {
  const prepared=JSON.parse(await readFile(preparedPath,'utf8'));
  if(stableJson(prepared.packet,0)!==stableJson(packet,0))throw new Error('Prepared packet mismatch.');
  process.stdout.write(JSON.stringify(prepared.report));
  process.exit(0);
} catch(error) {
  if(error.code!=='ENOENT')throw error;
}
// Serialize only identical packet requests; unrelated checks remain independent.
await mkdir(dirname(preparedPath), {recursive:true});
const claimPath=preparedPath+'.inflight';
const claimStarted=Date.now();
while (true) {
  try { await mkdir(claimPath); break; }
  catch(error) {
    if(error.code!=='EEXIST')throw error;
    try {
      const prepared=JSON.parse(await readFile(preparedPath,'utf8'));
      if(stableJson(prepared.packet,0)!==stableJson(packet,0))throw new Error('Prepared packet mismatch.');
      process.stdout.write(JSON.stringify(prepared.report));
      process.exit(0);
    } catch(error) { if(error.code!=='ENOENT')throw error; }
    if(Date.now()-claimStarted>910000)throw new Error('Timed out waiting for an identical reviewer request.');
    await new Promise(resolve=>setTimeout(resolve,250));
  }
}
process.on('exit',()=>rmSync(claimPath,{recursive:true,force:true}));
// A previous owner may publish and release its claim between our last read
// and successful mkdir. Recheck only after we own the claim, before any API use.
try {
  const prepared=JSON.parse(await readFile(preparedPath,'utf8'));
  if(stableJson(prepared.packet,0)!==stableJson(packet,0))throw new Error('Prepared packet mismatch.');
  process.stdout.write(JSON.stringify(prepared.report));
  process.exit(0);
} catch(error) {
  if(error.code!=='ENOENT')throw error;
}
const key = (process.env.QMD_PROVER_API_KEY || await readFile(process.env.QMD_PROVER_API_KEY_FILE || join(homedir(), '.config/qmd-prover/cliproxy-8219.key'), 'utf8')).trim();
if (!key) throw new Error('Missing reviewer API key.');
const prompt = buildPrompt(packet);
const root = join(process.cwd(), 'reports/api');
await mkdir(root, {recursive:true});
const id = String(packet.target.id).replace(/[^\w.-]/g, '_');
const stem = join(root, `${id}-${Date.now()}`);
await writeFile(stem+'.packet.json', JSON.stringify(packet,null,2));
await writeFile(stem+'.prompt.txt', prompt);
const payload = {
  model,
  service_tier:'fast',
  input: [{role:'user',content:prompt}],
  reasoning:{effort:contract.effort},
  max_output_tokens:24000,
  stream:true,
  store:false,
};
const started = Date.now();
// A long request runs asynchronously under qmd-prover; the author can inspect progress.
const response = await fetch(BASE+'/responses', {
  method:'POST',
  headers:{Authorization:'Bearer '+key, 'Content-Type':'application/json'},
  body:JSON.stringify(payload),
  signal:AbortSignal.timeout(900000),
  redirect:'error',
});
if (!response.ok) {
  const error=(await response.text()).replaceAll(key,'[redacted]');
  throw new Error(`8219 HTTP ${response.status}: ${error.slice(0,2000)}`);
}
let pending='', text='', completed=null;
const events=[];
function consume(line) {
  if (!line.startsWith('data:')) return;
  const raw=line.slice(5).trim();
  if (!raw || raw==='[DONE]') return;
  const event=JSON.parse(raw);events.push(event);
  if (event.type==='response.output_text.delta') text+=event.delta??'';
  if (event.type==='response.completed') completed=event.response;
  if (event.type==='response.failed' || event.type==='error') throw new Error(JSON.stringify(event).replaceAll(key,'[redacted]'));
}
const decoder=new TextDecoder();
for await (const chunk of response.body) {
  pending+=decoder.decode(chunk,{stream:true});
  let end;
  while ((end=pending.indexOf('\n'))>=0) {
    const line=pending.slice(0,end).replace(/\r$/,'');
    pending=pending.slice(end+1);consume(line);
  }
}
pending+=decoder.decode();if(pending.trim())consume(pending.trim());
await writeFile(stem+'.response.json', JSON.stringify({endpoint:BASE,requested_model:model,requested_service_tier:payload.service_tier,actual_service_tier:completed?.service_tier??null,elapsed_ms:Date.now()-started,events},null,2));
if (!completed || completed.status!=='completed') throw new Error('No completed API response; no verdict is accepted.');
if (completed.model!==model || completed.reasoning?.effort!==contract.effort) {
  throw new Error('API returned a different model or reasoning effort; no verdict is accepted.');
}
if (!text) text=(completed.output??[]).flatMap(i=>i.content??[]).filter(c=>c.type==='output_text').map(c=>c.text).join('');
await writeFile(stem+'.output.txt',text);
const {verdict,malformed}=findVerdict(text);
if (!verdict) throw new Error('No parseable verdict: '+(malformed?.error??'missing object'));
// Pass the model's entire verdict to the engine for schema and strictness validation.
const emitted={...verdict,usage:completed.usage};
await writeFile(stem+'.verdict.json',JSON.stringify(emitted,null,2));
const preparedTemporary=preparedPath+'.'+process.pid+'.tmp';
await writeFile(preparedTemporary,JSON.stringify({packet,report:emitted,received_at:new Date().toISOString()},null,2));
await rename(preparedTemporary,preparedPath);
process.stdout.write(JSON.stringify(emitted));
