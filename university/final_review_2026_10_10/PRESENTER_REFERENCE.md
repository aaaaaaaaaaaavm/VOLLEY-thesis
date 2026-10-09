---
title: "VOLLEY | Presenter Reference"
subtitle: "Slide notes, key numbers, equations, and viva preparation"
author:
  - Adityavardhan Mishra
  - Pratham Chawla
date: "10 October 2026"
geometry: margin=18mm
papersize: a4
fontsize: 11pt
colorlinks: true
linkcolor: teal
toc: true
toc-depth: 1
---

**Guide:** Vikas Gulia<br>
**Student PRNs:** Adityavardhan Mishra — 23070125054; Pratham Chawla — 23070125029<br>
**Carry with:** main PPTX and panel handbook<br>
**Purpose:** private cue book for both presenters; it is not a script to read word-for-word.

> **One-line answer if asked what exists:** “We have a documented computational Gen5 design with numerical cross-checks. We have not built or experimentally validated it. The later Gen6 programme is an open architecture trade aimed at a reviewable first test article.”

# Before entering the room

- Bring the main PPTX, a PDF export of the same slides, the panel handbook PDF, and this reference PDF on two devices/USB copies if possible.
- Confirm the projector can read the title, units, figure axes and footer caveats. Use the PDF export if animations or fonts shift in PowerPoint.
- Open the model result files or screenshots for the simulation demonstration. Do not imply a live physical demo.
- Decide which student covers each section. A natural handoff is after **Timeline** (slide 10) or after **Methodology** (slide 8); either student should be ready to answer questions across the whole project.
- With an unknown time limit, begin with a brief introduction and ask the panel for their preferred duration before presenting. If they want a short version, use the route below.

## Short route if time is limited

Prioritize slides **1, 3, 5–7, 9, 11–13, 15–21**, keeping the literature and model tables brief. Never skip the mass failure, evidence boundary, or conclusion. Slides 22–23 are references for questions. The full route follows all 23 slides in order.

# Slide-by-slide speaking notes

## 1. Title

“We are Adityavardhan Mishra and Pratham Chawla, guided by Vikas Gulia. VOLLEY studies controlled release of CubeSats from a hosted orbital platform. Today we present the Gen5 analytical thesis results, then clearly separate the Gen6 direction and the evidence still needed.” Point to the image as a CAD render, not physical hardware.

## 2. Outline

Follow the university-requested order exactly: introduction, literature, gap, objectives, methodology, timeline, progress, results, conclusion, future work and references. Explain that results include failures and limitations because these are part of the engineering decision.

## 3. Introduction

The central problem is that a rideshare CubeSat gets the primary mission's orbit. Springs provide essential clearance but generally only a small separation velocity. Timing can already create in-track phasing; VOLLEY's additional question is whether commandable release changes orbital energy enough to justify its mass. The host, if capable and permitted, makes coarse moves. VOLLEY would set the local release state of each satellite. There is no approved host.

## 4. Literature review

Do not describe springs as “obsolete” or “unable to change orbit.” Every impulse changes the orbit. Springs are the benchmark for simplicity and heritage. Timed release and differential drag address some phasing needs. A transfer vehicle addresses larger moves but carries its own burden. Electromagnetic work predates VOLLEY: Feng *et al.* models high-speed on-orbit launch, and Zhao *et al.* studies stacked CubeSat transfer/storage. These works narrow the novelty claim.

## 5. Research gap

Say: “Our contribution is the coupled, installed-system question: commandable release for an unmodified satellite at moderate acceleration, with magazine, power, brake, host interaction and mass counted.” Do not claim the first electromagnetic deployer. “Unmodified” is a design objective, not proof that every payload is compatible; the magnetic and mechanical interface still needs qualification.

## 6. Objectives

Walk down the status column. Architecture is defined and modelled. Shot and orbit outcomes are predictions. Installed mass was counted and produced an unfavorable 3U result. The next-test path is specified but not completed. If asked whether objectives were “achieved,” distinguish the **research objectives** (study, quantify, compare) from **product maturity** (hardware performance and compatibility). Do not award yourself completion solely because documents exist.

## 7. Research methodology — flow

Describe one example along the chain: choose the 3U case; size the geometry and magnet sled; calculate force, pulse and release state; propagate the orbit; compare its value against a spring and its burden against a spring canister; challenge the model with independent numerical checks. The process is iterative: findings changed the baseline, including the sled mass and magnetic thrust integral.

## 8. Research methodology — evidence

Field agreement at a tested location is not an independent thrust measurement. ngspice checks circuit behavior under assumed components. CalculiX checks a defined structural boundary case. OpenFOAM checks aerodynamic behavior, not vacuum release contact. GMAT and alternate propagation show that atmosphere matters. Use the words **numerical verification** or **cross-check** for these, and reserve **experimental validation** for physical measurements.

## 9. Timeline — past

Emphasize documented decisions rather than claiming all early dates were exact. The host concept is documented in 2023. The move toward a linear synchronous motor is approximately mid-2025. CAD and model development spans 2025–26. July–September 2026 focused on cross-checks, corrections and thesis preparation. The Gen6 trade reopened in September 2026.

## 10. Timeline — future

N0 through N5 are evidence gates, not a promise of completion by a particular calendar date. The sequence prevents choosing hardware before the mission/payload/host case and acceptance bands are fixed. N5 is a first-test evidence package; independent build/test release needs additional closure. The 1 km/s high end could be rejected by acceleration, energy, travel, payload or provider constraints.

## 11. Work progress

Show the tangible record: manuscript, CAD, scripts, numerical run sheets, baseline, provenance and defect register. Distinguish it from what is absent: a built article, measured field/shot, qualified payload and host agreement. Avoid any percentage-complete claim. Acknowledge that the later gas and spring-cell studies are historical comparators, not selected Gen6 hardware.

## 12. Results — architecture

Explain the chain in the CAD render: cassettes feed a 3U satellite; the reusable magnet sled is driven along the 1.5 m track; the payload departs; the sled is arrested. The model includes a 9.45 kg CAD-derived sled. The large sled makes recovery, braking, power and mass central rather than ancillary details. No component in this image has been built for VOLLEY.

## 13. Results — rated shot

At the rated 3U operating point, the model predicts 16.029 m/s and 10.07 g. Gross electrical draw is 2,782 J, of which the payload receives about 514 J as kinetic energy. Only 47 J is recovered after release within the available 39 mm zone; 1,162 J of sled energy goes to the brake. Net electrical-to-payload efficiency is 18.8%. Peak current is 320 A over a 162.3 ms pulse. Do not say “tested,” “measured,” or “qualified.”

## 14. Results — command precision

The closed-loop simulation produces a 0.0274 m/s ($3\sigma$) spread around a 15.8 m/s setpoint. It includes assumed sensor and plant tolerances, with control headroom. A panel member may ask whether that precision survives real contacts, thermal changes or payload variability. Answer: those are unmeasured and require an instrumented release test and model correlation.

## 15. Results — orbit

The model predicts a 28.8 km semi-major-axis rise and a 1.60× lifetime multiplier at mean solar activity for one maximum-velocity release. The exact multiplier is not universal. A prior invariance claim failed an independent propagator check, and the current 1.60 result has not been independently rerun at its precise updated operating point. Timing alone can phase satellites; the energy change is the reason to consider a larger release impulse.

## 16. Results — mass

This is the decisive negative result. Dry mass is 126.6 kg, loaded mass 174.6 kg. The twelve-3U configuration spends 10.55 kg of deployer per satellite, about 1.76 times the roughly 6 kg spring-canister comparison. The predeclared criterion was within 15%, so Gen5 fails. A modelled 50.04 kg enclosure replaced an 8 kg placeholder and exposed the penalty. Do not imply the full assembly is mass-competitive for 3U.

## 17. Results — limits

The three major practical uncertainties are payload interface (contact, arrest load, magnetic cleanliness), shared reliability (a jam can affect later satellites), and host compatibility. These determine whether a modelled shot could become a safe product. Explain that a numerical result at a declared boundary is useful but narrower than physical evidence. A single well-designed discriminating coupon can be more decisive than many new plots.

## 18. Results — simulation demonstration

Walk through four transparent steps: choose the modelled 3U case; show the shot figure and operating-point table; feed its release state into the orbit model; compare predicted orbital change and installed mass with the spring benchmark. The panel can inspect the scripts and records in the project archive. If the computer cannot run a script during the review, the slide and handbook reproduce the same model chain. Call this a **computational demonstration**.

## 19. Conclusion

“The thesis establishes a coherent analytical case for commandable release and records a conditional orbital benefit. It also finds that Gen5 fails the 3U mass criterion and is not physically validated. The conclusion is to retain the evidence and reopen the mechanism trade.” End on the decision supported by results, not on an unsupported promise of flight use.

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
That is a valid way to obtain in-track spacing and must be the baseline. Timing alone does not provide the same immediate semi-major-axis change that a directed impulse can supply.

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
