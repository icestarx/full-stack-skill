# full-stack-skill

An agent-portable skill that orchestrates the full-stack development lifecycle from requirements through shipped software. Codex is a first-class target; Claude Code and other Agent Skills-compatible hosts can use the same core workflow through adapters.

## Features

- **Four-track delivery**: Product, Engineering, Verification, and Delivery & Learning advance through shared evidence gates
- **Change-aware routing**: Distinct paths for new products, feature changes, bug fixes, maintenance, and incidents
- **Requirements discipline**: New, Review, and Change modes with capability trees, state machines, operational semantics, and a Definition of Ready
- **Major-version baselines**: Separates long-lived product/UX/engineering versions from minor/patch release records
- **End-to-end traceability**: Links requirements to decisions, tasks, code, tests, PRs, releases, and production signals
- **Capability orchestration**: Selects available skills, agents, MCP tools, or portable fallbacks by outcome
- **Codex adapter**: Supports `$full-stack-skill`, `AGENTS.md`, native subagents, and optional MCP providers
- **Lifecycle templates**: Activity documents plus change, version, release, verification, and traceability records
- **Risk-driven gates**: Control depth follows blast radius, reversibility, contracts, data, and operational risk
- **Long-running handoffs**: Durable change state, evidence, blockers, and next-action records survive agent sessions
- **Dependency checker**: `setup` script audits what's installed and what's missing

## Quick Start

Repository-scoped Codex installation:

```bash
mkdir -p .agents/skills
git clone https://github.com/icestarx/full-stack-skill.git .agents/skills/full-stack-skill
bash .agents/skills/full-stack-skill/setup --strict
```

Invoke with `$full-stack-skill`, or describe a multi-layer build/change and allow implicit selection. For Claude Code or another host, place the same folder in that host's supported skill location. See [DEPENDENCIES.md](DEPENDENCIES.md) for adapters and degraded operation.

## Operating Model

| Track | Continuous responsibility |
|---|---|
| **Product** | Problem, scope, UX, domain rules, requirements, acceptance, decisions |
| **Engineering** | Repository analysis, architecture, contracts, tasks, code, migrations |
| **Verification** | Test design, deterministic checks, reviews, quality and risk evidence |
| **Delivery & Learning** | Environments, compatibility, rollout, observability, incidents, feedback |

Each substantial change has a shared work item. The tracks synchronize at Change
Ready, Slice Ready, Merge Ready, Release Ready, and Learning Closed. Work proceeds
in small vertical slices; the existing 15 steps remain available as a detailed
activity catalog rather than a fixed waterfall.

Execution depth is risk-driven. Low-risk work uses lean records and focused checks;
medium-risk work adds impact/compatibility analysis, independent review, and staged
rollout; high-risk work adds formal decisions, named approvals, recovery rehearsal,
and applicable security, performance, migration, and failure evidence.

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
    ├── four-track-model.md        # Track ownership, routing, gates, and slice loop
    ├── document-organization.md   # Major-version baselines vs release records
    ├── requirements-workflow.md   # New/review/change requirement modes and gates
    ├── traceability.md            # Stable IDs, link ledger, propagation, and gates
    ├── process-steps.md           # 15-step detailed instructions
    ├── skills-mapping.md          # Per-step capability mapping
    ├── tech-selection.md          # Technology choice guide
    ├── capability-domains.md      # Domain best practices
    └── templates/                 # Activity and cross-cutting document templates
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
        ├── change-work-item.md
        ├── verification-evidence.md
        ├── traceability-ledger.md
        ├── version-manifest.md
        └── release-manifest.md
```

## Non-Negotiable Rules

1. Every change has a valid product or non-product origin and testable acceptance.
2. Verification covers changed behavior and risk; defects gain regression evidence.
3. No hardcoded secrets; affected security, privacy, permissions, and audit controls are reviewed.
4. Data changes define compatibility, recovery, and tested rollback or roll-forward.
5. Review precedes merge; high-risk work receives independent review and approval.
6. Production changes use a controlled pre-production/cohort check, health signals, and recovery path.
7. Accessibility is part of acceptance for affected user interfaces.
8. Baselines, contracts, evidence, and release records change with the implementation.

## Background Documents

The local `SKILL.md` and `references/` files are authoritative for this version.
Earlier process background is available in the [auto-dev-skills](https://github.com/icestarx/auto-dev-skills) repository:

- [fullstack-process.md](https://github.com/icestarx/auto-dev-skills/blob/main/docs/fullstack-process.md) — 15-step process V4 spec
- [skills-mapping.md](https://github.com/icestarx/auto-dev-skills/blob/main/docs/skills-mapping.md) — Skill mapping matrix V4
- [fullstack-process-review.md](https://github.com/icestarx/auto-dev-skills/blob/main/docs/fullstack-process-review.md) — Review & decision record

## License

MIT
