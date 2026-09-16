> ## What is synchronized here, and what is not
>
> **Synchronized** from [aaaaaaaaaaaavm/VOLLEY](https://github.com/aaaaaaaaaaaavm/VOLLEY) at commit
> `68c26ae`: the analysis scripts and their results, the validation run sheets, the figures,
> and the reference records. Any edit to those is replaced by the next companion export.
> **Fix them in VOLLEY and this repository picks the fix up.**
>
> **Authored here, and never overwritten:** the manuscript and its figures under `source/`, and everything under `university/`. VOLLEY is an engineering
> record and holds no manuscript source.
>
> Where a synchronized file disagrees with VOLLEY, VOLLEY is right and this copy is stale.
>
> **This repository may be improved until the work is presented, and freezes at that
> moment.** What enters it has to be stable, effective and reliable against the problem
> statement -- not merely newer.

Live programme studies at this export: [sequential campaign allocation](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/68c26ae/docs/CAMPAIGN_ALLOCATION.md)
and [architecture decision gates](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/68c26ae/docs/PROGRAMME_EXECUTION.md).
[Terminal-state timing](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/68c26ae/docs/TERMINAL_TIMING.md)
extends the single-payload benchmark.
[Two-payload manifest timing](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/68c26ae/docs/MANIFEST_TIMING.md)
adds shared-host coupling while P113/E5 remain open.
[Clean-sheet Gen6 reference](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/68c26ae/docs/GEN6_REFERENCE_ARCHITECTURE.md)
carries that bounded mission result into a compact reference cell while P92 remains open. These studies extend the engineering record;
the authored manuscript remains Gen5.

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

<p align="center"><img src="source/figures/V00_system_overview.svg" alt="VOLLEY mission chain and the evidence boundary between Gen5 and later architecture work" width="100%"></p>

<p align="center"><sub>The thesis preserves the analysed Gen5 baseline while the engineering
record continues beyond it. The existing gas-guide Gen6 remains a comparator and clean-sheet
mechanism selection is open; newer directions do not inherit Gen5 evidence.</sub></p>

<p align="center">
  <img src="cad/renders/gen5/exploded.png" alt="Exploded Gen5 electromagnetic drive stack" width="32%">
  <img src="source/figures/A29_cfd_report.png" alt="Gen5 CFD convergence, force history and surface pressure" width="32%">
  <img src="cad/renders/gen6/hero_open.png" alt="Existing Gen6 stage-integrated gas-guide study" width="32%">
</p>

<p align="center"><sub>The thesis keeps the analysed Gen5 machine, its numerical evidence, and
the less mature gas-guide investigation visually separate.</sub></p>

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
| Stage-integrated gas-guide study, existing Gen6 | The stage's own structure and roughly 8 m of length become part of the machine; cold gas replaces the drive. This remains an investigated comparator while clean-sheet selection is reopened |

> What is worth noticing is that the objective never changed. What the generations record is a
> series of answers to how much of this VOLLEY needs to build for itself, and the honest cost
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

This repository may be improved until the thesis is presented, and freezes at that moment. What
enters it has to be stable, effective and reliable against the problem statement.


## The manuscript describes Gen5, and the programme has moved beyond it

This is deliberate and worth stating plainly. Everything reproduced in the manuscript is Gen5,
the analysed baseline -- a frozen computational one, with no hardware behind it -- and the record
of what a self-contained deployer costs. On 2026-08-14 the main repository introduced the
stage-integrated cold-gas guide as Gen6 (ADR-032). Later contact/release and trim work exposed
limits in that architecture, and the flagship has since reopened mechanism selection.

Nothing in the existing gas-guide Gen6 is measured, and no launch provider has agreed to lend a
stage. That is exactly why the manuscript still carries Gen5. A paper reports what has been
analysed to a declared standard, not whichever architecture is currently being investigated.

The main repository carries Gen5, the existing gas-guide comparator and the clean-sheet selection
work, with failures kept at the same standard as results.

## Before citing

Every number here is a model output. Nothing has been built or measured. The defect ledger is
published deliberately rather than tidied away, and it is the honest measure of how far the work
has actually got.
