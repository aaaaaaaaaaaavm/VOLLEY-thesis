> ## Generated repository, do not edit here
>
> Every file in this repository is generated from the **VOLLEY flagship** by
> `tools/export_companion.py`. Nothing here is authored, and any edit made here will be
> destroyed the next time it is regenerated.
>
> **Source:** [aaaaaaaaaaaavm/VOLLEY](https://github.com/aaaaaaaaaaaavm/VOLLEY) at commit `0ca5cd4`
> **Found a mistake?** Fix it in the flagship. This repository will pick it up.
>
> The flagship is the authoritative engineering record. Where this repository and the
> flagship disagree, the flagship is right and this copy is stale.

<!-- PROGRAMME-HEADER-START -->
| Repository | Role | You are here |
|---|---|---|
| [VOLLEY](https://github.com/aaaaaaaaaaaavm/VOLLEY) | Flagship: the authoritative engineering record, and the portfolio |  |
| [VOLLEY-paper](https://github.com/aaaaaaaaaaaavm/VOLLEY-paper) | IEEE companion: manuscript and reproducibility package *(generated)* |  |
| **[VOLLEY-thesis](https://github.com/aaaaaaaaaaaavm/VOLLEY-thesis)** | Thesis companion: university submission *(generated)* | ← |
| [VOLLEY-lab](https://github.com/aaaaaaaaaaaavm/VOLLEY-lab) | Phase II: research, redesign, deliberately unstable |  |
<!-- PROGRAMME-HEADER-END -->

---

# VOLLEY: thesis companion

Final-year thesis submission material, generated from the VOLLEY flagship.

**[Read the manuscript](source/VOLLEY_IEEE_Conference.pdf)**

## Layout

| | |
|---|---|
| `source/` | Manuscript and figures |
| `analysis/` | Six scripts producing every number in the work |
| `validation/` | Nine analyses, each with its acceptance band declared before the run |
| `cad/` | Three CAD generations, with the defect audit for each |
| `appendix/` | Baseline, defect ledger, validation report, provenance, prior art, literature, decision records |

## For an examiner, in reading order

1. `appendix/PROVENANCE.md`, which says what stands behind each claim and what does not.
2. `appendix/BASELINE.md`, the twenty frozen values, and the rule for changing any of them.
3. `appendix/adr/`, eighteen decision records. Each states the alternatives considered and the
   consequences accepted. ADR-003 carries its own amendment showing an argument it got wrong.
4. `appendix/OPEN_PROBLEMS.md`, every known defect, including the ones that damage the work's own
   claims.
5. `appendix/PRIOR_ART.md`, the nearest published work, and the two claims retracted after reading
   it.

The decision records are the part most worth reading. They are where the reasoning lives, and
several of them record the alternative that was rejected and why.

## University material goes in `university/`

That directory is the one place in this repository where hand-written content survives.
Submission forms, formatting mandates and viva material are university-specific and do not belong
upstream. **Everything outside `university/` is regenerated and will be overwritten.**

## Before citing

Every number here is a model output. Nothing has been built or measured. The defect ledger is
published deliberately rather than tidied away, and it is the honest measure of how far the work
has actually got.
