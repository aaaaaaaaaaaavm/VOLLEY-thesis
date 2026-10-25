#!/usr/bin/env python3
"""Verify current ACR1 local identities, numerical claims, links and document containers."""
from pathlib import Path
from zipfile import ZipFile
import hashlib,json,re,sys,subprocess
from urllib.parse import unquote
R=Path(__file__).resolve().parents[1];C=R/'current'
def require(ok,why):
 if not ok:raise SystemExit('FAIL: '+why)
count=0
for line in (C/'MANIFEST.sha256').read_text().splitlines():
 digest,path=line.split('  ',1);p=C/path
 require(p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest,'stale/missing '+path);count+=1
for filename,key in [('ASSET_MAP.json','asset'),('EVIDENCE_MAP.json','local')]:
 for row in json.loads((C/'academic'/filename).read_text()):
  p=C/'academic'/row[key];require(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],'academic map mismatch '+str(p))
fixed={'academic/GEN5_FINAL_YEAR_REPORT.md':'0dbf624af075b4afd1584174d25138f4acffa07a069a41264266c6f94f1d9786','academic/paper/paper.tex':'a045926305baa45f4240b0e9c9a738d2ba9478d3ff2e207af66098ef2d85b824','academic/GEN5_FINAL_YEAR_REPORT.pdf':'67db0ff61a563bd195f84539a64ac4e257c862f4138c18bfd37282e2db4659c3','academic/GEN5_FINAL_YEAR_REPORT.docx':'1da2daeb5f5622841299058ae3512bbe16e5aac2ac4d9b02284aae72a849a353','academic/paper/paper.pdf':'b7dc232dff8ce81bad5cefeadfc59e0ccee41a678b9029356f353054858c2688'}
for p,h in fixed.items():require(hashlib.sha256((R/'archive/2026-10-24-acr1-original'/p).read_bytes()).hexdigest()==h,'archived original academic artifact changed '+p)
for current,heading in [('GEN5_FINAL_YEAR_REPORT.md','# Bibliography'),('paper/paper.tex',r'\begin{thebibliography}')]:
 original=(R/'archive/2026-10-24-acr1-original/academic'/current).read_text();active=(C/'academic'/current).read_text()
 require(active.split(heading)[0]==original.split(heading)[0],'ED1 changed technical source before bibliography '+current)
 require('H. Q. Yamaguchi' not in active and '10.1541/ieejias.143.570' in active and '10.1155/ijae/3000765' in active,'ED1 bibliography corrections missing '+current)
for name in ['academic/GEN5_FINAL_YEAR_REPORT.pdf','academic/paper/paper.pdf','presentation/VOLLEY_BTech_Presentation.pdf']:
 raw=(C/name).read_bytes();require(raw.startswith(b'%PDF-') and b'%%EOF' in raw[-2048:],'PDF container '+name)
with ZipFile(C/'presentation/VOLLEY_BTech_Presentation.pptx') as z:
 require(z.testzip() is None,'PPTX CRC');require(len([n for n in z.namelist() if re.fullmatch(r'ppt/slides/slide\d+.xml',n)])==17,'slide count')
with ZipFile(C/'academic/GEN5_FINAL_YEAR_REPORT.docx') as z:require(z.testzip() is None,'DOCX CRC')
get=lambda p:json.loads((C/p).read_text())
m=get('cad/release/MOTION_VERIFICATION.json');require(m['case_count']==154 and m['failed_case_count']==0 and m['all_sampled_cases_pass'],'motion claims')
cad=get('cad/release/FINAL_CAD_MANIFEST.json');require(len(cad['states'])==8,'native state inventory')
for state in cad['states']:
 for name,item in state['files'].items():
  path=C/'cad/release'/name
  require(path.is_file() and path.stat().st_size==item['bytes'] and hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'],'local native/STEP/BOM identity '+name)
coverage=get('CORE_COVERAGE.json');require(len(coverage['files'])==258,'complete published core coverage')
for item in coverage['files']:
 require(hashlib.sha256((C/item['path']).read_bytes()).hexdigest()==item['sha256'],'core identity '+item['path'])
 if item['role']=='declared_local_portability_adapter':
  require(hashlib.sha256((C/item['preserved_source']).read_bytes()).hexdigest()==item['published_source_sha256'],'preserved core source '+item['path'])
supplement=get('SUPPLEMENT_ASSETS.json');require(len(supplement['files'])==60,'raw solver member inventory')
subprocess.run([sys.executable,str(C/'supplements/materialize.py'),'--verify-only'],check=True)
l=get('analysis/TRANSFER_INTERLOCKS.json');require(l['accepted_nominal_commands']==24 and l['tests']==166 and l['all_passed'],'logic claims')
require(get('verification/COUPLED_SHOT_REVIEW.json')['summary']['all_refined_cases_pass'],'refined shot audit')
require(abs(get('analysis/RESOURCE_LEDGER.json')['CAD_dry_kg']-149.55671970039353)<1e-9,'mass')
require(get('mission/NATIVE_REPLAY_CHECKS.json')['all_declared_numerical_checks_pass'],'native mission capture')
links=0
for p in [R/'README.md',R/'LICENSING.md',R/'archive/README.md',*C.glob('*.md'),C/'academic/README.md',C/'sources/README.md',C/'presentation/README.md']:
 fenced=False
 for line in p.read_text().splitlines():
  if line.lstrip().startswith('```'):fenced=not fenced;continue
  if fenced:continue
  for raw in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',line):
   target=unquote(raw.strip('<>').split('#',1)[0])
   if not target or re.match(r'\w+:|//',target):continue
   q=(p.parent/target).resolve();require(q.is_relative_to(R) and q.exists(),'broken current link '+str(p.relative_to(R))+' '+target);links+=1
source=(C/'academic/paper/paper.tex').read_text()
for name in re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}',source):require((C/'academic/assets'/name).exists(),'missing manuscript figure '+name)
for p in C.rglob('*.py'):
 require('/workspace/' not in p.read_text(),'private runtime path '+str(p.relative_to(R)))
print(f'PASS: {count} current hashes, {links} reader links; ED1 and archived-original sources, 17-slide deck, eight local native/STEP states, 60 raw solver members, current numerical claims and portable runtime paths')
