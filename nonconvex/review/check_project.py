from pathlib import Path
import json,re,hashlib,collections
import yaml

ROOT=Path(__file__).resolve().parents[1]
decls={}; proofs=collections.defaultdict(list); imports={}; files={}; findings=[]
blockpat=re.compile(r'^::: \{([^\n]+)\}\n(.*?)^:::\s*$',re.M|re.S)
refpat=re.compile(r'@((?:def|lem|prp|thm|cor)-[A-Za-z0-9-]+)')
tagpat=re.compile(r'\\tag\{([^}]+)\}')
alltags=collections.defaultdict(list)

for p in sorted(ROOT.rglob('*.qmd')):
    if '.qmd-prover' in p.parts:continue
    s=p.read_text(); files[p]=s
    fm={}
    if s.startswith('---\n'):
        fm=yaml.safe_load(s.split('---',2)[1]) or {}
    im={}
    for x in fm.get('qmd-prover',{}).get('imports',[]):
        for k in x['use']:
            im[k]=(p.parent/x['from']).resolve()
    imports[p]=im
    for attrs,body in blockpat.findall(s):
        a=dict(re.findall(r'([\w-]+)="([^"]*)"',attrs))
        kind=re.findall(r'\.(definition|lemma|proposition|theorem|corollary|proof)\b',attrs)
        if len(kind)!=1:
            findings.append({'kind':'shape','file':str(p.relative_to(ROOT)),'attrs':attrs});continue
        ident=re.search(r'#([\w-]+)',attrs)
        if kind[0]=='proof':
            ident=a.get('of')
            if not ident:findings.append({'kind':'proof_no_target','file':str(p)})
            else:proofs[ident].append({'file':p,'body':body,'attrs':attrs})
        elif ident:
            ident=ident[1]
            if ident in decls:findings.append({'kind':'duplicate_id','id':ident})
            decls[ident]={'file':p,'body':body,'attrs':a,'kind':kind[0]}
            if not a.get('name') or not re.fullmatch(r'\d{4}-\d{2}-\d{2}',a.get('date','')):
                findings.append({'kind':'declaration_metadata','id':ident})
        else:findings.append({'kind':'missing_id','file':str(p)})
    for t in tagpat.findall(s):alltags[t].append(str(p.relative_to(ROOT)))
    for i,b in enumerate(p.read_bytes()):
        if b<32 and b not in [9,10]:findings.append({'kind':'control_character','file':str(p.relative_to(ROOT)),'position':i,'byte':b})

edges={k:set() for k in decls}
for ident,d in decls.items():
    ps=proofs.get(ident,[])
    if d['kind']!='definition' and len(ps)!=1:findings.append({'kind':'proof_count','id':ident,'count':len(ps)})
    if len(ps)>1:findings.append({'kind':'multiple_proofs','id':ident})
    for block in [d]+ps:
        p=block['file']
        for ref in set(refpat.findall(block['body'])):
            if ref not in decls:
                findings.append({'kind':'unresolved_ref','id':ident,'ref':ref});continue
            rd=decls[ref]
            if rd['file']!=p:
                if imports[p].get(ref)!=rd['file']:
                    findings.append({'kind':'missing_import','id':ident,'ref':ref,'file':str(p.relative_to(ROOT))})
                if rd['attrs'].get('export')!=ref:
                    findings.append({'kind':'not_exported','id':ident,'ref':ref})
            edges[ident].add(ref)
for ident in proofs:
    if ident not in decls:findings.append({'kind':'orphan_proof','id':ident})
for p,im in imports.items():
    for ref,fp in im.items():
        if ref not in decls or decls[ref]['file']!=fp:
            findings.append({'kind':'bad_import','file':str(p.relative_to(ROOT)),'ref':ref})

color={k:0 for k in edges}; stack=[]; cycles=[]
def visit(k):
    color[k]=1;stack.append(k)
    for v in sorted(edges[k]):
        if color[v]==0:visit(v)
        elif color[v]==1:cycles.append(stack[stack.index(v):]+[v])
    stack.pop();color[k]=2
for k in sorted(edges):
    if color[k]==0:visit(k)
for c in cycles:findings.append({'kind':'cycle','path':c})

protected=['goals.qmd','.qmd-prover/statement-locks.json','AGENTS.md','.qmd-prover/config.yml']
expected_hashes=json.loads((ROOT/'review/protected-file-sha256.json').read_text())
preserved={s:hashlib.sha256((ROOT/s).read_bytes()).hexdigest()==expected_hashes[s] for s in protected}
for p,good in preserved.items():
    if not good:findings.append({'kind':'protected_file_changed','file':p})

book=yaml.safe_load((ROOT/'_quarto.yml').read_text())['book']['chapters']
missing_chapters=sorted(str(p.relative_to(ROOT)) for p in files if str(p.relative_to(ROOT)) not in book)
for s in missing_chapters:findings.append({'kind':'missing_chapter','file':s})
untranslated=[str(p.relative_to(ROOT)) for p,s in files.items() if p.name!='goals.qmd' and re.search(r'[\u3000-\u303f\u3400-\u9fff\uff00-\uffef]',s)]
for p in untranslated:findings.append({'kind':'untranslated_qmd','file':p})
for p,s in files.items():
    if re.search(r'^::: \{[^\n]*(?:\.assumed|\.draft|status=)',s,re.M):
        findings.append({'kind':'unexpected_workflow_state','file':str(p.relative_to(ROOT))})
counts=collections.Counter(d['kind'] for d in decls.values())
summary={
    'scope':'Custom static source checks only; not qmd-prover, not a mathematical verifier.',
    'official_qmd_prover_run':False,'qmd_files':len(files),'declarations':len(decls),'proof_blocks':sum(map(len,proofs.values())),
    'kinds':dict(counts),'preserved_files':preserved,'findings':findings,
    'duplicate_equation_tags':{t:xs for t,xs in alltags.items() if len(xs)>1},
    'source_bytes_after':sum(p.stat().st_size for p in files),
    'goals_sha256':hashlib.sha256((ROOT/'goals.qmd').read_bytes()).hexdigest(),
    'dependency_edges':{k:sorted(v) for k,v in edges.items()}
}
out=ROOT/'review/source_check.json'
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='dependency_edges'},ensure_ascii=False,indent=2))
