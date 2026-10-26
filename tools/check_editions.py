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
