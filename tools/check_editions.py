#!/usr/bin/env python3
"""Verify versioned academic artifact identities and source containers."""
from pathlib import Path
from zipfile import ZipFile
import hashlib, json

root = Path(__file__).resolve().parents[1]
edition = root / 'editions/ED2'
record = json.loads((edition / 'MANIFEST.json').read_text())
assert (record['report_pages'], record['presentation_slides'], record['presentation_planned_seconds']) == (57, 17, 900)
for item in record['files']:
    path = edition / item['path']
    assert path.parent == edition and path.is_file(), item['path']
    raw = path.read_bytes()
    assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'], item['path']
    if path.suffix == '.pdf':
        assert raw.startswith(b'%PDF-') and b'%%EOF' in raw[-2048:], path.name
    if path.suffix == '.zip':
        with ZipFile(path) as archive:
            assert archive.testzip() is None, path.name
            assert all(not p.startswith('/') and '..' not in Path(p).parts for p in archive.namelist()), path.name
with ZipFile(edition / 'VOLLEY_ED2_Document_Sources.zip') as archive:
    names = set(archive.namelist())
    assert {'README.md', 'BUILD_REFERENCE.json', 'materialize_assets.py', 'ASSET_MAP.json', 'SOURCE_MANIFEST.json', 'cache_docx_indexes.py', 'requirements-documents.txt', 'current/academic/build_report.py', 'current/presentation/build_presentation.py'} <= names
    reference = json.loads(archive.read('BUILD_REFERENCE.json'))
    for name in names:
        if name.endswith(('.py', '.md', '.tex', '.lua')):
            assert b'/workspace/' not in archive.read(name), name
print('PASS: ED2 artifact identities, PDF/ZIP containers, portable sources and 57-page/17-slide route')

new = root / 'editions/ED3'
r = json.loads((new/'MANIFEST.json').read_text())
assert (r['report_pages'],r['presentation_slides'],r['presentation_planned_seconds']) == (58,17,900)
for item in r['files']:
 p = new/item['path'];raw=p.read_bytes()
 assert p.parent==new and len(raw)==item['bytes'] and hashlib.sha256(raw).hexdigest()==item['sha256'],item['path']
 if p.suffix=='.pdf':assert raw.startswith(b'%PDF-') and b'%%EOF' in raw[-2048:]
 if p.suffix=='.zip':
  with ZipFile(p) as z:
   assert z.testzip() is None
   assert all(not n.startswith('/') and '..' not in Path(n).parts for n in z.namelist())
print('PASS: ED3 artifact identities and 58-page/17-slide route')

presentation = root / 'editions/presentation-2026-10'
record = json.loads((presentation / 'MANIFEST.json').read_text())
assert (record['core_slides'], record['technical_appendix_slides'], record['total_slides'], record['planned_seconds']) == (19, 12, 31, 900)
assert sorted(record['speaker_seconds'].values()) == [450, 450]
for item in record['files']:
    path = (presentation / item['path']).resolve()
    assert path.is_relative_to(presentation.resolve()) and path.is_file(), item['path']
    raw = path.read_bytes()
    assert len(raw) == item['bytes'] and hashlib.sha256(raw).hexdigest() == item['sha256'], item['path']
with ZipFile(presentation / 'VOLLEY_Presentation.pptx') as archive:
    import re
    assert archive.testzip() is None
    assert len([name for name in archive.namelist() if re.fullmatch(r'ppt/slides/slide\d+\.xml', name)]) == 31
    assert len([name for name in archive.namelist() if name.startswith('ppt/media/') and name.endswith('.mp4')]) == 2
route = json.loads((presentation / 'ROUTE.json').read_text())
assert route['core_count'] == 19 and route['appendix_count'] == 12 and route['planned_seconds'] == 900
print('PASS: October presentation, 19 core/12 appendix slides, 450+450 seconds, two embedded clips and portable asset identities')
