# Engineering models and supporting evidence

This directory contains the original report/manuscript, presentation, engineering source/results, all **eight native/STEP/BOM states**, and the **60-member raw conductor/structural solver supplement** as two exact byte parts. [Core coverage](CORE_COVERAGE.json) inventories all 258 published engineering files (249 exact copies and 9 local portability adapters with their original bytes preserved). [Build and reproduction](REPRODUCE.md), [chapter/figure map](ACADEMIC_MAP.md), [current file identities](MANIFEST.sha256), [CAD inventory](cad/release/FINAL_CAD_MANIFEST.json) and [raw archive identities](SUPPLEMENT_ASSETS.json) identify each role.

Verify local source, data, documents and archive members from the repository root:

```bash
python3 tools/check_acr1.py
```

Restore the raw solver files into a separate scratch directory:

```bash
python3 current/supplements/materialize.py --output /tmp/volley-academic-raw
```

The standard-library materializer verifies both parts, the combined ZIP and every decompressed member before writing. It refuses unsafe paths and nonmatching existing output. Each archive part is below 30 MB. The frozen source record retains its upstream `extract_to` label; this local command uses the explicit scratch output and does not depend on that upstream filesystem path.

[Current academic sources](academic/README.md) identify the citation-corrected files and preserve the original issue. Source/solver evidence is project-created material under the [repository license](../LICENSING.md). Supplier PDFs and full-text extracts are excluded. Independent tool installation and actual solver reruns remain separate from captured-data verification; no hardware or flight qualification is implied.
