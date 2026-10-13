#!/usr/bin/env python3
"""Verify from a clone with full Git history and OpenSSL installed."""
from pathlib import Path
import hashlib, json, subprocess
here = Path(__file__).resolve().parent
root = here.parent.parent
manifest = json.loads((here / 'manifest.json').read_text())
subprocess.run(['openssl', 'ts', '-verify', '-data', str(here / 'manifest.json'), '-in', str(here / 'response.tsr'), '-CAfile', str(here / 'cacert.pem'), '-untrusted', str(here / 'tsa.crt')], check=True)
subprocess.run(['openssl', 'ts', '-verify', '-queryfile', str(here / 'request.tsq'), '-in', str(here / 'response.tsr'), '-CAfile', str(here / 'cacert.pem'), '-untrusted', str(here / 'tsa.crt')], check=True)
for item in manifest['files']:
    name = item['path']
    if name.startswith('evidence/'):
        data = (root / name).read_bytes()
    else:
        data = subprocess.check_output(['git', 'show', manifest['snapshot_commit'] + ':' + name], cwd=root)
    if len(data) != item['bytes'] or hashlib.sha256(data).hexdigest() != item['sha256']:
        raise SystemExit('FAILED: ' + name)
subprocess.run(['git', 'bundle', 'verify', str(here / 'history.bundle')], cwd=root, check=True)
print('Verified TSA signature, request nonce, all 9 snapshot hashes, and Git bundle.')
