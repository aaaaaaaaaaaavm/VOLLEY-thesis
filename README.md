# VOLLEY academic report

**VOLLEY: Design and Computational Evaluation of a Commanded Electromagnetic CubeSat Deployment Mechanism**

Adityavardhan Mishra and Pratham Chawla · Mechanical Engineering, Symbiosis Institute of Technology, Pune · Gen5 ACR1, 24 October 2026

VOLLEY stores twelve 4 kg 3U payload surrogates in two fixed banks and feeds a captive pallet onto a reusable magnetic carrier. A finite linear synchronous motor commands release in the studied **1–3 m/s** range, then arrests and returns the carrier and pallet. This repository presents the completed computational design study and its reproducible academic record.

<p><a href="figures/acr1-polish/assembly_hero.png"><img src="figures/acr1-polish/assembly_hero.webp" alt="CAD-derived render of all 387 represented VOLLEY Gen5 ACR1 parts in the home pose; teal marks the selected feed and captive-pallet path." width="760"></a></p>

*CAD-derived Blender render · ACR1 home pose · all 387 represented objects present. Teal identifies the selected feed/pallet path; surface colours are display choices. [View provenance](figures/acr1-polish/POLISH_PROVENANCE.json).*

[Guided-feed close-up](figures/acr1-polish/feeder_detail_annotated.png) · [Four-state custody sequence](figures/acr1-polish/operating_sequence.png) · [Caption and visibility notes](figures/acr1-polish/CAPTIONS.md)


Start with the updated [58-page ED3 report](editions/ED3/VOLLEY_ED3_Report.pdf), [17-slide ED3 presentation](editions/ED3/VOLLEY_ED3_Presentation.pdf) and [portable edition sources](editions/ED3/README.md). ED3 adds a simple custody flow, annotated assembly and larger single-result figures to the matched-load chassis evidence. Use the [ED3 speaking notes](editions/ED3/SPEAKER_NOTES.md) and source archive to prepare the presentation; the [ED2 offline handoff](docs/ED2_PRESENTATION_HANDOFF.md) preserves that earlier edition. The table below preserves the ED1 engineering capture and its original academic files.

| Preserved ED1 artifact | Download and source |
|---|---|
| ED1 report · 55 pages | [PDF](current/academic/GEN5_FINAL_YEAR_REPORT.pdf) · [DOCX](current/academic/GEN5_FINAL_YEAR_REPORT.docx) · [Markdown](current/academic/GEN5_FINAL_YEAR_REPORT.md) |
| ED1 manuscript · 9 pages | [PDF](current/academic/paper/paper.pdf) · [LaTeX](current/academic/paper/paper.tex) |
| ED1 presentation · 17 slides, 900 s | [PDF](current/presentation/VOLLEY_BTech_Presentation.pdf) · [PPTX](current/presentation/VOLLEY_BTech_Presentation.pptx) · [speaker notes](current/presentation/SPEAKER_NOTES.md) |
| Reproduce and inspect | [Build and examples](current/REPRODUCE.md) · [chapter and figure map](current/ACADEMIC_MAP.md) · [current evidence](current/RESULTS.md) · [all eight local CAD/STEP states](current/cad/release/) |

The selected geometry has eight native/STEP states and 154 accepted motion/refinement checks. Its represented dry CAD mass is **149.557 kg**, with a separate **7 kg** power/control allowance. The averaged source-coupled reference includes finite motor force, actual conductor resistance, host recoil, payload departure and active carrier arrest. An executable custody specification accepts 24 nominal commands and passes 166 declared logic tests. [Results and method boundaries](current/RESULTS.md) identify the evidence behind these figures.

<p><a href="current/academic/assets/coupled_shot_reference.png"><img src="current/academic/assets/coupled_shot_reference.png" alt="Computed ACR1 nominal 3 m/s reference shot: velocity, phase current and source voltage versus time" width="720"></a></p>

*Computed result · ACR1 nominal 3 m/s reference case, averaged source/motion model. The retained carrier is actively arrested after payload departure. [Numerical cases](current/analysis/COUPLED_SHOT.json) · [model source](current/analysis/coupled_shot.py).*

The matched mission study compares twelve-release campaigns with commanded and spring deployment at a shared target boundary. Results depend on target family and host authority: commanded deployment does not provide a universal propellant advantage. The [supplement](current/ACADEMIC_MAP.md) links source, raw commands and independent numerical replay records.

Builds and selected numerical examples run from this checkout. [Reproduction instructions](current/REPRODUCE.md) distinguish document builds, numerical examples and native solver regeneration. Geometry and logic checks establish the declared computational criteria; hardware, payload interface, environmental and flight qualification remain subsequent development.

The unchanged `current/` report/manuscript capture is the [ED1 editorial revision](current/academic/EDITORIAL_REVISION.json), correcting bibliography identities without changing the engineering argument or results. The latest report/deck is separately versioned as [ED3](editions/ED3/README.md); the nine-page manuscript remains ED1. The [original dated issue](archive/2026-10-24-acr1-original/README.md) preserves the original source/PDF/DOCX/manuscript bytes. Academic approval, genuine similarity feedback, an independent human technical read and venue requirements retain their actual external status in the [editorial checklist](current/SUBMISSION_CHECKLIST.md). No individual contribution allocation is asserted.

[Scientific figure conventions](docs/FIGURE_STANDARD.md) · All eight native/STEP/BOM states and the 60-member raw solver supplement are included in this checkout. [Local data and restoration](current/README.md) provide source identities and scratch extraction; the captured conductor solution arrays are also bundled.

[ED1 capture verification](VALIDATION_CURRENT.json) · [Licensing and third-party rights](LICENSING.md) · [Citation](CITATION.cff) · [Dated development archive](archive/README.md) · [Release and errata policy](RELEASE_POLICY.md) · [Publication policy](PUBLICATION_POLICY.md)

The academic freeze remains scheduled for **30 October 2026, evening IST**. ED3 report/deck and the ED1 manuscript retain their separate identities; the exact cutoff snapshot is recorded when created.
