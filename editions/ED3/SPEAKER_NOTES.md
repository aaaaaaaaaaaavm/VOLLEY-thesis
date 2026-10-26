# VOLLEY — 15-minute two-speaker presentation

Delivery allocation: Adityavardhan Mishra, slides 1–8 (7 min 30 s); Pratham Chawla, slides 9–17 (7 min 30 s). This allocates speaking time without assigning individual research contributions.

## 01. Project introduction
Adityavardhan Mishra — 30 seconds

Good morning. We are Adityavardhan Mishra and Pratham Chawla, presenting VOLLEY under the guidance of Vikas Gulia. This project develops and computationally evaluates a commanded electromagnetic CubeSat deployment mechanism. The presentation focuses on the completed Gen5 ACR1 computational reference and the physical validation proposed for Gen6.

## 02. Presentation outline
Adityavardhan Mishra — 20 seconds

We begin with the deployment problem and relevant prior work, then define the research gap and objectives. We explain the computational method and progress before moving to the mechanism and results. We close with the mission trade, conclusions and the proposed Gen6 validation programme.

## 03. Commanded release adds a local delivery variable
Adityavardhan Mishra — 65 seconds

A deployer is an interface between a host platform and a free-flying spacecraft. The host can manoeuvre before release, while the deployer sets a local relative velocity at a specific event. These are related but distinct controls. A release impulse can change orbital energy and subsequent phasing, and its usefulness depends on the delivery objective and the available host resources. Our schematic identifies the event rather than depicting a flight vehicle. The design question is therefore broader than generating force. The payload must remain retained and guided before command, the moving carrier must be arrested and returned, and its momentum and installed mass must remain in the mission budget. This is the system boundary used throughout the study.

## 04. Prior work establishes the mechanisms and comparison context
Adityavardhan Mishra — 90 seconds

Electromagnetic CubeSat deployment and high-volume storage are established prior art. Zhao and colleagues reported stacked electromagnetic release in 2022, including gravity-compensated laboratory tests. Their measured velocities belong to their mechanism, payloads and test conditions. The 2025 storage study examines pushing, receiving guides and magnetic transport, including spacecraft-side grooves and iron patches. That interface differs from the passive rectangular envelope represented here. Feng and colleagues examine a higher-speed launcher and reachable domain, which provides mission context but uses a different operating regime. Halbach supplies the permanent-magnet field concept, while finite-motor literature identifies the importance of longitudinal end effects. The present contribution is the integration and evaluation of one explicit retained-carrier reference: custody, finite force, source limits, arrest and host burden are assessed together. We preserve the distinction between third-party experimental evidence and our numerical results.

## 05. Research gap: closing the complete retained-carrier cycle
Adityavardhan Mishra — 70 seconds

The research gap addressed here is integration at a defined reference boundary. First, a storage-to-release mechanism needs an explicit answer to who holds the payload at every transition. Second, a useful electromagnetic result requires the force map, real moving mass and electrical source to be solved as one problem, including what happens after the spacecraft separates. Third, the retained carrier and installed hardware affect the host even when the payload has departed. The study connects these questions using one controlled mechanical revision. This supplies a reproducible basis for evaluating operating cases and for deciding which measurements a physical prototype must provide. It is a design-specific integration contribution rather than a claim that adjustable electromagnetic ejection is a new principle.

## 06. Objectives and controlled reference requirements
Adityavardhan Mishra — 60 seconds

The reference manifest contains twelve identical four-kilogram 3U envelope surrogates. The represented contact envelope is 340.5 by 100 by 100 millimetres. The current computational operating study covers commands from one to three metres per second. The rail is 2250 millimetres long, and the post-release arrest allocation is 210 millimetres. Within this boundary, the objectives are to define continuous payload custody, evaluate the finite motor geometry, solve the coupled source and mechanical cycle, and carry the retained burden into structural and mission evaluation. These values identify the analysed configuration. The later mixed-size prototype will need its own payload interfaces and verification rather than inheriting this twelve-3U definition.

## 07. One source chain connects the machine to the mission
Adityavardhan Mishra — 80 seconds

The source chain begins with geometry, retained mass and custody. Those inputs enter the finite motor and source-coupled shot, including release and arrest. The resulting forces support the structural and interface budgets. The achieved release map and full installed burden then enter the same-target mission comparison. Independent checks have different roles: native and STEP readback test exchanged geometry, alternative field and current formulations check numerical approximations, the principal shot is timestep refined, and Orekit replays the mission trajectories. The corrected ANSYS static comparison adds a separate solver under matched bare-chassis assumptions. This dependency chain keeps the results on one declared ACR1 reference.

## 08. Timeline and work progress
Adityavardhan Mishra — 35 seconds

The work has progressed from literature and problem framing to the Gen5 ACR1 reference, followed by the coupled computational study. The current stage is the academic report and presentation capture. The computational design study is complete within its stated reference cases. Gen6 is the proposed physical development stage, beginning with an instrumented mixed 1U and 3U prototype. Pratham will now explain the reference mechanism and the engineering results.

## 09. Reference architecture: fixed banks and one captive pallet
Pratham Chawla — 70 seconds

The reference mechanism has two fixed banks with six cells per bank. Positive guided pushers feed one selected payload toward the central lift. The lift carries a single captive pallet, and that same physical pallet docks to the launch carrier. The magnet arrays remain on the reusable carrier rather than on the payload. This is the complete native CAD home state, including the storage banks and generic mounting ladder. The retained moving carrier, pallet, lock pins and reference actuators total 13.128 kilograms. Represented dry CAD mass is 149.557 kilograms, with a separate seven-kilogram power and control allowance. These masses are part of the system assessment. They are material-volume and assigned-reference totals, rather than a weighed physical article.

## 10. Capture before release: one pallet, two holders
Pratham Chawla — 70 seconds

This enlarged native CAD handoff view shows the receiving interface. The lift still holds the pallet while its four feet land on the carrier. The upper capture caps and both bayonet locks engage and prove receiving custody before the lift grip pins retract. The lift then rises clear. That same pallet stays on the retained carrier during launch, arrest and return. The view hides the banks, host ladder and fixed lift frame to expose the actual interfaces. Fixed passive cams later open the forekeepers through twelve millimetres over fifty millimetres of carrier travel, completing five millimetres before release. Slow guided transfer and position-defined release remain distinct parts of the cycle.

## 11. Finite geometry gives the force used by the shot model
Pratham Chawla — 55 seconds

The motor has forty-two discrete magnet blocks on each opposed retained array and two hundred and sixteen active stator bars. The graph shows the captured force-position coefficients. Active conductors give approximately 1.3287 newtons per peak phase ampere in the interior. Represented return conductors bring the simpler result to about 1.3991. Actual conductor-current FEM differs by 0.172 percent at the checked interior station under the same permanent field. This is local model agreement, not a physical accuracy bound. Position dependence is retained in the source-coupled launch and arrest calculations. Force, resistance, inductance and back-emf correlation are defined measurements for the later physical prototype.

## 12. The carrier accelerates, releases, then arrests
Pratham Chawla — 65 seconds

This single trace follows carrier speed relative to the host. The loaded carrier accelerates, and electrical braking reduces the rear-contact reaction to zero near 1.3 metres. The payload then departs while the carrier and pallet remain on the rail. The motor actively arrests the retained carrier at 1.507 metres, within the allocated 210 millimetres after release. The nominal twenty-microhenry case gives a release speed of 2.999864 metres per second and source draw of 379.7 joules. Six principal three-metre-per-second nominal/adverse and inductance cases pass the reviewed five-microsecond timestep audit. The detailed current, voltage, loss and thermal evidence remains in the report. Conservation and numerical agreement support the stated model; measured device temperatures and release distributions require physical correlation.

## 13. A second solver agrees under the matched chassis boundary
Pratham Chawla — 65 seconds

The corrected ANSYS package checks the same bare chassis, material, opposed 3.010-kilonewton patch forces and six scalar numerical restraints. Primary paired closure is 0.286392 millimetres against 0.285983 from CalculiX, a difference of 0.143 percent. The three ANSYS meshes span 0.285241 to 0.287589 millimetres. They supply sensitivity evidence rather than a formal convergence or error guarantee. Independent native-result interpolation reproduces all 11,448 primary samples. The existing face budget remains tied to CalculiX: applying its explicit centred formula to the finest ANSYS peak gives a conditional 0.263067 millimetres instead of 0.264111. This comparison does not establish actual assembled clearance. Contact-energy rate bounds remain separate in the report; support behavior and physical qualification require their own evidence.

## 14. The preplanned mission trade favours ideal ground pretrim
Pratham Chawla — 65 seconds

The displayed selected case uses alternating one and three metre-per-second target families and a five-newton host ceiling. VOLLEY uses about 0.28987 kilograms of host fuel; ideal ground pretrim uses about 0.05365. Both use the same five-hundred-kilogram wet bus and twelve four-kilogram payloads, while retained device mass differs. VOLLEY retains 156.557 kilograms against the declared seventy-two-kilogram spring-class assumption. The initial wet totals are 704.557 and 620 kilograms. In the uniform two-metre-per-second family, VOLLEY uses 0.05244 kilograms and fixed spring uses 0.04696. Pretrim also has a tested one-newton alternating solution. These preplanned cases demonstrate no mass or fuel advantage. The full table records different release/burn guards, and failure within sampled policies is not global infeasibility.

## 15. Conclusions of the computational design study
Pratham Chawla — 30 seconds

The study produces a complete computational reference for a repeated deployment cycle, from retained storage to carrier return. The declared low-speed cases are evaluated with finite motor geometry, actual retained mass and a stated source, and the principal three-metre-per-second cases receive an independently reviewed shared-solver timestep audit. The system burden remains substantial and the mission comparison supplies no mass or fuel advantage over ideal pretrim. This defines the outcome and the next physical validation step.

## 16. Gen6: an instrumented mixed 1U / 3U physical prototype
Pratham Chawla — 20 seconds

Gen6 is the proposed physical prototype stage. It should characterise the motor and source, correlate custody and contact behaviour, and then demonstrate instrumented release, arrest and repeated duty. Mixed one-unit and three-unit handling needs fresh envelopes, retention definitions and mass accounting. Higher-speed scaling requires new coupled energy, acceleration, arrest and thermal budgets.

## 17. Selected references
Pratham Chawla — 10 seconds

These selected references support the interface assumptions, prior-work comparison and numerical methods. The full bibliography and traceable engineering records accompany the report. Thank you; we welcome questions.
