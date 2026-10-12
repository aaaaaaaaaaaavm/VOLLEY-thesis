# VOLLEY final-year black book: submission-readiness checklist

**12 October 2026.** This is a planning checklist based on the supplied SIT Mechanical Engineering review rubric and the current VOLLEY repositories. The uploaded *B-Tech Docs required.pdf* gives a **40-mark final presentation/demonstration rubric**, not a mandatory black book template. The uploaded presentation-format PDF supplies an eleven-part slide outline using another project's content; it is not a report-format instruction. Obtain the actual university black book template and submission rules before declaring format compliance.

## The defensible thesis statement

The evaluated **Gen5 twelve-3U configuration** is a completed *computational feasibility study with a negative design-selection result*. Its historical 16.029 m/s shot is challenged by a 12.448 m/s ideal finite-geometry screen; its modeled mass fails the preset 3U criterion; its reference side feed clashes by 11 mm; and no sampled twelve-shot mission case closes. It is not a built, verified or flight-qualified machine. The mixed-size Gen6 mission, two partial first-article CAD candidates and all feeder concepts are clearly labeled **future research**. A new feeder may be studied in a separate revision; it cannot silently repair or retroactively validate Gen5.

The absence of a physical prototype does **not** itself violate the supplied 40-mark rubric: a functional prototype is listed under *additional recognition*. The report must therefore make numerical verification, model limitations and unrun hardware tests unmistakable.

## What already exists

| Record | Current state |
|:--|:--|
| Chaptered academic report and PDF | `university/GEN5_FINAL_YEAR_REPORT.md/.pdf`; Gen6 P130–P132 appear only as future work. |
| IEEE-formatted manuscript and PDF | `source/paper.tex` and `source/VOLLEY_IEEE_Conference.pdf`; IEEE venue and final submission rules remain unselected. |
| Presentation and presenter materials | 26-slide PPTX/PDF, handout, run sheet, presenter reference and panel handbook under `university/final_review_2026_10_10/`. |
| Traceable numerical record | Local `analysis/`, `validation/`, figures, adverse results, model scripts and captured JSON. |
| CAD and visualization | Gen5 native FreeCAD/STEP review, failed fit record, unselected wider R1 geometry; separate Gen6 partial FreeCAD/STEP envelopes and labeled renders. No working feeder mechanism is modeled. |
| Offline handover | `university/final_review_2026_10_10/GO3_ACADEMIC_REVIEW_PACK.zip`, with embedded SHA-256 list. |

## Must be finished for a clean black book submission

1. **Obtain the official black book rules:** report template, page/print/binding or digital format, required certificate/declaration/approval pages, plagiarism/similarity rule, signature process and deadline. Do not infer them from the example slides.
2. **Agree the exact claim with the guide:** title, abstract, objectives and conclusion should all say *computational study and design disposition*. State the feeder as an unresolved Gen5 configuration failure and a Gen6 future design task. Keep individual student contributions unstated unless the university requires a declaration; confirm any mandatory wording with both students and the guide.
3. **Freeze one academic revision:** report source/PDF, manuscript source/PDF, deck, CAD and STEP revision IDs, model inputs/results, figure provenance, bibliography, software versions, run logs, file hashes and known exceptions must agree. Preserve the adverse numbers rather than replacing them with newer Gen6 assumptions.
4. **Run a final claim audit:** every headline speed, force/work, energy, mass, CAD clearance, orbital result and mission comparison needs a page/figure/table-to-script/result path. Separate assumption, derived result, independent numerical check, published comparator and unrun physical test in captions and tables.
5. **Resolve or explicitly disposition the decisive open checks:** selected-circuit and winding feasibility, feed/release contact, brake, structural and thermal loads, payload magnetic exposure, complete mass and host interface, lifetime and matched mission. A black book can report these as limitations of a negative computational study; it cannot say the deployer is validated if they remain open.
6. **Complete the research and citation read:** verify close electromagnetic deployer papers in full text, distinguish prior art from VOLLEY's system-level contribution, cite the exact revisions of CubeSat and dispenser documents, and remove unsupported price or performance claims.
7. **Independent review and signatures:** ask the guide and one technically independent reader to examine the report, numerical examples, figures and limitations. Record corrections and required university approval. The repository checks are reproducibility aids, not examiner approval.
8. **Submission rehearsal:** build from a clean checkout, open the actual final PDF and all figures, inspect links and page breaks, rehearse the 15-minute two-speaker defense, and keep a printed/offline response for the 16.029/12.448 m/s distinction, 11 mm clash, 10.547 kg/3U mass and lack of prototype.

## To claim a *complete working machine* instead

This would be a different evidence threshold. The feeder needs a selected architecture, full editable CAD/STEP and drawings for the magazine, individual payload restraints, cell selection, pusher, cradle, barrier and safe reset. The drive needs a selected source, inverter and winding with coupled force/circuit/thermal results. The payload handoff and sled departure need contact/tip-off, jam, abort, host-recoil, brake/containment and tolerance analysis. Installed mass/CG/inertia must include every part and be compared on a real customer/host mission. Physical build, repeated calibrated shots, environmental qualification and provider approval would be needed before claiming hardware reliability. None is present today.

## How the supplied 40-mark rubric exposes the gaps

| College criterion | Marks | What a rigorous examiner can inspect | Remaining concern |
|:--|--:|:--|:--|
| Achievement of objectives | 10 | A clearly bounded Gen5 feasibility question and negative decision | A claim to have produced a complete deployer would fail; align stated objectives with what was actually evaluated. |
| Technical quality and innovation | 10 | Model chain, CAD/STEP, system-level negative finding and distinct Gen6 hypotheses | No selected feeder, circuit or safe release design; electromagnetic ejection itself has prior art. |
| Results, validation and analysis | 5 | Source-linked results, finite-force checks, orbit check, failed fit/mass criteria | No hardware validation; important coupled and uncertainty checks remain open. |
| Report and documentation | 5 | Report, references, run sheets, captions, figures and artifact hashes | Official black book format, final claim sweep and guide approval open. |
| Presentation, demonstration and viva | 10 | Deck, two-speaker run sheet, offline evidence and live CAD/results walkthrough | Demonstrate *computational work*, label renders and unrun physical tests honestly. |

The college rubric reserves **additional recognition** for a functional physical prototype, industry involvement, impact and publication potential; it does not list prototype construction as a prerequisite for the 40 marks. The engineering case for a future product must be assessed separately from this academic result.
