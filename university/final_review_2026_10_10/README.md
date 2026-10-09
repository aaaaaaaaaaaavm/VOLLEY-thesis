# Final B.Tech project review — 10 October 2026

**Presenters:** Adityavardhan Mishra (PRN 23070125054) and Pratham Chawla (PRN 23070125029)<br>
**Guide:** Vikas Gulia<br>
**Institution:** Symbiosis Institute of Technology, Pune

This directory is the complete review pack. It follows the user's eleven-part outline and the visual format of the supplied university example PDF: SIT cover and logo, cyan content headings, white body, and numbered slides. The example PDF contained another project's work; none of that work was reused as VOLLEY content.

**Presentation thesis:** the Gen5 system-level computational evaluation is complete. It predicts a conditional orbital benefit and finds that the complete Gen5 configuration fails the preset 3U mass criterion. Slides 1–19 tell that finished research story. Slides 20–21 label Gen6 as future work, with no achieved Gen6 speed or selected mechanism. Completion here means an answered analytical question, not a qualified flight product.

## Bring to the review

| Item | Present/print | Editable source |
|:--|:--|:--|
| Main presentation, 23 slides | [PPTX](VOLLEY_Final_Review_2026-10-10.pptx) · [PDF](VOLLEY_Final_Review_2026-10-10.pdf) | [Build script](build_presentation.py) |
| Panel handbook, detailed explanation and figures | [PDF](PANEL_HANDBOOK.pdf) | [Markdown](PANEL_HANDBOOK.md) · [DOCX](PANEL_HANDBOOK.docx) |
| Presenter reference, slide notes and viva answers | [PDF](PRESENTER_REFERENCE.pdf) | [Markdown](PRESENTER_REFERENCE.md) · [DOCX](PRESENTER_REFERENCE.docx) |

The [claim and evidence map](CLAIM_EVIDENCE_MAP.md) traces every substantive slide to the manuscript, numerical result and/or project-plan source. The [Gen6 direction](GEN6_DIRECTION.md) records precisely what the forward-looking slides mean. The thesis's full technical detail remains in the [manuscript PDF](../../source/VOLLEY_IEEE_Conference.pdf) and [source](../../source/paper.tex), [`analysis/`](../../analysis/), [`validation/`](../../validation/), [`cad/`](../../cad/) and [`appendix/`](../../appendix/); these are the underlying record, rather than a claim that 23 slides reproduce every calculation.

## Evidence language

- The Gen5 research **analysis and decision record are complete** for the stated computational cases. Results are predictions; numerical cross-checks apply to named models and cases. No VOLLEY hardware has been built or physically tested.
- The modelled Gen5 3U system fails its preset mass-parity criterion against a spring canister. This negative finding is included in the presentation and handbook.
- Gen6 is an **open architecture trade**. Its approximately 1–2 m/s to 1 km/s span is an investigation envelope. No 1 km/s performance, mechanism selection, payload qualification, host compatibility or build/test release is claimed.
- The historical thesis manuscript is authored under Adityavardhan Mishra's name. This review pack credits both named presenters; it does not retroactively change manuscript authorship.

## University final-review rubric coverage

| Criterion | Review evidence |
|:--|:--|
| Achievement of objectives (10 marks) | Slides 6, 11, 19; handbook §§4, 7–9 |
| Technical quality and innovation (10 marks) | Slides 4–8, 12–17; handbook §§2–5, 8 |
| Results, validation and analysis (5 marks) | Slides 13–18; handbook §8 and claim map |
| Report and documentation (5 marks) | Manuscript, baseline, validation, provenance and this pack |
| Presentation, demonstration and viva (10 marks) | Slide 18 computational demonstration; presenter reference |

## Rebuild

From this directory, run `python build_presentation.py`, then convert the resulting PPTX to PDF with LibreOffice/PowerPoint. The Markdown files can be exported to PDF and DOCX with Pandoc. All image references point to files already in this repository. The SIT logo in `assets/` was extracted from the user-provided university example PDF solely for this university-format review pack.
