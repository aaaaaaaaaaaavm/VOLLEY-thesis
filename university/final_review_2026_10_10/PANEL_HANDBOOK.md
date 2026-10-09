---
title: "VOLLEY | Final B.Tech Project Review"
subtitle: "Panel handbook: completed Gen5 study, findings, and future direction"
author:
  - Adityavardhan Mishra
  - Pratham Chawla
date: "10 October 2026"
geometry: margin=20mm
papersize: a4
fontsize: 10pt
colorlinks: true
linkcolor: teal
toc: true
toc-depth: 2
---

**Guide:** Vikas Gulia<br>
**Student PRNs:** Adityavardhan Mishra — 23070125054; Pratham Chawla — 23070125029<br>
**Department:** Mechanical Engineering, Symbiosis Institute of Technology<br>
**Review type:** Final Project Presentation & Demonstration

> **Scope of the completed thesis.** VOLLEY is a system-level engineering design and computational research project. The Gen5 evaluated configuration and adverse numerical findings are documented; decisive force and mission closure remain open. The results are predictions, with numerical cross-checks where identified. Physical prototype testing, CubeSat qualification and provider accommodation belong to a later development phase. Gen6 is presented separately as future work.

![Analysed Gen5 electromagnetic deployer configuration. CAD render; no physical article exists.](<../../cad/renders/gen5/exploded.png>){width=88%}

# Executive summary

VOLLEY investigates a last-mile problem in rideshare launches: a secondary CubeSat reaches orbit but ordinarily receives the orbit selected for the primary payload. A spring deployer separates it safely, often at roughly 1–2 m/s; that relative impulse, later drag differences, or host maneuvering can change its in-track phase. Deployment time by itself does not create persistent phase separation from an otherwise unchanged co-orbital host. A larger, deliberately commanded release velocity can also change orbital energy. The thesis evaluates whether that added capability justifies a complete deployer system. The mission model splits responsibilities between a maneuvering host, which performs coarse repositioning, and a deployer, which supplies each satellite's commanded release condition.

The authored thesis analyses one Gen5 solution: a magazine-fed, linear synchronous motor driving a reusable magnetic sled. The historical periodic-force 3U model predicts **16.0 m/s** exit speed at **10.07 g**. Its modeled dry-mass rollup is **126.6 kg**, and the power model predicts **2.782 kJ** gross electrical draw per shot. A closed-loop simulation predicts **0.0274 m/s ($3\sigma$)** exit-speed dispersion at a 15.8 m/s setpoint. For an assumed historical 16.029 m/s input, the orbit model raises semi-major axis by **28.8 km**, with a **1.60×** modelled lifetime multiplier at mean solar activity. The lifetime result is atmosphere-sensitive and has not been independently rerun for that assumed historical input.

Gen5 also produced a decisive negative result. With twelve 3U satellites, its deployer mass is **10.55 kg per customer**, versus about **6 kg** for the spring canister comparator used in the thesis. This is **1.76×** as much hardware per 3U payload and fails the preset 15% mass-parity band. The study therefore reaches a decision: the conditional modelled orbital benefit does not make this Gen5 configuration a defensible 3U selection. The result completes the analytical comparison; it does not require a prototype to know that the modelled mass criterion failed. Physical payload loads, magnetic cleanliness, cycle life, and provider interfaces remain questions for a different evidence phase.

The later Gen6 programme retains the hosted sequential-deployment mission while reopening mechanism choice. It investigates an approximately **1–2 m/s to 1 km/s** release-speed envelope across electromagnetic, mechanical, stored-energy, gas/fluid, hybrid, BOLLEY and conventional options. The high end is a requirement to examine and may prove infeasible. The near-term goal is one named, reproducible, independently reviewable test-article configuration with a corresponding build/test release decision.

# New decisive findings: finite force, feeder route and matched mission

The 16.029 m/s shot result assumes periodic thrust throughout a 1.3 m powered stroke. A new 3-D analytic integration of the exact cuboid field over the CAD's finite 162-belt stator finds **1.042 kJ ideal work**, corresponding to **12.448 m/s only under optimal phase with switching, voltage and friction losses omitted**. The modeled mover array and stator stop directly overlapping after 1.066 m travel. The 336 mm magnetic model and 340 mm CAD envelope also disagree. Cross-section quadrature refinement changes the three checked station forces by at most 0.369%; halving station spacing changes work by 0.096%. The magnetic field law is shared with the earlier model, so this is an adverse analytic screen, **not an independent 3-D FEM or a hardware test**. The historical 16.029 m/s remains in older tables for traceability and must not be called demonstrated performance. See [P118](../../validation/P118_gen5_finite_force_map.md).

![Finite-array/stator model force versus position; no physical measurement.](<../../figures/gen5_finite_force_map.png>){width=96%}

A separate **2-D finite-element magnetostatic solve** of the finite magnet array gives **1.082 kJ ideal work** on its finest 1 mm mesh, compared with the 3-D analytic screen's 1.042 kJ. The 2-to-1 mm mesh change is 0.59%; a larger air boundary changes the 2 mm work by 0.0004%. The solver uses a different field formulation but omits magnet-depth end effects, so the two absolute results must not be combined into an achieved speed. [P119](../../validation/P119_gen5_finite_force_fem2d.md) records meshes, convergence and assumptions.

![Independent 2-D finite-element force screen, not a measurement.](<../../figures/gen5_finite_force_fem2d.png>){width=96%}

A separate **depth-resolved 3-D numerical surface-charge implementation** integrates the full 90 mm magnet depth and all 162 stator belts. It independently returns **1.042 kJ ideal work**, matching P118 under shared geometry, remanence and ideal-phase assumptions. Face quadrature refinement from 16 to 24 nodes changes work by 0.00002%; halving the station spacing changes work by 0.096%. This checks the numerical formulation, not a selected motor or physical thrust. An illustrative 14 mm face gap gives **0.907 kJ** rather than 1.042 kJ at 12 mm, a 13.0% ideal-work reduction. A 10 mm copper-depth offset gives 0.961 kJ. These are deterministic sensitivity cases, not tolerance specifications. See [P121](../../validation/P121_gen5_finite_force_surface3d.md) and [P122](../../validation/P122_gen5_finite_force_sensitivity.md).

![Ideal gap/depth sensitivity; scenarios rather than measured tolerances.](<../../figures/gen5_finite_force_sensitivity.png>){width=96%}

A **conditional finite-force bank/trajectory rerun** retains the historical 96 V, 6 F, 12 mΩ source and assumed converter. With the full 1.3 m winding energized it computes **2.099 kJ gross capacitor draw** and 927 J copper heat; an illustrative 0.34 m active-copper branch gives 1.394 kJ gross and 243 J copper heat. Both report 12.448 m/s because the force curve is imposed at ideal phase; no voltage-limited switching law or selected winding/inverter exists. The old 2.782 kJ, brake and control outputs are not revised ratings. [P120](../../validation/P120_gen5_finite_coupled_shot.md) gives the time history and energy ledger.

![Finite-force speed and assumed bank energy histories.](<../../figures/gen5_finite_coupled_shot.png>){width=96%}

An **unselected R1 geometry candidate** uses a 570 mm wide enclosure. Its native FreeCAD document and STEP parts pass exact-solid static fit and twelve scripted 3U envelope transfer paths with conservative fixed-part swept boxes. It lacks the actual lift/carriage, launch restraint, actuation, tolerances, fault recovery and revised installed mass. Its increased envelope has no approved host. This candidate does not alter the evaluated Gen5 configuration or repair the performance discrepancy. See [R1 CAD record](../../cad/FEEDER_CANDIDATE_R1.md).

![R1 candidate section; geometry drawing, not a qualified mechanism.](<../../figures/gen5_feeder_candidate_r1.png>){width=90%}

A **matched reference comparison** uses twelve identical 4 kg payloads at 450 km, the same 300 kg base host with 10 kg assumed fuel and 220 s specific impulse, and installed device masses of 72 kg for a spring class versus 126.562 kg modeled Gen5. To meet one common +16.029 m/s inertial payload target at the same epoch, ideal host preburn takes 2.693 kg of propellant with 2.5 m/s spring release and 0.827 kg with the 12.448 m/s finite Gen5 estimate. The subsequent common-input, assumed-100 N twelve-shot optimizer accepts prefixes of **4/12 spring, 1/12 finite Gen5, 1/12 historical Gen5**. None closes. These are bounded numerical cases, not a supplier quote, proof of infeasibility or product advantage. Onboard propulsion, transport services and long-horizon drag remain unmodeled. See [matched mission inputs](../../docs/MATCHED_MISSION_REFERENCE.md).

![Matched reference results; assumed host and device classes.](<../../figures/matched_mission_reference.png>){width=96%}

# 1. Introduction

## The deployment problem

The primary mission determines the launch vehicle's delivered orbit. Secondary CubeSats may have limited onboard propulsion, mass, power, or programmatic freedom to correct that orbit. Standard canisterised spring systems are mature and effective at clearance and separation. Their release conditions, however, are governed by spring energy, payload mass, and the device rather than a separately commanded velocity profile for every satellite.

The distinction between **release timing** and **relative-state change** is central. Waiting alone between zero-relative-impulse releases from an unchanged host does not produce persistent in-track phase spacing. Spring impulse, differential drag or a host maneuver can produce a relative state; a commanded velocity along or against orbital motion can change the satellite's orbital energy and semi-major axis. VOLLEY studies the latter capability while retaining a clear comparison with spring release and other alternatives. It does not claim that all constellation phasing requires a motor.

The host is an active participant in the mission model. After its primary mission, a suitable hosted platform would need attitude control, available resources and permission to operate. It could perform coarse orbital repositioning; VOLLEY would assign each secondary payload a local release state. No specific upper stage has been selected or approved for that role.

## Buyer and spacecraft fit

The [audited market and customer-fit report](../../MARKET_AND_CUSTOMER_FIT.md) checks the relevant Drive market thesis and independent business-case review against current primary sources. [Planet's FY2026 filing](https://www.sec.gov/Archives/edgar/data/1836833/000119312526119957/pl-20260131.htm) and [Spire's 2025 filing](https://www.sec.gov/Archives/edgar/data/1816017/000119312526116169/spir-20251231.htm) show repeatable, configurable smallsat production. [NASA's 2026 launch review](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/) confirms that a primary mission can constrain the orbit available to rideshare payloads. Together, these support a *mission hypothesis*, not customer demand.

The likely party that could pay for individualized release states is a carrier, rideshare integrator or constellation operator responsible for a delivered manifest. A standardized satellite-bus maker may specify interfaces but need not buy the system. Replenishment batches and mixed-payload rideshare are candidate jobs. A one-satellite mission already in a suitable orbit is a poor fit and should favor a qualified conventional dispenser. The analyzed Gen5 system carries twelve 3U spacecraft but fails its own 3U mass screen; a PocketQube batch is a **future interface redesign**, not an accommodated or qualified Gen5 payload class. Payloads sensitive to magnetic fields need an explicit exclusion or design remedy. No buyer, payload or provider has confirmed these requirements.

For an economic result, price and simulate the same manifest delivered with ordinary spring impulse, spring plus host manoeuvres, onboard propulsion, an orbital-transport service and VOLLEY. The published [SpaceX rideshare starting price](https://new.spacex.com/rideshare) cannot stand in for an installed VOLLEY cost or savings quote. A three-to-five-year replacement cycle and a 5–50 m/s release range are research hypotheses from the Drive market report, not Gen5 operating requirements or established market demand. The Gen6 1 km/s upper objective is a different, unvalidated regime.

![Gen5 layout and mission hardware elements. Diagram from the thesis analysis.](<../../source/figures/D02_layout.png>){width=100%}

# 2. Literature review

| Approach | Established capability | Relevance and limit |
|:--|:--|:--|
| Spring deployers | Flight heritage and simple separation near the low-m/s range [1] | Strong benchmark for reliability and installed mass; release energy is largely built into the device. |
| Spring release and differential drag | In-track spacing and gradual orbital adjustment [3] | A relative impulse or drag difference creates the separation; waiting alone from an unchanged co-orbital host does not. |
| Orbital transfer vehicles | Coarse orbital repositioning through a propulsive carrier | Valuable comparator for whole-mission delivery; greater spacecraft and integration burden must be counted. |
| Electromagnetic CubeSat studies | Magazine transport and electromagnetic launch have already been studied [4–6] | Some configurations impose conductive armatures, high acceleration or different maturity; novelty cannot be claimed for electromagnetic deployment alone. |

The most relevant high-speed electromagnetic comparison in the manuscript is Feng *et al.* [4], which models a 321.56 m/s launch of a 20 kg CubeSat but at acceleration on the order of thousands of g and with an armature/interface issue. Zhao *et al.* [5,6] study stacked CubeSat transfer and storage, including measured transport behavior in a related mechanism. These works establish that electromagnetic delivery and magazine transport are prior art. VOLLEY's more limited question is whether a **commandable** release can be delivered to an **unmodified** satellite at a much lower acceleration while accounting for the whole installed system. No universal CubeSat quasi-static acceleration qualification is assumed; the launch provider and payload-specific limits must govern a real design [2,8].

# 3. Research gap

The analytical gap is not “no one has considered electromagnetic deployment.” It is the coupled trade between: (i) commanded release, (ii) payload-side interface and acceleration, (iii) a reusable feed/release architecture, (iv) host reaction and mission utility, and (v) installed system mass and faults. A speed-only comparison can make a concept appear attractive while omitting its sled, power bank, brake, magazine, enclosure, control, and retained mass after each shot.

The thesis addresses that gap by constructing a documented Gen5 reference configuration and testing its own claims against explicit comparisons. It also records when those tests weaken the concept. Physical viability remains a separate research gap: numerical model agreement cannot establish manufactured tolerances, actual force, payload cleanliness, cycle reliability or provider compatibility.

# 4. Objectives and outcome

| Analytical research objective | Completed outcome | Interpretation |
|:--|:--|:--|
| Model a commandable 3U system | Gen5 CAD, magazine, sled, motor, arrest and power architecture | System-level design record, not manufactured hardware |
| Quantify the release | Rated shot, circuit and closed-loop simulations | Predicted performance under stated assumptions |
| Evaluate orbital value | Orbit model and selected independent numerical cross-checks | Conditional energy and lifetime benefit |
| Test whole-system competitiveness | Mass rollup, spring/alternatives comparison and preset criteria | Gen5 fails the 3U mass target |
| Challenge model credibility | Numerical verification, defect corrections and provenance record | Scope and remaining physical uncertainties made explicit |

These objectives summarize the completed analytical research for this final-review presentation. They are a presentation synthesis, not a claim that the university approved this exact list in advance. The physical development tasks are shown later under future work.

# 5. Research methodology

The project follows an engineering evidence chain:

1. **Mission/use-case framing:** specify the payload, host responsibilities, target orbital change, safety limits and competent conventional comparators.
2. **Architecture trade:** examine force production, loading, restraint, guidance, arrest, reset and fault behavior, rather than only ideal acceleration.
3. **Geometry and installed mass:** build CAD geometry and count the sled, arrays, enclosure, feed, power, controls and other installed parts.
4. **Coupled models:** compute magnetic field and thrust, shot dynamics, power/circuit behavior, control dispersion, structural/flow responses and orbital consequences.
5. **Challenge the claims:** use alternate numerical methods and acceptance bands, preserve misses and update the baseline only with a recorded reason.
6. **Decision:** compare orbital benefit against mass, reliability, payload/host compatibility and the available alternatives.

![Historical modeled shot: velocity, bank voltage and current.](<../../source/figures/F01_shot.png>){width=100%}

## Numerical checks and their limits

The magnetic field was compared across an analytical representation, magpylib, and 2-D/3-D finite-element calculations. A 3-D midgap FEM solve supports the field model at its tested location; P121 separately checks the ideal depth-integrated thrust by numerical surface-charge integration. Neither is a motor measurement. Shot and circuit predictions were compared with ngspice at stated assumptions. Structural calculations use CalculiX; airflow calculations use OpenFOAM. Orbital calculations include Cowell and GMAT cases. The independent orbit work rejected an earlier assertion that lifetime benefit was invariant across solar activity. Each check applies to its declared case and boundary conditions; none is a hardware test.

![Representative magnetic-field model output. Source: thesis figure A02.](<../../source/figures/A02_field_map.png>){width=83%}

# 6. Timeline

## Documented evolution

| Period | Milestone | Confidence in date |
|:--|:--|:--|
| 2023 | Free-flyer idea reframed around a host platform | Documented design decision |
| Mid-2025 | Coilgun concept shifted toward a linear synchronous motor | Approximate historical milestone |
| 2025–July 2026 | CAD generations and mass model developed | Some dates reconstructed/approximate |
| July–September 2026 | Gen5 analysis, numerical checks, defects and thesis record | Dated repository/analysis records |
| October 2026 | Gen5 findings and design decision presented for final review | Review package dated 10 October 2026 |

The thesis repository's reconstructed history expressly marks several early milestone dates as approximate. The analytical baseline was revised as evidence improved: a CAD-derived sled mass displaced a lighter parametric estimate; a depth-resolved thrust calculation lowered the rated speed; an enclosure buildup exposed the 3U mass penalty; and an independent orbit check rejected an overbroad solar-invariance claim. These revisions are part of the completed study, not signs that the final numbers are placeholders. Gen6 research gates are described only in §10, Future work.

# 7. Work progress

The thesis deliverables are in hand: an authored manuscript, CAD renders and model geometry, analysis scripts/results, numerical verification run sheets, figures, a baseline record, a defect register, and a provenance statement. Numerical investigations cover the motor field, shot dynamics, bank/circuit, mass, orbit propagation, separation and selected structural, airflow and reliability issues. The study closes by retaining failed criteria and superseded results rather than silently replacing them.

The deliverable here is a completed computational thesis, not a flight article. The later long gas-guide and independent spring-cell studies are historical comparators. Gen6 has a mission direction and investigation envelope but is not a result of the Gen5 thesis. Its mechanism and exact payload/provider cases remain future choices.

# 8. Results

## Gen5 configuration

The analysed system uses a double-sided Halbach-array linear synchronous motor to propel a reusable permanent-magnet sled to a release station 1.5 m from the breech on 1.8 m structural longerons. Two transverse cassettes are intended to feed twelve 3U satellites, but the present side-fed placement fails the fit check. A capacitor-based bank supplies the modeled pulse, and a brake is intended to arrest the sled after payload release. The **9.45 kg** sled input comes from historical Gen3 CAD solid volumes; this value reduced the exit speed relative to an earlier optimistic parametric estimate. The CAD render conveys a concept, not manufactured or assembled hardware.

## Rated 3U shot

| Model output | Rated result | Interpretation |
|:--|--:|:--|
| Exit velocity | 16.029 m/s | Modelled 3U reference shot |
| Payload acceleration | 10.07 g | Not a payload qualification claim |
| Pulse duration | 162.3 ms | Modelled motor actuation |
| Peak current | 320 A | Component implementation unverified |
| Electrical energy drawn, gross | 2,782 J | Bank/circuit model |
| Recovered after release | 47 J | 39 mm available recovery zone |
| Sled energy to brake | 1,162 J | Major loss and arrest burden |
| Electrical-to-payload efficiency, net | 18.8% | 514 J payload kinetic energy / net draw |

The energy flow matters more than the velocity headline. The sled and its arrest hardware are part of the modeled price of avoiding a payload-side drive armature. Regeneration returns only a small fraction of sled energy within the available length. [P117](../../validation/P117_rated_energy_mass_audit.md) separately checks the reported mass and energy identities and reconciles the historical **124.488 J (4.47%) compact-output remainder** to 90.964 J assumed converter loss, 32.460 J auxiliary draw and 1.064 J of forward-Euler step excess, with a rounded residual below 0.001 J. This closes historical model arithmetic only. Selected hardware, switching and installed power verification remain open.

## Command precision

The closed-loop Monte Carlo model predicts **0.0274 m/s ($3\sigma$)** exit-velocity dispersion around a **15.8 m/s** fleet setpoint. It uses assumed sensing and plant tolerances, with headroom below the open-loop ceiling. This is a simulated distribution, not a measured release repeatability.

![Closed-loop simulation distribution at the fleet setpoint.](<../../source/figures/F03_mc.png>){width=84%}

## Orbital utility

For the stated orbit and mean-solar-activity case, an assumed historical 16.029 m/s release predicts a **28.8 km** semi-major-axis increase and a **1.60×** lifetime multiplier for a propulsionless satellite. A separate Cartesian two-body integration of that assumed historical state returns **28.800775 km**, agreeing within the declared numerical band. This checks only the immediate orbital-energy result. The atmospheric lifetime multiplier has not been independently reproduced at the exact current point. Timing alone, with zero relative impulse and no host or drag difference, produces neither persistent phasing nor this semi-major-axis change.

![Independent rated-state two-body orbit check. The lifetime claim is outside its scope.](<../../figures/rated_orbit_crosscheck.png>){width=92%}

![Modelled orbital-lifetime response. Absolute values depend on atmosphere.](<../../source/figures/F04_life.png>){width=87%}

## Installed mass changes the decision

The modeled Gen5 dry rollup is **126.6 kg** and loaded mass **174.6 kg**; these include assumed hardware and historical Gen3 sled volume, not a mass extraction from a complete installed Gen5 assembly. At twelve 3U customers, the deployer weighs **10.55 kg per customer**, compared with approximately **6 kg** for the spring canister comparator used in the analysis. The ratio is **1.758**; the preset acceptance band required parity within 15%. That band fails by a large margin. Replacing an **8 kg enclosure placeholder** with a **50.04 kg** geometry-derived buildup exposed much of the penalty. Even changing structure alone does not recover parity in the studied options. The result is a reason to reopen the architecture, not to conceal the comparison.

![Constraint and mass-attribution analysis; mass is a model rollup.](<../../source/figures/A35_ledger.png>){width=100%}

## Native CAD and packaging review

The geometry package now includes a FreeCAD 1.0 native document, eight re-exported STEP parts, and a 20-instance STEP assembly. Each imported solid passed FreeCAD validity and nonzero-volume checks. The source solids were produced in CadQuery; importing them into FreeCAD does not create parametric feature history or prove that the assembly can be manufactured. The [CAD review report](../../cad/GEN5_CAD_REVIEW.pdf) identifies source revisions and checks, while [P116](../../validation/P116_gen5_assembly_packaging.md) records the numerical intersection result.

The side-fed reference assembly has **526 mm** clear enclosure width. Its **205 mm** track plus two **166 mm** cassettes require **537 mm**, an **11 mm** shortfall even before running clearance. The exact solids overlap by **32,915 mm³ per side** in this placement. This fails that packaging arrangement. A different feed architecture, enclosure or dimension set requires a new configuration and reassessment; the current render must not be presented as an assembled flight article.

![Dimensioned side-fed reference cross-section; this configuration fails the width check.](<../../figures/gen5_packaging_section.png>){width=92%}

## Decision and evidence boundary

The analytical result has four parts. The model supports a commandable release and conditional orbital-energy benefit; the full-system 3U mass criterion fails; the stated side-fed layout fails its CAD width check; and physical behavior remains unverified. The latter includes release-cycle reliability, shock and arrest loads transmitted to stowed satellites, field exposure near a customer payload, host attitude/control authority and provider approval. The known-problems register ranks several as potentially design-fatal. These findings limit product claims and define the research conclusion.

# 9. Conclusion

The Gen5 computational thesis reaches a research conclusion within its stated scope. Its model predicts a commandable moderate-acceleration release and a conditional orbital-energy benefit, with a separate check of the immediate two-body orbital change. Installed-mass accounting misses its preset 3U benchmark, and the side-fed reference CAD assembly fails its width check. The current configuration is therefore not a selected flight baseline. Hardware behavior and interfaces remain outside the tested evidence.

The thesis's strongest engineering contribution is the transparent decision record: the full machine was modelled, independent numerical checks corrected several claims, and an unfavourable mass result was retained. That closes the Gen5 study and provides a defensible input to a separate future architecture trade.

# 10. Future work

Gen6's controlling objective is a reusable launch path that sequentially accepts different supported CubeSat sizes and commands each departure condition. The approximately 1–2 m/s to 1 km/s span is an investigation envelope; the upper end may force acceleration, energy, travel, payload or provider constraints that reject candidates. Electromagnetic systems are preferred for comparison but are not preselected. Competent springs, electromechanical/stored-energy, gas/fluid, hybrid, BOLLEY and conventional mission substitutes belong in the same comparison boundary.

The near-term milestone is one named test-article configuration that can be independently reviewed. Its package needs controlled geometry and drawings, a bill of materials, host and payload interfaces, full installed mass/energy/thermal accounting, assembly and inspection instructions, instrumented procedures, predetermined pass/fail and stop criteria, uncertainty and model-credibility evidence, retained failures, and an explicit build/test release decision. A rejected candidate is a valid research outcome; it must not be presented as a build-ready survivor.

# 11. References and project records

1. JAXA, *JEM Payload Accommodation Handbook*, Vol. 8, small-satellite deployment interface control document, cited in the VOLLEY thesis.
2. California Polytechnic State University, *CubeSat Design Specification*, Rev. 14, 2020.
3. C. Foster *et al.*, “Constellation phasing with differential drag on Planet Labs satellites,” *Journal of Spacecraft and Rockets*, 55(2), 2018.
4. H. Feng, Y. Yang and Y. Wu, “Design and reachable domain analysis of on-orbit electromagnetic launcher for CubeSats,” *International Journal of Aerospace Engineering*, art. 3000765, 2025.
5. Y. Zhao *et al.*, “Design and analysis of a new deployer for the in-orbit release of multiple stacked CubeSats,” *Remote Sensing*, 14(17), 4205, 2022.
6. Y. Zhao *et al.*, “Simulation analysis and experimental verification of the transport characteristics of a high-volume CubeSat storage device,” *Aerospace*, 12(6), 466, 2025.
7. K. Halbach, “Design of permanent multipole magnets with oriented rare earth cobalt material,” *Nuclear Instruments and Methods*, 169, 1980.
8. NASA, *General Environmental Verification Standard*, GSFC-STD-7000A, 2013.
9. D. A. Vallado, *Fundamentals of Astrodynamics and Applications*, 4th ed., 2013.
10. A. Mishra, *VOLLEY-thesis*: authored manuscript, baseline, provenance, figures and validation records, repository head `b30ffdc`, 28 September 2026. Project record, not independent experimental evidence.
11. VOLLEY/BOLLEY, *Current Plan and Status — PLAN-R2*, controlled working baseline, 29 September 2026. Project plan, not achieved performance.
