# VOLLEY speaker notes

Planned 15-minute route; actual rehearsal timing is recorded separately.

## 1 · VOLLEY
Page 1 · Adityavardhan Mishra · planned 15 seconds

VOLLEY is a commanded electromagnetic CubeSat deployment mechanism. We developed and computationally evaluated a complete storage, transfer, launch and carrier-recovery reference. This presentation explains the engineering, the results and the programme it supports.

Sources: Design and Computational Evaluation · October 2026

## 2 · From the delivery problem to the engineering result
Page 2 · Adityavardhan Mishra · planned 15 seconds

We begin with the mission and the design choices, then follow one payload through the machine. We explain the coupled motor and source, geometric and structural checks, and matched mission comparison. We close with the completed study and the next development steps.

Sources: Department presentation format; blackbook chapters 1–11

## 3 · The host moves the orbit. VOLLEY commands departure.
Page 3 · Adityavardhan Mishra · planned 40 seconds

A satellite inherits the host state and a relative release vector at separation. POEM demonstrated a powered, attitude-controlled platform using a spent PS4 stage. Electron’s Kick Stage demonstrated manoeuvres before satellite release. These are architectural precedents. Our evaluated host remains a generic manoeuvring reference, with no approved vehicle accommodation. The service question is whether additional local release control is worth its installed and operating burden.

Sources: Blackbook §§1.1,2.2,8.1; ISRO POEM; Rocket Lab Kick Stage

## 4 · The contribution is the integrated retained-carrier cycle
Page 4 · Adityavardhan Mishra · planned 40 seconds

Adjustable electromagnetic separation is established prior art. We credit the published deployers and their experimental evidence. Our contribution is the design-specific integration and evaluation of a reusable retained-carrier architecture. The same represented geometry and mass connect the feeder, finite motor, source-limited shot, structural budget and mission comparison. Results from another apparatus support methods and comparisons; they are not measurements of VOLLEY.

Sources: Blackbook chapter 3; doi:10.3390/rs14174205; doi:10.3390/aerospace12060466; doi:10.1155/ijae/3000765

## 5 · A complete reference for twelve retained payloads
Page 5 · Adityavardhan Mishra · planned 45 seconds

The academic reference holds twelve identical four-kilogram 3U surrogates. Their contact envelope is 340.5 by 100 by 100 millimetres. Two fixed six-cell banks feed one captive pallet on an indexed lift. The pallet docks to a retained magnetic carrier. The objectives are continuous custody, finite electromagnetic force, source-coupled release and arrest, and a mission assessment including retained resources. Mixed 1U/3U belongs to the subsequent prototype programme.

Sources: Blackbook §§2.1–2.3,5.1

## 6 · Feed one cell into a supported receiver
Page 6 · Adityavardhan Mishra · planned 65 seconds

Follow the payload, not just the actuator. It begins retained in a fixed cell. The lift-held pallet is indexed to the source. A guided positive pusher advances the payload along the restrained path. The receiving end frames and keepers contain it before the pusher retracts and the source closes. The receiver then moves to the carrier. The lead screw offers controlled travel and a defined load path. Seven feeder alternatives were compared in Labs; their scores are engineering judgments, not measured reliability. We retained the runner-up and rejected concepts for traceability.

Sources: Blackbook §§5.1–5.4,7.4; Labs feeder selection

## 7 · Transfer custody before withdrawing support
Page 7 · Adityavardhan Mishra · planned 55 seconds

Four pallet feet land on the carrier while the lift remains engaged. Capture caps, lock pins and the keyed pallet shafts establish carrier capture. Lift grips retract by 26 millimetres only after the permitted state is established. Before departure, fixed cams open the forekeepers. Electrical braking reduces the unilateral rear-contact reaction to zero; the payload then leaves. The pallet and magnetic carrier remain on the host, arrest under the motor map and return. This separates payload release from carrier recovery.

Sources: Blackbook §§5.2–5.4,9.2

## 8 · Finite geometry sets the motor force
Page 8 · Adityavardhan Mishra · planned 55 seconds

The phased fixed winding and moving magnet arrays form a linear synchronous motor. Current density and magnetic field give longitudinal Lorentz force. The equal and opposite reaction acts on the moving array carrier. A periodic wave is useful for initial sizing, but finite end geometry and returns matter to launch and arrest. We report approximately 1.328 newtons per peak phase ampere for active conductors and 1.399 including represented returns. Pratham will now explain how those forces were coupled to a finite source and checked against the mechanical cycle.

Sources: Blackbook §§4.2,6.1–6.2

## 9 · Solve source, current and motion together
Page 9 · Pratham Chawla · planned 60 seconds

The shot calculation couples current dynamics, finite force, source voltage and motion. The phase relation contains winding resistance, inductance and back-emf. The capacitor is not ideal: its internal voltage, ESR and physical power root are evaluated. Requested braking is also constrained by regenerative terminal voltage. Payload and carrier initially interact through compressive rear contact. That contact cannot pull the payload. After detachment, the reduced mechanical system changes and the same finite motor arrests the retained carrier. The audit checks the algebra and limiting logic of an instrumented production solver; it is not an unrelated full physics implementation.

Sources: Blackbook §§4.3–4.4,6.3–6.4

## 10 · The principal 3 m/s case completes release and arrest
Page 10 · Pratham Chawla · planned 75 seconds

The source reference uses 64 Eaton-family cells in a 32-series two-parallel arrangement. Nominal capacitance is 6.25 farads and ESR 0.176 ohms; adverse source assumptions are separate. One three-half-bridge inverter uses ten MOSFETs per switch position, sixty in total. We show the nominal twenty-microhenry principal replay. Relative release is 2.999864 metres per second; stopping occurs at 1.507289 metres from the model origin. All six principal combinations of nominal/adverse conditions and three inductances pass declared checks in the refined audit. The 1 and 2 metre-per-second cases support the analysed range, while the full timestep audit applies specifically to 3 metres per second.

Displayed result context: 64 cells, 32S2P; 86.4 V initial source command; Principal nominal replay: 2.999864 m/s relative departure; Carrier stops at 1.507289 m, inside the post-release allocation

Sources: Blackbook §§6.3–6.4; coupled shot and timestep audit

## 11 · Check solids, states and the represented motion path
Page 11 · Pratham Chawla · planned 45 seconds

An isometric rendering explains the assembly, but geometric checks use individual shapes, connected-solid status and intersections. Eight states preserve the part identities and physical pallet count. The accepted motion record combines 135 retained poses and 19 final direct checks. Certain changes also have strict material-subset or conservative travel-envelope arguments. These are nominal geometric checks with stated allocations, not a measured manufacturing tolerance distribution. Represented dry CAD mass is 149.557 kilograms; a separate seven-kilogram power/control allowance is carried into mission accounting.

Sources: Blackbook §§7.1,7.3–7.5; native/STEP readback

## 12 · Independent static calculations reproduce paired closure
Page 12 · Pratham Chawla · planned 60 seconds

Magnetic attraction loads the carrier across the gap. The actual connected bare-chassis geometry is subjected to opposed inward patches with matched numerical restraints. Each resultant is approximately 3010.481 newtons. CalculiX gives 0.285983 millimetres paired closure; the primary ANSYS sample gives 0.286392, approximately 0.143 percent higher. Three ANSYS meshes examine refinement sensitivity. A sum of two remaining gaps does not establish each individual assembled gap. The individual-face budget additionally uses centring, flatness, assembly and thermal allocations. Solver agreement supports this matched numerical boundary; it does not measure complete assembled hardware.

Displayed result context: Each array patch receives approximately 3.010 kN inward; CalculiX reference paired closure: 0.285983 mm; Primary ANSYS sampled closure: 0.286392 mm

Sources: Blackbook §7.2; corrected matched ANSYS static cross-check

## 13 · Thermal budgets and interlocks complete the operating boundary
Page 13 · Pratham Chawla · planned 50 seconds

Energy accounting includes mechanical change, copper, inverter, bank and auxiliary terms. Thermal estimates distinguish bulk temperature rise from local adiabatic observations. The 3.295053-kelvin quantity in the repeated-operation discussion is a temperature rise, not a percentage. Four hundred and fifty seconds is assumed shot spacing, not the diffusion time. The interlock model checks twenty-four nominal commands and one hundred and sixty-six tests, including declared power-loss, jam, disagreement, timeout and host-burn cases. These test the represented logic. They do not provide a measured probability of successful release.

Sources: Blackbook §§5.4,7.6–7.7; source energy and interlock records

## 14 · Compare equal delivery targets and count retained resources
Page 14 · Pratham Chawla · planned 90 seconds

A fair comparison includes device mass, changing host mass, recoil, fuel and allowed operations. We use the same target position and velocity states at a common terminal epoch. In the selected alternating-family five-newton cases, VOLLEY uses about 0.28987 kilograms of host propellant and ideal ground-pretrimmed springs about 0.05365. Retained device assumptions are 156.557 and 72 kilograms respectively. The result establishes no mass or fuel advantage for VOLLEY in this tested preplanned service. This identifies where a customer case must be stronger, such as a genuine need for on-orbit command flexibility. That flexibility has not itself been priced as demonstrated economic benefit. Native Orekit replay checks the declared mission arcs and J2 boundary; it is not a full flight safety analysis.

Displayed result context: Common payload manifest, target states and terminal epoch; Compare host-assisted VOLLEY with host-assisted spring alternatives; In the tested preplanned case, ideal ground pretrim uses less propellant

Sources: Blackbook §§8.2–8.5; mission comparison and native Orekit replay

## 15 · A complete computational reference connects the machine to the mission
Page 15 · Pratham Chawla · planned 40 seconds

The achieved result is a complete computational design reference. It provides an explicit payload path, a finite motor and source-coupled operating study, geometric and structural checks, thermal and control budgets, and a matched mission comparison. The 1–3 metre-per-second study supplies the evaluated academic envelope. The conclusions include both the supported operation and the system trade revealed by the mission case. This is the engineering basis for selecting and instrumenting a physical article.

Sources: Blackbook chapters 9–11

## 16 · Development follows linked engineering questions
Page 16 · Pratham Chawla · planned 30 seconds

VOLLEY developed over more than five years. We describe the stages using the documented lineage rather than assigning every related repository the same age. Concept selection led to payload handling, finite motor geometry, coupled source and motion, structural and mission evaluations. The completed reference now supports prototype requirements. Related tools emerged from specific engineering needs. Adityavardhan will close by showing that ecosystem and its staged development direction.

Sources: Blackbook development appendix; documented project history

## 17 · An engineering ecosystem grew around the deployment problem
Page 17 · Adityavardhan Mishra · planned 35 seconds

The ecosystem is organised by the questions it answers. Labs preserves mechanism alternatives, experimental comparisons, new speed configurations and lunar architecture studies. The related repositories extract reusable tools for motor design, separation dynamics, orbital comparison, CAD evidence and numerical traceability. GatewayCX is a separate cislunar communications architecture. Future VOLLEY delivery studies could consider deployment of suitable infrastructure for that network; no integrated flight system is claimed. The technical paper is planned as a publication of the checked study, with a venue still unselected.

Sources: VOLLEY Labs research catalogue; engineering tool repositories; GatewayCX architecture

## 18 · Gen6 turns the reference into an instrumented hardware programme
Page 18 · Adityavardhan Mishra · planned 65 seconds

Gen6 begins with instrumented mechanism and motor articles and an integrated mixed one-unit/three-unit prototype. A separately specified Labs configuration has computed ten-metre-per-second release cases. Kilometre-per-second performance is a stretch research objective requiring a different source, stroke, loading and host architecture. The 3.5-kilometre-per-second case is a longer-term departure scenario, not an achieved launcher rating or automatic lunar-orbit delivery; lunar targeting and capture remain separate. The wider service hypothesis is standardised batches of short-life spacecraft, clustered or phased deployment, replenishment and planned disposal where mission needs permit. Artemis-era lunar infrastructure motivates later communications and science applications, including a possible GatewayCX relationship.

Sources: Blackbook §11.2; Labs high-speed and lunar architecture studies; NASA lunar infrastructure programme

## 19 · Commanded deployment, evaluated as a complete system
Page 19 · Adityavardhan Mishra · planned 20 seconds

The full references and source routes are provided in the technical appendix and supporting records. The study connects a defined machine, coupled calculations and a clear hardware measurement programme. We welcome questions; both of us can address the mechanism, methods and results.

Sources: Full bibliography in blackbook; technical appendix and source-linked study records

## A1 · Reference quantities and mass boundaries
Page 20 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Reference configuration

## A2 · Why a guided lead screw?
Page 21 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Feeder selection

## A3 · Capture before lift release
Page 22 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Pallet custody

## A4 · Finite-field and current-path comparisons
Page 23 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Electromagnetic methods

## A5 · Source and switching allocations
Page 24 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Electrical reference

## A6 · Principal nominal energy account
Page 25 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Energy verification

## A7 · Gap closure and individual-face budgets
Page 26 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Structural interpretation

## A8 · Thermal and fault interpretation
Page 27 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Thermal and control scope

## A9 · Host reaction and the common terminal epoch
Page 28 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Mission mechanics

## A10 · Higher-speed work already in Labs
Page 29 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Research configurations

## A11 · Lunar departure and capture are separate operations
Page 30 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: Cislunar architecture

## A12 · Selected bibliography and research record
Page 31 · Shared questions · planned 0 seconds

Technical question slide: use the displayed source and configuration boundaries.

Sources: Blackbook: References and research ecosystem
