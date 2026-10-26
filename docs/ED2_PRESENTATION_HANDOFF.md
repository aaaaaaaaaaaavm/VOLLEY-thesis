# Academic edition ED2 — presentation handoff

The presentation explains the completed Gen5 ACR1 computational study in **17 slides and 15 planned minutes**, with **450 seconds per student** and a separate five-minute question period.

## Collect the exact edition

- [ED2 presentation PDF](../editions/ED2/VOLLEY_ED2_Presentation.pdf) — the ready-to-open slide fallback.
- [ED2 speaking notes](ED2_SPEAKER_NOTES.md) — the source-linked script and handoff for all 17 slides.
- [ED2 report PDF](../editions/ED2/VOLLEY_ED2_Report.pdf) — 57 pages, including the matched-load ANSYS/CalculiX static comparison.
- [Portable document sources](../editions/ED2/VOLLEY_ED2_Document_Sources.zip) — editable presentation/report builders, local assets and dependency instructions.
- [Edition identities](../editions/ED2/MANIFEST.json) — exact hashes and sizes for the published downloads.

The report PDF SHA-256 is `7a183d32d3de630391a18153076ed9e6b2a8773213381a95e5f185a3885b78fd`. The presentation PDF SHA-256 is `6e866c49e80e72ff2f034c10e17e22475d7c276726919b30ff8975940189c347`. The source ZIP SHA-256 is `320675134ea608b5148341a7a330eb6a23269c76cb9648288d9170a6cb66a450`.

## Prepare an editable deck

Extract the source ZIP and follow its README to install the pinned Python packages before disconnecting. From the extracted directory:

```sh
python3 materialize_assets.py
python3 current/presentation/build_presentation.py
```

Use the Python interpreter with the installed requirements. The builder creates `current/presentation/VOLLEY_BTech_Presentation.pptx`, `SPEAKER_NOTES.md` and `SPEAKER_NOTES.json` from the included figures and captured inputs. All 36 original asset paths restore from 22 hash-verified unique assets. The source archive's `BUILD_REFERENCE.json` pins the distributed editable-deck identity; rebuilt package metadata can vary.

The ED2 deck embeds its raster images and has no external file/media relationship. Its 17-slide route does not require a video player or an internet connection. Check font substitution and slide layout in the presentation application on the actual laptop; retain the PDF fallback alongside the editable deck.

## Speaking route and source boundary

Adityavardhan Mishra presents slides 1–8; Pratham Chawla presents slides 9–17. These are speaking allocations, without an invented allocation of individual research contributions. The notes retain 450 seconds per speaker.

The principal computational range is 1–3 m/s. Slide 13 adds the matched-load bare-chassis numerical comparison, including the three-mesh sensitivity boundary. Slide 14 retains architecture-specific device mass and the adverse ideal-pretrim comparison. The [nine-page paper](https://github.com/aaaaaaaaaaaavm/VOLLEY-paper/blob/main/current/academic/paper/paper.pdf) remains the separately identified ED1 manuscript.

The earlier [ED1 speaker notes](../current/presentation/SPEAKER_NOTES.md) accompany the original preserved deck. Use the ED2 notes linked above with the ED2 slide PDF.

## Optional film and target-device check

The separate [complete storage-to-orbit film](https://aaaaaaaaaaaavm.github.io/VOLLEY/delivery-film.html) has an [MP4 download](https://raw.githubusercontent.com/aaaaaaaaaaaavm/VOLLEY/main/docs/films/delivery-journey/film.mp4), [captions](https://raw.githubusercontent.com/aaaaaaaaaaaavm/VOLLEY/main/docs/films/delivery-journey/captions.vtt) and [transcript](https://github.com/aaaaaaaaaaaavm/VOLLEY/blob/main/docs/films/delivery-journey/TRANSCRIPT.md). If using that film, save its media locally and test playback before the event; it is supplementary to the 15-minute deck.

Keep the exact report, presentation, notes and optional media together on the laptop and backup storage. Perform the actual timed 15-minute run, five-minute question period and projector check. Those observations, institutional approval/signatures and the scheduled 30 October evening IST cutoff retain their actual dates and outcomes.
