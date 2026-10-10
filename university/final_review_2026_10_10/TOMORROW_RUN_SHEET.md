---
title: "VOLLEY | 15-minute final-review run sheet"
subtitle: "10 October 2026 · two presenters · computational Gen5 study"
author: "Adityavardhan Mishra and Pratham Chawla"
geometry: margin=16mm
papersize: a4
fontsize: 10pt
colorlinks: true
---

# The answer to present

**One sentence:** We completed a traceable computational evaluation of Gen5 and found conditional orbital utility, but the evaluated 3U configuration fails its preset mass criterion, its side-fed reference CAD clashes, and its historical speed depends on a challenged force assumption. This is a completed *study and design decision*, not a built or qualified product.

**Opening, about 30 seconds (Adityavardhan):** “We asked whether a shared, commandable CubeSat deployer could create useful orbital choices while justifying its complete installed mass and integration burden. We modelled the Gen5 architecture, checked its shot and orbital results, assembled its CAD, and compared it with a conventional release on the same reference mission. The answer is mixed: the modeled impulse can be useful, but this Gen5 configuration does not pass our 3U mass screen or its current side-fed fit check. We will show how the evidence led us there.”

**Close, about 25 seconds (Adityavardhan):** “Our research result is a documented Gen5 design rejection for the evaluated 3U case, with an unresolved finite-force discrepancy and a clear route to the next experiment. Gen6 is a new architecture trade, including higher-speed targets; 1 km/s has not been demonstrated. We welcome questions on the assumptions, failed criteria and source files.”

## Timed route using the existing 26-slide deck

The spoken route is **13:55**, leaving **1:05** for slide changes and interruption. Speaker names are an assignment for rehearsal and can be swapped. Keep the PDF open as the display fallback. The reference slides remain at the back of the deck; do not read them aloud.

| Elapsed | Slides | Speaker | Time | Say this, then move on |
|:--|:--|:--|--:|:--|
| 0:00–0:40 | 1–2 | Adityavardhan | 0:40 | Opening thesis; follow the college outline. |
| 0:40–1:30 | 3 | Adityavardhan | 0:50 | Candidate mission and buyer; no confirmed customer or host. Waiting alone does not create persistent separation. |
| 1:30–2:40 | 4–5 | Adityavardhan | 1:10 | Springs, differential drag, OTVs and electromagnetic prior art. Contribution is the installed-system test, not the first electromagnetic deployer. |
| 2:40–3:20 | 6 | Adityavardhan | 0:40 | Objectives are answered research questions; hardware qualification was outside the evidence. |
| 3:20–4:30 | 7–8 | Adityavardhan | 1:10 | Walk from geometry through force, circuit, release, orbit, mass and numerical checks. Call checks numerical verification, not experimental validation. |
| 4:30–5:20 | 9–10 | Adityavardhan | 0:50 | Show evolution and corrections; dates marked approximate where reconstructed. |
| 5:20–5:50 | 11 | Adityavardhan | 0:30 | State deliverables, then hand over: “Pratham will show the results that changed our design decision.” |
| 5:50–6:35 | 12 | Pratham | 0:45 | Point out cassette, track, sled, release station and brake. It is a FreeCAD review assembly, not built hardware. |
| 6:35–8:25 | 13–14 | Pratham | 1:50 | Historical periodic model: 16.029 m/s. Finite analytic 3-D integral: 1.042 kJ ideal work. Independent 2-D FEM: 1.082 kJ in-plane; separate 3-D numerical surface-charge check: 1.042 kJ ideal. A 14 mm gap gives 0.907 kJ in an illustrative scenario. Conditional assumed-bank rerun: 2.099 kJ gross. None is an achieved or selected speed rating. |
| 8:25–9:10 | 15–16 | Pratham | 0:45 | Precision and orbital lifetime are modeled. Immediate orbital geometry has a two-body cross-check; lifetime does not have the same independent check. |
| 9:10–10:45 | 17–19 | Pratham | 1:35 | Decision slides: 126.6 kg dry / 10.55 kg per 3U fails the ~6 kg spring comparison; side-fed reference layout is 11 mm too narrow; R1 clears scripted routes but is an unselected candidate. |
| 10:45–12:20 | 20–21 | Pratham | 1:35 | Demonstrate the computational chain on slide 20. The finite Gen5 case saves 1.866 kg ideal host propellant in one matched event, yet its device plus resized fuel is 52.717 kg heavier; no twelve-shot case closes. Hand back: “The system-level result is therefore a decision, not a performance claim.” |
| 12:20–13:00 | 22 | Adityavardhan | 0:40 | State the three adverse findings and what the study actually establishes. |
| 13:00–13:45 | 23–24 | Adityavardhan | 0:45 | P124 shows why 1 km/s over 1.3 m implies about 39,220 g for 4 kg; it is separate research. The first Gen6 article needs mission-derived speed, payload load and measured accuracy. |
| 13:45–13:55 | 25–26 | Adityavardhan | 0:10 | Point to sources and invite questions. |

**Handoff rule:** either student must be able to explain slides 13–14, 17–19 and 21. Those are likely to attract technical questions.

## If the panel says eight minutes

Use the *same* deck and skip slides **2, 4, 8–11, 15–16, 19–20, 24–26** while retaining their source pages for questions. Adityavardhan: slides 1, 3, 5–7 in 2:15. Pratham: slides 12–14, 17–18, 21 in 4:20. Adityavardhan: slides 22–23 in 1:05. Allow 0:20 for transitions. Never drop the finite-force, mass or CAD failure slides to save time.

## Demonstration and equipment

1. **Tonight:** each student speaks their half aloud with a stopwatch. Do one uninterrupted rehearsal together and one eight-minute fallback. Cut explanation, not the adverse results. Verify both know who advances slides.
2. **Before the room:** copy the ZIP and its extracted files to two laptops and one USB drive. Open the deck PDF on one machine and the PPTX on the other. Check aspect ratio, readable units/axes, projector colors and fonts. Turn off notifications and sleep. Keep local copies; no network should be required.
3. **During slide 20:** use the two embedded results to explain the reproducible path: historical operating point → adverse finite-force check → matched-mission screen. Explain separately that the two-body orbit check assumes the historical release speed; it does not prove that speed. If asked, open `GEN5_COMPUTATIONAL_REVIEW.pdf` and `GEN5_CAD_REVIEW.pdf`, then the two FreeCAD files. The STEP assemblies are inspection artifacts, not manufacture or motion proof. Do not start a new solver run unless there is extra time and a tested setup.
4. **If software fails:** continue from `VOLLEY_Final_Review_2026-10-10.pdf`. The slides, report PDF, handbook and result JSON are already captured. State plainly that the demonstration is computational and that no hardware exists.
5. **After the talk:** keep `PANEL_HANDBOOK.pdf` open for details and `CLAIM_EVIDENCE_MAP.md` for exact source tracing. Record panel corrections for the report rather than improvising unsupported answers.

## Fast answers for a technical panel

**Where is the prototype?** “There is no physical VOLLEY article. This thesis is a computational system study. I can show the native FreeCAD geometry, STEP exports, solver inputs/results and numerical checks. Qualification requires an instrumented build and provider-specific interface work.”

**Why call it complete if it fails?** “The research question is answered for this defined Gen5 case. The installed 3U mass fails our criterion, the current side-fed layout clashes, and a more finite force treatment challenges the historical speed. We are not claiming design or product maturity.”

**Is 12.448 m/s validated?** “No. It is an ideal-phase result from a finite 3-D analytic force integral. A separate 2-D FEM supports the finite-force decline; P121 independently checks the ideal full-depth integral under shared design assumptions. The bank rerun assumes ideal phase and unselected electrical hardware. No thrust has been measured.”

**Can the R1 STEP file solve the fit problem?** “It resolves the exact-solid route clearance for twelve scripted 3U envelopes after widening the enclosure from 530 to 570 mm. It does not yet supply a credible feed actuator, retention system, tolerance stack or revised mass. We did not silently substitute it for evaluated Gen5.”

**What is the value over springs?** “For one explicitly assumed reference event, our model gives lower ideal host propellant for the finite Gen5 release. But the 12-shot mission does not close in the bounded optimizer, and installed mass loses the 3U comparison. Springs remain a strong baseline.”

**Why no independent thrust FEM or test?** “Those are open closure tasks. Our honest result is a negative screen and a bounded model discrepancy, not a motor rating. A selected configuration should be compared with an independent electromagnetic solver and a calibrated force measurement.”

**What about 1 km/s?** “That is a Gen6 investigation limit, not an achieved result or current product specification. We will compare mechanisms and reject any target that fails acceleration, energy, mass, thermal or integration constraints.”

**Is the IEEE paper accepted?** “No. We have an IEEE-formatted draft and companion computation record. A venue is not selected and no peer-review acceptance is claimed.”

**What can we defend today?** “The exact model definitions, reported numerical runs, CAD interference finding, mass arithmetic, bounded mission comparison and limitations. We cannot defend actual flight performance, universal payload compatibility, provider approval or commercial demand.”

## Numbers to memorize

| Finding | Correct description |
|:--|:--|
| 16.029 m/s | Historical periodic-force model prediction; challenged |
| 12.448 m/s | Ideal-phase finite-geometry analytic screen; 2-D FEM supports force trend, but no selected motor rating |
| 126.6 kg dry; 174.6 kg loaded | Modeled Gen5 installed mass |
| 10.55 kg versus about 6 kg | Per-3U deployer mass; preset parity test fails |
| 11 mm; 32,915 mm³ per cassette | Reference side-fed CAD width deficit and overlap |
| 4/12 spring; 1/12 finite Gen5 | Accepted prefixes in one bounded common-input campaign; no full closure |

**One final rule:** when challenged, give the source and boundary condition first. Do not turn numerical verification into physical validation or future Gen6 targets into achieved Gen5 results.
