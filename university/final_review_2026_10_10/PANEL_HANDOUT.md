---
title: "VOLLEY Gen5 | Final-review evidence handout"
date: "10 October 2026"
geometry: margin=15mm
papersize: a4
fontsize: 9pt
---

**Adityavardhan Mishra · Pratham Chawla | Symbiosis Institute of Technology, Pune**

**Research question.** Can a shared, commandable CubeSat deployer provide useful release states while meeting the installed mass and integration burden of a 12 × 3U reference case?

**Decision.** The evaluated Gen5 configuration is **not selected** for that case. The computational study records both conditional orbital benefit and adverse system findings. No VOLLEY hardware was built or tested.

| Finding | Result and evidence boundary |
|:--|:--|
| Release speed | 16.029 m/s belongs to a historical periodic-force model. P118's finite 3-D **analytic** force screen gives 12.448 m/s under ideal phase and omitted circuit losses. It is not an independently verified rating. |
| Electrical chain | Historical gross draw is 2,782 J; 124.488 J remains unitemized in its compact energy account. A coupled force–power rerun is open. |
| Installed mass | Modeled dry mass is 126.6 kg, or 10.55 kg per 3U customer, against an approximate 6 kg spring-canister comparator. The predeclared 15% parity band fails. |
| CAD fit | The reference side-fed layout needs 537 mm within 526 mm clear width and overlaps the track by 32,915 mm³ per cassette. The separate widened R1 geometry clears twelve scripted routes; it lacks a selected feeder, retention and revised mass. |
| Orbital value | +28.8008 km immediate two-body axis rise is checked **for an assumed historical 16.029 m/s release**, not as achieved Gen5 behavior. The 1.60× atmosphere-dependent lifetime figure remains open. |
| Matched mission | A single assumed target yields ideal host propellant of 2.693 kg spring versus 0.827 kg at the finite Gen5 *ideal upper* speed. No bounded twelve-shot campaign closes; this is not a proven service advantage. |

**Evidence classes.** The pack contains source scripts, captured run outputs, numerical cross-checks, FreeCAD native review assemblies, STEP exports, figures, reports and an explicit claim-to-source map. These establish only their stated models, geometry and boundary conditions. They do not establish payload qualification, supplier component ratings, host/provider approval, customer demand or flight readiness.

**Next gate.** Independently check finite integrated thrust; rerun the coupled circuit and trajectory; select a feasible feeder and reconcile its mass, clearances and loads; repeat the matched mission; then build an instrumented coupon or test article when resources and interfaces are available. Gen6 and 1 km/s are future trade targets, not results.

**Source trail.** `P118_gen5_finite_force_map.md`; `P117_rated_energy_mass_audit.md`; `P116_gen5_assembly_packaging.md`; `P115_rated_orbit_cartesian.md`; `GEN5_COMPUTATIONAL_REVIEW.pdf`; `GEN5_CAD_REVIEW.pdf`; `CLAIM_EVIDENCE_MAP.md`. The complete pack is in the VOLLEY-thesis repository's `university/final_review_2026_10_10/` directory.
