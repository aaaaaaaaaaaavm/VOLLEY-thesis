# VOLLEY — Commanded CubeSat Deployment

## Design and computational evaluation

**Adityavardhan Mishra and Pratham Chawla**  
Mechanical Engineering · Symbiosis Institute of Technology, Pune  
Guide: Vikas Gulia

The presentation follows the complete evaluated deployment cycle: retained storage, guided feed, pallet docking, commanded departure, active carrier arrest and return. Finite electromagnetic calculations, a source-coupled operating study, CAD and structural checks, thermal budgets and a matched mission comparison support the engineering discussion. The closing section connects this reference to prototype development and separately identified research configurations.

| Material | File |
|:--|:--|
| Presentation PDF | [31 slides: 19 core and 12 technical appendix slides](VOLLEY_Presentation.pdf) |
| Editable PowerPoint | [PPTX with native text, shapes and two embedded mechanism clips](VOLLEY_Presentation.pptx) |
| Offline browser edition | [Download this directory and open the HTML](VOLLEY_Presentation.html) |
| Content and source references | [Slide data](SLIDES.json) |
| Portable renderer | [Build script](render_deck.py) |
| Artifact identities | [Manifest](MANIFEST.json) |

The 19-slide core route is planned for 15 minutes. The technical appendix supplies additional mass boundaries, feeder selection, custody, force comparisons, source topology, energy accounting, structural interpretation, mission mechanics, higher-speed research, cislunar architecture and references.

## Read the engineering record

- [Final blackbook report](../final-2026-10/VOLLEY_Blackbook.pdf)
- [Standalone engineering and reproduction guide](../../current/README.md)
- [CAD/STEP assembly states](../../current/cad/release/)
- [Finite motor calculation](../../current/analysis/FINITE_MOTOR.json)
- [Coupled shot cases](../../current/analysis/COUPLED_SHOT.json)
- [Numerical timestep review](../../current/verification/COUPLED_SHOT_REVIEW.json)
- [Mission inputs and results](../../current/mission/)

The evaluated command cases remain **1–3 m/s**. Approximately 10 m/s launcher computations use a separate Labs configuration. Kilometre-per-second and cislunar objectives belong to the staged research programme; departure scenarios do not establish lunar capture or flight capability. The source-linked plots describe the stated computational models. CAD-derived animations explain operating sequence with edited display timing.

## Rebuild the presentation

The local content file and derivative assets are sufficient to rebuild the document layouts. Python dependencies are `python-pptx`, `reportlab` and `Pillow`.

```bash
python render_deck.py --data SLIDES.json
```

The browser edition uses local assets and no external font or script service. The PDF preserves selectable text and provides the static visual equivalent of the animated segments. Original scientific source figures remain in the engineering record; resized derivatives serve presentation layout.

Earlier report and presentation editions retain their published identities in the [edition archive](../ED3/README.md). This presentation is a separate document issue and does not replace those captured files.
