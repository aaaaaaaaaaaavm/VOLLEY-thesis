# Earlier report and presentation — document sources

This earlier edition contains a 57-page report and 17-slide presentation. The final submitted documents are the [64-page blackbook](../editions/final-2026-10/README.md) and [31-slide presentation](../editions/presentation-2026-10/README.md). The intermediate [third document edition](../editions/ED3/README.md) remains available in the archive.

## Edition artifacts

- [ED2 report](../editions/ED2/VOLLEY_ED2_Report.pdf)
- [ED2 presentation](../editions/ED2/VOLLEY_ED2_Presentation.pdf)
- [Portable document sources](../editions/ED2/VOLLEY_ED2_Document_Sources.zip)
- [Artifact manifest](../editions/ED2/MANIFEST.json)

## Build

Extract the source archive, install its listed dependencies and run:

```sh
python3 materialize_assets.py
python3 current/presentation/build_presentation.py
```

The builder exports the editable PPTX from included figures and captured inputs. The archive restores 36 original asset paths from 22 hash-verified assets. Its BUILD_REFERENCE.json identifies the distributed output; rebuilt Office metadata may vary with the toolchain.

The scientific reference retains the 1–3 m/s cases. ED2 adds the separately identified matched-load ANSYS/CalculiX bare-chassis comparison. The nine-page manuscript retains its ED1 identity.
