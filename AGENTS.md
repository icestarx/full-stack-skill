# Repository Guidelines

## Project Structure & Module Organization

This repository defines a portable full-stack lifecycle skill rather than a deployable application. `SKILL.md` is the main entry point and must remain aligned with the 15-step, 10-phase workflow. `references/platform-adapters.md` defines host-neutral capability contracts and Codex/Claude adapters; `agents/openai.yaml` supplies Codex-facing metadata. Detailed guidance lives under `references/`, and reusable document skeletons are in `references/templates/`. The executable `setup` script audits the core structure, supported hosts, and optional providers.

When changing a pipeline step, check every related source: `SKILL.md`, `references/process-steps.md`, `references/skills-mapping.md`, and the relevant template. Avoid duplicating detailed instructions in the README.

## Build, Test, and Development Commands

There is no compilation step or package-manager setup. Use these checks from the repository root:

```bash
bash setup          # Audit the runtime and optional providers
bash setup --strict # Fail only when the core skill is invalid
bash -n setup       # Validate Bash syntax without executing it
shellcheck setup    # Run optional static analysis when ShellCheck is installed
git diff --check    # Detect whitespace errors in all edits
```

Missing optional providers are informational and should not fail validation.

## Coding Style & Naming Conventions

Write concise Markdown with ATX headings, fenced code blocks, and repository-relative links. Preserve each template's existing section hierarchy and placeholder style. Use lowercase kebab-case for reference and template filenames, such as `tech-selection.md` and `database-design.md`.

For Bash, retain `#!/usr/bin/env bash` and `set -euo pipefail`. Quote variable expansions, use uppercase names for environment or script-wide constants, four-space indentation inside control blocks, and descriptive snake_case function names.

## Testing Guidelines

No automated test framework or repository coverage threshold currently exists. For documentation changes, verify links, command examples, capability identifiers, phase/step counts, and consistency across affected files. For runtime changes, run `bash -n setup`, `bash setup --strict`, the skill validator, and `git diff --check`.

## Commit & Pull Request Guidelines

Follow Conventional Commits, matching the existing history and documented policy: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, or `chore:`. Keep each commit focused; for example, `docs: clarify staging deployment gate`.

Pull requests should explain the workflow impact, list files kept in sync, and include validation commands and results. Link relevant issues. Include screenshots only when rendered Markdown or terminal output changes materially.
