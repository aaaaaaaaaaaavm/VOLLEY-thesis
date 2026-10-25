# Academic reading and evidence map

The [report source](academic/GEN5_FINAL_YEAR_REPORT.md) contains eleven chapters and three appendices. The [paper source](academic/paper/paper.tex) presents the same selected configuration in IEEE format.

| Report chapters / paper theme | Local method and evidence |
|---|---|
| 1–3: problem, objectives, literature | [Closest full-text review](academic/evidence/literature/FEEDER_FULL_TEXT_REVIEW_2026_10_19.md), [source/DOI identities](academic/evidence/literature/FEEDER_FULL_TEXT_SOURCES.json) and document bibliographies |
| 4–5: governing models and controlled configuration | [Engineering definition](academic/evidence/ENGINEERING_DEFINITION_R1.json), [parameters](cad/PARAMETERS.json), [CAD inventory](cad/release/FINAL_CAD_MANIFEST.json) |
| 6: electromagnetic drive, source and controls | [Analysis sources/results](analysis/), [shot audit](verification/COUPLED_SHOT_REVIEW.json), [supplier source register](sources/README.md) |
| 7: CAD, packaging, mass | [Home native/STEP/BOM](cad/release/), [mass/CG/inertia](verification/MASS_CG_INERTIA_SUMMARY.json) |
| 8: matched orbital delivery | [Mission model](mission/mission_model.py), [targets](mission/TARGETS.json), [raw commands and event histories](mission/release/), [native replay outputs](mission/native/), [comparison table](mission/MISSION_RESULTS.csv) |
| 9–11: results, resources, conclusion | [Supported result summary](RESULTS.md), [manuscript](academic/paper/paper.pdf), [reproduction](REPRODUCE.md) |
| Appendices A–C: evidence, history, Gen6 | [Local evidence](academic/evidence/), [dated archive](../archive/README.md); mixed-size and high-speed cases retain separate configuration identities |

| Figure group | Bundled figures and source |
|---|---|
| Assembly, pallet handoff, captured/source and docked states | [Academic assets](academic/assets/); native-geometry renders, with [asset hashes](academic/ASSET_MAP.json) |
| Custody / operating cycle | [Cycle SVG](academic/assets/operating_cycle.svg), [editable drawing script](academic/draw_operating_cycle.py) |
| Force coefficient and magnetic gap | [Finite motor](analysis/finite_motor.py), [figure assets](academic/assets/) |
| Coupled shot and energy ledger | [Shot source](analysis/coupled_shot.py), [numerical output](analysis/COUPLED_SHOT.json) |
| Actual chassis deformation/stress | [Figure source record](academic/evidence/verification/chassis_fea/d4b53d520c1bc0d3_h8/ACTUAL_CHASSIS_FIGURE.json) |
| Mission resources and targets | [Plot source](mission/report_and_plot.py), [raw case data](mission/release/) |

[Evidence hashes](academic/EVIDENCE_MAP.json) identify local captures. [Package manifest](MANIFEST.sha256) identifies every current distributed source/result/output. The frozen document manifest preserves the original build identities; [ED1 revision records](academic/EDITORIAL_REVISION.json) identify the current citation-corrected derivative and its preserved original. The package includes the home native/STEP geometry; all eight native/STEP states and large raw solver outputs are catalogued by the final CAD manifest and the [main engineering package](https://github.com/aaaaaaaaaaaavm/VOLLEY/tree/main/validation/acr1). They are optional for document and selected numerical reproduction.
