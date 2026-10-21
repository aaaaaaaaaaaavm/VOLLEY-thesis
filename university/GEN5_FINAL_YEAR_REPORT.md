---
title: "VOLLEY Gen5: Computational Feasibility and Engineering Disposition of a CubeSat Deployer"
author:
  - Adityavardhan Mishra
  - Pratham Chawla
date: "21 October 2026"
lang: en-GB
papersize: a4
fontsize: 12pt
mainfont: Liberation Serif
sansfont: Liberation Sans
monofont: DejaVu Sans Mono
geometry:
  - left=32mm
  - right=25mm
  - top=25mm
  - bottom=25mm
---

# Abstract {.unnumbered .unlisted}

This final-year project report evaluates a magazine-fed electromagnetic CubeSat deployer as a *computational design study*. For a twelve-payload 3U configuration, the historical periodic-force model predicts a 16.029 m/s release at 10.068 g and 2.782 kJ gross shot draw. A finite-array/stator 3-D analytic integral challenges that speed prediction, giving 12.448 m/s under ideal phase. A separate 2-D finite-element screen gives 1.082 kJ ideal work; an independent numerical 3-D surface-charge formulation reproduces 1.042 kJ under shared assumptions. An illustrative 14 mm face gap lowers ideal work to 0.907 kJ, while a conditional full-winding bank rerun gives 2.099 kJ gross draw. These are model results, not a selected motor rating. An independent Cartesian two-body calculation reproduces a 28.800775 km immediate semi-major-axis rise for the imposed historical input at 450 km. A native FreeCAD 1.0 review document and STEP exports expose an 11 mm transverse shortfall in the specified side-fed layout, with 32,915 mm³ of exact-solid overlap per cassette. The estimated 126.6 kg dry mass gives 10.547 kg of deployer per carried 3U, failing both the 2 kg economic screen and an approximately 6 kg spring-canister parity comparison. Atmospheric lifetime, exact payload interfaces and full mission delivery remain conditional or open. There is no physical prototype or VOLLEY test data. The completed result is a documented model-based decision against this Gen5 3U configuration, with Gen6 scale-up treated as future research.

**Keywords:** CubeSat deployment; electromagnetic launcher; systems engineering; numerical verification; CAD interference; orbital mechanics; model credibility.

# Abbreviations and evidence convention {.unnumbered .unlisted}

| Term | Meaning |
|:--|:--|
| CAD / STEP | Computer-aided design / ISO 10303 solid-geometry exchange |
| CG / ICD | Centre of gravity / interface control document |
| FEM / FEA | Finite-element method / finite-element analysis |
| J2 / LEO | Second zonal gravity term / low Earth orbit |
| LSM / OTV | Linear synchronous motor / orbital transfer vehicle |
| 1U / 3U | CubeSat form-factor classes; no specific spacecraft is qualified |

: Abbreviations and evidence convention — Term.


All plotted VOLLEY results are computations unless explicitly described as external experimental data. CAD views and Blender renders show geometry rather than manufactured hardware. “Failed” identifies a missed evaluated criterion; “unverified” identifies behavior unresolved by the stated method. Numerical verification is distinguished from physical validation throughout.

This issue contains the evaluated Gen5 study and separately identified Gen6 research through 21 October 2026. It is issued for first similarity review; institutional approval and the similarity result are not asserted. Gen6 research does not alter the evaluated Gen5 configuration.

\clearpage
\pagenumbering{arabic}



# Introduction and problem definition

## The deployment problem

The primary mission determines the launch vehicle's delivered orbit. Secondary CubeSats may have limited onboard propulsion, mass, power, or programmatic freedom to correct that orbit. Standard canisterised spring systems are mature and effective at clearance and separation. Their release conditions, however, are governed by spring energy, payload mass, and the device rather than a separately commanded velocity profile for every satellite.

The distinction between **release timing** and **relative-state change** is central. Waiting alone between zero-relative-impulse releases from an unchanged host does not produce persistent in-track phase spacing. Spring impulse, differential drag or a host maneuver can produce a relative state; a commanded velocity along or against orbital motion can change the satellite's orbital energy and semi-major axis. VOLLEY studies the latter capability while retaining a clear comparison with spring release and other alternatives. It does not claim that all constellation phasing requires a motor.

The host is an active participant in the mission model. After its primary mission, a suitable hosted platform would need attitude control, available resources and permission to operate. It could perform coarse orbital repositioning; VOLLEY would assign each secondary payload a local release state. No specific upper stage has been selected or approved for that role.

## Buyer and spacecraft fit

The [audited market and customer-fit report](../MARKET_AND_CUSTOMER_FIT.md) checks the relevant Drive market thesis and independent business-case review against current primary sources. [Planet's FY2026 filing](https://www.sec.gov/Archives/edgar/data/1836833/000119312526119957/pl-20260131.htm) and [Spire's 2025 filing](https://www.sec.gov/Archives/edgar/data/1816017/000119312526116169/spir-20251231.htm) show repeatable, configurable smallsat production. [NASA's 2026 launch review](https://www.nasa.gov/smallsat-institute/sst-soa/integration-launch-and-deployment/) confirms that a primary mission can constrain the orbit available to rideshare payloads. Together, these support a *mission hypothesis*, not customer demand.

The likely party that could pay for individualized release states is a carrier, rideshare integrator or constellation operator responsible for a delivered manifest. A standardized satellite-bus maker may specify interfaces but need not buy the system. Replenishment batches and mixed-payload rideshare are candidate jobs. A one-satellite mission already in a suitable orbit is a poor fit and should favor a qualified conventional dispenser. The analyzed Gen5 system carries twelve 3U spacecraft but fails its own 3U mass screen; a PocketQube batch is a **future interface redesign**, not an accommodated or qualified Gen5 payload class. Payloads sensitive to magnetic fields need an explicit exclusion or design remedy. No buyer, payload or provider has confirmed these requirements.

An economic comparison requires the same manifest delivered with ordinary spring impulse, spring plus host manoeuvres, onboard propulsion, an orbital-transport service and VOLLEY. The published [SpaceX rideshare starting price](https://new.spacex.com/rideshare) cannot stand in for an installed VOLLEY cost or savings quote. A three-to-five-year replacement cycle and a 5–50 m/s release range are research hypotheses from the Drive market report, not Gen5 operating requirements or established market demand. The Gen6 1 km/s upper objective is a different, unvalidated regime.

![Gen5 layout and mission hardware elements. Diagram from the thesis analysis.](<../source/figures/D02_layout.png>){width=100%}

## Research question

The analytical gap is not “no one has considered electromagnetic deployment.” It is the coupled trade between: (i) commanded release, (ii) payload-side interface and acceleration, (iii) a reusable feed/release architecture, (iv) host reaction and mission utility, and (v) installed system mass and faults. A speed-only comparison can make a concept appear attractive while omitting its sled, power bank, brake, magazine, enclosure, control, and retained mass after each shot.

The thesis addresses that gap by constructing a documented Gen5 reference configuration and testing its own claims against explicit comparisons. It also records when those tests weaken the concept. Physical viability remains a separate research gap: numerical model agreement cannot establish manufactured tolerances, actual force, payload cleanliness, cycle reliability or provider compatibility.



# Objectives and study scope

| Analytical research objective | Completed outcome | Interpretation |
|:--|:--|:--|
| Model a commandable 3U system | Reference CAD, magazine concept, sled, motor, arrest and power architecture | Feed and release mechanics remain unresolved |
| Quantify the release | Historical periodic shot, circuit and closed-loop simulations; adverse finite-force screen | No selected or verified speed rating |
| Evaluate orbital value | Historical-input orbit model and selected numerical cross-checks | Conditional geometry; rated lifetime remains open |
| Test whole-system competitiveness | Mass rollup, spring/alternatives comparison and preset criteria | Gen5 fails the 3U mass target |
| Challenge model credibility | Numerical verification, defect corrections and provenance record | Scope and remaining physical uncertainties made explicit |

: Objectives and study scope — Analytical research objective.


The objectives define an evaluated computational study. Completion of an analysis is distinguished from satisfaction of a design requirement. A failed mass or fit criterion remains a result; it does not establish flight readiness. No physical prototype or experimental VOLLEY measurements are reported.




# Literature review and research contribution

| Approach | Established capability | Relevance and limit |
|:--|:--|:--|
| Spring deployers | Flight heritage and simple separation near the low-m/s range [1] | Strong benchmark for reliability and installed mass; release energy is largely built into the device. |
| Spring release and differential drag | In-track spacing and gradual orbital adjustment [3] | A relative impulse or drag difference creates the separation; waiting alone from an unchanged co-orbital host does not. |
| Orbital transfer vehicles | Coarse orbital repositioning through a propulsive carrier | Valuable comparator for whole-mission delivery; greater spacecraft and integration burden must be counted. |
| Electromagnetic CubeSat studies | Magazine transport and electromagnetic launch have already been studied [4–6] | Some configurations impose conductive armatures, high acceleration or different maturity; novelty cannot be claimed for electromagnetic deployment alone. |

: Literature review and research contribution — Approach.


A high-speed electromagnetic comparator summarized in the project literature record is Feng *et al.* [4], which models a 321.56 m/s launch of a 20 kg CubeSat but at acceleration on the order of thousands of g and with an armature/interface issue. Zhao *et al.* [5,6] study stacked CubeSat transfer and storage, including measured transport behavior in a related mechanism. These works establish that electromagnetic delivery and magazine transport are prior art [4–6]. VOLLEY's more limited question is whether a **commandable** release can be delivered to an **unmodified** satellite at a much lower acceleration while accounting for the whole installed system. No universal CubeSat quasi-static acceleration qualification is assumed; the launch provider and payload-specific limits must govern a real design [2,8].

## Closest feeder and deployer studies

The [full-text feeder comparison](../docs/FEEDER_FULL_TEXT_REVIEW_2026_10_19.md) examines the closest 2022 and 2025 studies with page references and publisher-source hashes. The 2022 electromagnetic release prototype reports gravity-compensated dummy releases, not VOLLEY performance. The 2025 storage prototype uses spacecraft-side grooves, guides and iron patches; this does not establish the unchanged passive-payload objective adopted here. Its 1200 N receiving-force result is simulated, while its fast laboratory pushes are gravity-assisted. The distinction requires actual payload interface approval, contact/load analysis and shared-path isolation in future VOLLEY work. Broader end-effect, mission and carrier literature and independent technical review remain outstanding.

The numerical results reported in [4] are contextual literature evidence and have not been independently reproduced here. The full-text inspection of [5,6] supports the detailed interface and test-condition comparison above. A shared release principle does not transfer another device’s measured performance or reliability to VOLLEY. The defensible contribution is the coupled, reproducible feasibility assessment of the stated Gen5 configuration, including its adverse findings.




# Research methodology and governing models

The project follows an engineering evidence chain:

1. **Mission/use-case framing:** specify the payload, host responsibilities, target orbital change, safety limits and competent conventional comparators.
2. **Architecture trade:** examine force production, loading, restraint, guidance, arrest, reset and fault behavior, rather than only ideal acceleration.
3. **Geometry and installed mass:** build CAD geometry and count the sled, arrays, enclosure, feed, power, controls and other installed parts.
4. **Coupled models:** compute magnetic field and thrust, shot dynamics, power/circuit behavior, control dispersion, structural/flow responses and orbital consequences.
5. **Challenge the claims:** use alternate numerical methods and acceptance bands, preserve misses and update the baseline only with a recorded reason.
6. **Decision:** compare orbital benefit against mass, reliability, payload/host compatibility and the available alternatives.

## Controlled question and acceptance logic

The evaluated configuration is the twelve-3U, side-fed Gen5 reference. Its mission and mechanical claims cannot be transferred to the later R1 enclosure or Gen6 first-article candidates without new analyses. The study asks whether this reference yields a credible commandable release and an installed advantage while fitting its stated geometry. A failed criterion is a completed result of that question; it is not a validated deployer.

| Decision question | Test and evidence | Acceptance interpretation |
|:--|:--|:--|
| Can the specified side-fed parts coexist? | Native FreeCAD/STEP exact-solid checks and width arithmetic ([P116](../validation/P116_gen5_assembly_packaging.md)) | Nonintersection and positive service clearance required; reference **fails** before tolerance stack |
| Does the historical 3U speed survive finite force geometry? | Periodic model versus finite 3-D integral, independent formulation and 2-D FEM ([P118](../validation/P118_gen5_finite_force_map.md), [P119](../validation/P119_gen5_finite_force_fem2d.md), [P121](../validation/P121_gen5_finite_force_surface3d.md)) | Historical 16.029 m/s is challenged; 12.448 m/s is an ideal screen, not a rated pass |
| Can a source supply the assumed shot? | Conditional voltage/current and bank cases ([P120](../validation/P120_gen5_finite_coupled_shot.md), [P125](../validation/P125_gen5_voltage_limited_screen.md)) | No selected source or inverter; one commercial single-string ESR case **fails** |
| Does installed mass meet the predeclared 3U criterion? | Component rollup, 12-customer division and 15% parity band ([P117](../validation/P117_rated_energy_mass_audit.md), [P123](../validation/P123_gen5_one_event_mass_screen.md)) | 10.55 kg/3U exceeds the approximately 6 kg comparator and 6.9 kg allowed band; **fails** |
| Does the release yield mission value? | Historical-input orbit check and [matched host/payload comparison](../docs/MATCHED_MISSION_REFERENCE.md) ([P115](../validation/P115_rated_orbit_cartesian.md)) | Immediate semimajor-axis result is conditional; no twelve-shot matched campaign closes |

: Controlled question and acceptance logic — Decision question.


## Reproducibility and uncertainty rule

Each quantitative result must retain its input configuration, model method, software/source file, output file, comparison band and stated limits. A second implementation under the same geometry is a useful **numerical cross-check**, but shared material laws and boundary assumptions remain common-mode uncertainty. Mesh or quadrature convergence establishes discretization behavior within a model; it cannot establish physical accuracy. Supplier ratings, fabrication tolerance distributions, payload limits and host ICD limits are absent. Deterministic gap, current and bank sweeps therefore show sensitivity, not measured statistical confidence intervals. The open issues in Appendix A are held as exceptions rather than treated as zeros.

![Historical modeled shot: velocity, bank voltage and current.](<../source/figures/F01_shot.png>){width=100%}

## Numerical checks and their limits

The magnetic field was compared across an analytical representation, magpylib, and 2-D/3-D finite-element calculations. A 3-D midgap FEM solve supports the field model at its tested location; P121 separately checks the ideal depth-integrated thrust by numerical surface-charge integration. Neither is a motor measurement. Shot and circuit predictions were compared with ngspice at stated assumptions. Structural calculations use CalculiX; airflow calculations use OpenFOAM. Orbital calculations include Cowell and GMAT cases. The independent orbit work rejected an earlier assertion that lifetime benefit was invariant across solar activity. Each check applies to its declared case and boundary conditions; none is a hardware test.

![Representative magnetic-field model output. Source: thesis figure A02.](<../source/figures/A02_field_map.png>){width=83%}

## Governing relationships and boundary conditions

The historical shot model applies translational dynamics to the payload and reusable carrier. With moving mass $m_{\mathrm{mov}}$, longitudinal electromagnetic force $F_x$, and represented resistance $F_r$,

$$m_{\mathrm{mov}}\,\dot v=F_x(x,I,\phi)-F_r,\qquad \dot x=v.$$

The finite-force screen evaluates a winding-volume Lorentz integral and ideal longitudinal work,

$$F_x=\int_{V_{\mathrm{Cu}}}(\mathbf J\times\mathbf B)_x\,dV,\qquad W=\int_0^{s}F_x(x)\,dx,\qquad v_{\mathrm{ideal}}=\sqrt{2W/m_{\mathrm{mov}}}.$$

Optimal phase and the absence of electrical, switching and contact losses make this an ideal screen, not a component rating. The periodic-wave approximation $B(y)=B_0e^{-ky}$, with $k=2\pi/\lambda$, is distinguished from the finite cuboid-field and surface-charge implementations. The stator and mover end geometry therefore enter the decisive comparison explicitly [7,12].

A lumped winding/source model relates capacitor state and current through

$$L\,\frac{dI}{dt}=V_C-R_{\mathrm{tot}}I-K_ev,\qquad C\,\frac{dV_C}{dt}=-I_C,\qquad Q_{\mathrm{Cu}}=\int I^2R_{\mathrm{Cu}}\,dt.$$

These equations state the model family; the captured implementations retain their actual three-phase definitions and current conventions. A physically selected inverter, bus, winding, insulation and source are absent. Adiabatic $\Delta T=Q/(mc_p)$ is a single-pulse energy estimate and excludes heat transfer, hotspots and duty-cycle accumulation.

For two-body energy at an imposed release state,

$$\epsilon=\tfrac12\lVert\mathbf v\rVert^2-\mu/r,\qquad a=-\frac{\mu}{2\epsilon}.$$

For an internal release with pre-release system mass $M$, payload mass $m$, and specified payload-to-parent relative velocity $\mathbf u$, momentum conservation gives

$$\mathbf v_{\mathrm{payload}}=\mathbf v_0+(1-m/M)\mathbf u,\qquad \mathbf v_{\mathrm{parent}}=\mathbf v_0-(m/M)\mathbf u.$$

The point-mass host-burn calculation uses

$$M_{\mathrm{after}}=M_{\mathrm{before}}\exp[-\lVert\Delta\mathbf v\rVert/(I_{sp}g_0)].$$

The instantaneous two-body energy identity is not an atmospheric-life prediction. J2, atmosphere and host-control cases use separate inputs and boundaries [9]. Matched comparisons count device proxies, fuel, recoil and restoration at one terminal epoch. Ideal impulses do not resolve finite-burn navigation.




# Controlled Gen5 configuration

The controlled Gen5 reference is the evaluated twelve-3U configuration. Dimensions and analytical revisions are held together even where they fail the intended criterion. The later R1 and Gen6 geometries are separate studies and cannot replace this reference without a new evaluation.

| Parameter | Evaluated basis | Qualification status |
|:--|:--|:--|
| Payload manifest | Twelve nominal 4 kg 3U spacecraft | Envelope/mass surrogates; no approved customer spacecraft |
| Host used for the matched Gen5 comparison | 300 kg base host; 10 kg initial fuel; 220 s specific impulse | Computational surrogate; no selected provider |
| Structure | 1.8 m longerons; release station 1.5 m from breech | Native/STEP reference retains interferences |
| Powered travel | 1.3 m | Finite stator overlap decreases over the stroke |
| Carrier input | 9.445 kg from historical Gen3 solid-volume accounting | Not a supplier-complete installed Gen5 mass extraction |
| Rail/cassette widths | 205 mm and two × 166 mm; 526 mm available clear width | 537 mm required; 11 mm shortfall |
| Electrical source | Modeled pulse bank and winding/circuit branches | No selected source/inverter/winding rating |

: Controlled Gen5 configuration — Parameter.


## Carrier, feed and release arrangement

The analysed system uses a double-sided Halbach-array linear synchronous motor to propel a reusable permanent-magnet sled to a release station 1.5 m from the breech on 1.8 m structural longerons. Two transverse cassettes are intended to feed twelve 3U satellites, but the present side-fed placement fails the fit check. A capacitor-based bank supplies the modeled pulse, and a brake is intended to arrest the sled after payload release. The **9.45 kg** sled input comes from historical Gen3 CAD solid volumes; this value reduced the exit speed relative to an earlier optimistic parametric estimate. The CAD render conveys a concept, not manufactured or assembled hardware.

![Gen5 reference assembly from STEP/FreeCAD rendered in Blender, with enclosure hidden. Recorded clashes remain; no physical article is shown.](../cad/renders/step_review/gen5_reference_open.jpg){width=94%}




# Electromagnetic drive, power and control analysis

## Historical periodic model

The table below preserves the older model run for traceability. Its constant periodic-force input is challenged by the finite-geometry screen above. These numbers cannot be promoted together as the current machine's demonstrated or independently verified operating point.

| Model output | Historical result | Interpretation |
|:--|--:|:--|
| Exit velocity | 16.029 m/s | Historical periodic-force input; finite geometry challenges it |
| Payload acceleration | 10.07 g | Not a payload qualification claim |
| Pulse duration | 162.3 ms | Modelled motor actuation |
| Peak current | 320 A | Component implementation unverified |
| Electrical energy drawn, gross | 2,782 J | Bank/circuit model |
| Recovered after release | 47 J | 39 mm available recovery zone |
| Sled energy to brake | 1,162 J | Major loss and arrest burden |
| Electrical-to-payload efficiency, net | 18.8% | 514 J payload kinetic energy / net draw |

: Historical periodic model — Model output.


The energy flow matters more than the velocity headline. The sled and its arrest hardware are part of the modeled price of avoiding a payload-side drive armature. Regeneration returns only a small fraction of sled energy within the available length. [P117](../validation/P117_rated_energy_mass_audit.md) separately checks the reported mass and energy identities and reconciles the historical **124.488 J (4.47%) compact-output remainder** to 90.964 J assumed converter loss, 32.460 J auxiliary draw and 1.064 J of forward-Euler step excess, with a rounded residual below 0.001 J. This closes historical model arithmetic only. Selected hardware, switching and installed power verification remain open.

## Finite geometry and conditional source cases

The 16.029 m/s shot result assumes periodic thrust throughout a 1.3 m powered stroke. A new 3-D analytic integration of the exact cuboid field over the CAD's finite 162-belt stator finds **1.042 kJ ideal work**, corresponding to **12.448 m/s only under optimal phase with switching, voltage and friction losses omitted**. The modeled mover array and stator stop directly overlapping after 1.066 m travel. The 336 mm magnetic model and 340 mm CAD envelope also disagree. Cross-section quadrature refinement changes the three checked station forces by at most 0.369%; halving station spacing changes work by 0.096%. The magnetic field law is shared with the earlier model, so this is an adverse analytic screen, **not an independent 3-D FEM or a hardware test**. The historical 16.029 m/s remains in older tables for traceability and must not be called demonstrated performance. See [P118](../validation/P118_gen5_finite_force_map.md).

![Finite-array/stator model force versus position; no physical measurement.](<../figures/gen5_finite_force_map.png>){width=96%}

A separate **2-D finite-element magnetostatic solve** of the finite magnet array gives **1.082 kJ ideal work** on its finest 1 mm mesh, compared with the 3-D analytic screen's 1.042 kJ. The 2-to-1 mm mesh change is 0.59%; a larger air boundary changes the 2 mm work by 0.0004%. The solver uses a different field formulation but omits magnet-depth end effects, so the two absolute results must not be combined into an achieved speed. [P119](../validation/P119_gen5_finite_force_fem2d.md) records meshes, convergence and assumptions.

![Independent 2-D finite-element force screen, not a measurement.](<../figures/gen5_finite_force_fem2d.png>){width=96%}

An independent **depth-resolved 3-D numerical surface-charge implementation** integrates all finite magnet faces and 162 belts. It returns **1.042 kJ ideal work**, agreeing with the analytic cuboid-field implementation under shared geometry, remanence and ideal-phase assumptions. Face quadrature refinement changes work by 0.00002%; halving station spacing changes it by 0.096%. This is a formulation cross-check, not 3-D FEM or hardware validation. An illustrative 14 mm face gap gives **0.907 kJ**, 13.0% below the 12 mm case. These deterministic cases are not fabrication tolerances. [P121](../validation/P121_gen5_finite_force_surface3d.md) and [P122](../validation/P122_gen5_finite_force_sensitivity.md) include source, results and convergence.

![Ideal finite-force gap and depth scenarios; not measured tolerances.](<../figures/gen5_finite_force_sensitivity.png>){width=96%}

A **conditional finite-force bank/trajectory rerun** retains the historical 96 V, 6 F, 12 mΩ source and assumed converter. With the full 1.3 m winding energized it computes **2.099 kJ gross capacitor draw** and 927 J copper heat; an illustrative 0.34 m active-copper branch gives 1.394 kJ gross and 243 J copper heat. Both report 12.448 m/s because the force curve is imposed at ideal phase; no voltage-limited switching law or selected winding/inverter exists. The old 2.782 kJ, brake and control outputs are not revised ratings. [P120](../validation/P120_gen5_finite_coupled_shot.md) gives the time history and energy ledger.

The [P125 conditional voltage/current screen](../validation/P125_gen5_voltage_limited_screen.md) adds a source-power check to the finite force map. Under the old, **unselected** 12 mΩ bank and periodic winding values, the quasi-steady reference still gives 12.448 m/s, while halving the phase-current limit gives 8.802 m/s. Under the older distributor-data 116–185 mΩ **single-string** ESR bound, the source-power quadratic fails at 0.612 m and 0.160 m respectively, before release. Ideal two- or three-parallel-string branches complete numerically only by multiplying capacitance, cell count and source mass. None is a manufacturer-rated, thermally checked switching design; the model assumes instantaneous q-axis current. The 12.448 m/s result must therefore not be presented as a sourceable release rating.

![Finite-force speed and assumed bank energy histories.](<../figures/gen5_finite_coupled_shot.png>){width=96%}

## Historical control simulation

The closed-loop Monte Carlo model predicts **0.0274 m/s ($3\sigma$)** exit-velocity dispersion around a **15.8 m/s** fleet setpoint. It uses assumed sensing and plant tolerances, with headroom below the open-loop ceiling. This is a simulated distribution, not a measured release repeatability.

![Closed-loop simulation distribution at the fleet setpoint.](<../source/figures/F03_mc.png>){width=84%}





# CAD integration, packaging and installed mass

## Installed mass and comparator

The modeled Gen5 dry rollup is **126.6 kg** and loaded mass **174.6 kg**; these include assumed hardware and historical Gen3 sled volume, not a mass extraction from a complete installed Gen5 assembly. At twelve 3U customers, the deployer weighs **10.55 kg per customer**, compared with approximately **6 kg** for the spring canister comparator used in the analysis. The ratio is **1.758**; the preset acceptance band required parity within 15%. That band fails by a large margin. Replacing an **8 kg enclosure placeholder** with a **50.04 kg** geometry-derived buildup exposed much of the penalty. Even changing structure alone does not recover parity in the studied options. The result is a reason to reopen the architecture, not to conceal the comparison.

![Constraint and mass-attribution analysis; mass is a model rollup.](<../source/figures/A35_ledger.png>){width=100%}

## Native solid and assembly checks

The geometry package now includes a FreeCAD 1.0 native document, eight re-exported STEP parts, and a 20-instance STEP assembly. Each imported solid passed FreeCAD validity and nonzero-volume checks. The source solids were produced in CadQuery; importing them into FreeCAD does not create parametric feature history or prove that the assembly can be manufactured. The [CAD review report](../cad/GEN5_CAD_REVIEW.pdf) identifies source revisions and checks, while [P116](../validation/P116_gen5_assembly_packaging.md) records the numerical intersection result.

The side-fed reference assembly has **526 mm** clear enclosure width. Its **205 mm** track plus two **166 mm** cassettes require **537 mm**, an **11 mm** shortfall even before running clearance. The exact solids overlap by **32,915 mm³ per side** in this placement. A full census of the 20 leaf solids finds **17 intersecting pairs**. In the reference placement, the sled intersects the track by **82,983 mm³** and stator by **6,300 mm³**. The interface-ring proxy also intersects track, stator and enclosure proxies; stored-payload boxes intersect cassette bodies. Proxy contact and physical collision require separate engineering disposition, but the sled/track and sled/stator conflicts prevent acceptance of the assembly as drawn. The scripted feeder-path check did not evaluate these pairs. A different feed architecture, enclosure or dimension set requires a new configuration and reassessment; the current render must not be presented as an assembled flight article. The [all-leaf audit](../cad/GEN5_FULL_INTERFERENCE_AUDIT_2026_10_12.md) supplies the pair inventory and source script.

![Dimensioned side-fed reference cross-section; this configuration fails the width check.](<../figures/gen5_packaging_section.png>){width=92%}

## Separately evaluated widened geometry and arrest bounds

An **unselected R1 geometry candidate**uses a 570 mm wide enclosure. Its native FreeCAD document and STEP parts clear the original cassette--track overlap and twelve scripted 3U envelope transfer paths against selected fixed parts. A subsequent all-leaf exact-solid audit finds five other intersecting pairs in this widened assembly, including sled--track and sled--stator conflicts. The reference track beam occupies the roller corridor because its solid model has no channel cut; the sled backstop occupies the stator proxy. R1 therefore does not pass complete assembly integration. It also lacks the actual lift/carriage, launch restraint, actuation, tolerances, fault recovery and revised installed mass. Its increased envelope has no approved host. This candidate does not alter the evaluated Gen5 configuration or repair the performance discrepancy. See [R1 CAD record](../cad/FEEDER_CANDIDATE_R1.md) and the [all-leaf audit](../cad/GEN5_FULL_INTERFERENCE_AUDIT_2026_10_12.md).

The separate [P126 lateral tolerance screen](../cad/FEEDER_R1_TOLERANCE_SCREEN.md) uses R1's CAD-derived 5 mm nominal cassette-to-track gap. With declared 1 mm track placement, 1 mm cassette placement, 0.5 mm combined form and 0.2° angular error across a 340.5 mm payload proxy, worst-case residual is 1.31 mm; a 0.5° band overlaps by 0.47 mm. These are illustrative assumptions, not measured process capability or released GD&T.

[P127 conservation bounds](../validation/P127_gen5_release_arrest_bounds.md) put 731.8 J of kinetic energy into the modeled 9.445 kg sled at the **ideal** finite-force speed. Across the provisional CAD brake's 210 mm length, stopping requires at least 37.6 g mean sled deceleration. Eddy-current peak force, repeated-shot heat, payload contact and host attitude remain unsolved; the mean bound is not a brake acceptance test.

![R1 candidate section; geometry drawing, not a qualified mechanism.](<../figures/gen5_feeder_candidate_r1.png>){width=90%}

## Mass-property scope

The 23-line historical mass model sums to 126.561588 kg dry, with an assumed axial CG of 0.457690 m. This is not a complete Gen5 material extraction or full inertia tensor. Potential enclosure/thermal/bracket allocation overlap remains unresolved; no unverified mass credit is taken. The original mass failure is retained.

All 17 evaluated Gen5 and five widened-R1 intersections are classified as confirmed conflicts or unresolved adapter/payload proxy intersections. None is accepted as intentional contact without an interface definition; no geometry repair is claimed. Historical isolated FE results do not qualify the failed assembly.





# Orbital mechanics and matched mission comparison

## Immediate orbit and atmosphere-model lifetime

For the stated orbit and mean-solar-activity case, an **assumed historical 16.029 m/s release** predicts a **28.8 km** semi-major-axis increase and a **1.60×** lifetime multiplier for a propulsionless satellite. A separate Cartesian two-body integration of that assumed historical release state returns **28.800775 km**, agreeing within the declared numerical band. This checks only the immediate orbital-energy result. P134 independently integrates the shared static-atmosphere model and gives a 1.602165 ratio; that numerical agreement does not validate real lifetime or solar invariance. Timing alone, with zero relative impulse and no host or drag difference, produces neither persistent phasing nor this semi-major-axis change.

![Independent rated-state two-body orbit check. The lifetime claim is outside its scope.](<../figures/rated_orbit_crosscheck.png>){width=92%}

![Modelled orbital-lifetime response. Absolute values depend on atmosphere.](<../source/figures/F04_life.png>){width=87%}

P134 uses a separate orbit-averaged DOP853 integration of the shared static atmosphere. At imposed inertial increments of 2.5, 12.448437 and 16.029 m/s it gives lifetime ratios of 1.082110, 1.451222 and 1.602165. The maximum refinement change is 0.000145%, below its 0.5% numerical band. Space weather, ballistic coefficient history and actual achieved release remain outside that evidence.

## Matched Gen5 host and payload comparison

A **matched reference comparison**uses twelve identical 4 kg payloads at 450 km, the same 300 kg base host with 10 kg assumed fuel and 220 s specific impulse, and installed device masses of 72 kg for a spring class versus 126.562 kg modeled Gen5. To meet one common +16.029 m/s inertial payload target at the same epoch, ideal host preburn takes 2.693 kg of propellant with 2.5 m/s spring release and 0.827 kg with the 12.448 m/s finite Gen5 estimate. The subsequent common-input, assumed-100 N twelve-shot optimizer accepts prefixes of **4/12 spring, 1/12 finite Gen5, 1/12 historical Gen5**. None closes. These are bounded numerical cases, not a supplier quote, proof of infeasibility or product advantage. Onboard propulsion, transport services and long-horizon drag remain unmodeled. See [matched mission inputs](../docs/MATCHED_MISSION_REFERENCE.md).

![Matched reference results; assumed host and device classes.](<../figures/matched_mission_reference.png>){width=96%}

## Service precision and scaling bounds

The economic case is a **delivered orbital state at a specified epoch and tolerance**, not a high release speed by itself. [P123's reproducible one-event mass screen](../validation/P123_gen5_one_event_mass_screen.md) finds that, with the same assumed host and 10 kg initial fuel, an ideal finite-force Gen5 release saves 1.866 kg of host propellant relative to a 2.5 m/s spring release. Its modeled hardware is 54.562 kg heavier. If fuel is resized to the one event plus the same 2 kg reserve, Gen5 still carries 52.717 kg more device plus fuel. Even a hypothetical zero-burn release needs a device at or below 74.659 kg to tie this specific spring reference. This is a serious architecture requirement, although it is not a full twelve-shot economic result or a price for a tailored orbital state.

[P124's independent orbit and stroke screen](../validation/P124_precision_delivery_design_space.md) works backward from ideal orbit targets. At 450 km circular altitude, a 20 km immediate semi-major-axis rise requires about 11.149 m/s of *inertial tangential* increment. A ±0.1 km axis band leaves roughly 0.0555 m/s on its smaller side **if every other error is zero**. A flight requirement must divide the error among host state, release direction and speed, timing, orbit propagation and tracking, and must include along-track, plane and disposal constraints. The old 0.0274 m/s modeled release dispersion is unmeasured and cannot be applied to P118's challenged finite-stator case.

Over the evaluated 1.3 m powered stroke, an ideal 10 g constant-acceleration limit allows 15.97 m/s. At 1 km/s, the same stroke implies roughly 39,220 g and 2 MJ of payload kinetic energy for a 4 kg 3U; a 10 g stroke would be about 5.10 km. This makes the 1 km/s objective unsuitable as the specification for a first ordinary-3U Gen6 prototype. The first test article should instead inherit a **named mission, payload load limit and host interface**, and select a lower-speed command range only after a matched service comparison. This preserves the longer-range research goal while making prototype tests technically meaningful.

![Ideal acceleration required by speed on a 1.3 m stroke; not a VOLLEY motor rating.](<../figures/precision_delivery_design_space.png>){width=95%}

## Native propagation harmonization

The [local harmonization report](../validation/orbit_harmonization/README.md) isolates the earlier gravity-axis/configuration mismatch. GMAT R2026a and Orekit 13.1.6 agree to approximately **1.285 mm maximum** over one day with shared prescribed pole and JGM2 constants, using one continuous GMAT arc. Independent Cartesian and time-step comparisons are retained. This is numerical consistency, not physical orbit accuracy, independent Earth-orientation validation or demonstrated release speed. The frozen Gen5 record is unchanged.

![Matched native solver result and diagnostic sequence; numerical model agreement only.](../validation/orbit_harmonization/figures/harmonization.png){width=98%}

## Historical multi-orbit archive

The corrected A15 R1 archive, executed in GMAT R2026a on 30 September and reparsed on 16 October, returns a 14.558545° circular RAAN span and a 190.149944 m focused-window minimum sampled separation. These preloaded orbits do not establish continuous clearance or a coupled sequential campaign. The historical 367° span is withdrawn.







# Results and engineering discussion

The evaluated configuration has three decisive outcomes: its mass criterion fails, its side-fed packaging criterion fails, and its historical speed claim is challenged by finite geometry. The result is a negative design disposition for this particular twelve-3U Gen5 reference. It does not rule out all commanded-deployment concepts.

| Question | Result | Decision |
|:--|:--|:--|
| Does Gen5 meet the stated 3U mass-parity band? | 10.547 kg per customer versus a 6.9 kg allowed comparison band | Fails the model criterion |
| Do the reference parts coexist with positive clearance? | 11 mm width shortfall and 17 exact-solid intersecting pairs | Fails the represented geometry |
| Is 16.029 m/s supported as an installed rating? | Finite geometry gives 1.042 kJ ideal work and a 12.448 m/s ideal upper screen | Historical prediction challenged; no rating selected |
| Does the tested twelve-release Gen5 campaign close? | All sampled optimizer cases reject complete delivery | No closure demonstrated; not a universal impossibility proof |
| Is physical release quality established? | No VOLLEY prototype or measured releases | Unverified |
| Does later native propagation agreement prove precision? | Same-model numerical consistency under prescribed controls | Software verification only |

: Results and engineering discussion — Question.


The analytical result has four parts. The historical model represents a proposed commandable release and a conditional orbital-energy benefit, but its speed is challenged by finite geometry; the full-system 3U mass criterion fails; the stated side-fed layout fails its CAD width check; and physical behavior remains unverified. The latter includes release-cycle reliability, shock and arrest loads transmitted to stowed satellites, field exposure near a customer payload, host attitude/control authority and provider approval. The known-problems register ranks several as potentially design-fatal. These findings limit product claims and define the research conclusion.

The field, circuit, CAD, mass and mission studies are not interchangeable demonstrations. A converged numerical answer under a shared assumption can coexist with an incorrect physical assumption. Similarly, nominal nonpenetration of a simplified geometry can coexist with an unretained payload after power loss. The study therefore retains failed cases and open mechanisms rather than interpreting coverage as acceptance.




# Computational resources and limitations

## Computational resources

The work uses inspectable source models and captured outputs. Python provides analytical dynamics, quadrature, interval and sensitivity calculations; FreeCAD/OpenCascade provide native solid and STEP inspection; Blender supplies explicitly labelled renders. Native GMAT R2026a and Orekit 13.1.6 provide the stated orbital cases. CalculiX fixture results apply only to their declared support and loading. Historical OpenFOAM, ngspice and electromagnetic records have case-specific run sheets; they are not blanket verification of a current installed assembly.

No physical mechanism was fabricated, weighed, released or environmentally qualified. The report contains no measured VOLLEY reliability, magnetic cleanliness, shock or deployment-repeatability result. Public hardware and published tests support methods and comparisons only.

## Technical limitations and retained exceptions

Gen5 is a computational study with recorded adverse findings. Its evaluated configuration is not a qualified deployer or released product. The decisive electromagnetic, feed/release, brake, host, structural and installed-system questions remain open or bounded as recorded in the validation files. Physical bench and qualification tests are future work and remain marked unrun.

| System question | What this study actually establishes | Final Gen5 decision boundary |
|:--|:--|:--|
| Motor and electrical source | Historical 16.029 m/s periodic-model shot; finite-geometry ideal-phase screen 12.448 m/s; historical gross/net shot energy reconciled algebraically in P117 | **No component-rated release speed.** Winding, switching, source impedance, derating and coupled repeated-shot performance are unselected. The historical value is a model output, not a flight command. |
| Shot and brake heat | P117 identifies modeled copper, bank, converter and auxiliary terms; P127 puts 731.8 J into one ideal sled arrest and 8.782 kJ across twelve identical events before recovery/cooling | Heat deposition, peak temperature, duty interval, material limits, source warming and brake cooling are **unverified**. The twelve-shot sum is an energy bound, not a thermal qualification. |
| Magazine feed and release contact | The evaluated cassette placement fails by 11 mm; R1 gives a separate scripted path; tip-off calculations are model studies | No selected Gen5 feed actuator, launch restraint, contact law, tip-off acceptance or recontact test exists. No verified release-quality or P-POD-class reliability claim is made. |
| Carrier arrest and return | P127 gives a 3.485 kN *mean* braking-force floor over the provisional 210 mm corridor at the ideal 12.448 m/s screen | Peak force, brake heating, carrier containment, safe stop, reset, jam and abort behavior are **unverified**. Mean deceleration does not prove peak deceleration. |
| Structure and environment | Preliminary structural and geometry studies identify loads and the side-fed clash | No same-revision launch-load, vibration, shock, thermal-distortion or converged structural acceptance is claimed. |
| Magnetic/payload compatibility | Field studies identify exposure concerns, including possible magnetometer saturation | A passive spacecraft is only a surrogate envelope. Payload magnetic limits, shielding, safe standoff and provider approval are **unknown**. |
| Orbit and campaign | Independent Cartesian two-body calculation checks only the immediate 28.800775 km axis change *if* the historical 16.029 m/s departure state is imposed; sampled twelve-shot cases do not close | The 1.60× lifetime is a conditional atmosphere-model output; P134 checks its numerical implementation under shared assumptions, not the real atmosphere. Delivered-state covariance, conjunction clearance, host abort/recovery and disposal are outside the demonstrated mission result. |
| Installed system and interface | Modeled 10.547 kg per carried 3U fails the study's mass criterion; side-fed reference fails fit | No supplier-complete installed bill of materials, named accepted spacecraft/host/provider interface or packaging approval exists. |

: Technical limitations and retained exceptions — System question.


In this report, **failed** denotes an evaluated configuration that misses a declared criterion; **unverified** denotes an effect not resolved by the reported method. Neither status changes because a separate Gen6 geometry has been explored. The one-cell feeder study retains an unresolved power-loss restraint condition and does not establish a working Gen5 magazine.

## Required physical correlation

| Future validation | Purpose | Current status |
|:--|:--|:--|
| Instrumented force/current/position tests | Correlate force map, commutation and winding/source model | Unrun |
| Repeated restrained transfer and fault injection | Establish actual custody, gate holding, jam/abort/reset behavior | Unrun |
| Dummy payload release/contact tests | Measure velocity, tip-off, recontact and payload loads | Unrun |
| Instrumented carrier arrest and thermal cycling | Establish peak load, containment, heat and repeated-shot duty | Unrun |
| Vibration, shock and thermal-vacuum tests | Verify an actual manufactured configuration against its provider limits | Unrun; provider limits unselected |
| EMC and magnetic compatibility | Establish payload-specific electrical/magnetic accommodation | Unrun; payload/interface limits unselected |

: Required physical correlation — Future validation.


Simulation cannot supply the acceptance of a launch provider, a calibrated hardware result or a reliability demonstration. Those requirements remain conditions for future hardware development. No safety or qualification pass is claimed from the analytical fixtures.




# Conclusion and future development

The Gen5 computational thesis reaches a research conclusion within its stated scope. Its historical model predicts a moderate-acceleration release, but finite geometry challenges the speed; an independent two-body calculation checks only the immediate orbital change under that assumed release state. Installed-mass accounting misses its preset 3U benchmark, and the side-fed reference CAD assembly fails its width check. The current configuration is therefore not a selected flight baseline. Hardware behavior and interfaces remain outside the tested evidence.

The thesis's strongest engineering contribution is the transparent decision record: system budgets and idealized mechanisms were modelled, independent numerical checks corrected several claims, and an unfavourable mass result was retained. That closes the Gen5 study and provides a defensible input to a separate future architecture trade.

## Gen6 direction and research boundary

Gen6's controlling objective is a reusable launch path that sequentially accepts different supported CubeSat sizes and commands each departure condition. The approximately 1–2 m/s to 1 km/s span is an investigation envelope; the upper end may force acceleration, energy, travel, payload or provider constraints that reject candidates. Electromagnetic systems are preferred for comparison but are not preselected. Competent springs, electromechanical/stored-energy, gas/fluid, hybrid and conventional mission substitutes belong in the same comparison boundary.

The next milestone is an independently reviewable test-article configuration: controlled CAD and drawings; a sourceable bill of materials; host/payload interfaces; installed mass, energy and thermal accounting; assembly and inspection procedures; instrumented tests with predetermined pass/fail and stop criteria; uncertainty and retained failures; and an explicit build/test release decision. A rejected candidate remains a valid research result.

Appendix C details the passive 1U/3U service objective and manoeuvring-host surrogate. Its 3–6 m/s first-article objective and distant 1 km/s research objective are distinct. No final feeder, physical prototype or hardware build release is asserted.

\appendix

# Numerical and CAD evidence trail

| Result | Reproducible record | What remains outside the check |
|:--|:--|:--|
| Historical periodic shot and energy | [`analysis/results/motor_results.json`](../analysis/results/motor_results.json), [`analysis/motor_model.py`](../analysis/motor_model.py) | Unmeasured force and actual circuit parasitics |
| Imposed-state immediate orbital change | [`P115`](../validation/P115_rated_orbit_cartesian.md), [`rated_orbit_independent.py`](../analysis/rated_orbit_independent.py) | Atmospheric lifetime and controlled host mission |
| 3U mass decision | [`mass_properties.json`](../analysis/results/mass_properties.json), [`BASELINE`](../appendix/BASELINE.md) | Hardware weighing, complete installed host burden |
| Native geometry and collision | [`Gen5_Review.FCStd`](../cad/native/Gen5_Review.FCStd), [`FREECAD_EXPORT.json`](../cad/FREECAD_EXPORT.json), [`P116`](../validation/P116_gen5_assembly_packaging.md) | Tolerance, feed motion, payload accommodation and provider fit |
| Wider model and open gates | [`computational review`](../reports/GEN5_COMPUTATIONAL_REVIEW.pdf), [`CAD review`](../cad/GEN5_CAD_REVIEW.pdf), [`open problems`](../appendix/OPEN_PROBLEMS.md) | Final verification closure and physical development |

: Numerical and CAD evidence trail — Result.


The run sheets report software, inputs, declared comparison bands and files. Figures are generated model or CAD visualizations. A screenshot of a solver interface would not by itself establish a correct result; the editable model, data and case boundary are the audit trail.

## Current technical-evidence identity

The unchanged 68-file [Gen5 technical baseline](../docs/GEN5_TECHNICAL_BASELINE.json) controls the evaluated physics/CAD record. The numerical checks and later Gen6 studies are identified separately. The submission identity file records the exact source, figure, PDF and DOCX hashes for this issue; this is a document freeze, not a hardware release.

| Evidence package | Local source and captured results | Claim boundary |
|:--|:--|:--|
| Gen5 recorded failures | [Engineering audit](../docs/GEN5_UNCERTAINTY_AND_ACCEPTANCE.md) | Computational criteria and open exceptions |
| GMAT/Orekit harmonization | [Native propagation](../validation/orbit_harmonization/README.md) | Shared prescribed pole and gravity; software consistency |
| Four/twelve campaign construction | [Coupled delivery](../validation/coupled_delivery/README.md) | Constructed targets, proxies and ideal impulses |
| Seven feeder concepts | [FDR-08](../validation/feeder_review/README.md) | Comparable bounded screens; no hardware downselect |
| Captive-transfer correction | [CT-01](../validation/captive_transfer_review/README.md) | Prescribed primitives; actual custody/contact open |
| Replenishment concept | [RPL-01](../validation/replenishment_feasibility/README.md) | Negative baseline integration disposition |
| Full native event replay | [CNR-01](../validation/native_campaign_review/README.md) | Numerical cross-check and assumed error budgets |

: Current technical-evidence identity — Evidence package.



# Development history

## Documented evolution

| Period | Milestone | Confidence in date |
|:--|:--|:--|
| 2023 | Free-flyer idea reframed around a host platform | Documented design decision |
| Mid-2025 | Coilgun concept shifted toward a linear synchronous motor | Approximate historical milestone |
| 2025–July 2026 | CAD generations and mass model developed | Some dates reconstructed/approximate |
| July–September 2026 | Gen5 analysis, numerical checks, defects and thesis record | Dated repository/analysis records |
| October 2026 | Gen5 findings and design decision assembled for academic review; final presentation scheduled for 31 October | Review package dated 10 October |

: Documented evolution — Period.


The thesis repository's reconstructed history expressly marks several early milestone dates as approximate. The analytical baseline was revised as evidence improved: a CAD-derived sled mass displaced a lighter parametric estimate; a depth-resolved thrust calculation lowered the rated speed; an enclosure buildup exposed the 3U mass penalty; and an independent orbit check rejected an overbroad solar-invariance claim. These revisions are part of the review record; the historical 16.029 m/s shot remains traceable, but no final speed rating is selected. Gen6 studies are separately identified in Appendix C.

# Separate Gen6 research studies

## Surrogate service and first-article progression

(P130–P132)

The follow-on mission is an explicitly **surrogate** four-release case: two passive 1U and two passive 3U spacecraft, a roughly 500 km sun-synchronous host, all releases within one orbit, and a distinct full position/velocity target for each satellite 24 hours after the last release. The [matched J2 campaign](../validation/P130_gen6_matched_campaign.md) lets both commanded release and spring plus host maneuvers meet the **same** four exact mathematical targets. With assumed installed masses of 30 kg for VOLLEY and 16 kg for springs, VOLLEY saves 3.2823 kg of host fuel but adds 14 kg of installed device, leaving a 10.7177 kg penalty on the narrow device-plus-consumed-fuel measure. A +0.1 m/s release-speed perturbation moves the one-day terminal position by roughly 25–27 km in either strategy. Exact numerical matching is not delivered-state accuracy; the study has no customer tolerance, navigation covariance or physical dispenser rating.

Two editable [FreeCAD/STEP 3U first-article envelope candidates](../cad/gen6_first_article/README.md) provide a separate geometry screen. A captured permanent-magnet carrier is the analysis lead; a captured conductive-plate carrier remains a challenger. Their **partial** frame, guide and carrier material proxies are 9.926 and 9.945 kg. Under the surrogate P130 mission, only about 9.35 kg remains for all unmodelled hardware before device-plus-consumed-fuel parity is lost. Five nominal positions have no solid intersection, but the assumed 0.7° yaw with a 1.5 mm linear stack clashes with the simple guide corridor. [P131](../validation/P131_gen6_go2_article_bounds.md) gives an ideal 6 m/s moving-energy floor of about 82 J. At an assumed 10% wall-to-kinetic efficiency, [P132](../validation/P132_gen6_go2_power_instrument_screen.md) requires at least 818 J of input; it does not select a source, motor or brake. P130 used hypothetical release commands up to approximately 9 m/s, outside the proposed 3–6 m/s first-article band. The later coupled construction below limits the imposed release input to 3–6 m/s and supplies the remaining change through host assistance. Neither policy establishes actual motor performance.

A separate [one-cell fixed-cassette feeder study](../cad/gen6_feeder/README.md) begins the transfer design with one inert 3U envelope and a captive lead-screw pusher as an analysis reference. Four editable FreeCAD states and STEP exports depict stowed, armed, midway and seated positions. Its 81-station nominal B-rep transfer sweep over 200 mm has no internal feeder-solid intersection; that check did **not** include the first-article track and carrier. A later cross-assembly audit found a **34,050 mm³** transfer-bridge/guide overlap and a **74,910 mm³** mid-transfer payload/guide overlap. An unselected integration revision clears exact-solid overlap in four STEP states and 81 sampled transfer stations by lifting a guide window, shortening stop proxies and removing duplicate study solids. R1 leaves a **10 mm unsupported handoff gap**. A separately saved [R2 bridge revision](../cad/gen6_integration_r2/README.md) meets the support lip in sampled nominal states, with four STEP states and 81 sampled transfer stations again showing no exact-solid penetration. The bridge-extension/guide-lift sequence, continuous swept volume, contact load, tolerance and power-off restraint remain unverified. Under *assumed*, not manufacturing, perturbations, the earlier feeder-only interval screen leaves 3.5 mm side and 2.5 mm end-stop clearance. The [state/fault analysis](../cad/gen6_feeder/cycle_and_faults.md) finds a decisive unresolved condition: a payload partway between cassette and cradle lacks a demonstrated positive restraint after power loss. Neither the pusher actuator nor launch locks, contact loads, jam recovery or a working four-cell 1U/3U feed mechanism is selected. The [integration audit](../cad/GEN6_INTEGRATION_AUDIT_2026_10_12.md) records the boundary of the new check. A 6U cell is a later expansion. These follow-on files do not change the Gen5 result or establish P-POD-like reliability.

The subsequent [four-cell R0 study](../cad/gen6_four_cell_r0/README.md) positions two 1U and two 3U inert envelopes in staggered and paired fixed cells. Each unselected layout has 13 editable FreeCAD and STEP states with zero represented nominal solid penetration; four lateral transfer paths and a stowed-carrier docking path were sampled separately. In the staggered layout the final cell has only 330 mm of modeled acceleration path before the brake boundary, requiring 5.56 g *ideal mean* acceleration for 6 m/s. Paired sides give every cell at least 900 mm, reducing that largest ideal mean value to 2.04 g, without changing the 1,800 mm rail. Both layouts span 560 mm laterally before host mounting or access. These are geometry and kinematic screens, not proof of achievable speed, safe contact, power-off retention, carrier docking accuracy or host compatibility.

![FreeCAD-derived paired four-cell plan. Payload cells are envelope proxies; motion, loaded clearances and host fit are unverified.](<../cad/gen6_four_cell_r0/release_paired/Four_Cell_R0_Plan.png>){width=94%}

![FreeCAD-derived handoff section. R1 has a 10 mm open support gap; R2 has nominal face contact. Bridge loads and transition motion are not verified.](<../cad/gen6_integration_r2/release/Gen6_R1_R2_Handoff_Section.png>){width=94%}

![STEP-checked FreeCAD geometry rendered in Blender for four Gen6 one-cell transfer states. Moving hardware and fault containment are incomplete.](<../cad/gen6_feeder/release/Gen6_Feed_One_Cell_Storyboard.jpg>){width=92%}

The [provisional seven-concept weighted screen](../cad/gen6_feeder/WEIGHTED_TRADE_SCREEN_2026_10_12.md) applies the selected 35/25/20/10/10 weights for fault safety, fit/mass, positioning, cycle/power and manufacture. A captive lead screw ranks first as an **analysis reference** at 3.650/5; varying each unmeasured ordinal criterion by one point gives 2.650–4.650. That interval overlaps the spring-follower and rack-pawl alternatives. None has passed the mechanism-level four-cell, power-off-restraint, load or installed-resource gates, so the result does not select a feed mechanism. Alternative concepts remain in the laboratory archive for comparison.

![Provisional feeder ordinal scores and one-point sensitivity intervals; not measured reliability or mass.](<../cad/gen6_feeder/release/Gen6_Feeder_Provisional_Trade.png>){width=94%}

These screens make the next research questions specific, while preserving Gen5 as the sole evaluated thesis configuration. They do **not** close Gen6's mission value, full installed mass, moving-contact/release design, electrical and thermal ratings, qualification or build authorization. The [claim and gate disposition](../GO3_ACADEMIC_RELEASE_REVIEW.md) traces the open items for examination.

![Surrogate four-release comparison. Both strategies reach the same ideal mathematical targets; installed mass assumptions decide this narrow comparison.](<../figures/gen6_matched_campaign.png>){width=88%}

![Gen6 first-article partial CAD material mass versus the remaining surrogate allowance. Unmodelled installed items are excluded.](<../figures/gen6_go2_mass_gate.png>){width=88%}

## Coupled four/twelve-payload construction

The [local coupled-delivery supplement](../validation/coupled_delivery/README.md) adds host pre-burn, finite-mass shot recoil, 20 s coast, transfer/recovery impulses, propellant accounting and final host-state restoration. It uses a 500 km, 97.4° surrogate and constructed 3–9 m/s prograde target increments, with common state assessment at 90000 s. A 3–6 m/s imposed input can reach the targets with host assistance; no motor capability or delivered-state accuracy is demonstrated.

The twelve-payload spring case exceeds a 10 kg reserve but completes with 20 kg initially available, consuming approximately **15.35 kg**. The corresponding 3–6 m/s case consumes approximately **4.05 kg**. The assumed device proxies are 48 and 90 kg, so the fuel saving does not recover the mass penalty. No optimized customer mission or commercial advantage is established. Conditional adaptive interval bounds for nominal point centers exclude the first 20 s near-field phase and assume a 1 cm numerical state-error bound; they are not a physical clearance or collision-probability result.

![Declared mass proxies and consumed fuel; no installed-system advantage inferred.](../validation/coupled_delivery/release/figures/resource_comparison.png){width=98%}

## Seven-concept engineering evidence

The [local feeder review](../validation/feeder_review/README.md) includes all seven candidates, 1U/3U native CAD, STEP states, material-only BOM/CG/inertia, 108 analytical load cases, 12 tolerance stacks and 36 conditional state/fault records. Six native CalculiX runs examine an assumed clamped storage-floor fixture; they do not analyze actual joints or qualify the assembly. The spring sizing fails higher resistance cases and the adverse alignment stack loses clearance. A 972-case rectangular capture-tooth sensitivity reaches approximately 1.97 GPa nominal root bending under the largest calculated mean arrest force, exceeding even the assumed 1000 MPa yield band. Actual material allowable, peak impact force and positive engagement are unknown; this is a redesign finding.

The connected fork-frame correction is distinct from proven mechanical load transfer. Gate/latch engagement, front-barrier handoff, continuous return/indexing, purchased components, actual host mounts and loaded restraint/contact remain open. Ordinal safety-led trade intervals overlap; no concept meets the evidence gate for final baseline selection. The report and source/CAD archive preserve this bounded result without claiming a completed or manufactured feeder.

![Independent STEP-derived nominal lead-screw reference geometry; unselected mechanism with open handoff/contact verification.](../validation/feeder_review/release/figures/lead_screw_cad.png){width=98%}

## Continuous prescribed transfer and servicing disposition

The separately versioned [CT-01 local report](../validation/captive_transfer_review/README.md) provides 22 native/STEP states and continuous interval checks for prescribed rectilinear 1U/3U transfer, receiver capture, fork withdrawal and reset. The storage gate now retracts downward through a floor slot; the 120 mm stroke requires under-deck accommodation. Receiver locks use separate motion bands. All represented nominal primitive pairs clear over the 20 phase cases, with 60 independent native B-rep poses. This does not validate actuator joints, loaded fit, contact or actual receiver-to-sled custody.

![CT-01 STEP side projections with common axes; nominal prescribed motion only](../validation/captive_transfer_review/release/figures/step_sequence.png){width=98%}

A separate enlarged 16 × 6 mm rack-root coupon has one modeled face-contact pose and six native CalculiX fixture cases. Its peak stress remains unconverged and its actual material/impact/attachment are unqualified. The 972-case compliant-stop investigation retains 226 cases exceeding a proposed 24 mm total allowance; 148 of 243 local fit sensitivities are nonpositive. False receiver-lock indication, uncontrolled gate closure and missing external sled custody remain explicit physical counterexamples. No feeder selection or hardware release follows.

![Genuine Python-hosted FreeCAD Qt/Coin viewport of the CT-01 receiver-capture pose. Source document and capture provenance are retained; this is a native application view, not hardware or a completed mechanism.](../validation/captive_transfer_review/release/FreeCAD_CT01_receiver.png){width=92%}

The [limited replenishment concept](../validation/replenishment_feasibility/README.md) defines a closed cooperative cartridge, provisional datums, capture/retention and contamination interfaces, operations and recovery requirements. Its 108 capture and 36 insertion sensitivities retain 18 failed fits. Because the baseline lacks removable-cartridge integration, real servicing access and verified double custody, operational replenishment is a no-go for this configuration. Ground loading remains the assumed campaign boundary. The limited study is complete as a bounded negative feasibility/interface finding; it is not a docking or robotic hardware demonstration.

## Complete native event replay and precision budgets

The separately versioned [CNR-01 native campaign report](../validation/native_campaign_review/README.md) checks the complete prescribed four/twelve-payload host-burn, finite-mass release and recovery sequence from a single initial host state using Orekit 13.1.6. Fifty-one native cases include five nominal baselines, two step refinements and 44 deterministic command-error probes. Native rocket mass loss, recoil and payload propagation agree with the original source at nominal payload endpoints to within 8 µm; the twelve-case step refinement changes payload endpoints by less than 17 µm. These are software consistency results under a fixed-axis J2 model, not physical delivery accuracy or a rigorous continuous error enclosure. Both implementations use DOP853; commanded controls and constructed targets are shared inputs.

![Common-epoch position sensitivity to stated deterministic probes; surrogate missions and no navigation feedback](../validation/native_campaign_review/figures/control_sensitivity.png){width=98%}

A common +0.1% release-speed bias produces approximately 1.53 km position error in the imposed VOLLEY cases. A first-order allocation of the entire illustrative 100 m / 0.1 m/s full-state budget to common speed bias alone is approximately 0.0059%, with all other errors zero. This is not a customer requirement or supported actuator precision. Three hundred twenty-four constant-speed photogate interval cases and 108 dynamic metrology cases expose calibration, timing, thermal, mean-to-exit-speed and frame-compensation dependencies. A longer optical baseline can worsen the exit-speed bound when relative acceleration persists. Post-release measurements cannot correct an already released passive payload.

The twenty equivalent-thrust time screens apply only to the frozen impulse policy. At 5 N, the twelve-spring control plan requires approximately 6135 s of thrust-on time before a 3600 s final release, while the imposed 3–6 m/s case requires approximately 1488 s. These necessary totals omit finite-burn targeting, slew, coast, plume and operational scheduling. Other host-assisted spring strategies may improve this result; no universal service advantage follows. Device mass proxies continue to exceed the fuel saving. Actual installed hardware, finite-burn optimization, navigation feedback and full near-field integration remain unresolved.



## Finite-duration host targeting

The separately versioned [FBR-01 finite-force report](../validation/finite_burn_review/README.md) targets actual finite-duration resultant-force windows with integrated mass consumption. Eighteen solutions vary the two-window fraction, numerical step and fuel reserve; 46 native Orekit runs include nominal replays, refinements and deterministic force/release/initial-state probes. Preparation from −900 s, 20 s post-release guards and recovery to 4200 s are counted. All payloads retain the common 90000 s assessment epoch. The inputs remain imposed release velocities and a fixed-axis J2 point-mass model.

At the 35%/35% policy, four-release spring/VOLLEY inputs require 13.36/6.50 N peak and 6.056/1.895 kg fuel. Twelve-release inputs require 33.83/18.00 N and 23.122/6.123 kg. The twelve-spring 20 kg reserve is exhausted at 3509.06 s; subsequent formal trajectory is diagnostic only. With a common 30 kg reserve and 100 N limit, both twelve-release controls reach the constructed full-state targets. The 17.460 kg propellant saving remains smaller than the 42 kg device-proxy penalty.

![Retargeted finite-force schedules under common mission targets. Each point is a separate solution; limits and hardware resources are surrogate assumptions.](../validation/finite_burn_review/figures/force_fuel_trade.png){width=98%}

Native nominal terminal differences stay below 23 µm and eight numerical refinement differences below 13 µm. These verify numerical consistency, not real delivery accuracy. A single fixed-thruster interpretation requires nearly 9°/s mean direction reversal in some 20 s gaps, with no settling allowance. Opposed thrust allocation might avoid whole-host reversal, but its plumbing, mass, plume geometry and attitude requirements are undefined. Host compatibility, physical near-field safety, navigation feedback, installed hardware and the motor/circuit rating remain open; no operational service is established.


## Feeder actuation and revised custody geometry

The separate [FM-02 engineering review](../validation/feeder_actuation_review/README.md) replaces the tall receiving latch with a 12 mm underfloor entry frame, two positive endpoint crosspins and a physically represented sled. Twenty-eight native FreeCAD/STEP poses and 26 continuous prescribed rigid-translation phases have no represented positive-volume penetration. The storage crossbolt and each receiving pin obstruct the tested adverse motions. Axial pin capture, actual release actuators, loaded contacts and complete deployment/reset remain unimplemented; no hardware containment or manufacturing release follows.

![FM-02 captive handling sequence from actual STEP exchanges. The payload remains retained during the illustrated 80 mm sled translation and return; no launch is represented.](../validation/feeder_actuation_review/figures/step_sequence.png){width=98%}

The integrated ball-screw candidate is a separate ambient component screen and is not installed in this CAD. A quintic rest-to-rest law, moving load, drag, rotational inertia and component limits are checked in 972 scenarios. Polynomial extrema and exact piecewise integrals reproduce every decision; at 801 samples the maximum relative torque and input-energy-proxy discrepancies are $8.58\times10^{-8}$ and $1.08\times10^{-6}$. These are numerical model errors, not physical uncertainties. The sampled 10, 15 and 20 s cases meet the declared ambient screen; 5 s cases fail.

The study retains 115 of 324 nonpositive fit residuals, 12 of 54 winding-temperature failures, 96 no-stop brake sensitivities and 72 finite runouts above the proposed 24 mm allowance. Actual component temperature domains differ, and the two-node thermal model is uncorrelated. A slow 103.0 s handling assumption does not fit eleven later twelve-release coasts of 92.182 s; a faster 74.5 s assumption fits, without actuator, attitude, indexing or full campaign validation. These findings define remaining engineering requirements. All seven feeder alternatives remain unselected; Gen5's achieved computational result is unchanged.

## Feeder geometry, component stiffness and contact limitations: 21 October 2026

The separate [FM06-R1 record](../validation/feeder_integrity_review/README.md) introduces integral support tines, a 12 mm front-restraint stroke and longer receiver guides. Thirty native FreeCAD/STEP poses, seventy individual part exchanges and 28 continuous prescribed rigid-translation checks retain no represented nominal positive-volume interference. An edge-only backstop/rail junction, missed by solid-validity checks, is corrected and all seventy component contact surfaces pass a closed, consistently wound mesh audit. These are reference geometries, not manufacturing drawings or physical qualification.

![FM06-R1 cassette-to-sled transfer state, rendered from native FreeCAD geometry using Blender Workbench. The payload remains retained; installed actuation, rail-end interfaces and free separation are unresolved.](../validation/feeder_integrity_review/figures/FM06_Technical_transfer.png){width=94%}

Twelve native FLR03 cases analyze the actual FM06-R1 receiver solid. Forty historical FLR01 cases provide a separately identified revision comparison. Under 1,000 N reference loads and assumed steel stiffness, the 3U one-dog mean loaded-face displacement changes from 1.8829 mm for FM02 to 0.05998 mm for current FM06. The historical FM03 result is 0.05811 mm and is not substituted for the current revision. The largest final FLR03 mesh-to-mesh compliance change is 0.200%. Both pin bores are fully clamped, so the reduction applies to this component fixture and does not bound assembled stiffness. Reaction force and moment balance are checked; no selected alloy allowable or assembled pin-contact acceptance follows.

Four native unit-load tine meshes yield 0.0101446 mm/N mean end compliance at the finest 53,650-element mesh, with a final 0.0334% change. Forty linear-scaled load sensitivities retain large-deflection and gap failures. At 6 kg and 1 g, an assumed equal load split gives approximately 0.298 mm displacement per tine against a nominal 0.6 mm slot gap; one-tine loading nearly consumes that gap before root/frame flexibility and tolerances. The clamped isolated tine is not a qualification model.

![Native component-fixture compliance comparison. The logarithmic axis covers historical and current receiver revisions under identical reference loads; the supports are idealized clamped bores.](../validation/feeder_integrity_review/figures/component_compliance.png){width=96%}

Longer guides reduce the bounded rigid rocking excursion, but the tighter fit creates a separate manufacturing problem: 1,117 of 1,215 deterministic adverse width/alignment/thermal/deflection combinations have nonpositive residual width. The count is not a statistical hardware failure rate.

The [FCE12 contact-verification study](../validation/feeder_contact_verification/README.md) uses nine disjoint convex native payload cells and exact orthogonal mechanism cells, with full original body mass and inertia. Internal kg/mm/s scaling is checked against a no-contact SI replay. Fourteen analytical planar-gap controls detect imposed 10 µm–1 mm overlaps; the largest checked reported-gap error is 4.28 nm. This is a calibration of the stated planar controls, not a general contact-accuracy claim.

Ten of twelve native sequences reach the 26.5 s transfer/capture/withdrawal endpoint; deliberate jam and stuck-pin cases abort at 11 s. Independent full-solid checks cover 84 targeted poses. Two residual material intersections, at most 0.000124 mm³, admit a nonintersecting pose after a 1 µm Y translation; original trajectories and residuals remain preserved. These discrete checks do not certify continuous loaded clearance.

![Analytical planar-gap controls and fixed-pose replay in the native contact solver. The millimetre-coordinate calculation resolves the imposed overlaps; calibration does not establish final-state convergence or measured precision.](../validation/feeder_contact_verification/figures/contact_calibration.png){width=96%}

The 250-to-125 µs final centre-of-mass differences are 1.509 mm for 1U and 1.466 mm for 3U; the provisional 0.05 mm numerical criterion is not met. Impulsive rigid-contact peaks remain step-sensitive and are not design loads. The capture begins with the storage gate open and does not include free separation or a complete reset. Source-rated installed actuation, actual loaded joints, payload interface approval and mixed-size installed integration remain engineering acceptance requirements. The evidence-gated seven-architecture downselect remains open.

# Bibliography {.unnumbered}

1. JAXA, *JEM Payload Accommodation Handbook*, Vol. 8, small-satellite deployment interface control document, cited in the VOLLEY thesis.
2. California Polytechnic State University, *CubeSat Design Specification*, [Rev. 14.1, 2022](https://www.cubesat.org/s/CDS-REV14_1-2022-02-09.pdf).
3. C. Foster *et al.*, “Constellation phasing with differential drag on Planet Labs satellites,” *Journal of Spacecraft and Rockets*, 55(2), 2018.
4. H. Feng, Y. Yang and Y. Wu, “Design and reachable domain analysis of on-orbit electromagnetic launcher for CubeSats,” *International Journal of Aerospace Engineering*, art. 3000765, 2025.
5. Y. Zhao *et al.*, “Design and analysis of a new deployer for the in-orbit release of multiple stacked CubeSats,” *Remote Sensing*, 14(17), 4205, 2022, doi: [10.3390/rs14174205](https://doi.org/10.3390/rs14174205).
6. Y. Zhao *et al.*, “Simulation analysis and experimental verification of the transport characteristics of a high-volume CubeSat storage device,” *Aerospace*, 12(6), 466, 2025, doi: [10.3390/aerospace12060466](https://doi.org/10.3390/aerospace12060466).
7. K. Halbach, “Design of permanent multipole magnets with oriented rare earth cobalt material,” *Nuclear Instruments and Methods*, 169, 1980.
8. NASA, *General Environmental Verification Standard*, GSFC-STD-7000A, 2013.
9. D. A. Vallado, *Fundamentals of Astrodynamics and Applications*, 4th ed., 2013.
10. A. Mishra, *VOLLEY-thesis*: authored manuscript, baseline, provenance, figures and validation records, technical evidence snapshot `b2e2c1f3932deed363281cc4a94bedfdc155c495`, 19 October 2026. Project record, not independent experimental evidence.
11. VOLLEY, *Gen6 G0 Mission and Article Requirements*, 12 October 2026. Reference study requirements, not achieved performance.
12. H. Q. Yamaguchi and M. Morishita, “End effects of Halbach field magnet-type linear motor,” *Electrical Engineering in Japan*, 2023, doi: [10.1002/eej.23450](https://doi.org/10.1002/eej.23450). Bibliographic context; not an experimental validation of VOLLEY.
