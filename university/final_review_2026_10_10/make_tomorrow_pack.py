"""Build the offline review pack from the checked repository artifacts."""

from __future__ import annotations

import hashlib
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
OUTPUT = HERE / "TOMORROW_PRESENTATION_PACK.zip"

FILES = {
    "START_HERE/READ_THIS_FIRST.pdf": HERE / "READ_THIS_FIRST.pdf",
    "START_HERE/TOMORROW_RUN_SHEET.pdf": HERE / "TOMORROW_RUN_SHEET.pdf",
    "START_HERE/PANEL_HANDOUT.pdf": HERE / "PANEL_HANDOUT.pdf",
    "START_HERE/README.md": HERE / "README.md",
    "PRESENTATION/VOLLEY_Final_Review_2026-10-10.pdf": HERE / "VOLLEY_Final_Review_2026-10-10.pdf",
    "PRESENTATION/VOLLEY_Final_Review_2026-10-10.pptx": HERE / "VOLLEY_Final_Review_2026-10-10.pptx",
    "PRESENTATION/PRESENTER_REFERENCE.pdf": HERE / "PRESENTER_REFERENCE.pdf",
    "EVIDENCE/PANEL_HANDBOOK.pdf": HERE / "PANEL_HANDBOOK.pdf",
    "EVIDENCE/CLAIM_EVIDENCE_MAP.md": HERE / "CLAIM_EVIDENCE_MAP.md",
    "EVIDENCE/GEN5_FINAL_YEAR_REPORT.pdf": REPO / "university/GEN5_FINAL_YEAR_REPORT.pdf",
    "EVIDENCE/GEN5_COMPUTATIONAL_REVIEW.pdf": REPO / "reports/GEN5_COMPUTATIONAL_REVIEW.pdf",
    "EVIDENCE/GEN5_CAD_REVIEW.pdf": REPO / "cad/GEN5_CAD_REVIEW.pdf",
    "EVIDENCE/P115_rated_orbit_cartesian.md": REPO / "validation/P115_rated_orbit_cartesian.md",
    "EVIDENCE/P116_gen5_assembly_packaging.md": REPO / "validation/P116_gen5_assembly_packaging.md",
    "EVIDENCE/P117_rated_energy_mass_audit.md": REPO / "validation/P117_rated_energy_mass_audit.md",
    "EVIDENCE/P118_gen5_finite_force_map.md": REPO / "validation/P118_gen5_finite_force_map.md",
    "EVIDENCE/P119_gen5_finite_force_fem2d.md": REPO / "validation/P119_gen5_finite_force_fem2d.md",
    "EVIDENCE/P120_gen5_finite_coupled_shot.md": REPO / "validation/P120_gen5_finite_coupled_shot.md",
    "EVIDENCE/MATCHED_MISSION_REFERENCE.md": REPO / "docs/MATCHED_MISSION_REFERENCE.md",
    "RESULTS/gen5_finite_force_map.json": REPO / "analysis/results/gen5_finite_force_map.json",
    "RESULTS/gen5_finite_force_fem2d.json": REPO / "analysis/results/gen5_finite_force_fem2d.json",
    "RESULTS/gen5_finite_coupled_shot.json": REPO / "analysis/results/gen5_finite_coupled_shot.json",
    "RESULTS/matched_mission_reference.json": REPO / "analysis/results/matched_mission_reference.json",
    "CAD/Gen5_Review.FCStd": REPO / "cad/native/Gen5_Review.FCStd",
    "CAD/Feeder_Candidate_R1.FCStd": REPO / "cad/native/Feeder_Candidate_R1.FCStd",
    "CAD/VOLLEY_Review_Assembly_FreeCAD_Gen5.step": REPO / "cad/step/gen5/VOLLEY_Review_Assembly_FreeCAD_Gen5.step",
    "CAD/VOLLEY_Feeder_Assembly_FreeCAD_R1.step": REPO / "cad/step/feeder_candidate_r1/VOLLEY_Feeder_Assembly_FreeCAD_R1.step",
}


def main() -> None:
    missing = [str(path) for path in FILES.values() if not path.is_file()]
    if missing:
        raise SystemExit("Missing pack inputs:\n" + "\n".join(missing))

    lines = []
    with ZipFile(OUTPUT, "w", compression=ZIP_DEFLATED, compresslevel=6) as archive:
        for name, source in FILES.items():
            data = source.read_bytes()
            archive.writestr(name, data)
            lines.append(f"{hashlib.sha256(data).hexdigest()}  {name}")
        archive.writestr("SHA256SUMS.txt", "\n".join(lines) + "\n")

    with ZipFile(OUTPUT) as archive:
        if archive.testzip() is not None:
            raise SystemExit("ZIP integrity check failed")
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size:,} bytes, {len(FILES)} files)")
    print("SHA-256:", hashlib.sha256(OUTPUT.read_bytes()).hexdigest())


if __name__ == "__main__":
    main()
