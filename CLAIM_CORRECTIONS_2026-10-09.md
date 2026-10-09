# Gen5 manuscript claim audit — 9 October 2026

**Purpose:** record changes made before using the manuscripts in the college review or a later IEEE submission. These are editorial corrections to evidence scope. The rated shot model and its captured numerical output were not silently re-baselined.

| Earlier manuscript wording or implication | Current treatment | Reason |
|:--|:--|:--|
| A 1.5 m physical track | 1.5 m release station and 1.3 m powered stroke on 1.8 m structural longerons | [`cad/parameters.json`](cad/parameters.json) specifies 1800 mm longerons, 1500 mm release point and 1300 mm acceleration-zone end. |
| Lateral feed and retention were effectively free; release followed automatically from sled braking | Feed, restraint, contact, release timing and tip-off are proposed functions that require moving-contact analysis and tests | The [FreeCAD review](cad/GEN5_CAD_REVIEW.pdf) finds a side-fed packaging clash; no feed/release test exists. |
| A restartable or POEM-class stage could host the device with routine electrical taps | Host examples are context only; no provider ICD, mounting approval, magnetic accommodation or safety review exists | A public host description does not establish an interface. |
| A twelve-3U spring-deployer system weighed 10–20 kg in the service table | Approximate comparator is 12 × 6 kg = 72 kg; the comparison remains approximate | The 6 kg per-3U figure used elsewhere in the study must be multiplied by twelve for a matched count. |
| A 2 K bulk thermal rise meant successive shots could not be significantly preheated | 2 K is a uniform bulk-average calculation; the brake-fin no-cooling bound is 108 K over twelve shots | No transient local thermal model has closed between-shot temperature. |
| Balancing, shielding, segmentation and fault controls were described as achieved | They are proposed controls with open component, circuit, EMC and fault-injection checks | No installed power system or measured fault test exists. |
| A ground or captive test automatically delivered a named TRL or needed no approval | Future tests are conditional milestones; TRL and provider approval require a separate assessment | No hardware or host acceptance exists. |
| Less than 1 Wh shot energy meant negligible service cost | Energy is a modeled electrical quantity; installed mass, host power, integration, operations and risk dominate the open business case | A matched priced mission comparison is unavailable. |
| Release timing alone produced lasting phase | Persistent phase requires a relative-state change such as release impulse, host manoeuvre or differential drag | Zero-relative-impulse waiting from an unchanged host has no lasting co-orbital phase benefit. |

The [P117 independent algebra audit](validation/P117_rated_energy_mass_audit.md) additionally finds that **124.488 J (4.47%) of gross electrical draw is unitemized** by the compact published energy terms. This is an accounting gap, not a measured loss. [P115](validation/P115_rated_orbit_cartesian.md) confirms the immediate two-body orbit result only; [P116](validation/P116_gen5_assembly_packaging.md) records the failed side-fed CAD fit. No line here asserts physical validation of Gen5.
