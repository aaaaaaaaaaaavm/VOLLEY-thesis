# Build and reproduce the academic package

Run commands from the repository root. Python 3.12 is the reference interpreter. The selected numerical environment is pinned in [requirements-numerical.txt](requirements-numerical.txt); the document environment is pinned in [requirements-documents.txt](requirements-documents.txt).

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r current/requirements-numerical.txt
.venv/bin/python tools/reproduce_example.py
python3 tools/check_acr1.py
```

The example runs the actual command/proof state model (24 nominal commands and 166 declared checks), recomputes feeder sizing, and reproduces the nominal 3 m/s, 20 µH coupled shot against the captured source result. It uses a temporary package copy so the distributed outputs stay intact. The shot includes the source limit, finite force table, measured-in-model departure event, host recoil and active arrest. No private checkout, cloud path or native solver is needed for these examples.

To rebuild the report PDF and editable DOCX, install Pandoc 3.1.3 or later, TeX Live 2022 or later with XeLaTeX, and the document requirements. The packaged PDF uses Liberation Serif; the DOCX requests Times New Roman and editable Word fields. Font substitution and tool versions can change pagination. Rebuild in a copy when comparing to the distributed ED1 outputs or archived originals.

```bash
.venv/bin/python -m pip install -r current/requirements-documents.txt
.venv/bin/python current/academic/build_report.py
bash current/academic/paper/build.sh
.venv/bin/python current/presentation/build_presentation.py
```

The paper builder runs pdfLaTeX twice and uses the bundled unmodified IEEEtran 1.8b class. The presentation builder creates the editable 17-slide PPTX and notes from local data/assets; PDF conversion needs LibreOffice Impress or PowerPoint. The checked download PDF is bundled. A rebuilt output is a new local build. Current ED1 outputs have their own recorded identities; original sent-version bytes remain in the [dated archive](../archive/2026-10-24-acr1-original/README.md).

For more numerical work, sources and required inputs are under [analysis](analysis/), [cad](cad/) and [mission](mission/). `analysis/coupled_shot.py` recomputes the full sampled shot set; `verification/review_coupled_shot.py` performs the six-case refined timestep audit. `mission/mission_model.py` generates the matched campaign; its raw commands/results are already bundled. The optional independent Java replay uses Java 21, Orekit 13.1.6 and Hipparchus 4.0.3: obtain exact JARs from the URLs in [SOFTWARE_LOCK.json](mission/SOFTWARE_LOCK.json), verify their hashes, place them under `current/mission/jars/`, then run `python current/mission/native_checks.py`. No JARs are redistributed.

Native CAD/mesh/elastic/current-density regeneration needs the corresponding FreeCAD/Gmsh/CalculiX environment and raw geometry. [Software capture](sources/SOFTWARE_ENVIRONMENT.json), [home native/STEP](cad/release/) and [full asset inventory](cad/release/FINAL_CAD_MANIFEST.json) pin these tools and inputs. Large remaining raw assets are linked from the [main engineering package](https://github.com/aaaaaaaaaaaavm/VOLLEY/tree/main/validation/acr1). Native and FE regeneration is distinct from the locally verified examples and document builds; this receipt does not claim those solvers were rerun here.

Optional lift-sizing regeneration also requires the catalog text extraction `sources/faulhaber_ratios.txt`; retrieve the cited FAULHABER reduction-ratio catalog, extract its text and verify the captured text identity in `sources/EXTERNAL_TEXT_IDENTITIES.json`. This historical hash input is not needed for the selected examples.

Supplier PDFs and full text extractions are not redistributed because no express redistribution permission was established. Their authoritative URLs, source hashes and catalog reference values are in the [source register](sources/README.md). They are not needed by the selected examples or document build.
