# Building the thesis manuscript

`paper.tex` and `IEEEtran.cls` are **authored here** as of 2026-08-13
([ADR-028](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/main/docs/adr/028-no-latex-in-the-flagship.md)).
The VOLLEY flagship is an engineering record and holds no LaTeX.

```
pdflatex paper.tex     # three passes from clean
```

`source/figures/` and everything under `appendix/`, `analysis/`, `validation/` and `cad/` are
**generated** from the flagship by `tools/export_companion.py`. Do not hand-edit them — change
the analysis, regenerate, re-export.
