# Four-Track Capability Mapping

This mapping is host-neutral. It defines capabilities by four-track responsibility
and detailed activity, not a mandatory product, plugin, skill name, agent name, or
invocation syntax. Read `four-track-model.md` to route work and
`platform-adapters.md` before selecting a provider.

## Selection Principles

1. Preserve the required outcome and quality gate.
2. Honor providers explicitly selected by the user or project.
3. Discover active skills, agents, and tools before invoking them.
4. Prefer the smallest provider set that completes the work.
5. Use deterministic repository tools for build, test, lint, and state checks.
6. Use independent context for consequential review when available.
7. Fall back to the main agent instead of blocking on a missing specialist.

## Track Mapping

| Track | Core capabilities | Risk-triggered supplements |
|---|---|---|
| Product | `product.discovery`, `product.scope-review`, `product.requirements-review`, `design.system` | `design.prototype`, `design.review` |
| Engineering | `architecture.review`, `planning.decompose`, `development.tdd` | `database.review`, `spec.change`, domain specialist |
| Verification | Deterministic project commands, `review.code` | `qa.browser`, `review.accessibility`, `review.security`, `review.performance` |
| Delivery & Learning | `delivery.release`, `operations.monitor`, `operations.retro` | `database.review`, platform/incident specialist |

The same activity may require more than one track. Select providers for bounded
outcomes; never assign a whole track to a provider merely because its name sounds
similar.

## Detailed Activity Mapping

### Step 1: Clarify Requirements

| Field | Value |
|---|---|
| Primary | `product.discovery` |
| Supplement | `product.scope-review`, `product.requirements-review` |
| Outcome | Source-grounded New, Review, or Change requirements with a complete capability tree, explicit stateful behavior, operational semantics, boundaries, quality attributes, and impact |
| Evidence | Capability-to-requirement coverage, stable P0 IDs, baseline/ledger entries, transition tables, operational semantics, acceptance criteria, decisions/open questions, and Definition of Ready result |

### Steps 2-3: UI/UX and Demo Confirmation

| Field | Value |
|---|---|
| Primary | `design.system`, `design.prototype` |
| Review | `design.review` |
| Outcome | Implementable design specification and reviewable prototype mapped to committed behavior |
| Evidence | REQ/AC-to-flow/screen/state links, responsive views, feedback resolution, and linked approval |

### Steps 4-5: Technical Planning and Module Boundaries

| Field | Value |
|---|---|
| Primary | `architecture.review` |
| Optional | `spec.change` |
| Outcome | Stack rationale, boundaries, dependency direction, contract points, ADRs, and capability-to-module alignment |
| Evidence | REQ/AC-to-decision/contract links, architecture documents, module map, dependency graph, and trade-offs |

### Step 6: Development Plan

| Field | Value |
|---|---|
| Primary | `planning.decompose` |
| Optional | `spec.change` |
| Outcome | Dependency-ordered, bounded, verifiable tasks with stable origins |
| Evidence | Every TASK has REQ/AC/BUG/TECH/SEC/OPS origin, planned code/test evidence, dependencies, owner, and status |

### Step 7: Database and API Contracts

| Field | Value |
|---|---|
| Primary | `architecture.review`, `database.review` |
| Optional | `spec.change` |
| Outcome | Data model, indexes, migrations, API/event schemas, errors, auth, and contract traceability |
| Evidence | REQ/AC/ADR-to-data/API/contract-test links, validated contracts, and documented risks |

### Step 8: Environment Setup

| Field | Value |
|---|---|
| Primary | `delivery.release`, `database.review` |
| Outcome | Reproducible local environment, CI, resettable data, deployable staging |
| Evidence | NFR/OPS/SEC origins plus commands and CI runs that demonstrate readiness |

### Step 9: Development and Integration

| Field | Value |
|---|---|
| Primary | `development.tdd` |
| Supplements | `qa.browser`, `review.accessibility` |
| Outcome | Working vertical behavior with actual code/test links and unit, integration, component, and E2E evidence |
| Evidence | TASK origins, `path:symbol`, TEST IDs, fail-before/pass-after results, build output, and screenshots where relevant |

Use subagents only for bounded tasks. In Codex, native subagents can isolate exploration, tests, and review; avoid parallel overlapping writes.

### Step 10: Code Review

| Field | Value |
|---|---|
| Primary | `review.code` |
| Risk-triggered | `review.security`, `database.review`, language/framework specialist |
| Outcome | Independent findings on code risk and forward/backward trace completeness |
| Evidence | Reviewed diff, origin audit, orphan/stale-link report, and resolution of blocking findings |

### Step 11: PR Management

| Field | Value |
|---|---|
| Primary | `delivery.release` |
| Outcome | Contextual PR with portable origins, actual code surfaces, verification, and ledger delta |
| Evidence | Affected IDs, TEST evidence, docs/ledger update, checks, approvals, and merge record |

### Step 12: Test Summary

| Field | Value |
|---|---|
| Primary | Deterministic project test commands |
| Risk-triggered | `review.security`, `review.performance`, `review.accessibility`, `qa.browser` |
| Outcome | Aggregated AC-to-TEST quality evidence, gaps, and known limitations |
| Evidence | Stable TEST references, results, uncovered ACs, orphan/stale mappings, and defect links |

### Step 13: Production Deployment

| Field | Value |
|---|---|
| Primary | `delivery.release` |
| Outcome | Approved progressive rollout with a closed release manifest and recovery readiness |
| Evidence | Baseline/docs commit, scope IDs, PR/commit/build/test/deployment/approval evidence, signals, and rollback plan |

### Steps 14-15: Monitoring and Retrospective

| Field | Value |
|---|---|
| Primary | `operations.monitor`, `operations.retro` |
| Outcome | Requirement-linked production signals, incident learning, owned origins, and synchronized baselines/releases |
| Evidence | REQ-to-signal links, dashboards/logs, incident/release IDs, retrospective actions, and stale-link disposition |

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
