> **Programme status, 2026-09-28:** Gen6 is in development. No architecture or speed envelope is selected or validated. The independent spring-cell bank and the historical gas guide are unselected studies. This thesis preserves older model studies; it must not be read as a physical test or a current design specification.

> ## What is generated here, and what is not
>
> **Generated** from [aaaaaaaaaaaavm/VOLLEY](https://github.com/aaaaaaaaaaaavm/VOLLEY) at commit
> `06ebd07` by `tools/export_companion.py`: the analysis scripts and their results, the
> validation run sheets, the figures, and the reference records. Any edit to those is
> destroyed on the next export. **Fix them in VOLLEY and this repository picks the fix up.**
>
> **Authored here, and never overwritten:** the manuscript and its figures under `source/`, and everything under `university/`. VOLLEY is an engineering
> record and holds no manuscript source.
>
> Where a generated file disagrees with VOLLEY, VOLLEY is right and this copy is stale.
>
> **This repository may be improved until the work is presented, and freezes at that
> moment.** What enters it has to be stable, effective and reliable against the problem
> statement -- not merely newer.

Live programme studies at this export: [sequential campaign allocation](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/06ebd07/docs/CAMPAIGN_ALLOCATION.md)
and [architecture decision gates](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/06ebd07/docs/PROGRAMME_EXECUTION.md).
[Terminal-state timing](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/06ebd07/docs/TERMINAL_TIMING.md)
extends the single-payload benchmark. These studies extend the engineering record;
the authored manuscript remains Gen5.

The latest [review and restart record](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/06ebd07/docs/REVIEW_20260916.md)
adds combined conditional release-error corners, reference-cell mechanics and the verification matrix.
These bounded calculations do not close the full campaign or select flight hardware.

<!-- PROGRAMME-HEADER-START -->
| Repository | Role | You are here |
|---|---|---|
| [VOLLEY](https://github.com/aaaaaaaaaaaavm/VOLLEY) | Main: the authoritative engineering record. Improved continuously |  |
| [VOLLEY-paper](https://github.com/aaaaaaaaaaaavm/VOLLEY-paper) | The concept at its most reliable, as an IEEE-formatted manuscript. **Frozen when published** |  |
| **[VOLLEY-thesis](https://github.com/aaaaaaaaaaaavm/VOLLEY-thesis)** | The same concept as a full submission. **Frozen when presented** | ← |
| [VOLLEY-lab](https://github.com/aaaaaaaaaaaavm/VOLLEY-lab) | The vault: ideas that never became a complete thing, and why each stopped |  |
<!-- PROGRAMME-HEADER-END -->

---

# VOLLEY: the thesis

A final-year thesis on giving rideshare CubeSats an orbit their host was not going to, and
the full record of what went wrong on the way there.

<p align="center"><img src="source/figures/V00_system_overview.svg" alt="VOLLEY mission chain and the evidence boundary between Gen5 and historical study" width="100%"></p>

<p align="center"><sub>The thesis preserves the analysed Gen5 baseline while the next architecture remains open. Later studies do not inherit the Gen5 evidence.</sub></p>

<p align="center">
  <img src="cad/renders/gen5/exploded.png" alt="Exploded Gen5 electromagnetic drive stack" width="32%">
  <img src="source/figures/A29_cfd_report.png" alt="Gen5 CFD convergence, force history and surface pressure" width="32%">
  <img src="cad/renders/legacy_study/hero_open.png" alt="Historical stage-integrated gas study" width="32%">
</p>

<p align="center"><sub>The thesis keeps the analysed Gen5 machine and a historical gas study visually separate.</sub></p>

[Read the manuscript](source/VOLLEY_IEEE_Conference.pdf)

The submission is here with its analyses, its acceptance tests and its defect register attached.
The defects are deliberate: an examiner should be able to see what failed, when it was found, and
what was done about it. Nothing in it has been built or measured.

## The design evolution this thesis is about

One mission, held constant. One architecture, changed repeatedly. That is the shape of the
work, and it is worth stating before the chapters.

The mission is last-mile orbital distribution. After the primary spacecraft separates, the
launch vehicle's final stage can continue, where host capability allows, as a temporary controlled
orbital delivery platform. The host does the coarse orbital repositioning. VOLLEY produces each
secondary satellite's individually commanded release condition. That was decided in 2023, by
the second architectural decision the project ever took.

The architecture, in four steps:

| | |
|---|---|
| Free-flyer | VOLLEY is its own spacecraft, carrying attitude control, power and recoil mass. Rejected in 2023, *"which is most of a spacecraft"* |
| Hosted deployer | The spent upper stage supplies all three. VOLLEY becomes a payload rather than a mission |
| Self-contained electromagnetic system aboard the platform, Gen5 | Its own track, linear synchronous drive, sled, supercapacitor bank, eddy brake and magazine. This is the machine the manuscript reports |
| Historical stage-integrated gas study | The stage's own structure and about 8 m of length become part of the machine; retained as a comparator after guide/contact and trim/tube problems were exposed |
| Independent spring-cell study | Separate retained cells use slowly charged mechanical storage, a latch, short guided pusher and local catcher. Withdrawn as the current architecture because they do not supply the shared reload path or broad commanded speed goal |

> What is worth noticing is that the objective never changed. What the generations record is a
> steadily better answer to how much of this VOLLEY needs to build for itself, and the honest cost
> of each answer, including the one that made Gen5's enclosure 50.04 kg of skin the stage already
> had.
>
> Host capability stays parametric in every generation. No launch provider has supplied stage
> propulsion, restart or control-authority data, and the thesis says so wherever it matters.

## Layout

| | |
|---|---|
| `source/` | Manuscript and figures |
| `analysis/` | The scripts producing every number in the work |
| `validation/` | The analyses, each with its acceptance bands declared before the run |
| `cad/` | The CAD generations, with the defect audit for each |
| `appendix/` | Baseline, defect ledger, validation report, provenance, prior art, literature, decision records |

## For an examiner, in reading order

1. `appendix/PROVENANCE.md`, which says what stands behind each claim and what does not.
2. `appendix/BASELINE.md`, the frozen values, and the rule for changing any of them.
3. `appendix/adr/`, the decision records. Each states the alternatives considered and the
   consequences accepted. ADR-003 carries its own amendment showing an argument it got wrong.
4. `appendix/OPEN_PROBLEMS.md`, every known defect, including the ones that damage the work's own
   claims, and the ones found by checking this work against itself rather than by anyone asking.
5. `appendix/PRIOR_ART.md`, the nearest published work, and the two claims retracted after reading
   it.

The decision records are the part most worth reading. They are where the reasoning lives, and
several of them record the alternative that was rejected and why.

## What is authored here

`source/` holds the manuscript, which is written in this repository, the main record is an
engineering record and carries no manuscript source. `university/` holds submission forms,
formatting mandates and viva material, which are university-specific and do not belong upstream.
Neither is ever touched by the export. Everything else is regenerated and will be overwritten.

The [10 October 2026 final-review pack](university/final_review_2026_10_10/README.md)
contains the university-format slides, panel handbook, presenter reference and a
slide-by-slide map to the detailed calculations and validation limits in this repository.

This repository may be improved until the thesis is presented, and freezes at that moment. What
enters it has to be stable, effective and reliable against the problem statement.


## The thesis describes Gen5; the next architecture is open

This is deliberate and worth stating plainly. The authored manuscript describes Gen5, the
analysed baseline -- a frozen computational one, with no hardware behind it -- and the record of
what one self-contained deployer model costs. The long gas guide and compact independent spring
cells were later investigated and remain unselected comparators. The best sampled two-payload
campaign cannot select a product mechanism or speed ceiling; the later twelve-payload screens did
not complete a full manifest. The next design must restore the reusable shared path and loading
objective, then be compared under complete installed and mission accounting.

No performance has been physically measured, and no launch provider has supplied an accommodation.
The thesis retains Gen5 as a historical computational case, not a current product specification.

The main repository retains these studies and their recorded failures.

## Before citing

Every number here is a model output. Nothing has been built or measured. The defect ledger is
published deliberately rather than tidied away, and it is the honest measure of how far the work
has actually got.
