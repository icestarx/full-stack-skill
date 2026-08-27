# Full-Stack Process Capability Mapping

This mapping is host-neutral. It defines the capability required at each lifecycle step, not a mandatory product, plugin, skill name, agent name, or invocation syntax. Read `platform-adapters.md` before selecting a provider.

## Selection Principles

1. Preserve the required outcome and quality gate.
2. Honor providers explicitly selected by the user or project.
3. Discover active skills, agents, and tools before invoking them.
4. Prefer the smallest provider set that completes the work.
5. Use deterministic repository tools for build, test, lint, and state checks.
6. Use independent context for consequential review when available.
7. Fall back to the main agent instead of blocking on a missing specialist.

## Per-Step Mapping

### Step 1: Clarify Requirements

| Field | Value |
|---|---|
| Primary | `product.discovery` |
| Supplement | `product.scope-review` |
| Outcome | Problem, users, alternatives, scope, priorities, acceptance criteria, success metrics |
| Evidence | Confirmed requirements document and explicit unresolved questions |

### Steps 2-3: UI/UX and Demo Confirmation

| Field | Value |
|---|---|
| Primary | `design.system`, `design.prototype` |
| Review | `design.review` |
| Outcome | Implementable design specification and reviewable prototype |
| Evidence | State coverage, responsive views, feedback resolution, stakeholder decision |

### Steps 4-5: Technical Planning and Module Boundaries

| Field | Value |
|---|---|
| Primary | `architecture.review` |
| Optional | `spec.change` |
| Outcome | Stack rationale, boundaries, dependency direction, contract points, ADRs |
| Evidence | Architecture documents, module map, dependency graph, known trade-offs |

### Step 6: Development Plan

| Field | Value |
|---|---|
| Primary | `planning.decompose` |
| Optional | `spec.change` |
| Outcome | Dependency-ordered, bounded, verifiable tasks |
| Evidence | Every task has scope, acceptance evidence, dependencies, and owner/status |

### Step 7: Database and API Contracts

| Field | Value |
|---|---|
| Primary | `architecture.review`, `database.review` |
| Optional | `spec.change` |
| Outcome | Data model, indexes, migration strategy, API schemas, errors, auth |
| Evidence | Validated schemas/contracts and documented risks |

### Step 8: Environment Setup

| Field | Value |
|---|---|
| Primary | `delivery.release`, `database.review` |
| Outcome | Reproducible local environment, CI, resettable data, deployable staging |
| Evidence | Commands and CI runs that demonstrate readiness |

### Step 9: Development and Integration

| Field | Value |
|---|---|
| Primary | `development.tdd` |
| Supplements | `qa.browser`, `review.accessibility` |
| Outcome | Working vertical behavior with unit, integration, component, and E2E evidence |
| Evidence | Fail-before/pass-after results, build output, screenshots where relevant |

Use subagents only for bounded tasks. In Codex, native subagents can isolate exploration, tests, and review; avoid parallel overlapping writes.

### Step 10: Code Review

| Field | Value |
|---|---|
| Primary | `review.code` |
| Risk-triggered | `review.security`, `database.review`, language/framework specialist |
| Outcome | Independent findings classified by impact, with actionable evidence |
| Evidence | Reviewed diff and resolution of blocking findings |

### Step 11: PR Management

| Field | Value |
|---|---|
| Primary | `delivery.release` |
| Outcome | Contextual PR, green CI, resolved feedback, controlled merge |
| Evidence | PR description, checks, approvals, and merge/deploy record |

### Step 12: Test Summary

| Field | Value |
|---|---|
| Primary | Deterministic project test commands |
| Risk-triggered | `review.security`, `review.performance`, `review.accessibility`, `qa.browser` |
| Outcome | Aggregated quality evidence and known limitations |
| Evidence | Test artifacts rather than agent assertions |

### Step 13: Production Deployment

| Field | Value |
|---|---|
| Primary | `delivery.release` |
| Outcome | Approved progressive rollout with health checks and recovery readiness |
| Evidence | Deployment record, smoke tests, metrics, rollback or roll-forward plan |

### Steps 14-15: Monitoring and Retrospective

| Field | Value |
|---|---|
| Primary | `operations.monitor`, `operations.retro` |
| Outcome | Production signals, incident learning, owned improvements, synchronized docs |
| Evidence | Dashboards/logs, retrospective actions, and documentation changes |

## Provider Classes

| Provider class | Examples | Portability rule |
|---|---|---|
| Native host features | Main agent, Codex subagents, browser, shell, patch tools | Prefer when they satisfy the capability directly |
| Repository skills | `.agents/skills`, host-specific skill folders | Discover by description; do not assume an invocation spelling |
| Custom agents | Codex project agents or host-specific reviewer agents | Treat as optional role implementations |
| MCP tools | Browser, design, docs, issue tracker, observability | Require configuration and authorization; keep a non-MCP fallback where possible |
| Legacy ecosystems | gstack, Superpowers, OpenSpec | Optional accelerators mapped in `platform-adapters.md` |

## Degraded Operation

Missing optional providers must reduce automation, not invalidate the lifecycle. Record which fallback was used and any evidence that could not be collected. Stop only when a required outcome cannot be produced safely—for example, a private production system is inaccessible, a destructive migration lacks approval, or no runnable verification environment exists.
