# Final B.Tech project review — 10 October 2026

**Presenters:** Adityavardhan Mishra (PRN 23070125054) and Pratham Chawla (PRN 23070125029)<br>
**Guide:** Vikas Gulia<br>
**Institution:** Symbiosis Institute of Technology, Pune

This directory is the review pack for the computational Gen5 study. It follows the user's eleven-part outline and the visual format of the supplied university example PDF: SIT cover and logo, cyan content headings, white body, and numbered slides. The example PDF contained another project's work; none of that work was reused as VOLLEY content.

**Presentation thesis:** the Gen5 system-level computational evaluation reports a conditional orbital benefit, a failed 3U mass criterion, and a failed side-fed CAD reference fit. Slides 1–22 present the research and its limitations. Slides 23–24 label Gen6 as future work, with no achieved Gen6 speed or selected mechanism. Completion here means an answered analytical question, not a qualified flight product or final design freeze.

## Bring to the review

**Start with [How to present the old numbers and known errors](READ_THIS_FIRST.md)** and give the panel the [one-page evidence handout](PANEL_HANDOUT.pdf). The [15-minute two-speaker run sheet](TOMORROW_RUN_SHEET.pdf) assigns the handoff, timing and fallback route. The deck places the historical shot beside the 3-D analytic force screen, independent 2-D FEM, and conditional bank rerun; slide 20 shows the computational force-to-mission chain. An offline presentation and core-evidence ZIP is provided as `TOMORROW_PRESENTATION_PACK.zip`; the reproducible source remains in this repository.

| Item | Present/print | Editable source |
|:--|:--|:--|
| Main presentation, 26 slides | [PPTX](VOLLEY_Final_Review_2026-10-10.pptx) · [PDF](VOLLEY_Final_Review_2026-10-10.pdf) | [Build script](build_presentation.py) |
| Panel handbook, detailed explanation and figures | [PDF](PANEL_HANDBOOK.pdf) | [Markdown](PANEL_HANDBOOK.md) · [DOCX](PANEL_HANDBOOK.docx) |
| Presenter reference, slide notes and viva answers | [PDF](PRESENTER_REFERENCE.pdf) | [Markdown](PRESENTER_REFERENCE.md) · [DOCX](PRESENTER_REFERENCE.docx) |

The [claim and evidence map](CLAIM_EVIDENCE_MAP.md) traces every substantive slide to the manuscript, numerical result and/or project-plan source. The [Gen6 direction](GEN6_DIRECTION.md) records precisely what the forward-looking slides mean. The full technical detail remains in the [manuscript PDF](../../source/VOLLEY_IEEE_Conference.pdf), [computational report](../../reports/GEN5_COMPUTATIONAL_REVIEW.pdf), [FreeCAD review report](../../cad/GEN5_CAD_REVIEW.pdf), [`analysis/`](../../analysis/), [`validation/`](../../validation/), [`cad/`](../../cad/) and [`appendix/`](../../appendix/). The reports include simulation plots and software-generated CAD views; none represents a physical test.

The deck's assembly images are [STEP-derived, Blender-rendered review views](../../cad/renders/step_review/README.md). The source STEP and FreeCAD files, image hashes, visible parts and hidden enclosure are recorded in the [view provenance](../../cad/renders/step_review/PROVENANCE.json). The offline ZIP includes all six JPEGs alongside the deck. It also includes an optional [four-stage operations storyboard](../../cad/renders/sequence/gen5_operations_hero.png) and [eight-second video](../../cad/renders/sequence/gen5_intended_sequence.mp4) under `VISUALS/`, with provenance. The video is a **conceptual motion aid** for a viva; it does not validate feed, contact, clearance or braking. The exact-solid width and interference findings come from the CAD audit.

Slide 3 and the handbook introduce the [audited market and spacecraft-fit report](../../MARKET_AND_CUSTOMER_FIT.md). They identify candidate buyer jobs without claiming customer interviews, qualified spacecraft or product-market fit. The source-linked report corrects the Drive material before it enters the review narrative.

**Review corrections:** an earlier draft said release timing alone could create persistent in-track phase. That was wrong for zero-relative-impulse releases from an unchanged co-orbital host. A separate historical-input two-body run now checks the immediate 28.800775 km axis change, but not the 1.60× atmospheric lifetime. A native FreeCAD assembly review identifies the 11 mm side-fed width shortfall. The current PPTX, PDF, handbook and presenter notes include these findings and the new finite-force, R1 feeder and matched-mission screens.

## Evidence language

- The captured Gen5 computational cases and their negative 3U selection decision are documented. Results are predictions; numerical cross-checks apply to named models and cases. No VOLLEY hardware has been built or physically tested.
- The modelled Gen5 3U system fails its preset mass-parity criterion against a spring canister. Its stated side-fed reference assembly also fails a width and exact-solid interference check. Both negative findings are in the presentation and handbook.
- Gen6 is an **open architecture trade**. Its approximately 1–2 m/s to 1 km/s span is an investigation envelope. No 1 km/s performance, mechanism selection, payload qualification, host compatibility or build/test release is claimed.
- The historical thesis manuscript is authored under Adityavardhan Mishra's name. This review pack credits both named presenters; it does not retroactively change manuscript authorship.

## University final-review rubric coverage

| Criterion | Review evidence |
|:--|:--|
| Achievement of objectives (10 marks) | Slides 6, 11, 22; handbook §§4, 7–9 |
| Technical quality and innovation (10 marks) | Slides 4–8, 12–19; handbook §§2–5, 8 |
| Results, validation and analysis (5 marks) | Slides 13–21; handbook §8 and claim map |
| Report and documentation (5 marks) | Manuscript, baseline, validation, provenance and this pack |
| Presentation, demonstration and viva (10 marks) | Slide 20 computational demonstration; presenter reference |

## Rebuild

From this directory, run `python build_presentation.py` and `python render_review_pdf.py` to build the PPTX and matching 26-page PDF. The renderer checks text for overflow. The handbook and presenter PDFs and DOCXs can be rebuilt with Pandoc and XeLaTeX from their Markdown sources. All image references point to files already in this repository. The SIT logo in `assets/` was extracted from the user-provided university example PDF solely for this university-format review pack. Check [file hashes](CHECKSUMS.sha256) after copying the submission pack.
