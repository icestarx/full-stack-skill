#!/usr/bin/env python3
"""Validate the eval suite and optionally score captured agent responses."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "evals" / "cases.json"
MODES = {
    "new_product_or_major_version", "feature_change", "bug_fix", "maintenance", "incident"
}
RISKS = {"low", "medium", "high"}
TRACKS = {"product", "engineering", "verification", "delivery_learning"}
CASE_FIELDS = {
    "id", "prompt", "expected_mode", "risk", "applicable_tracks",
    "required_outcomes", "forbidden_actions",
}


def require_string_list(value: object, context: str, *, allow_empty: bool = False) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
        raise ValueError(f"{context} must be an array of non-empty strings")
    if not allow_empty and not value:
        raise ValueError(f"{context} cannot be empty")
    if len(value) != len(set(value)):
        raise ValueError(f"{context} must contain unique values")
    return value


def load_cases() -> list[dict]:
    data = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    if data.get("schema_version") != 1 or not isinstance(data.get("cases"), list):
        raise ValueError("eval suite must have schema_version 1 and a cases array")
    cases = data["cases"]
    ids: set[str] = set()
    covered_modes: set[str] = set()
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            raise ValueError(f"case[{index}] must be an object")
        missing = sorted(CASE_FIELDS - case.keys())
        if missing:
            raise ValueError(f"case[{index}] missing: {', '.join(missing)}")
        extra = sorted(case.keys() - CASE_FIELDS)
        if extra:
            raise ValueError(f"case[{index}] has unexpected fields: {', '.join(extra)}")
        if not isinstance(case["id"], str) or not case["id"]:
            raise ValueError(f"case[{index}] id must be a non-empty string")
        if not isinstance(case["prompt"], str) or not case["prompt"].strip():
            raise ValueError(f"{case['id']}: prompt must be a non-empty string")
        if case["id"] in ids:
            raise ValueError(f"duplicate case id: {case['id']}")
        ids.add(case["id"])
        if case["expected_mode"] not in MODES:
            raise ValueError(f"{case['id']}: invalid mode")
        if case["risk"] not in RISKS:
            raise ValueError(f"{case['id']}: invalid risk")
        applicable_tracks = require_string_list(case["applicable_tracks"], f"{case['id']}.applicable_tracks")
        if not set(applicable_tracks).issubset(TRACKS):
            raise ValueError(f"{case['id']}: invalid track")
        require_string_list(case["required_outcomes"], f"{case['id']}.required_outcomes")
        require_string_list(case["forbidden_actions"], f"{case['id']}.forbidden_actions")
        covered_modes.add(case["expected_mode"])
    if covered_modes != MODES:
        raise ValueError(f"missing mode coverage: {sorted(MODES - covered_modes)}")
    return cases


def score(cases: list[dict], response_path: Path) -> int:
    responses = json.loads(response_path.read_text(encoding="utf-8"))
    if not isinstance(responses, list):
        raise ValueError("responses must be a JSON array")
    if not all(isinstance(item, dict) for item in responses):
        raise ValueError("every response must be an object")
    response_ids = [item.get("case_id") for item in responses]
    if len(response_ids) != len(set(response_ids)):
        raise ValueError("response case_id values must be unique")
    response_map = {item.get("case_id"): item for item in responses}
    failures = 0
    for case in cases:
        result = response_map.get(case["id"])
        reasons: list[str] = []
        if result is None:
            reasons.append("missing response")
        else:
            if result.get("mode") != case["expected_mode"]:
                reasons.append("mode mismatch")
            if result.get("risk") != case["risk"]:
                reasons.append("risk mismatch")
            outcomes = set(require_string_list(result.get("outcomes"), f"{case['id']}.outcomes", allow_empty=True))
            missing = set(case["required_outcomes"]) - outcomes
            if missing:
                reasons.append(f"missing outcomes {sorted(missing)}")
            actions = set(require_string_list(result.get("actions"), f"{case['id']}.actions", allow_empty=True))
            forbidden = set(case["forbidden_actions"]) & actions
            if forbidden:
                reasons.append(f"forbidden actions {sorted(forbidden)}")
            evidence = require_string_list(result.get("evidence"), f"{case['id']}.evidence", allow_empty=True)
            if not evidence:
                reasons.append("no evidence")
        if reasons:
            failures += 1
            print(f"FAIL {case['id']}: {'; '.join(reasons)}")
        else:
            print(f"PASS {case['id']}")
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--responses", type=Path)
    args = parser.parse_args()
    try:
        cases = load_cases()
        if args.responses:
            return score(cases, args.responses)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"INVALID: {error}", file=sys.stderr)
        return 1
    print(f"OK: {len(cases)} eval cases cover all five operating modes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
