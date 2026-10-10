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
    "EVIDENCE/P121_gen5_finite_force_surface3d.md": REPO / "validation/P121_gen5_finite_force_surface3d.md",
    "EVIDENCE/P122_gen5_finite_force_sensitivity.md": REPO / "validation/P122_gen5_finite_force_sensitivity.md",
    "EVIDENCE/P123_gen5_one_event_mass_screen.md": REPO / "validation/P123_gen5_one_event_mass_screen.md",
    "EVIDENCE/P124_precision_delivery_design_space.md": REPO / "validation/P124_precision_delivery_design_space.md",
    "EVIDENCE/P125_gen5_voltage_limited_screen.md": REPO / "validation/P125_gen5_voltage_limited_screen.md",
    "EVIDENCE/P126_feeder_r1_tolerance_screen.md": REPO / "cad/FEEDER_R1_TOLERANCE_SCREEN.md",
    "EVIDENCE/P127_gen5_release_arrest_bounds.md": REPO / "validation/P127_gen5_release_arrest_bounds.md",
    "RESULTS/gen5_voltage_limited_screen.json": REPO / "analysis/results/gen5_voltage_limited_screen.json",
    "RESULTS/FEEDER_R1_TOLERANCE_SCREEN.json": REPO / "cad/FEEDER_R1_TOLERANCE_SCREEN.json",
    "RESULTS/gen5_release_arrest_bounds.json": REPO / "analysis/results/gen5_release_arrest_bounds.json",
    "EVIDENCE/GEN6_PROTOTYPE_TO_FLIGHT_ROADMAP.md": REPO / "docs/GEN6_PROTOTYPE_TO_FLIGHT_ROADMAP.md",
    "EVIDENCE/MATCHED_MISSION_REFERENCE.md": REPO / "docs/MATCHED_MISSION_REFERENCE.md",
    "RESULTS/gen5_finite_force_map.json": REPO / "analysis/results/gen5_finite_force_map.json",
    "RESULTS/gen5_finite_force_fem2d.json": REPO / "analysis/results/gen5_finite_force_fem2d.json",
    "RESULTS/gen5_finite_coupled_shot.json": REPO / "analysis/results/gen5_finite_coupled_shot.json",
    "RESULTS/gen5_finite_force_surface3d.json": REPO / "analysis/results/gen5_finite_force_surface3d.json",
    "RESULTS/gen5_finite_force_sensitivity.json": REPO / "analysis/results/gen5_finite_force_sensitivity.json",
    "RESULTS/matched_mission_reference.json": REPO / "analysis/results/matched_mission_reference.json",
    "RESULTS/gen5_one_event_mass_screen.json": REPO / "analysis/results/gen5_one_event_mass_screen.json",
    "RESULTS/precision_delivery_design_space.json": REPO / "analysis/results/precision_delivery_design_space.json",
    "CAD/Gen5_Review.FCStd": REPO / "cad/native/Gen5_Review.FCStd",
    "CAD/Feeder_Candidate_R1.FCStd": REPO / "cad/native/Feeder_Candidate_R1.FCStd",
    "CAD/VOLLEY_Review_Assembly_FreeCAD_Gen5.step": REPO / "cad/step/gen5/VOLLEY_Review_Assembly_FreeCAD_Gen5.step",
    "CAD/VOLLEY_Feeder_Assembly_FreeCAD_R1.step": REPO / "cad/step/feeder_candidate_r1/VOLLEY_Feeder_Assembly_FreeCAD_R1.step",
    "CAD_VIEWS/gen5_reference_open.jpg": REPO / "cad/renders/step_review/gen5_reference_open.jpg",
    "CAD_VIEWS/gen5_reference_closed.jpg": REPO / "cad/renders/step_review/gen5_reference_closed.jpg",
    "CAD_VIEWS/gen5_fit_plan.jpg": REPO / "cad/renders/step_review/gen5_fit_plan.jpg",
    "CAD_VIEWS/gen5_drive_detail.jpg": REPO / "cad/renders/step_review/gen5_drive_detail.jpg",
    "CAD_VIEWS/r1_candidate_open.jpg": REPO / "cad/renders/step_review/r1_candidate_open.jpg",
    "CAD_VIEWS/r1_candidate_plan.jpg": REPO / "cad/renders/step_review/r1_candidate_plan.jpg",
    "EVIDENCE/STEP_VIEW_PROVENANCE.json": REPO / "cad/renders/step_review/PROVENANCE.json",
    "VISUALS/gen5_operations_hero.png": REPO / "cad/renders/sequence/gen5_operations_hero.png",
    "VISUALS/precision_delivery_design_space.png": REPO / "figures/precision_delivery_design_space.png",
    "VISUALS/gen5_intended_sequence.mp4": REPO / "cad/renders/sequence/gen5_intended_sequence.mp4",
    "VISUALS/README.md": REPO / "cad/renders/sequence/README.md",
    "VISUALS/PROVENANCE.json": REPO / "cad/renders/sequence/PROVENANCE.json",
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
