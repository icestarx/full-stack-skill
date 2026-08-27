# full-stack-skill

An agent-portable skill that orchestrates the full-stack development lifecycle from requirements through shipped software. Codex is a first-class target; Claude Code and other Agent Skills-compatible hosts can use the same core workflow through adapters.

## Features

- **Complete pipeline**: Requirements → Design → Technical Planning → Development → Quality → Deployment → Operations
- **Requirements discipline**: New, Review, and Change modes with capability trees, state machines, operational semantics, and a Definition of Ready
- **Major-version baselines**: Separates long-lived product/UX/engineering versions from minor/patch release records
- **End-to-end traceability**: Links requirements to decisions, tasks, code, tests, PRs, releases, and production signals
- **Capability orchestration**: Selects available skills, agents, MCP tools, or portable fallbacks by outcome
- **Codex adapter**: Supports `$full-stack-skill`, `AGENTS.md`, native subagents, and optional MCP providers
- **Lifecycle templates**: Phase documents plus version, release, and traceability manifests
- **Quality gates**: Hard checkpoints between phases — no skipping
- **Project sizing**: Auto-detects Small/Medium/Large and tailors the pipeline
- **Dependency checker**: `setup` script audits what's installed and what's missing

## Quick Start

Repository-scoped Codex installation:

```bash
mkdir -p .agents/skills
git clone https://github.com/icestarx/full-stack-skill.git .agents/skills/full-stack-skill
bash .agents/skills/full-stack-skill/setup --strict
```

Invoke with `$full-stack-skill`, or describe a multi-layer build/change and allow implicit selection. For Claude Code or another host, place the same folder in that host's supported skill location. See [DEPENDENCIES.md](DEPENDENCIES.md) for adapters and degraded operation.

## Pipeline Overview

```
PHASE 1: REQUIREMENTS ─── Step 1: Clarify Requirements → 📄 Requirements Doc
PHASE 2: DESIGN ───────── Step 2: UI/UX Design Spec → 📄 UI Design Doc
                          Step 3: Demo Confirmation → Sign-off
PHASE 3: TECH PLANNING ── Step 4: Technical Planning → 📄 Frontend + Backend Design
                          Step 5: Module Decomposition → Module List + Dependency Graph
PHASE 4: DEV PLAN ─────── Step 6: Development Plan → 📄 Dev Plan Doc
PHASE 5: TECH DOCS ────── Step 7: Module Tech Docs → 📄 DB Doc + 📄 API Doc
PHASE 6: ENV SETUP ────── Step 8: Environment Setup → 📄 Staging Deploy Doc
PHASE 7: DEVELOPMENT ──── Step 9: Module Development [backend → frontend → integrate]
PHASE 8: QUALITY ──────── Step 10: Code Review → Step 11: PR → Step 12: Test Summary
PHASE 9: DEPLOYMENT ───── Step 13: Production Deploy → 📄 Production Deploy Doc
PHASE 10: OPERATIONS ──── Step 14: Monitoring → Step 15: Retrospective
```

## Project Sizing

The skill automatically assesses project scale and asks you to confirm:

| Size | Team | Timeline | Pipeline |
|------|------|----------|----------|
| **Small** | 1-2 people | 1-2 weeks | ~9 steps (condensed) |
| **Medium** | 5-10 people | 1-3 months | Full 15 steps |
| **Large** | 10+ people | 3+ months | 15 steps + extensions |

## Dependencies

This skill is an orchestrator, but it has no mandatory dependency on gstack, Superpowers, OpenSpec, named reviewer agents, or a particular MCP server. Those are optional capability providers. Missing providers fall back to the main agent and repository-native tools.

Run `bash setup` for a host/provider audit. See [DEPENDENCIES.md](DEPENDENCIES.md) for the complete runtime contract.

## File Structure

```
full-stack-skill/
├── SKILL.md                       # Portable lifecycle conductor
├── agents/openai.yaml             # Codex-facing metadata
├── setup                          # Host and provider audit
├── DEPENDENCIES.md                # Runtime/provider contract
├── README.md                      # This file
└── references/
    ├── platform-adapters.md       # Capability contracts and host adapters
    ├── document-organization.md   # Major-version baselines vs release records
    ├── requirements-workflow.md   # New/review/change requirement modes and gates
    ├── traceability.md            # Stable IDs, link ledger, propagation, and gates
    ├── process-steps.md           # 15-step detailed instructions
    ├── skills-mapping.md          # Per-step capability mapping
    ├── tech-selection.md          # Technology choice guide
    ├── capability-domains.md      # Domain best practices
    └── templates/                 # Phase and cross-cutting document templates
        ├── requirements.md
        ├── ui-design.md
        ├── frontend-design.md
        ├── backend-design.md
        ├── development-plan.md
        ├── database-design.md
        ├── api-design.md
        ├── staging-deploy.md
        ├── testing.md
        ├── production-deploy.md
        ├── traceability-ledger.md
        ├── version-manifest.md
        └── release-manifest.md
```

## Non-Negotiable Rules

1. **TDD**: RED → GREEN → REFACTOR, coverage ≥ 80%
2. **Conventional Commits**: `feat/fix/refactor/perf/test/docs/chore/style/ci`
3. **Security scan in CI**: SAST + dependency scan on every push
4. **No hardcoded secrets**: Env vars or secret manager only
5. **Reversible migrations**: Every `up` has a tested `down`
6. **Code review before merge**: Automated self-check before PR creation
7. **Staging before production**: Code hits staging and passes E2E first
8. **Accessibility baseline**: Semantic HTML, ARIA, keyboard navigation

## Design Documents

The full process specification and skill mapping matrix are maintained in the [auto-dev-skills](https://github.com/icestarx/auto-dev-skills) repository:

- [fullstack-process.md](https://github.com/icestarx/auto-dev-skills/blob/main/docs/fullstack-process.md) — 15-step process V4 spec
- [skills-mapping.md](https://github.com/icestarx/auto-dev-skills/blob/main/docs/skills-mapping.md) — Skill mapping matrix V4
- [fullstack-process-review.md](https://github.com/icestarx/auto-dev-skills/blob/main/docs/fullstack-process-review.md) — Review & decision record

## License

MIT
