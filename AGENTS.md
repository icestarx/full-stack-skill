# Repository Guidelines

## Project Structure & Module Organization

This repository defines a portable full-stack lifecycle skill. `SKILL.md` is the four-track router; `references/four-track-model.md` defines state/gates, `references/operating-modes.md` defines playbooks, and `references/tracks/` holds conditional detail. A1-A15 remain an index in `references/process-steps.md`, not a waterfall. `references/platform-adapters.md` defines host-neutral capability contracts and Codex/Claude adapters; `agents/openai.yaml` supplies Codex metadata. Templates and schemas live under `references/`; `scripts/` validates structure, traceability, and eval contracts.

When changing a track, mode, activity, or gate, check `SKILL.md`, the corresponding track/mode reference, `references/process-steps.md`, `references/skills-mapping.md`, affected templates, validators, and eval cases. Requirement changes must stay aligned with `references/requirements-workflow.md`; versioning and evidence-chain changes must stay aligned with `references/document-organization.md`, `references/traceability.md`, and its JSON schema. Avoid duplicating detailed instructions in the README.

## Build, Test, and Development Commands

There is no compilation step or package-manager setup. Use these checks from the repository root:

```bash
bash setup          # Audit the runtime and optional providers
bash setup --strict # Fail only when core validation is invalid
bash -n setup       # Validate Bash syntax without executing it
python3 scripts/validate_skill.py # Validate metadata, references, Markdown, schema, and eval suite
python3 scripts/run_evals.py      # Validate behavior-eval case coverage
shellcheck setup    # Run optional static analysis when ShellCheck is installed
git diff --check    # Detect whitespace errors in all edits
```

Missing optional providers are informational and should not fail validation.

## Coding Style & Naming Conventions

Write concise Markdown with ATX headings, fenced code blocks, and repository-relative links. Preserve each template's existing section hierarchy and placeholder style. Use lowercase kebab-case for reference and template filenames, such as `tech-selection.md` and `database-design.md`.

For Bash, retain `#!/usr/bin/env bash` and `set -euo pipefail`. Quote variable expansions, use uppercase names for environment or script-wide constants, four-space indentation inside control blocks, and descriptive snake_case function names.

## Testing Guidelines

The Python validators use only the standard library. For documentation changes, verify links, examples, capability identifiers, track/activity mappings, and consistency across affected files. For runtime/schema/eval changes, run `python3 scripts/validate_skill.py`, focused validator/eval commands, `bash -n setup`, `bash setup --strict`, and `git diff --check`.

## Commit & Pull Request Guidelines

Follow Conventional Commits, matching the existing history and documented policy: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, or `chore:`. Keep each commit focused; for example, `docs: clarify staging deployment gate`.

Pull requests should explain the workflow impact, list files kept in sync, and include validation commands and results. Link relevant issues. Include screenshots only when rendered Markdown or terminal output changes materially.
