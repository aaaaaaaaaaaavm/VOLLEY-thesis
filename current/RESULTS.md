# Computational results

| Result | Controlled evidence and interpretation |
|---|---|
| Twelve 4 kg, 340.5 × 100 × 100 mm surrogates | [CAD parameters](cad/PARAMETERS.json); two banks, six cells each |
| Eight native/STEP states; 154 accepted sampled checks | [Final CAD inventory](cad/release/FINAL_CAD_MANIFEST.json), [motion](cad/release/MOTION_VERIFICATION.json), [refinement](cad/release/FINAL_REFINEMENT_VERIFICATION.json); nominal geometry and custody, without dynamic contact precision |
| 149.5567197 kg represented dry CAD; 156.5567197 kg device including allowance; 204.5567197 kg loaded | [Resource ledger](analysis/RESOURCE_LEDGER.json); 7 kg allowance is not spatially represented in CAD CG/inertia |
| 13.127806 kg retained carrier/pallet | [Home BOM](cad/release/VOLLEY_G5_ACR1_home.json), [mass/CG/inertia](verification/MASS_CG_INERTIA_SUMMARY.json) |
| Approximately 1.328 N/A active force, 1.399 N/A including represented returns | [Finite motor](analysis/FINITE_MOTOR.json), [independent source-face check](analysis/SURFACE_CHARGE_CHECK.json), [actual-current field integration](analysis/CURRENT_FIELD_FORCE.json); peak phase-current convention and free-space assumptions |
| 1–3 m/s operating study with source limits and active arrest | [Coupled shot cases](analysis/COUPLED_SHOT.json), [timestep and implementation audit](verification/COUPLED_SHOT_REVIEW.json); accepted 3 m/s audit samples span nominal/adverse source and inductance assumptions |
| 24 nominal commands; 166 declared interlock tests | [Executable state model](analysis/transfer_interlocks.py), [captured results](analysis/TRANSFER_INTERLOCKS.json); command/proof sequencing, without measured sensor coverage |
| 250 mm feed in 40 s; 784 mm lift in 120 s | [Feeder sizing](analysis/FEEDER_SIZING.json), [lift sizing](analysis/LIFT_SIZING.json); explicit resistance, efficiency, load-sharing and catalog assumptions |
| Actual-carrier nominal paired face-separation reduction 0.285983 mm; declared 1.3× linear sensitivity 0.371778 mm | [Report §9 and figure](academic/GEN5_FINAL_YEAR_REPORT.md), [actual chassis review](academic/evidence/verification/CHASSIS_ACTUAL_REVIEW.md); the stated deformation/stress screening does not qualify the overall assembly |
| Twelve-release host-assisted comparison | [Selected cases](mission/SELECTED_CASES.json), [inputs](mission/MISSION_INPUTS.json), [comparison](mission/MISSION_COMPARISON.json), [native replay](mission/NATIVE_REPLAY_CHECKS.json); synthetic fixed-axis J2 point-release model |

The source-coupled calculation retains adverse and failed higher-speed samples in its data. The supported operating conclusion concerns the declared 1–3 m/s cases; it does not inherit the original tens-of-m/s concept rating. Mission errors quantify numerical consistency in the declared model, not flight delivery accuracy. The manuscript and report discuss payload contact/tip-off, magnetic exposure, source parasitics, complete assembly structure, thermal and environmental development.
