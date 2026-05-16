# full-stack-skill

A Claude Code skill that orchestrates the complete full-stack development lifecycle — from requirements through shipped software. 15 steps, 10 phases, 10 mandatory documents.

## Features

- **Complete pipeline**: Requirements → Design → Technical Planning → Development → Quality → Deployment → Operations
- **Skill orchestration**: Delegates to 30+ specialized skills and agents at each step (gstack, superpowers, OpenSpec)
- **10 document templates**: Every phase produces structured, reviewable documents
- **Quality gates**: Hard checkpoints between phases — no skipping
- **Project sizing**: Auto-detects Small/Medium/Large and tailors the pipeline
- **Dependency checker**: `setup` script audits what's installed and what's missing

## Quick Start

```bash
# 1. Clone to your Claude Code skills directory
git clone https://github.com/icestarx/full-stack-skill.git ~/.claude/skills/full-stack-skill

# 2. Run the dependency check
bash ~/.claude/skills/full-stack-skill/setup

# 3. Install missing dependencies (gstack, superpowers, agents)
#    See DEPENDENCIES.md for details

# 4. Use in Claude Code
#    Just describe what you want to build — the skill auto-triggers
```

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

This skill is an **orchestrator** — it delegates to other skills and agents.

### Required

| Dependency | Purpose |
|------------|---------|
| [gstack](https://github.com/icestarx) | Product, design, deployment, QA, ops (16+ sub-skills) |
| superpowers | Development discipline — TDD, planning, code review |

### Agents

11 core agents (architect, code-reviewer, security-reviewer, database-reviewer, e2e-runner, a11y-architect, performance-optimizer, tdd-guide, build-error-resolver, doc-updater, refactor-cleaner) plus 13 language-specific reviewers.

Run `bash setup` for a full audit. See [DEPENDENCIES.md](DEPENDENCIES.md) for complete details.

## File Structure

```
full-stack-skill/
├── SKILL.md                       # Main conductor — 413 lines
├── setup                          # Dependency detection & install helper
├── DEPENDENCIES.md                # Full dependency inventory
├── README.md                      # This file
└── references/
    ├── process-steps.md           # 15-step detailed instructions
    ├── skills-mapping.md          # Per-step skill selection rationale
    ├── tech-selection.md          # Technology choice guide
    ├── capability-domains.md      # Domain best practices
    └── templates/                 # 10 document templates
        ├── requirements.md
        ├── ui-design.md
        ├── frontend-design.md
        ├── backend-design.md
        ├── development-plan.md
        ├── database-design.md
        ├── api-design.md
        ├── staging-deploy.md
        ├── testing.md
        └── production-deploy.md
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
