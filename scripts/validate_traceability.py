#!/usr/bin/env python3
"""Validate a structured traceability ledger with Python's standard library."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "references/schemas/traceability.schema.json").read_text(encoding="utf-8"))
EDGE_PROPERTIES = SCHEMA["properties"]["edges"]["items"]["properties"]
ARTIFACT_TYPES = set(SCHEMA["properties"]["artifacts"]["items"]["properties"]["type"]["enum"])
RELATIONSHIPS = set(EDGE_PROPERTIES["relationship"]["enum"])
EDGE_STATUSES = set(EDGE_PROPERTIES["status"]["enum"])
RELATION_ENDPOINTS = {
    "contains": ({"CAP"}, {"CAP", "REQ", "RULE", "NFR"}),
    "accepted_by": ({"REQ"}, {"AC"}),
    "verified_by": ({"AC", "RULE", "NFR", "BUG", "TECH", "SEC", "OPS"}, {"TEST"}),
    "constrained_by": ({"REQ", "RULE", "NFR", "AC", "TASK", "CODE"}, {"PDR", "ADR", "CONTRACT", "DESIGN"}),
    "planned_by": ({"REQ", "RULE", "NFR", "AC", "BUG", "TECH", "SEC", "OPS"}, {"TASK"}),
    "implemented_by": ({"TASK", "REQ", "RULE", "NFR"}, {"CODE"}),
    "delivered_by": ({"TASK", "CODE", "TEST", "PR", "BUILD"}, {"PR", "BUILD", "RELEASE"}),
    "observed_by": ({"REQ", "RULE", "NFR", "AC"}, {"OBS"}),
}


def fail(message: str) -> None:
    raise ValueError(message)


def require_fields(item: dict, fields: set[str], context: str) -> None:
    missing = sorted(field for field in fields if field not in item)
    if missing:
        fail(f"{context}: missing fields: {', '.join(missing)}")


def reject_extra_fields(item: dict, fields: set[str], context: str) -> None:
    extra = sorted(set(item) - fields)
    if extra:
        fail(f"{context}: unexpected fields: {', '.join(extra)}")


def require_nonempty_strings(item: dict, fields: set[str], context: str) -> None:
    empty = sorted(field for field in fields if not isinstance(item.get(field), str) or not item[field].strip())
    if empty:
        fail(f"{context}: fields must be non-empty strings: {', '.join(empty)}")


def validate(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    root_fields = {"schema_version", "product", "artifacts", "edges", "exceptions"}
    if not isinstance(data, dict):
        fail("ledger: root must be an object")
    require_fields(data, root_fields, "ledger")
    reject_extra_fields(data, root_fields, "ledger")
    if data["schema_version"] != 1:
        fail("ledger: schema_version must be 1")
    if not isinstance(data["product"], str) or not data["product"].strip():
        fail("ledger: product must be a non-empty string")
    if not all(isinstance(data[field], list) for field in ("artifacts", "edges", "exceptions")):
        fail("ledger: artifacts, edges, and exceptions must be arrays")

    artifacts: dict[str, str] = {}
    artifact_required = {"id", "type", "title", "version_line", "status", "owner"}
    artifact_allowed = artifact_required | {"location", "supersedes"}
    for index, artifact in enumerate(data["artifacts"]):
        context = f"artifacts[{index}]"
        if not isinstance(artifact, dict):
            fail(f"{context}: must be an object")
        require_fields(artifact, artifact_required, context)
        reject_extra_fields(artifact, artifact_allowed, context)
        require_nonempty_strings(artifact, artifact_required, context)
        artifact_id = artifact["id"]
        artifact_type = artifact["type"]
        if artifact_id in artifacts:
            fail(f"artifacts[{index}]: duplicate id {artifact_id}")
        if artifact_type not in ARTIFACT_TYPES:
            fail(f"artifacts[{index}]: unknown type {artifact_type}")
        artifacts[artifact_id] = artifact_type

    for index, artifact in enumerate(data["artifacts"]):
        supersedes = artifact.get("supersedes", [])
        if not isinstance(supersedes, list) or not all(isinstance(item, str) for item in supersedes):
            fail(f"artifacts[{index}]: supersedes must be an array of unique IDs")
        if len(supersedes) != len(set(supersedes)):
            fail(f"artifacts[{index}]: supersedes must be an array of unique IDs")
        for prior in supersedes:
            if prior not in artifacts or artifacts[prior] != artifact["type"]:
                fail(f"artifacts[{index}]: supersedes must reference an artifact of the same type")

    edge_fields = {
        "source", "source_type", "relationship", "target", "target_type",
        "version_line", "status", "evidence", "owner", "last_verified",
    }
    seen_edges: set[tuple[str, str, str]] = set()
    for index, edge in enumerate(data["edges"]):
        context = f"edges[{index}]"
        if not isinstance(edge, dict):
            fail(f"{context}: must be an object")
        require_fields(edge, edge_fields, context)
        reject_extra_fields(edge, edge_fields, context)
        require_nonempty_strings(edge, edge_fields, context)
        source, target = edge["source"], edge["target"]
        if source not in artifacts or target not in artifacts:
            fail(f"edges[{index}]: source and target must exist in artifacts")
        if edge["source_type"] != artifacts[source] or edge["target_type"] != artifacts[target]:
            fail(f"edges[{index}]: endpoint type does not match artifact index")
        if edge["relationship"] not in RELATIONSHIPS:
            fail(f"edges[{index}]: unknown relationship {edge['relationship']}")
        allowed = RELATION_ENDPOINTS.get(edge["relationship"])
        if allowed and (edge["source_type"] not in allowed[0] or edge["target_type"] not in allowed[1]):
            fail(f"edges[{index}]: invalid endpoint types for {edge['relationship']}")
        if edge["relationship"] == "delivered_by":
            pair = (edge["source_type"], edge["target_type"])
            valid_pairs = {
                ("TASK", "PR"), ("CODE", "PR"), ("TEST", "PR"),
                ("PR", "BUILD"), ("BUILD", "RELEASE"),
            }
            if pair not in valid_pairs:
                fail(f"edges[{index}]: delivered_by cannot skip/collapse delivery stages")
        if edge["relationship"] in {"supersedes", "superseded_by"} and edge["source_type"] != edge["target_type"]:
            fail(f"edges[{index}]: replacement edges must connect the same artifact type")
        if edge["status"] not in EDGE_STATUSES:
            fail(f"edges[{index}]: unknown edge status {edge['status']}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", edge["last_verified"]):
            fail(f"edges[{index}]: last_verified must use YYYY-MM-DD")
        key = (source, edge["relationship"], target)
        if key in seen_edges:
            fail(f"edges[{index}]: duplicate edge {key}")
        seen_edges.add(key)

    exception_fields = {
        "artifact_or_edge", "rationale", "risk", "alternative_evidence",
        "approver", "owner", "review_or_expiry", "status",
    }
    for index, exception in enumerate(data["exceptions"]):
        context = f"exceptions[{index}]"
        if not isinstance(exception, dict):
            fail(f"{context}: must be an object")
        require_fields(exception, exception_fields, context)
        reject_extra_fields(exception, exception_fields, context)
        require_nonempty_strings(exception, exception_fields, context)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_traceability.py <ledger.json>", file=sys.stderr)
        return 2
    try:
        validate(Path(sys.argv[1]))
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"INVALID: {error}", file=sys.stderr)
        return 1
    print(f"OK: {sys.argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
