#!/usr/bin/env python3
"""Deterministic structural validation for this Skill repository."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "SKILL.md", "README.md", "AGENTS.md", "DEPENDENCIES.md", "setup",
    "agents/openai.yaml", "references/platform-adapters.md",
    "references/provider-registry.md",
    "references/four-track-model.md", "references/operating-modes.md",
    "references/process-steps.md", "references/requirements-workflow.md",
    "references/document-organization.md", "references/traceability.md",
    "references/tech-selection.md", "references/capability-domains.md",
    "references/tracks/product.md", "references/tracks/engineering.md",
    "references/tracks/verification.md", "references/tracks/delivery-learning.md",
    "references/schemas/traceability.schema.json",
    "references/templates/requirements.md", "references/templates/ui-design.md",
    "references/templates/frontend-design.md", "references/templates/backend-design.md",
    "references/templates/development-plan.md", "references/templates/database-design.md",
    "references/templates/api-design.md", "references/templates/staging-deploy.md",
    "references/templates/testing.md", "references/templates/production-deploy.md",
    "references/templates/change-work-item.md", "references/templates/verification-evidence.md",
    "references/templates/version-manifest.md", "references/templates/release-manifest.md",
    "references/templates/traceability-ledger.md", "references/templates/traceability-ledger.json",
    "evals/cases.json",
    "evals/rubric.md", "scripts/validate_skill.py",
    "scripts/validate_traceability.py", "scripts/run_evals.py",
}


def validate_frontmatter(errors: list[str]) -> None:
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.DOTALL)
    if not match:
        errors.append("SKILL.md: missing or malformed frontmatter")
        return
    frontmatter = match.group(1)
    keys = re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, re.MULTILINE)
    allowed = {"name", "description", "license", "allowed-tools", "metadata"}
    unexpected = set(keys) - allowed
    if unexpected:
        errors.append(f"SKILL.md: unexpected frontmatter keys {sorted(unexpected)}")
    if len(keys) != len(set(keys)):
        errors.append("SKILL.md: duplicate frontmatter key")
    name_match = re.search(r"^name:\s*([^\n]+)$", frontmatter, re.MULTILINE)
    name = name_match.group(1).strip() if name_match else ""
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("SKILL.md: invalid skill name")
    description_match = re.search(r"^description:\s*(.*?)(?=^[A-Za-z0-9_-]+:|\Z)", frontmatter, re.MULTILINE | re.DOTALL)
    if not description_match:
        errors.append("SKILL.md: missing description")
    else:
        raw_description = description_match.group(1).strip()
        if raw_description.startswith(">"):
            raw_description = raw_description[1:].strip()
        description = " ".join(line.strip() for line in raw_description.splitlines()).strip()
        if not description or len(description) > 1024 or "<" in description or ">" in description:
            errors.append("SKILL.md: invalid description")
    if re.search(r"^ {0,3}\[TODO:[^\n]*\]\s*$", text[match.end():], re.MULTILINE):
        errors.append("SKILL.md: unfinished TODO placeholder")


def validate_metadata(errors: list[str]) -> None:
    text = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    short = re.search(r'^\s*short_description:\s*"([^"]*)"\s*$', text, re.MULTILINE)
    prompt = re.search(r'^\s*default_prompt:\s*"([^"]*)"\s*$', text, re.MULTILINE)
    if not short or not 25 <= len(short.group(1)) <= 64:
        errors.append("agents/openai.yaml: short_description must be 25-64 characters")
    if not prompt or "$full-stack-skill" not in prompt.group(1):
        errors.append("agents/openai.yaml: default_prompt must mention $full-stack-skill")


def validate_fences(errors: list[str]) -> None:
    fence_re = re.compile(r"^[ \t]*(?:(?:[-+*]|\d+[.)])[ \t]+)?(`{3,}|~{3,})(.*)$")
    for path in sorted(ROOT.rglob("*.md")):
        marker = None
        length = 0
        opened = 0
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            match = fence_re.match(line)
            if not match:
                continue
            token, suffix = match.groups()
            if marker is None:
                marker, length, opened = token[0], len(token), line_number
            elif token[0] == marker and len(token) >= length and not suffix.strip():
                marker, length, opened = None, 0, 0
        if marker is not None:
            errors.append(f"{path.relative_to(ROOT)}:{opened}: unclosed Markdown fence")


def validate_references(errors: list[str]) -> None:
    pattern = re.compile(
        r"`((?:references|scripts|evals)/[A-Za-z0-9_.\[\]/-]+(?:\.md|\.json|\.py)"
        r"|(?:\.\./|tracks/|templates/|schemas/)[A-Za-z0-9_.\[\]/-]+(?:\.md|\.json|\.py))`"
    )
    sources = [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "AGENTS.md", *ROOT.glob("references/**/*.md")]
    for source in sources:
        lines: list[str] = []
        marker = None
        length = 0
        for line in source.read_text(encoding="utf-8").splitlines():
            fence = re.match(r"^[ \t]*(`{3,}|~{3,})(.*)$", line)
            if fence:
                token, suffix = fence.groups()
                if marker is None:
                    marker, length = token[0], len(token)
                elif token[0] == marker and len(token) >= length and not suffix.strip():
                    marker, length = None, 0
                continue
            if marker is None:
                lines.append(line)
        text = "\n".join(lines)
        for reference in pattern.findall(text):
            if "[" in reference or "]" in reference:
                continue
            target = ROOT / reference if reference.startswith(("references/", "scripts/", "evals/")) else source.parent / reference
            if not target.resolve().exists():
                errors.append(f"{source.relative_to(ROOT)}: missing reference {reference}")
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
            link = link.strip("<>").split("#", 1)[0]
            if not link or re.match(r"^[a-z][a-z0-9+.-]*:", link):
                continue
            target = source.parent / link
            if not target.resolve().exists():
                errors.append(f"{source.relative_to(ROOT)}: missing Markdown link {link}")


def validate_workflow_docs(errors: list[str]) -> None:
    workflow = (ROOT / "references/process-steps.md").read_text(encoding="utf-8")
    mapping = (ROOT / "references/skills-mapping.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for number in range(1, 16):
        activity = f"A{number}"
        if not re.search(rf"^## {activity} — ", workflow, re.MULTILINE):
            errors.append(f"references/process-steps.md: missing {activity} step heading")
        if not re.search(rf"^\| {activity} ", mapping, re.MULTILINE):
            errors.append(f"references/skills-mapping.md: missing {activity} capability row")
        if not re.search(rf"^\| \*\*{activity}\*\* ", readme, re.MULTILINE):
            errors.append(f"README.md: missing {activity} workflow row")
    if len(re.findall(r"^\*\*Capabilities\*\*:", workflow, re.MULTILINE)) != 15:
        errors.append("references/process-steps.md: every A1-A15 step must define capabilities")
    if len(re.findall(r"^\*\*Complete when\*\*:", workflow, re.MULTILINE)) != 15:
        errors.append("references/process-steps.md: every A1-A15 step must define completion criteria")


def validate_capability_contracts(errors: list[str]) -> None:
    paths = [
        ROOT / "SKILL.md",
        ROOT / "README.md",
        ROOT / "references/platform-adapters.md",
        ROOT / "references/skills-mapping.md",
        ROOT / "references/process-steps.md",
    ]
    texts = {path: path.read_text(encoding="utf-8") for path in paths}
    required = {
        "verification.completion",
        "delivery.environment",
        "delivery.change-review",
        "delivery.deploy",
        "delivery.recover",
    }
    for capability in sorted(required):
        for path, text in texts.items():
            if capability not in text:
                errors.append(f"{path.relative_to(ROOT)}: missing capability {capability}")
    for path, text in texts.items():
        if "delivery.release" in text:
            errors.append(f"{path.relative_to(ROOT)}: obsolete capability delivery.release")

    registry = (ROOT / "references/provider-registry.md").read_text(encoding="utf-8")
    for provider in ("Superpowers", "UI UX Pro Max", "Ponytail"):
        if f"## {provider}" not in registry:
            errors.append(f"references/provider-registry.md: missing {provider} profile")
    for uncurated in ("gstack", "OpenSpec"):
        if uncurated in registry:
            errors.append(f"references/provider-registry.md: uncurated provider {uncurated}")


def run_child(command: list[str], label: str, errors: list[str]) -> None:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        errors.append(f"{label}: {detail}")


def main() -> int:
    errors: list[str] = []
    for relative in sorted(REQUIRED):
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    if not errors:
        validate_frontmatter(errors)
        validate_metadata(errors)
        validate_fences(errors)
        validate_references(errors)
        validate_workflow_docs(errors)
        validate_capability_contracts(errors)
        try:
            json.loads((ROOT / "references/schemas/traceability.schema.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            errors.append(f"traceability schema: {error}")
        run_child([sys.executable, "scripts/validate_traceability.py", "references/templates/traceability-ledger.json"], "traceability example", errors)
        run_child([sys.executable, "scripts/run_evals.py"], "eval suite", errors)
    if errors:
        for error in errors:
            print(f"INVALID: {error}")
        return 1
    print("OK: skill structure, metadata, references, Markdown, traceability, and eval suite are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
