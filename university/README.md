# University report and presentation

- [Blackbook PDF](GEN5_FINAL_YEAR_REPORT.pdf), [editable DOCX](GEN5_FINAL_YEAR_REPORT.docx) and [Markdown source](GEN5_FINAL_YEAR_REPORT.md).
- [Presentation and claim map](final_review_2026_10_10/README.md): 37-slide editable/PDF package for a selected 15-minute route plus questions.
- [Native campaign report](../validation/native_campaign_review/README.md): full prescribed-event replay and precision budgets.

## Report structure and issue

The first similarity-review issue is dated 20 October 2026. Eleven main chapters present introduction, objectives, literature, methodology, controlled design, motor/power analysis, CAD/mass, orbital comparison, discussion, limitations and conclusions. Three appendices retain evidence identities, development history and separate Gen6 research. The bibliography and generated contents, figure and table lists support navigation.

The college-supplied sample informed the A4 cover, certification/acknowledgement sequence, numbered chapters and 12-point serif body. PDF uses the metrically compatible open Liberation Serif font; DOCX specifies Times New Roman for editing on systems where it is installed. Institutional approval of the adapted format is not implied. Certification remains visibly unsigned and no similarity result is inserted before one is received.

## Rebuild

From the repository root, run `python3 university/build_report.py`. It requires Pandoc, XeLaTeX with the referenced packages, Python and `requirements-build.txt`. The PDF and DOCX use the same Markdown content. Word may update its generated contents field on opening; the PDF supplies the checked, fixed pagination. Repository-local evidence links resolve to the immutable input snapshot named in the Lua filter. The report and figure identity ledgers must be refreshed after an accepted source change.

The Gen5 technical reference remains unchanged. Failed mass, fit and mission criteria are retained; all Gen6 studies remain separate. Hardware measurements, actual release precision, provider acceptance, guide approval and similarity results are outside the reported evidence.
