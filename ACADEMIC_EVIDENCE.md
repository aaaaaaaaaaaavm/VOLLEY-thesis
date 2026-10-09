# Academic evidence guide and examination questions

The thesis claim is narrow: **a fixed Gen5 system-level design was computationally evaluated and shown to fail an important 3U mass criterion despite modeled orbital utility.** This guide links the result, counterresult and limitation within this repository.

| Examiner question | Answer to present | Inspect here |
|:--|:--|:--|
| What exactly was designed? | A 1.5 m electromagnetic guide, 1.3 m powered stroke, reusable sled, energy store, arrest system and conceptual twelve-3U magazine. | [System manuscript](source/paper.tex), [Gen5 CAD](cad/step/gen5/) |
| Which values are predictions? | 16.029 m/s, 10.07 g, 2.78 kJ, 0.0274 m/s simulated 3σ and orbit outputs. None is a VOLLEY measurement. | [Baseline](appendix/BASELINE.md), [result JSON](analysis/results/), [provenance](appendix/PROVENANCE.md) |
| Which checks are independent? | Named field, circuit, structure and orbital comparisons; each checks only its stated model aspect. Other outputs remain single-sourced. | [Validation register](validation/README.md), [provenance](appendix/PROVENANCE.md) |
| Does it meet the economic objective? | **No.** 126.6 kg dry / 12 = 10.55 kg per satellite, above the approximately 2 kg/satellite criterion; it is also 1.758× a roughly 6 kg/3U canister against a ±15% parity band. | [Mass JSON](analysis/results/mass_properties.json), [payload family](analysis/results/payload_family.json), [manuscript comparison](source/paper.tex) |
| Does the orbital result establish a delivered mission? | No. The quoted 28.8 km and 1.60× refer to a stated single 450 km, mean-activity model case. Host operations, lifetime variability and complete manifested delivery need separate closure. | [Orbit JSON](analysis/results/astro_results.json), [manuscript limitations](source/paper.tex), [open problems](appendix/OPEN_PROBLEMS.md) |
| Can an ordinary CubeSat survive release? | Unproven. Modeled acceleration is not a payload-specific load qualification. Retention, contact, tip-off, vibration, contamination and interface approval remain open. | [Manuscript limitations](source/paper.tex), [open problems](appendix/OPEN_PROBLEMS.md) |
| What was built or physically validated? | No VOLLEY hardware. Literature and third-party products are comparators, not tests of this configuration. | [Provenance](appendix/PROVENANCE.md), [prior art](appendix/PRIOR_ART.md) |
| What is Gen6? | Future scale-up research toward a 1 km/s-class objective, without a selected architecture, qualified payload or achieved release speed. | [Gen6 review direction](university/final_review_2026_10_10/GEN6_DIRECTION.md) |

## Reproduce and inspect

1. Read the [manuscript](source/VOLLEY_IEEE_Conference.pdf) and [baseline](appendix/BASELINE.md) together. The baseline names result fields.
2. Inspect [analysis/results](analysis/results/) and the corresponding scripts in [analysis](analysis/). Follow the local [validation register](validation/README.md) for declared bands and failures.
3. For review-slide claims, use the [claim/evidence map](university/final_review_2026_10_10/CLAIM_EVIDENCE_MAP.md); its paths resolve inside this repository.
4. Inspect the [CAD](cad/) as model geometry, and the [defect register](appendix/OPEN_PROBLEMS.md) before describing readiness.

## What “complete” means at this review

The design configuration, analysis chain, captured results, negative mass decision, manuscript, final-review slides and explanatory material form a documented **computational academic study** with a negative mass finding. Decisive model verification, full mission closure and installed-system validation remain open as stated in the local evidence register. This is not hardware verification or a claim that all system requirements passed. A future product needs a provider and ICD, a complete installed-system and mission comparison, feeder/retention/recoil design, payload-specific loads, environmental qualification and repeatable calibrated releases.

The 23-slide deck is a concise presentation of the result. The manuscript and local analysis files carry the deeper evidence. A university-specific final report template was not provided; formatting compliance must be checked when the institution supplies one.

**CAD/mass provenance:** the 9.445 kg sled input was measured from historical Gen3 CAD solid volumes and checked with the A4 chassis idealization. The current Gen5 STEP package is a geometry model. The 126.6 kg rollup includes assumed component masses and is not a mass extraction from a complete installed Gen5 assembly.
