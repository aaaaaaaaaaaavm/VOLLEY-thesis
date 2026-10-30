"""Verify the final academic reading copies and standalone report source archive."""
from pathlib import Path
from zipfile import ZipFile
import hashlib, json, re, subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / 'editions/final-2026-10'
record = json.loads((EDITION/'MANIFEST.json').read_text())
assert record['report_pages'] == 64 and record['presentation_slides'] == 31
assert record['authors'] == ['Adityavardhan Mishra', 'Pratham Chawla']
for item in record['files']:
    p = EDITION/item['path']
    assert p.parent == EDITION and p.is_file()
    raw = p.read_bytes()
    assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'], str(p)
for item in record['associated_artifacts']:
    p = ROOT/item['path']
    raw = p.read_bytes()
    assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'], str(p)
for p, count in [(EDITION/'VOLLEY_Blackbook.pdf',64),(ROOT/'editions/presentation-2026-10/VOLLEY_Presentation.pdf',31)]:
    info = subprocess.check_output(['pdfinfo',str(p)],text=True)
    assert int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1)) == count
with ZipFile(EDITION/'VOLLEY_Blackbook.docx') as z:
    assert z.testzip() is None
    document = ET.fromstring(z.read('word/document.xml'))
    ns = {'m':'http://schemas.openxmlformats.org/officeDocument/2006/math','w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    assert len(document.findall('.//m:oMath',ns)) == 52
    assert len(document.findall('.//w:tbl',ns)) == 15
    core = z.read('docProps/core.xml').decode()
    assert 'Adityavardhan Mishra' in core and 'Pratham Chawla' in core
with ZipFile(EDITION/'VOLLEY_Blackbook_Sources.zip') as z:
    assert z.testzip() is None
    names = set(z.namelist())
    assert all(not n.startswith('/') and '..' not in Path(n).parts for n in names)
    inputs = json.loads(z.read('SOURCE_MANIFEST.json'))
    assert names == {x['path'] for x in inputs['files']} | {'SOURCE_MANIFEST.json'}
    assert {'README.md','LICENSE','requirements-documents.txt','cache_docx_indexes.py','current/academic/build_report.py','current/academic/GEN5_FINAL_YEAR_REPORT.md'} <= names
    for item in inputs['files']:
        raw = z.read(item['path'])
        assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'], item['path']
    forbidden = ('EMAIL_', 'AUTHOR_REMAINING_WORK', 'APPROVED_PRATHAM', 'MERGE_DECISIONS', 'FLAGGED_PASSAGE', 'BEFORE_', 'EVT-')
    assert not any(any(marker in n for marker in forbidden) for n in names)
    for name in names:
        if Path(name).suffix in {'.py','.md','.tex','.lua','.json'}:
            assert b'/workspace/' not in z.read(name), name
for line in (ROOT/'ARTIFACT_MANIFEST.sha256').read_text().splitlines():
    digest, name = line.split('  ',1)
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest() == digest, name
print('PASS: final 64-page blackbook, both authors, 52 native equations, 15 tables, exact 31-slide presentation, standalone source inputs and repository hashes')
