"""Check the fixed report issue, editable content and retained evidence boundary."""
from pathlib import Path
import hashlib,json,re,zipfile,xml.etree.ElementTree as E
R=Path(__file__).resolve().parents[1];U=R/'university'
d=json.loads((U/'REPORT_ISSUE.json').read_text())
assert d['issue']=='first_similarity_review_2026_10_23'
assert d['guide_approval'] is False and d['similarity_result'] is None
for rel,expected in d['files'].items():assert hashlib.sha256((R/rel).read_bytes()).hexdigest()==expected,rel
s=(U/'GEN5_FINAL_YEAR_REPORT.md').read_text();body=s.split('\\appendix',1)
main=re.findall(r'^# (.+)$',body[0],re.M);assert len([v for v in main if '{.unnumbered' not in v])==11
assert len(re.findall(r'^# (?!Bibliography)',body[1],re.M))==3
for term in ['16.029','12.448','10.547','11 mm','No physical prototype','APPENDIX']:
 if term=='APPENDIX':continue
 assert term.lower() in s.lower(),term
for bad in ['JAYESH','RAJPATHAK','BHAWALE','ALDALALI','HELMET','GUIDE_DECISION_REQUEST','BOLLEY']:
 assert bad not in s.upper(),bad
with zipfile.ZipFile(U/'GEN5_FINAL_YEAR_REPORT.docx') as z:
 assert z.testzip() is None
 x=z.read('word/document.xml');root=E.fromstring(x);ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
 text=' '.join(root.itertext());assert 'Unsigned review issue' in text
 assert 'CHAPTER XI' in text and 'APPENDIX C' in text
 assert x.count(b'SEQ Figure')==d['figure_count'] and x.count(b'SEQ Table')==d['table_count']
 rels=E.fromstring(z.read('word/_rels/document.xml.rels'));ids={r.get('Id') for r in rels}
 assert all(el.get('{'+ns['r']+'}embed') in ids for el in root.iter() if el.get('{'+ns['r']+'}embed'))
 assert x.count(b'<m:oMath>')>=10
pdf=(U/'GEN5_FINAL_YEAR_REPORT.pdf').read_bytes();assert pdf.startswith(b'%PDF-') and b'%%EOF' in pdf[-2048:]
# Distinguish a pointwise field ratio from a winding-integral reduction.
assert abs(.4759/.5041-.9441)<.00005
assert abs((.5041/.4759-1)*100-5.9256)<.001
assert abs(854/(6.29*385)-.3527)<.0001
print('PASS: fixed blackbook PDF/DOCX/source identities,11chapters/3appendices,native captions/math/images and unsigned first-check boundary. No similarity result or approval asserted.')
