# VOLLEY — Engineering thesis

**Design and Computational Evaluation of a Commanded Electromagnetic CubeSat Deployment Mechanism**

**Adityavardhan Mishra and Pratham Chawla**<br>
Mechanical Engineering · Symbiosis Institute of Technology, Pune<br>
Guide: Vikas Gulia · October 2026

The 64-page blackbook is the final report of the computational design study. It presents the selected storage, guided feed, pallet transfer and reusable electromagnetic carrier together with electromagnetic, electrical, structural, thermal and orbital analyses. Its conclusions distinguish the evaluated design from the subsequent prototype and qualification programme.

| Material | File |
|:--|:--|
| Blackbook · 64 pages | [PDF](VOLLEY_Blackbook.pdf) |
| Editable report | [Word document](VOLLEY_Blackbook.docx) |
| Report text, layouts, figures and builders | [Standalone source archive](VOLLEY_Blackbook_Sources.zip) |
| Presentation · 19 core + 12 technical appendix slides | [Approved PDF](../presentation-2026-10/VOLLEY_Presentation.pdf) |
| Editable presentation and animation assets | [Presentation source edition](../presentation-2026-10/README.md) |
| Exact document identities | [Manifest](MANIFEST.json) |

The PDF and Word report retain the approved text, 52 native mathematical expressions, 15 native Word tables and original figure assets. The PDF is the fixed reading copy. The Word document has editable mathematical content and refreshable contents, figure and table indexes; font substitution and field updates can change pagination.

## Reproduce and inspect

Extract the report source archive and follow its README. Its inputs are local, with individual checksums in `SOURCE_MANIFEST.json`; building the report does not require another repository. Numerical methods, captured results and software versions are available in the [standalone engineering record](../../current/README.md). [Native CAD and STEP](../../current/cad/release/), [matched structural solver sources](../ED2/ACR1_ANSYS_Static_Sources.zip), [raw solver supplement](../../current/SUPPLEMENT_ASSETS.json) and [numerical reproduction instructions](../../current/REPRODUCE.md) support the study.

The 31-slide presentation is preserved as a separate document issue with its own source, output and asset identities. Earlier report and presentation editions remain available through the [development archive](../../archive/README.md).

## Development beyond this study

The next stage is an instrumented prototype: component force measurements, feeder and lock sequencing, integrated release, carrier arrest and return. Mixed-size operation, host-specific interfaces and environmental qualification follow those measurements. Higher-speed and cislunar investigations retain separate configurations and requirements; they are development objectives rather than ratings of the evaluated mechanism.
