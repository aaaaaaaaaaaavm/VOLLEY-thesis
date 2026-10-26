# Academic edition ED2

**VOLLEY: Design and Computational Evaluation of a Commanded Electromagnetic CubeSat Deployment Mechanism**

Adityavardhan Mishra and Pratham Chawla · Mechanical Engineering, Symbiosis Institute of Technology, Pune · 27 October 2026

This edition presents the completed Gen5 ACR1 computational design study with updated CAD-derived illustrations and a matched-load ANSYS/CalculiX chassis comparison. The defined operating cases remain 1, 2 and 3 m/s, using twelve 4 kg 3U payload surrogates and the selected guided lead-screw/captive-pallet feeder.

| Artifact | File |
|---|---|
| Blackbook report · 57 pages | [Report PDF](VOLLEY_ED2_Report.pdf) |
| Presentation · 17 slides, 15 minutes, two speakers | [Presentation PDF](VOLLEY_ED2_Presentation.pdf) |
| Portable report/deck source, figures, inputs and build instructions | [Document source archive](VOLLEY_ED2_Document_Sources.zip) |
| Native static input decks, result tables and independent checks | [ANSYS static source archive](ACR1_ANSYS_Static_Sources.zip) |
| Distributed artifact identities | [Edition manifest](MANIFEST.json) |

## What this edition adds

The report retains populated contents, figure and table lists, native column tables and numbered technical sections. Assembly and feeder views identify the source geometry and display choices. The presentation includes a readable positive-custody sequence and the same-host mission boundary.

Section 7.2.1 compares the same bare chassis, opposed 3010.480631 N loading and declared 3-2-1 restraints. The primary ANSYS peak displacement is 0.286391914 mm against 0.285983350 mm in CalculiX, a 0.142863% difference. Three ANSYS meshes show sensitivity; native-result-derived plots are identified as such. This comparison does not establish full-assembly qualification or a formal discretization error bound. The finest-mesh substitution leaves a positive 0.263067 mm conditional clearance allocation under the stated budget.

## Reproduce and inspect

Extract the document source archive and follow its README. It contains the local numerical inputs, genuine figure assets, an asset materializer, the report/presentation builders and Python dependencies. The static archive has its own `check_capture.py`, native decks, original exported numerical samples, geometry/source identities and plot generator. The unchanged engineering core, all eight CAD/STEP states, and the other solver supplements remain locally available in [the engineering capture](../../current/README.md).

The evaluated hardware is a computational design. No physical test or flight qualification is represented by the solver comparison. Gen6 scaling and higher-speed configurations remain future research and do not change this edition's operating cases.

## Edition history

ED2 is a separately versioned academic edition. [ED1 report and manuscript](../../current/academic/README.md) and [ED1 presentation](../../current/presentation/README.md) retain their original published bytes. The original 24 October issue is preserved in the [dated archive](../../archive/2026-10-24-acr1-original/README.md). This version label records document identity; it does not certify institutional approval or a similarity-test outcome.
