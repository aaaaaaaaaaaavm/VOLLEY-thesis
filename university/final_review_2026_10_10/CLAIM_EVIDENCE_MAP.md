# Presentation claim and evidence map

This map connects each review slide to the most detailed available record in this repository. The 28 September 2026 thesis checkout at `b30ffdc` and the 29 September 2026 PLAN-R2 working baseline were used to prepare the 10 October 2026 review pack. A slide is an explanation of the evidence; it is not a substitute for its underlying analysis and run sheet.

| Slide | Claim or purpose | Detailed record | Evidence class / limit |
|:--|:--|:--|:--|
| 1–2 | Presenters, topic and required outline | `university/` review pack; user-supplied format and outline | Review metadata, not technical evidence |
| 3 | Rideshare problem; host/deployer role split | [`source/paper.tex`](../../source/paper.tex), Introduction; [`README.md`](../../README.md) | Mission concept; no selected host |
| 4 | Spring, timed-release/drag, OTV and electromagnetic comparisons | `source/paper.tex`, Related Work and bibliography; [`appendix/RELATED_WORK.md`](../../appendix/RELATED_WORK.md); [`appendix/PRIOR_ART.md`](../../appendix/PRIOR_ART.md) | Literature synthesis; prior art narrows novelty |
| 5 | Commandable release of an unmodified CubeSat at moderate acceleration, with installed burden | `source/paper.tex`, Abstract, Introduction and Limitations; [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md) | Research proposition; payload qualification absent |
| 6 | Objectives and status | `source/paper.tex`; [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`README.md`](../../README.md); [Gen6 direction](GEN6_DIRECTION.md) | Presentation synthesis; not a pre-approved university objective list |
| 7–8 | Model chain and numerical checks | `source/paper.tex`, Models and Verification; [`validation/README.md`](../../validation/README.md); [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md) | Model-specific numerical verification, not experiment |
| 9 | 2023–2026 evolution and approximate dates | [`appendix/HISTORY.md`](../../appendix/HISTORY.md); [`README.md`](../../README.md) | Several reconstructed dates marked approximate |
| 10 | Corrections adopted in the final Gen5 baseline | [`appendix/HISTORY.md`](../../appendix/HISTORY.md); [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md); `source/paper.tex`, Limitations | Change-controlled computational results, not physical validation |
| 11 | Completed computational thesis deliverables | [`README.md`](../../README.md); [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md); [`validation/README.md`](../../validation/README.md) | Analytical record complete; no measured VOLLEY article |
| 12 | 1.5 m track, Halbach LSM, magazine, reusable sled, bank and brake | `source/paper.tex`, System Architecture; [`cad/`](../../cad/); [`analysis/results/mass_properties.json`](../../analysis/results/mass_properties.json) | CAD/model configuration, not hardware |
| 13 | 16.029 m/s; 10.07 g; 2,782 J; 47 J; 1,162 J; 18.8% | [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`analysis/results/motor_results.json`](../../analysis/results/motor_results.json); `source/figures/F01_shot.png` | Rated Gen5 model point; unmeasured components |
| 14 | 0.0274 m/s (3σ) at 15.8 m/s setpoint | [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`analysis/results/motor_results.json`](../../analysis/results/motor_results.json); `source/figures/F03_mc.png` | Closed-loop Monte Carlo, not measured repeatability |
| 15 | 28.8 km semi-major-axis rise; 1.60× mean-activity lifetime | `source/paper.tex`, Astrodynamic Utility and Limitations; [`analysis/results/astro_results.json`](../../analysis/results/astro_results.json); [`validation/A5_astro_orekit.md`](../../validation/A5_astro_orekit.md); [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md) | Atmosphere-dependent model; exact current lifetime figure not independently rerun |
| 16 | 126.6 kg dry; 174.6 kg loaded; 10.55 versus ~6 kg per 3U; parity fails | [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`analysis/results/mass_properties.json`](../../analysis/results/mass_properties.json); [`analysis/results/payload_family.json`](../../analysis/results/payload_family.json); [`analysis/results/enclosure_buildup.json`](../../analysis/results/enclosure_buildup.json); `source/paper.tex`, Payload Class | Modelled mass comparison under the stated 3U/canister boundary |
| 17 | Supported benefit, rejected 3U mass, unverified physical behavior | Slides 13–16; [`appendix/OPEN_PROBLEMS.md`](../../appendix/OPEN_PROBLEMS.md), especially E30, E34, E35; [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md) | Engineering decision from model evidence; no physical qualification or approved host |
| 18 | Computational shot-to-orbit demonstration | [`analysis/`](../../analysis/), `motor_model.py` / orbit scripts and result JSON; `source/figures/F01_shot.png`, `F04_life.png` | Reproducible model chain, not physical demonstration |
| 19 | Completed Gen5 research answer: conditional benefit and 3U mass failure | Slides 13–17 records above; `source/paper.tex`, Conclusion | Evidence-based synthesis, not flight readiness |
| 20–21 | Gen6 investigation and first-test milestone | [Gen6 direction](GEN6_DIRECTION.md) summarizing PLAN-R2 | Open plan; no selected mechanism or 1 km/s result |
| 22–23 | Published/agency literature and project sources | `source/paper.tex`, bibliography; [`appendix/LITERATURE.md`](../../appendix/LITERATURE.md) | Sources are categorized; project records are not external validation |

## Exact Gen5 numbers and dependencies

The generated [`appendix/BASELINE.md`](../../appendix/BASELINE.md) is the presentation's preferred short numerical source. It names source fields in `analysis/results/*.json`. The presentation keeps superseded operating points out of headline slides. For mass and alternatives, read the payload-family and enclosure results with the manuscript's qualification that smaller payload classes need new cassette/retention design. For orbital lifetime, read the manuscript's solar-activity caveat and failed invariance check before quoting 1.60×.

## Reported limitations that must travel with the claims

- A **CAD render** establishes arrangement and dimensions in a model, not manufacture.
- A **finite-element or circuit result** establishes behavior under chosen material, geometry, boundary and component assumptions, not flight qualification.
- A **Monte Carlo distribution** depends on the assumed uncertainty model; it does not measure actual cycle variation.
- A **host example** is a worked interface case, not provider approval or endorsement.
- A **Gen6 target** is a trade requirement, not an achieved Gen5 or Gen6 operating point.
