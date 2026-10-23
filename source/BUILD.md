# Build the accompanying research manuscript

`paper.tex` is the editable article accompanying the university blackbook. The bundled `IEEEtran.cls` is the publisher's document class; its copyright and license notices are retained. The report and the IEEE-formatted article are distinct document editions.

The figures, analysis inputs, captured numerical results and validation records required by this manuscript are included in this repository. Rebuilding the article does not require another VOLLEY repository.

From this directory, run:

```bash
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
cp paper.pdf VOLLEY_IEEE_Conference.pdf
```

The three passes resolve figure, table and bibliography references from a clean build. `VOLLEY_IEEE_Conference.pdf` is the published article export. Source changes require refreshed figure/document identities and artifact hashes before publication. The blackbook PDF and DOCX are built separately with `university/build_report.py`.

The class supplies an IEEE conference layout. A venue remains unselected; its current length, formatting, copyright and submission requirements must govern any actual submission. No acceptance or submission is claimed by this export.
