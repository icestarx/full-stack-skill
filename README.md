# full-stack-skill

An agent-portable skill that orchestrates the full-stack development lifecycle from requirements through shipped software. Codex is a first-class target; Claude Code and other Agent Skills-compatible hosts can use the same core workflow through adapters.

## Features

- **Four-track delivery**: Product, Engineering, Verification, and Delivery & Learning advance through shared evidence gates
- **15-step end-to-end workflow**: A1 requirements through A15 learning, with explicit activities, capabilities, evidence, and completion criteria
- **Change-aware routing**: Distinct paths for new products, feature changes, bug fixes, maintenance, and incidents
- **Requirements discipline**: New, Review, and Change modes with capability trees, state machines, operational semantics, and a Definition of Ready
- **Major-version baselines**: Separates long-lived product/UX/engineering versions from minor/patch release records
- **End-to-end traceability**: Links requirements to decisions, tasks, code, tests, PRs, releases, and production signals
- **Capability orchestration**: Selects available skills, agents, MCP tools, or portable fallbacks by outcome
- **Curated provider registry**: Maps Superpowers, UI UX Pro Max, and Ponytail to suitable steps without making them hard dependencies
- **Codex adapter**: Supports `$full-stack-skill`, `AGENTS.md`, native subagents, and optional MCP providers
- **Lifecycle templates**: Activity documents plus change, version, release, verification, and traceability records
- **Risk-driven gates**: Control depth follows blast radius, reversibility, contracts, data, and operational risk
- **Long-running handoffs**: Durable change state, evidence, blockers, and next-action records survive agent sessions
- **Deterministic validation**: Standard-library validators check metadata, links, Markdown, traceability, and eval contracts
- **Behavior eval suite**: Forward-test cases cover all five operating modes and recurring failure patterns

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
through the default A1-A15 route in small vertical slices. New products normally
run the complete sequence. Other modes select applicable steps, reuse existing
evidence, and record `N/A` rationales rather than treating the sequence as a fixed
waterfall.

Execution depth is risk-driven. Low-risk work uses lean records and focused checks;
medium-risk work adds impact/compatibility analysis, independent review, and staged
rollout; high-risk work adds formal decisions, named approvals, recovery rehearsal,
and applicable security, performance, migration, and failure evidence.

## A1-A15 End-to-End Workflow

The 15 activities are the default coordination spine:

```text
A1 → A2 → A3 → A4 → A5 → A6 → A7 → A8
                                  │
                                  ▼
                           A9 → A10 → A11 → A12
                           ▲                 │
                           └── fix/rework ───┘
                                             │
                                             ▼
                                      A13 → A14 → A15
```

Verification design begins with acceptance at A1, and delivery concerns influence
A4-A8 before implementation. Repeat A6-A12 for every vertical slice. A14-A15
evidence can reopen an earlier step when production behavior changes the known
requirements, architecture, tests, or recovery plan. The detailed step contract is
in [references/process-steps.md](references/process-steps.md).

| Step | Flow activity | Main work and evidence | Capabilities |
|---|---|---|---|
| **A1** | Requirements and scope | Establish current truth, origins, scope, `REQ/RULE/NFR/AC`, state semantics, acceptance, and success/failure signals | `product.discovery`, `product.scope-review`, `product.requirements-review` |
| **A2** | UX and interaction contract | Cover affected flows, responsive behavior, permissions, and normal/empty/loading/error/boundary/recovery states | `design.system`; conditional `design.prototype` |
| **A3** | Product decision and acceptance | Review trade-offs, demonstrate uncertain interactions, resolve blockers, and record approvals or assumptions | `product.scope-review`, `design.review`; conditional `design.prototype` |
| **A4** | Repository reconnaissance and technical decisions | Inspect architecture, dependencies, consumers, contracts, history, versions, permissions, and operational boundaries | `architecture.review`; conditional technology/domain specialist |
| **A5** | Boundaries and dependency map | Confirm ownership, interfaces, data boundaries, dependency direction, shared foundations, and candidate slices | `architecture.review` |
| **A6** | Vertical slice plan | Create bounded, traceable, independently verifiable and recoverable slices with stable `TASK-*` IDs | `planning.decompose` |
| **A7** | Data and interface contracts | Define API/event/data contracts, compatibility, migrations, version skew, contract tests, recovery, and cleanup | `architecture.review`; conditional `database.review`, `spec.change` |
| **A8** | Environment and delivery readiness | Prepare the minimum reproducible target, data/secrets setup, build provenance, smoke checks, signals, and recovery | `delivery.environment`, repository-native environment/CI tools |
| **A9** | Implementation and integration | Produce fail-before/characterization evidence, implement one slice, integrate early, and record actual code/contract links | `development.tdd`; conditional `qa.browser`; project tools |
| **A10** | Review | Review diff, contracts, origins, failure modes, tests, and operational impact; resolve findings or approve exceptions | `review.code`; conditional security/accessibility/performance/database review |
| **A11** | PR and change evidence | Assemble a reconstructable review unit linking intent, tasks, code, tests, CI, approvals, rollout, and recovery | `review.code`, `delivery.change-review` |
| **A12** | Verification summary | Reconcile accepted, failed, blocked, stale, excepted, and `N/A` evidence, then rerun the checks that prove the completion claim | `verification.completion`, deterministic project commands; conditional reviewers |
| **A13** | Release and recovery | Pin source/build/artifact/cohort, execute the authorized rollout, verify health, and invoke recovery when thresholds fail | `delivery.deploy`, `delivery.recover` |
| **A14** | Observation | Compare requirement-linked infrastructure, application, business, security, and UX signals against thresholds | `operations.monitor` |
| **A15** | Learning and anti-entropy | Convert defects and friction into requirements, tests, rules, runbooks, follow-ups, and temporary-mechanism cleanup | `operations.retro` |

### Mode-Specific Routes

| Mode | How it uses A1-A15 |
|---|---|
| New product / major version | Run the complete sequence; repeat A6-A12 for each vertical slice before A13-A15 |
| Feature change | Start with an A1 baseline delta; select affected A2-A8 work; run A9-A12 per slice and A13-A15 when delivery applies |
| Bug fix | Link the bug and expected contract at A1, reproduce/map it at A4, then run the applicable implementation-through-learning route |
| Maintenance | Establish a `TECH/SEC/OPS` origin and invariant at A1; A2-A3 are commonly `N/A`; prove compatibility through applicable later steps |
| Incident | Perform authorized reversible containment first, preserve evidence, then re-enter A1 or A4 for the durable fix and complete observation/learning |

## Capability Guide

Capabilities describe outcomes rather than hard dependencies on a named skill,
agent, MCP server, or CLI. Resolve providers from the active host using
[references/platform-adapters.md](references/platform-adapters.md); when no
specialist exists, use the main agent and repository-native tools while preserving
the same evidence requirement.

| Capability | Required outcome |
|---|---|
| `product.discovery` | Confirm problem, users, goals, scope, assumptions, and acceptance inputs |
| `product.scope-review` | Recommend expanding, keeping, or reducing scope with value/risk/effort rationale |
| `product.requirements-review` | Find completeness, consistency, testability, boundary, and change-impact gaps |
| `design.system` | Define information architecture, flows, states, visual rules, and responsive behavior |
| `design.prototype` | Produce a reviewable mockup or runnable interaction prototype |
| `design.review` | Produce evidence-based UX and visual findings and decisions |
| `architecture.review` | Analyze boundaries, data flow, dependencies, consumers, decisions, and technical risk |
| `planning.decompose` | Produce small dependency-ordered slices and tasks with origins, evidence, and recovery |
| `database.review` | Review schema, queries, indexes, migrations, compatibility, backup, and recovery |
| `spec.change` | Maintain a versioned proposal or authoritative contract delta |
| `development.tdd` | Establish RED evidence, implement the minimum GREEN change, and refactor under tests |
| `qa.browser` | Reproduce and verify user-visible behavior in an interactive browser |
| `review.code` | Independently review correctness, maintainability, contracts, tests, and failure modes |
| `review.security` | Review affected trust boundaries, authentication, authorization, data, dependencies, secrets, and audit behavior |
| `review.accessibility` | Verify affected keyboard, semantic, ARIA, focus, content, and contrast behavior |
| `review.performance` | Measure affected client/server performance or reliability against explicit targets |
| `verification.completion` | Produce fresh command/result evidence that directly supports every completion claim |
| `delivery.environment` | Prepare a reproducible verification/delivery target with data, secrets, build, smoke, signal, and cleanup constraints |
| `delivery.change-review` | Preserve distinct PR/change, review, CI, approval, artifact, and recovery references |
| `delivery.deploy` | Execute an authorized immutable-artifact rollout with compatibility, migration, cohort, and health evidence |
| `delivery.recover` | Prove and execute the authorized rollback, roll-forward, containment, or stop path when required |
| `operations.monitor` | Evaluate infrastructure, application, business, security, and UX signals against thresholds |
| `operations.retro` | Turn release/incident evidence into owned improvements, documentation updates, and cleanup |

## Dependencies

This skill is an orchestrator with no mandatory specialist dependency. Its curated
optional profiles are Superpowers, UI UX Pro Max, and Ponytail. Missing providers
fall back to the main agent and repository-native tools; no provider replaces
deterministic project evidence.

Run `bash setup` for a host/provider audit. See [DEPENDENCIES.md](DEPENDENCIES.md) for the complete runtime contract.

Repository validation:

```bash
python3 scripts/validate_skill.py
python3 scripts/validate_traceability.py references/templates/traceability-ledger.json
python3 scripts/run_evals.py
```

## File Structure

```
full-stack-skill/
├── SKILL.md                       # Portable lifecycle conductor
├── agents/openai.yaml             # Codex-facing metadata
├── setup                          # Host and provider audit
├── scripts/                       # Deterministic Skill, traceability, and eval checks
├── evals/                         # Forward-testing cases and scoring rubric
├── DEPENDENCIES.md                # Runtime/provider contract
├── README.md                      # This file
└── references/
    ├── platform-adapters.md       # Capability contracts and host adapters
    ├── provider-registry.md       # Curated provider profiles and selection bounds
    ├── four-track-model.md        # Track ownership, routing, gates, and slice loop
    ├── operating-modes.md         # New/change/bugfix/maintenance/incident playbooks
    ├── document-organization.md   # Major-version baselines vs release records
    ├── requirements-workflow.md   # New/review/change requirement modes and gates
    ├── traceability.md            # Stable IDs, link ledger, propagation, and gates
    ├── process-steps.md           # Detailed A1-A15 end-to-end workflow
    ├── skills-mapping.md          # Per-step capability selection and fallbacks
    ├── tech-selection.md          # Technology choice guide
    ├── capability-domains.md      # Conditional domain review prompts
    ├── tracks/                    # Product, engineering, verification, delivery detail
    ├── schemas/                   # Machine-readable traceability schema
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
        ├── traceability-ledger.json
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
8. Completion claims cite fresh command/result evidence for the accepted scope and risk surface.
9. Baselines, contracts, evidence, and release records change with the implementation.

## License

MIT
