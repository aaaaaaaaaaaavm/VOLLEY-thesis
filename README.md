# VOLLEY academic report

**VOLLEY: Design and Computational Evaluation of a Commanded Electromagnetic CubeSat Deployment Mechanism**

Adityavardhan Mishra and Pratham Chawla · Mechanical Engineering, Symbiosis Institute of Technology, Pune · Gen5 ACR1, 24 October 2026

VOLLEY stores twelve 4 kg 3U payload surrogates in two fixed banks and feeds a captive pallet onto a reusable magnetic carrier. A finite linear synchronous motor commands release in the studied **1–3 m/s** range, then arrests and returns the carrier and pallet. This repository presents the completed computational design study and its reproducible academic record.

<p><a href="current/academic/assets/01_assembly_isometric.png"><img src="current/academic/assets/01_assembly_isometric.png" alt="ACR1 native-CAD-derived assembly view: two six-level storage banks, central indexed lift and reusable carrier track" width="680"></a></p>

*CAD-derived Blender view · ACR1 home state · all 387 native objects present. [Native/STEP source](current/cad/release/) · [current visual provenance](docs/ACR1_VISUALS.json).*

Start with the 55-page report, its editable source and the chapter evidence map.

| Academic artifact | Download and source |
|---|---|
| Report · 55 pages | [PDF](current/academic/GEN5_FINAL_YEAR_REPORT.pdf) · [DOCX](current/academic/GEN5_FINAL_YEAR_REPORT.docx) · [Markdown](current/academic/GEN5_FINAL_YEAR_REPORT.md) |
| Manuscript · 9 pages | [PDF](current/academic/paper/paper.pdf) · [LaTeX](current/academic/paper/paper.tex) |
| Presentation · 17 slides, 900 s | [PDF](current/presentation/VOLLEY_BTech_Presentation.pdf) · [PPTX](current/presentation/VOLLEY_BTech_Presentation.pptx) · [speaker notes](current/presentation/SPEAKER_NOTES.md) |
| Reproduce and inspect | [Build and examples](current/REPRODUCE.md) · [chapter and figure map](current/ACADEMIC_MAP.md) · [current evidence](current/RESULTS.md) · [home CAD/STEP](current/cad/release/) |

The selected geometry has eight native/STEP states and 154 accepted motion/refinement checks. Its represented dry CAD mass is **149.557 kg**, with a separate **7 kg** power/control allowance. The averaged source-coupled reference includes finite motor force, actual conductor resistance, host recoil, payload departure and active carrier arrest. An executable custody specification accepts 24 nominal commands and passes 166 declared logic tests. [Results and method boundaries](current/RESULTS.md) identify the evidence behind these figures.

<p><a href="current/academic/assets/coupled_shot_reference.png"><img src="current/academic/assets/coupled_shot_reference.png" alt="Computed ACR1 nominal 3 m/s reference shot: velocity, phase current and source voltage versus time" width="720"></a></p>

*Computed result · ACR1 nominal 3 m/s reference case, averaged source/motion model. The retained carrier is actively arrested after payload departure. [Numerical cases](current/analysis/COUPLED_SHOT.json) · [model source](current/analysis/coupled_shot.py).*

The matched mission study compares twelve-release campaigns with commanded and spring deployment at a shared target boundary. Results depend on target family and host authority: commanded deployment does not provide a universal propellant advantage. The [supplement](current/ACADEMIC_MAP.md) links source, raw commands and independent numerical replay records.

Builds and selected numerical examples run from this checkout. [Reproduction instructions](current/REPRODUCE.md) distinguish document builds, numerical examples and native solver regeneration. Geometry and logic checks establish the declared computational criteria; hardware, payload interface, environmental and flight qualification remain subsequent development.

The current report/manuscript files are the [ED1 editorial revision](current/academic/EDITORIAL_REVISION.json), correcting bibliography identities without changing the engineering argument or results. The [original dated issue](archive/2026-10-24-acr1-original/README.md) preserves the original source/PDF/DOCX/manuscript bytes. Academic approval, genuine similarity feedback, an independent human technical read and venue requirements retain their actual external status in the [editorial checklist](current/SUBMISSION_CHECKLIST.md). No individual contribution allocation is asserted.

[Scientific figure conventions](docs/FIGURE_STANDARD.md) · [Current verification](VALIDATION_CURRENT.json) · [Licensing and third-party rights](LICENSING.md) · [Citation](CITATION.cff) · [Dated development archive](archive/README.md) · [Release and errata policy](RELEASE_POLICY.md) · [Publication policy](PUBLICATION_POLICY.md)
