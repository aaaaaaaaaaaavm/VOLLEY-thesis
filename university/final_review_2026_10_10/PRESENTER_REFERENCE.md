---
title: "VOLLEY | Presenter Reference"
subtitle: "Slide notes, key numbers, equations, and viva preparation"
author:
  - Adityavardhan Mishra
  - Pratham Chawla
date: "10 October 2026"
geometry: margin=18mm
papersize: a4
fontsize: 10pt
colorlinks: true
linkcolor: teal
toc: true
toc-depth: 1
---

**Guide:** Vikas Gulia<br>
**Student PRNs:** Adityavardhan Mishra — 23070125054; Pratham Chawla — 23070125029<br>
**Carry with:** main PPTX and panel handbook<br>
**Purpose:** private cue book for both presenters; it is not a script to read word-for-word.

> **Opening thesis statement:** “We completed a system-level computational study of a commandable CubeSat deployer. It predicts an orbital benefit but fails our preset 3U mass comparison. The Gen5 research question has an answer; physical qualification and Gen6 belong to the next phase.”

## Rehearsed opening and close

**Opening (about 35 seconds):** “Our thesis asks whether a hosted deployer can give each rideshare CubeSat a commanded release condition that improves its orbit enough to justify the whole machine. We completed the Gen5 system design and computational evaluation. At the rated 3U point it predicts a 16.0 m/s release and an orbit benefit, but complete mass accounting fails the preset comparison with spring canisters. We will show the method, the numerical checks, and the decision that follows.”

**Close (about 25 seconds):** “The research question now has an evidence-based answer. A commanded release has conditional orbital value in the model, but this Gen5 configuration is not competitive on the stated 3U mass criterion. That finding closes the Gen5 analytical study. Physical qualification and the Gen6 mechanism trade are future work.”

Aim for an 11-minute full route in rehearsal, then shorten to the key slides if the panel gives a tighter slot. The numerical claims and failure criterion should remain in either route.

# Before entering the room

- Bring the main PPTX, a PDF export of the same slides, the panel handbook PDF, and this reference PDF on two devices/USB copies if possible.
- Confirm the projector can read the title, units, figure axes and footer caveats. Use the PDF export if animations or fonts shift in PowerPoint.
- Open the model result files or screenshots for the simulation demonstration. Do not imply a live physical demo.
- Decide which student covers each section. A natural handoff is after **Timeline** (slide 10) or after **Methodology** (slide 8); either student should be ready to answer questions across the whole project.
- If the review slot is still unknown on arrival, confirm it before starting and use the rehearsed full or short route accordingly.

## Short route if time is limited

Prioritize slides **1, 3, 5–7, 9–13, 15–16, 18–20**, keeping the literature and model tables brief. Lead with the thesis answer and close on the engineering decision. Keep the mass failure and evidence boundary. Slides 22–23 are references for questions. The full route follows all 23 slides in order.

# Slide-by-slide speaking notes

## 1. Title

“We are Adityavardhan Mishra and Pratham Chawla, guided by Vikas Gulia. We completed a system-level computational evaluation of controlled CubeSat deployment. The study predicts useful orbital change but finds that our Gen5 design fails the 3U mass target. We will show the design, methods and result before briefly outlining Gen6 future work.” The cover image is the university logo; show the CAD render on slide 12 as a model, not physical hardware.

## 2. Outline

Follow the university-requested order exactly: introduction, literature, gap, objectives, methodology, timeline, progress, results, conclusion, future work and references. Explain that results include failures and limitations because these are part of the engineering decision.

## 3. Introduction

The central problem is that a rideshare CubeSat gets the primary mission's orbit. Springs provide essential clearance but generally only a small separation velocity. Timing can already create in-track phasing; VOLLEY's thesis question is whether commandable release changes orbital energy enough to justify its full installed mass. Say the finding early: the model predicts orbital benefit, but Gen5's 3U mass comparison fails. The host, if capable and permitted, makes coarse moves; VOLLEY sets the local release state. There is no approved host.

## 4. Literature review

Do not describe springs as “obsolete” or “unable to change orbit.” Every impulse changes the orbit. Springs are the benchmark for simplicity and heritage. Spring impulse and differential drag address some phasing needs. Waiting alone between zero-relative-impulse releases from an unchanged host does not. A transfer vehicle addresses larger moves but carries its own burden. Electromagnetic work predates VOLLEY: Feng *et al.* models high-speed on-orbit launch, and Zhao *et al.* studies stacked CubeSat transfer/storage. These works narrow the novelty claim.

## 5. Research gap

Say: “Our contribution is the coupled, installed-system question: commandable release for an unmodified satellite at moderate acceleration, with magazine, power, brake, host interaction and mass counted.” Do not claim the first electromagnetic deployer. “Unmodified” is a design objective, not proof that every payload is compatible; the magnetic and mechanical interface still needs qualification.

## 6. Objectives

Walk down the outcome column as completed research tasks: the architecture was modelled; shot, circuit and orbital results were calculated; installed mass was counted; key numerical claims were challenged. The mass criterion failed, which is itself a finished result. If asked whether objectives were achieved, distinguish completing a research evaluation from proving hardware performance. The latter was outside this computational thesis's evidence.

## 7. Research methodology — flow

Describe the completed chain in past tense: we chose the 3U case; sized geometry and magnet sled; calculated force, pulse and release state; propagated the orbit; compared orbital value and installed mass with springs; and challenged models through independent numerical checks. The checks changed the final baseline, including the sled mass and magnetic thrust integral.

## 8. Research methodology — evidence

Summarize what the completed checks established and their scope. Field agreement at a tested location is not an independent thrust measurement. ngspice checks circuit behavior under assumed components. CalculiX checks a defined structural boundary case. OpenFOAM checks aerodynamic behavior, not vacuum release contact. GMAT and alternate propagation show that atmosphere matters. Use **numerical verification** or **cross-check** for these, and reserve **experimental validation** for physical measurements.

## 9. Timeline — past

Emphasize documented decisions rather than claiming all early dates were exact. The host concept is documented in 2023. The move toward a linear synchronous motor is approximately mid-2025. CAD and model development spans 2025–26. July–September 2026 focused on cross-checks, corrections and the thesis record. The final review presents that completed Gen5 analysis.

## 10. Timeline — corrections in the final baseline

This is the strongest proof that the thesis is a finished analysis rather than an early proposal. CAD-derived sled mass displaced an optimistic parametric estimate; a depth-resolved thrust integral lowered the rated velocity; a real enclosure buildup exposed the mass failure; and an independent propagator check rejected an overbroad solar-activity claim. State that the reported numbers are the corrected baseline and that failed claims were retained in the record. Do not present these as physical validation.

## 11. Work progress

Show tangible completed deliverables: manuscript, CAD, system model, scripts, numerical run sheets, baseline, provenance and defect register. State that the thesis closes an analytical question; hardware tests, a qualified payload and host agreement are separate development milestones. Avoid a percentage-complete claim, since research completion and product readiness are different dimensions.

## 12. Results — architecture

Explain the chain in the CAD render: cassettes feed a 3U satellite; the reusable magnet sled is driven along the 1.5 m track; the payload departs; the sled is arrested. The model includes a 9.45 kg CAD-derived sled. The large sled makes recovery, braking, power and mass central rather than ancillary details. No component in this image has been built for VOLLEY.

## 13. Results — rated shot

At the rated 3U operating point, the model predicts 16.029 m/s and 10.07 g. Gross electrical draw is 2,782 J, of which the payload receives about 514 J as kinetic energy. Only 47 J is recovered after release within the available 39 mm zone; 1,162 J of sled energy goes to the brake. Net electrical-to-payload efficiency is 18.8%. Peak current is 320 A over a 162.3 ms pulse. Do not say “tested,” “measured,” or “qualified.”

## 14. Results — command precision

The closed-loop simulation produces a 0.0274 m/s ($3\sigma$) spread around a 15.8 m/s setpoint. It includes assumed sensor and plant tolerances, with control headroom. A panel member may ask whether that precision survives real contacts, thermal changes or payload variability. Answer: those are unmeasured and require an instrumented release test and model correlation.

## 15. Results — orbit

The model predicts a 28.8 km semi-major-axis rise and a 1.60× lifetime multiplier at mean solar activity for one maximum-velocity release. The exact multiplier is not universal. A prior invariance claim failed an independent propagator check, and the current 1.60 result has not been independently rerun at its precise updated operating point. A relative state produced by spring impulse, drag or a host maneuver can phase satellites; the larger energy change is the reason to consider a commanded release impulse.

## 16. Results — mass

This is the decisive negative result. Dry mass is 126.6 kg, loaded mass 174.6 kg. The twelve-3U configuration spends 10.55 kg of deployer per satellite, about 1.76 times the roughly 6 kg spring-canister comparison. The predeclared criterion was within 15%, so Gen5 fails. A modelled 50.04 kg enclosure replaced an 8 kg placeholder and exposed the penalty. Do not imply the full assembly is mass-competitive for 3U.

## 17. Results — limits

Give the three-part decision in order: (1) the system model supports a commandable release with conditional orbital-energy benefit, (2) the full 3U mass result fails the selection criterion, and (3) physical behavior remains unverified. Payload interface, shared reliability and host compatibility are future tests, not missing steps in the completed mass comparison. A numerical result at a declared boundary is narrower than physical evidence.

## 18. Results — simulation demonstration

Walk through four transparent steps: choose the modelled 3U case; show the shot figure and operating-point table; feed its release state into the orbit model; compare predicted orbital change and installed mass with the spring benchmark. The panel can inspect the scripts and records in the project archive. If the computer cannot run a script during the review, the slide and handbook reproduce the same model chain. Call this a **computational demonstration**.

## 19. Conclusion

“We completed the Gen5 system-level computational evaluation. It predicts a useful orbital-energy change, but the complete configuration fails our preset 3U mass criterion. Numerical checks made that conclusion more credible and defined its limits. Gen5 is therefore a finished research result, not a selected 3U flight configuration.” End on this decision. Future work follows as a separate section.

## 20. Future work — Gen6

Gen6 retains the mission and reopens hardware selection. One reusable path must sequentially accept different supported payload classes. The research envelope is about 1–2 m/s through 1 km/s. The high end is a study target, not a validated speed. Electromagnetic drive is interesting but not selected; compare it with mechanical, stored energy, gas/fluid, hybrid, BOLLEY and conventional paths using the same mission and installed-burden accounting.

## 21. Future work — test article

The target is one named, independently reviewable test-article configuration: controlled geometry, BOM, interfaces, mass/energy/thermal budgets, assembly and inspection, calibration and instrumentation, pass/fail and stop criteria, uncertainty and retained failures. A configuration may be rejected. Physical manufacture, testing and qualification are later milestones. Avoid calling N5 itself “the prototype complete.”

## 22–23. References

Offer the panel handbook for the fuller bibliography. Distinguish published/agency sources from our own project manuscript and PLAN-R2. If a panel member asks for a numerical source, give the relevant baseline, figure and run sheet rather than citing “the internet.”

# Key numbers card

| Quantity | Defensible phrase |
|:--|:--|
| 16.029 m/s | “Gen5 modelled 3U exit velocity” |
| 10.07 g | “Modelled payload acceleration, not payload qualification” |
| 2,782 J | “Gross modelled bank draw per shot” |
| 47 J | “Modelled recovered energy in available zone” |
| 1,162 J | “Modelled sled energy dissipated by brake” |
| 18.8% | “Net modelled electrical-to-payload efficiency” |
| 0.0274 m/s ($3\sigma$) | “Closed-loop simulated velocity dispersion” |
| 126.6 / 174.6 kg | “Gen5 modelled dry / loaded mass” |
| 10.55 versus ~6 kg | “Gen5 versus spring mass per 3U customer” |
| 28.8 km | “Predicted semi-major-axis rise for the stated shot” |
| 1.60× | “Predicted lifetime at mean solar activity, conditional” |
| 1–2 m/s to 1 km/s | “Gen6 investigation envelope, not achieved performance” |

# Equations to recall

- Payload kinetic energy: $E_k = \tfrac12 m v^2$. With $m=4$ kg and $v\approx16$ m/s, $E_k\approx512$ J (baseline: 514 J).
- Mean acceleration over a constant-acceleration approximation: $a\approx v^2/(2s)$. It is a sanity check, not a substitute for the modelled time-varying force and the 10.07 g reported result.
- Release momentum/recoil is approximately $p=mv$ for the payload; the complete host impulse must also include sled and actuator dynamics. The thesis baseline reports 64.1 N·s recoil per shot for its defined case.
- Mass per 3U customer: $126.6/12=10.55$ kg. Against ~6 kg, the ratio is ~1.76; the target band was ±15%.
- Electrical-to-payload efficiency: payload kinetic energy divided by **net** electrical draw, $514/(2782-47)\approx18.8\%$.

# Likely viva questions

**What is genuinely new?**<br>
Not electromagnetic launch itself. The thesis's narrow contribution is a commandable moderate-acceleration release of an unmodified CubeSat with the whole magazine, power, brake, mass and orbital-use case analysed together. Prior art narrows even this, so it is a research proposition, not a proven patent claim.

**Why not just release satellites at different times?**<br>
Different release times can matter if the host maneuvers, spring impulses differ, or differential drag accumulates. Waiting alone between zero-relative-impulse releases from an unchanged host does not create persistent in-track spacing. A conventional spring release is the baseline; a larger directed impulse may change semi-major axis more quickly.

**Why not put propulsion on each CubeSat?**<br>
That is a competent alternative, especially at 3U. The thesis mass comparison even shows Gen5's per-customer deployer mass is unfavorable for 3U. The value proposition may vary by payload class and mission; it is not assumed.

**What is the strongest result against your own idea?**<br>
The full 3U mass rollup: 10.55 kg per customer against about 6 kg for the spring comparator. The preset 15% parity criterion fails.

**What has actually been validated?**<br>
No hardware. Some models have independent numerical checks at particular points and boundary conditions. We should call those verification/cross-checks and state exactly what they do not test.

**Can an unmodified CubeSat withstand 10 g and the magnetic field?**<br>
That cannot be assumed. Structural, shock and magnetic-cleanliness requirements are payload-specific and would need a named payload/interface, testing and provider approval.

**What about a failed reload or latch?**<br>
Shared mechanisms can threaten later releases. The defect and reliability analyses identify that exposure; cycle-life and fault-recovery measurements are needed before claiming reliability.

**Is 1 km/s achievable by Gen6?**<br>
No such result exists. It is an upper research target for screening architectures. Travel length, acceleration, energy, loads, thermal behavior and provider constraints may reject it.

**Has a provider agreed to host VOLLEY?**<br>
No. Published host examples are parametric worked cases. Compatibility requires provider interface data and agreement.

**What is the next experiment?**<br>
First freeze the selected mission and configuration. Then use a discriminating instrumented coupon to measure the mechanism's force/contact/release behavior and compare it with predeclared acceptance and stop criteria. The exact coupon follows the Gen6 trade, not the other way around.

# Phrases to avoid in the review

| Avoid | Say instead |
|:--|:--|
| “We built/tested VOLLEY” | “We designed and analysed Gen5; no hardware test has occurred.” |
| “Validated 16 m/s” | “The Gen5 model predicts 16 m/s; selected numerical checks exist.” |
| “CubeSats can tolerate 10 g” | “Payload-specific qualification has not been done.” |
| “VOLLEY is lighter than springs” | “Gen5 fails the 3U spring-canister mass comparison.” |
| “Gen6 reaches 1 km/s” | “Gen6 must investigate up to 1 km/s; no mechanism is selected.” |
| “ISRO/Skyroot is our partner” | “They were worked host examples, without approval or integration.” |
| “We invented electromagnetic CubeSat deployment” | “The literature contains related electromagnetic approaches.” |

# Source quick map

- Main results and narrative: `../../source/paper.tex` at local head `b30ffdc` (28 September 2026).
- Rated values: `../../appendix/BASELINE.md`.
- What is and is not checked: `../../appendix/PROVENANCE.md`.
- Design-critical open issues: `../../appendix/OPEN_PROBLEMS.md`.
- Historical milestone confidence: `../../appendix/HISTORY.md`.
- Gen6 target and gates: `CURRENT PLAN AND STATUS — PLAN-R2`, 29 September 2026.
- University scoring: attached `B-Tech Docs required.pdf`.
