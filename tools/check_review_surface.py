"""Check the public academic route and decisive captured results without a solver stack."""

from __future__ import annotations

import hashlib
import json
import math
import re
from pathlib import Path
from urllib.parse import unquote
from zipfile import ZipFile, is_zipfile


ROOT = Path(__file__).resolve().parents[1]
IS_PAPER = (ROOT / "paper/paper.tex").exists()
CURRENT = (
    ["README.md", "paper/README.md", "paper/BUILD.md", "EVIDENCE_LIMITS.md"]
    if IS_PAPER else
    ["README.md", "ACADEMIC_EVIDENCE.md", "university/GEN5_FINAL_YEAR_REPORT.md",
     "university/final_review_2026_10_10/README.md",
     "university/final_review_2026_10_10/READ_THIS_FIRST.md",
     "university/final_review_2026_10_10/TOMORROW_RUN_SHEET.md",
     "university/final_review_2026_10_10/CLAIM_EVIDENCE_MAP.md"]
)
SOURCE = "paper/paper.tex" if IS_PAPER else "source/paper.tex"
PDF = "paper/VOLLEY_IEEE_Conference.pdf" if IS_PAPER else "source/VOLLEY_IEEE_Conference.pdf"
FIGURES = "paper/figures" if IS_PAPER else "source/figures"
LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)]+)\)|<img\b[^>]*\bsrc=['\"]([^'\"]+)", re.I)
IMAGE = re.compile(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}")


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("FAIL: " + message)


def check_links() -> int:
    count = 0
    for name in CURRENT:
        path = ROOT / name
        require(path.is_file(), f"missing current-facing source {name}")
        fenced = False
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                fenced = not fenced
                continue
            if fenced:
                continue
            for match in LINK.finditer(line):
                raw = next((group for group in match.groups() if group), "")
                target = unquote(raw.strip("<>").split("#", 1)[0])
                if not target or target.startswith(("http:", "https:", "mailto:", "data:", "//")):
                    continue
                resolved = (path.parent / target).resolve()
                require(resolved.is_relative_to(ROOT.resolve()), f"link escapes repo: {name}:{line_number} {target}")
                require(resolved.exists(), f"broken local link: {name}:{line_number} {target}")
                count += 1
    return count


def check_manuscript_figures() -> int:
    source = (ROOT / SOURCE).read_text(encoding="utf-8")
    names = IMAGE.findall(source)
    for name in names:
        require((ROOT / FIGURES / name).is_file(), f"manuscript figure missing: {name}")
    require("historical periodic-force" in source.lower(), "historical shot caveat missing from manuscript")
    require("12.448" in source, "finite-force result missing from manuscript")
    return len(names)


def check_captured_results() -> None:
    finite = json.loads((ROOT / "analysis/results/gen5_finite_force_map.json").read_text())
    mass = json.loads((ROOT / "analysis/results/mass_properties.json").read_text())
    mission = json.loads((ROOT / "analysis/results/matched_mission_reference.json").read_text())
    derived = math.sqrt(2 * finite["ideal_finite_stator_work_J"] / finite["moving_mass_kg"])
    require(abs(derived - finite["ideal_finite_stator_exit_upper_m_s"]) < 0.001,
            "finite work/mass/speed identity changed")
    require(abs(mass["dry_kg"] / 12 - 10.547) < 0.02, "3U mass screen changed")
    require(all(not case["accepted_all_12"] for case in mission["finite_burn_campaign"]),
            "a twelve-shot campaign now closes; review text needs updating")


def check_manifest() -> int:
    manifest = ROOT / "ARTIFACT_MANIFEST.sha256"
    require(manifest.is_file(), "artifact manifest missing")
    count = 0
    for line in manifest.read_text().splitlines():
        if not line.strip():
            continue
        digest, name = line.split("  ", 1)
        path = ROOT / name
        require(path.is_file(), f"manifest artifact missing: {name}")
        require(hashlib.sha256(path.read_bytes()).hexdigest() == digest,
                f"manifest checksum stale: {name}")
        count += 1
    return count


def check_containers() -> None:
    pdf = (ROOT / PDF).read_bytes()
    require(pdf.startswith(b"%PDF-") and b"%%EOF" in pdf[-2048:], "paper PDF incomplete")
    if not IS_PAPER:
        package = ROOT / "university/final_review_2026_10_10/TOMORROW_PRESENTATION_PACK.zip"
        require(is_zipfile(package), "review ZIP missing or invalid")
        with ZipFile(package) as archive:
            require(archive.testzip() is None, "review ZIP contains a damaged member")


def main() -> None:
    local_links = check_links()
    figures = check_manuscript_figures()
    check_captured_results()
    artifacts = check_manifest()
    check_containers()
    print(f"PASS: {local_links} current local links, {figures} manuscript figures, "
          f"decisive identities, {artifacts} artifact hashes, PDF/ZIP integrity")


if __name__ == "__main__":
    main()
