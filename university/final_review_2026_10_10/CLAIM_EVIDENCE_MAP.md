# Presentation claim and evidence map

This map connects each review slide to the most detailed available record in this repository. The 28 September 2026 thesis checkout at `b30ffdc` and the 29 September 2026 PLAN-R2 working baseline were used to prepare the 10 October 2026 review pack. A slide is an explanation of the evidence; it is not a substitute for its underlying analysis and run sheet.

| Slide | Claim or purpose | Detailed record | Evidence class / limit |
|:--|:--|:--|:--|
| 1–2 | Presenters, topic and required outline | `university/` review pack; user-supplied format and outline | Review metadata, not technical evidence |
| 3 | Repeat-fleet context, candidate delivery buyer and same-mission trade | [Local market and spacecraft-fit audit](../../MARKET_AND_CUSTOMER_FIT.md); [`source/paper.tex`](../../source/paper.tex), Introduction | Industry context and buyer hypothesis; no confirmed customer, host or sale |
| 4 | Spring release/differential drag, OTV and electromagnetic comparisons | `source/paper.tex`, Related Work and bibliography; [`appendix/RELATED_WORK.md`](../../appendix/RELATED_WORK.md); [`appendix/PRIOR_ART.md`](../../appendix/PRIOR_ART.md) | Literature synthesis; persistent phasing needs a relative state change; prior art narrows novelty |
| 5 | Commandable release of an unmodified CubeSat at moderate acceleration, with installed burden | `source/paper.tex`, Abstract, Introduction and Limitations; [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md) | Research proposition; payload qualification absent |
| 6 | Objectives and status | `source/paper.tex`; [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`README.md`](../../README.md); [Gen6 direction](GEN6_DIRECTION.md) | Presentation synthesis; not a pre-approved university objective list |
| 7–8 | Model chain and numerical checks | `source/paper.tex`, Models and Verification; [`validation/README.md`](../../validation/README.md); [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md) | Model-specific numerical verification, not experiment |
| 9 | 2023–2026 evolution and approximate dates | [`appendix/HISTORY.md`](../../appendix/HISTORY.md); [`README.md`](../../README.md) | Several reconstructed dates marked approximate |
| 10 | Corrections adopted in the final Gen5 baseline | [`appendix/HISTORY.md`](../../appendix/HISTORY.md); [`appendix/PROVENANCE.md`](../../appendix/PROVENANCE.md); `source/paper.tex`, Limitations | Change-controlled computational results, not physical validation |
| 11 | Current computational review deliverables | [`README.md`](../../README.md); [computational review PDF](../../reports/GEN5_COMPUTATIONAL_REVIEW.pdf); [`validation/README.md`](../../validation/README.md) | Reported model cases and failed design gates; no measured VOLLEY article |
| 12 | 1.5 m track, Halbach LSM, magazine, reusable sled and brake | `source/paper.tex`, System Architecture; [native FreeCAD assembly](../../cad/native/Gen5_Review.FCStd); [FreeCAD STEP export](../../cad/step/gen5/VOLLEY_Review_Assembly_FreeCAD_Gen5.step) | Reference configuration has an unresolved side-fed interference |
| 13 | 16.029 m/s; 10.07 g; 2,782 J; 47 J; 1,162 J; 18.8%; 124.488 J unitemized | [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`analysis/results/motor_results.json`](../../analysis/results/motor_results.json); [`P117`](../../validation/P117_rated_energy_mass_audit.md); `source/figures/F01_shot.png` | Rated Gen5 model point; algebraic identities pass, complete loss budget and components unverified |
| 14 | 0.0274 m/s (3σ) at 15.8 m/s setpoint | [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`analysis/results/motor_results.json`](../../analysis/results/motor_results.json); `source/figures/F03_mc.png` | Closed-loop Monte Carlo, not measured repeatability |
| 15 | 28.800775 km immediate axis rise; 1.60× modeled mean-activity lifetime | [P115 Cartesian orbit check](../../validation/P115_rated_orbit_cartesian.md); `source/paper.tex`, Astrodynamic Utility; [`analysis/results/astro_results.json`](../../analysis/results/astro_results.json) | Current two-body geometry checked; current lifetime figure not independently rerun |
| 16 | 126.6 kg dry; 174.6 kg loaded; 10.55 versus ~6 kg per 3U; parity fails | [`appendix/BASELINE.md`](../../appendix/BASELINE.md); [`analysis/results/mass_properties.json`](../../analysis/results/mass_properties.json); [`analysis/results/payload_family.json`](../../analysis/results/payload_family.json); [`analysis/results/enclosure_buildup.json`](../../analysis/results/enclosure_buildup.json); `source/paper.tex`, Payload Class | Modelled mass comparison under the stated 3U/canister boundary |
| 17 | Side-fed reference configuration fails static packaging | [P116 CAD run sheet](../../validation/P116_gen5_assembly_packaging.md); [CAD PDF](../../cad/GEN5_CAD_REVIEW.pdf); [FreeCAD read-back JSON](../../cad/FREECAD_EXPORT.json) | 11 mm width shortfall, 32,915 mm³ exact clash per side; alternate architectures untested |
| 18 | Computational shot-to-orbit demonstration | [`analysis/`](../../analysis/), `motor_model.py` / orbit scripts and result JSON; `source/figures/F01_shot.png`, `rated_orbit_crosscheck.png` | Reproducible model chain, not physical demonstration |
| 19 | Gen5 study answer: conditional benefit, 3U mass and reference packaging failures | Slides 13–17 records above; `source/paper.tex`, Conclusion | Evidence-based negative selection, not flight readiness |
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
