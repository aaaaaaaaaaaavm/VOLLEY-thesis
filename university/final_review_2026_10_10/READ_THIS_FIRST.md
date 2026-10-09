# How to present Gen5 tomorrow with the old numbers and known errors

**Decision for the 10 October 2026 college review:** present VOLLEY as a **computational feasibility and design-decision study**. Do not call Gen5 a finished deployer, a frozen product baseline, a validated motor, or a qualified satellite interface. The value of the work is that it tests the whole installed system and records why the current 3U design cannot be selected. A negative engineering finding can be a valid research result when the assumptions, comparison and limitations are visible.

The college's supplied final-review rubric awards 10 marks for objectives, 10 for technical quality, 5 for results/validation/analysis, 5 for documentation, and 10 for presentation/demonstration/viva. Its separate “Additional Recognition” section offers special consideration for a functional physical prototype; the 40-mark rubric does **not** state that a prototype is mandatory. A computational demonstration is honest if it is called that.

## What to do with each headline claim

| Earlier headline | Tomorrow's treatment | Why |
|:--|:--|:--|
| 16.029 m/s rated Gen5 release | **Historical periodic-force model output. Do not use as a demonstrated or selected rating.** Keep one slide so the correction is traceable. | P118's finite-position force integral challenges the assumption of constant periodic force across the stroke. |
| 12.448 m/s finite-force result | **Ideal-phase analytic screen, not a replacement rated speed.** | A separate 2-D FEM gives 1.082 kJ ideal work, but omits magnet-depth end effects. No measured thrust or selected switching hardware exists. |
| 10.07 g, 2.782 kJ, 18.8%, 0.0274 m/s dispersion | **Conditional outputs of the historical shot/control model.** Do not carry them into a revised performance specification. | P117 reconciles the old 124.488 J remainder to model assumptions; P120 reruns finite force with an assumed bank and gives 2.099 kJ gross. Control, switching and contact remain open. |
| +28.8008 km immediate orbit rise, 1.60× lifetime | **Historical 16.029 m/s orbit-input scenario.** The immediate two-body geometry is cross-checked; lifetime is not independently closed for the current case. | Orbital propagation can correctly use an assumed impulse without proving that Gen5 can produce that impulse. |
| 126.6 kg dry; 10.55 kg per 3U versus ~6 kg spring canister | **Current modeled mass finding and clear adverse comparison.** | The installed system fails the stated 15% comparator band. A stricter historical 2 kg/3U screening target also fails; keep the distinct thresholds labeled. |
| 11 mm width deficit and 32,915 mm³ clash per cassette | **Reference side-fed placement fails the CAD check.** | Exact-solid check is a geometric finding for this placement, not a rejection of every possible feeder. |
| R1 twelve-route clearance | **Unselected geometry candidate only.** | It lacks feed actuation, launch retention, tolerances, revised mass, and provider interface; it cannot silently repair evaluated Gen5. |
| 2.693 versus 0.827 kg ideal host propellant | **One assumed, matched target screen using the finite-force ideal upper speed.** | Neither the bounded 12-shot spring nor Gen5 campaign closes. It is not a proven mission or customer saving. |
| Gen6 1 km/s | **Future upper investigation target.** | No selected mechanism or performance evidence exists. |

## What must be said before the results

“The original 16 m/s operating point remains in the record as a historical model case. A finite-geometry check has since challenged its force assumption; a separate 2-D field solve supports the declining finite-force trend. The bank rerun still assumes ideal phase and unselected components, so we are not claiming a verified speed. The old orbit and energy plots are conditional inputs, while the mass and CAD failures drive the design decision.”

This sentence prevents the panel from discovering the correction before you mention it. Do not wait for Q&A to reveal it.

## What the final slide should mean

**Defensible conclusion:** “For the defined 3U reference case, Gen5 as currently modeled does not pass selection. The evidence shows a mass disadvantage and an invalid side-fed placement; 2-D FEM and a conditional bank rerun narrow the speed question but do not establish a motor rating. The study produces a documented decision and a concrete experimental agenda.”

**Avoid:** “Gen5 is complete and validated, and Gen6 only scales it.” The newer force, mass and CAD evidence does not support that statement. Gen6 should reopen mechanism selection rather than promise a scaled copy.

## If asked why you are presenting before all engineering is complete

“A college final review can examine a finished computational investigation with adverse results. We have built the traceable models, CAD exchange files, cross-checks and reports, but no physical article and no flight qualification. The additional work required for an IEEE performance paper or a product is stated explicitly. We are submitting the study's actual answer, not substituting literature evidence for a test of VOLLEY.”

## Tonight's go/no-go checks

1. Use the **updated** `VOLLEY_Final_Review_2026-10-10.pdf` or `.pptx`, not an older download. Verify slide 1 says “Gen5 computational feasibility review” and slide 20 shows the finite-force and matched-mission figures.
2. Both speakers rehearse the 15-minute route in `TOMORROW_RUN_SHEET.pdf`. Either speaker must explain the 16.029/12.448 distinction, mass failure and CAD clash.
3. Check that the PDF, PPTX, handbook and full report open **offline** on the actual presentation computer. Bring a second copy. If the slide export is unreadable, present from the PDF.
4. Leave time for questions. When a question goes beyond evidence, identify the missing input or test; do not guess a performance figure.
