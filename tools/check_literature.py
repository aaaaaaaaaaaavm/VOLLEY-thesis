#!/usr/bin/env python3
"""Check the ED1 comparison's data, citation and reading-scope consistency.

This checks the distributed evidence record. It does not acquire full texts,
independently review articles, or certify completeness of a literature search.
"""
from pathlib import Path
import csv
import json
import math
import re


def require(ok, message):
    if not ok:
        raise ValueError(message)


def check_literature(root):
    current = Path(root) / "current"
    literature = current / "academic/evidence/literature"
    record = json.loads((literature / "ACR1_SOURCE_COMPARISON.json").read_text())
    sources = {row["id"]: row for row in record["sources"]}
    require(len(sources) == len(record["sources"]), "duplicate source id")
    expected_dois = {
        "Z22": "10.3390/rs14174205",
        "Z25": "10.3390/aerospace12060466",
        "F25": "10.1155/ijae/3000765",
        "E23": "10.1541/ieejias.143.570",
        "V22": "10.1109/TIE.2021.3134060",
    }
    for source_id, doi in expected_dois.items():
        require(sources[source_id]["doi"] == doi, "source DOI identity: " + source_id)
        require(bool(sources[source_id]["locations"]), "missing reading location: " + source_id)
    translation = "10.1002/eej.23450"
    require(sources["E23"]["related_translation_doi"] == translation,
            "end-effect original/translation identity")
    require(sources["E23"]["grade"] == "A_selected_full_text_original",
            "ED1 end-effect selected-passage scope changed")
    require(sources["V22"]["grade"] == "C_primary_metadata_abstract"
            and sources["V22"]["sha256"] is None,
            "ED1 V22 unread-full-text scope changed")

    rows = record["quantitative_comparison"]
    with (literature / "ACR1_QUANTITATIVE_COMPARISON.csv").open(newline="") as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames
        actual = list(reader)
    fields = ["source_id", "quantity", "min", "max", "unit", "condition",
              "evidence", "location", "comparison"]
    require(columns == fields, "comparison CSV schema")
    expected = [{key: "" if row[key] is None else str(row[key]) for key in fields}
                for row in rows]
    require(actual == expected, "comparison CSV differs from JSON (including null/blank values)")
    seen = set()
    for row in rows:
        identity = (row["source_id"], row["quantity"])
        require(identity not in seen, "duplicate comparison quantity: " + str(identity))
        seen.add(identity)
        require(row["source_id"] in sources, "unknown comparison source: " + str(identity))
        require(row["source_id"] != "V22", "numeric result imported from unread V22 full text")
        for key in ("unit", "condition", "evidence", "location", "comparison"):
            require(bool(row[key]), "missing comparison context: " + str(identity))
        for key in ("min", "max"):
            value = row[key]
            require(value is None or (type(value) in (int, float) and math.isfinite(value)),
                    "nonfinite/nonnumeric comparison value: " + str(identity))
        require(row["min"] is None or row["max"] is None or row["min"] <= row["max"],
                "reversed comparison range: " + str(identity))
    derived = next(row for row in rows if row["source_id"] == "F25"
                   and row["quantity"] == "mean_acceleration_at_maxspeed")
    require(math.isclose(derived["min"], 321.56 ** 2 / (2 * 3.9), rel_tol=1e-12)
            and derived["max"] == derived["min"]
            and derived["evidence"] == "derived_kinematic_screen",
            "derived Feng kinematic screen or evidence class")

    documents = [current / "academic/GEN5_FINAL_YEAR_REPORT.md",
                 current / "academic/paper/paper.tex"]
    for path in documents:
        text = path.read_text()
        bibliography = text.split("# Bibliography" if path.suffix == ".md"
                                  else r"\begin{thebibliography}", 1)[-1]
        for source_id in ("Z22", "Z25", "F25", "E23"):
            require(expected_dois[source_id] in bibliography,
                    "missing bibliography DOI: " + source_id + " in " + path.name)
        require(translation in bibliography and "H. Q. Yamaguchi" not in bibliography,
                "end-effect bibliography correction: " + path.name)
    paper = documents[1].read_text()
    cited = {key.strip() for group in re.findall(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}", paper)
             for key in group.split(",")}
    items = re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", paper)
    require(len(set(items)) == len(items), "duplicate manuscript bibliography key")
    require(not cited.difference(items), "unresolved manuscript citation keys: "
            + ", ".join(sorted(cited.difference(items))))
    return {"sources": len(sources), "quantities": len(rows), "citation_keys": len(cited)}


if __name__ == "__main__":
    try:
        result = check_literature(Path(__file__).resolve().parents[1])
    except (ValueError, KeyError, StopIteration) as exc:
        raise SystemExit("FAIL: literature consistency: " + str(exc)) from exc
    print("PASS: literature consistency " + json.dumps(result, sort_keys=True)
          + "; V22 remains metadata/abstract only; external review unchanged")
