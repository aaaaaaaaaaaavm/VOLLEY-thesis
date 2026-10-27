# Academic edition ED2 — presentation sources

ED2 contains a 57-page report and 17-slide presentation of Gen5 ACR1. The current academic report and presentation are distributed separately as [ED3](../editions/ED3/README.md).

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
