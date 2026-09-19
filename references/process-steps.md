# Full-Stack 15-Step Workflow

A1-A15 are the default end-to-end route from requirements through learning. Run
them in order for a new product or major version. For an existing-product change,
bug fix, maintenance task, or incident, keep the same identifiers while selecting
only the applicable steps. A skipped step requires existing evidence or a recorded
`N/A` rationale at the relevant gate.

The sequence is a coordination spine, not a batch waterfall. Verification design
starts with A1, delivery concerns may affect A4-A7, and A6-A12 repeat for each
vertical slice. Production evidence from A14-A15 may reopen any earlier step.

Read `references/four-track-model.md` for states and gates,
`references/operating-modes.md` for mode-specific routes, and
`references/skills-mapping.md` before selecting concrete providers.

## Workflow Shape

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

For multiple slices, repeat A6-A12 as needed. Revisit A1-A8 when a slice exposes
new scope, design, contract, dependency, environment, or recovery information.

## Step Contract

Each step below defines:

- **Activity**: the work performed;
- **Capabilities**: portable outcomes to resolve through
  `references/platform-adapters.md`, not assumed provider names;
- **Evidence**: durable output or a link to an authoritative existing source;
- **Complete when**: the checkable condition for advancing.

Use repository-native commands for build, test, lint, migration, and state checks.
Missing optional providers trigger the documented fallback; they do not remove the
required outcome.

## A1 — Requirements and Scope

**Activity**: Inventory current product and repository truth; select New, Review,
or Change requirement mode; define the problem, actors, scope, non-goals,
capabilities, `REQ/RULE/NFR/AC` items, state semantics, and success/failure signals.
Start verification design from the acceptance criteria.

**Capabilities**: `product.discovery`, `product.scope-review`, and
`product.requirements-review` as applicable.

**Evidence**: Approved requirement baseline or delta, origins, acceptance criteria,
assumptions, blockers, and trace links. Use `references/requirements-workflow.md`
and `references/templates/requirements.md`.

**Complete when**: The affected product scope satisfies the requirements Definition
of Ready, or a non-product change has a valid `BUG/TECH/SEC/OPS` origin and explicit
behavioral invariant. No hidden blocker affects the next step.

## A2 — UX and Interaction Contract

**Activity**: Map affected requirements and acceptance criteria to flows, screens,
components, content, permissions, responsive behavior, and normal, empty, loading,
error, denied, boundary, interruption, and recovery states. Produce the cheapest
reviewable design evidence appropriate to uncertainty and risk.

**Capabilities**: `design.system` and, when interaction uncertainty warrants it,
`design.prototype`.

**Evidence**: Annotated flow, UI delta, wireframe, prototype, or justified `N/A`;
links from affected `REQ/AC` items. Use `references/templates/ui-design.md`.

**Complete when**: Every affected user/operator interaction has reviewable state
coverage and trace links, or is explicitly inapplicable with rationale.

## A3 — Product Decision and Acceptance

**Activity**: Review scope and UX trade-offs, demonstrate uncertain interactions,
resolve product questions, record rejected alternatives when useful, and obtain the
human decisions required for policy, taste, cost, scope, or irreversible behavior.

**Capabilities**: `product.scope-review`, `design.review`, and
`design.prototype` when a runnable or clickable demonstration is the cheapest proof.

**Evidence**: Linked product decisions, review findings, approvals, exceptions, and
updated `REQ/AC` or design evidence.

**Complete when**: Product and UX evidence needed by the next slice is accepted;
every unresolved item is classified as a blocker, approved assumption, or follow-up.

## A4 — Repository Reconnaissance and Technical Decisions

**Activity**: Inspect repository instructions, architecture, dependencies, call
paths, similar implementations, contracts, tests, history, supported versions,
permissions, stored formats, and operational boundaries. Make only the durable
technical decisions required by the change.

**Capabilities**: `architecture.review`; add a domain specialist or a technology
selection review only when the affected surface or decision requires it.

**Evidence**: Repository-grounded impact map, unknowns, material decisions, and
affected origin/acceptance links. Record an ADR only for a consequential choice.

**Complete when**: Every material affected surface and known consumer is accounted
for, and consequential choices have evidence or an explicit decision owner.

## A5 — Boundaries and Dependency Map

**Activity**: Confirm domain and module ownership, public interfaces, data ownership,
dependency direction, shared foundations, independently mergeable slices, and the
critical path. Preserve established repository boundaries when they remain valid.

**Capabilities**: `architecture.review`.

**Evidence**: Module/consumer map, dependency order, contract boundaries, parallel
work constraints, and candidate vertical slices.

**Complete when**: Slice boundaries avoid hidden consumers and circular ownership;
shared-file or shared-contract coordination has an explicit owner.

## A6 — Vertical Slice Plan

**Activity**: Decompose work into the smallest independently useful or risk-reducing
vertical slices. Give tasks stable `TASK-*` IDs, origins, dependencies, affected
surfaces, verification, recovery, ownership, and state.

**Capabilities**: `planning.decompose`.

**Evidence**: Dependency-ordered slice plan in the change record, tracker, or
`references/templates/development-plan.md`.

**Complete when**: At least one slice is bounded, traceable, independently
verifiable, mergeable, and recoverable without unrelated work.

## A7 — Data and Interface Contracts

**Activity**: Define affected API, event, file, client, integration, and persistence
contracts, including validation, errors, authorization, concurrency, idempotency,
version skew, compatibility, migration, observability, recovery, and cleanup.

**Capabilities**: `architecture.review`; use `database.review` for persistence or
migration work and `spec.change` for a versioned proposal or contract delta.

**Evidence**: Executable or authoritative contracts, schema/migration plan,
compatibility matrix, contract tests, and rollback or roll-forward strategy. Use the
API/database templates only when the repository lacks an equivalent source.

**Complete when**: Every changed boundary has an authoritative contract, affected
consumers and mixed-version behavior are covered, and data recovery is testable.

## A8 — Environment and Delivery Readiness

**Activity**: Prepare the minimum reproducible environment for the current slice;
define data setup/reset, secrets, permissions, dependencies, build provenance,
deployment path, smoke checks, signals, and recovery constraints.

**Capabilities**: `delivery.release` plus repository-native environment, build, and
CI/CD tools.

**Evidence**: Runnable verification target and commands/configuration, or a recorded
limitation and risk decision. Use the staging template only when such an environment
is required.

**Complete when**: The current slice passes Slice Ready: origin, dependencies,
expected code/contracts, planned verification, environment, and recovery are known.

## A9 — Implementation and Integration

**Activity**: Establish fail-before or characterization evidence where practical;
implement the smallest coherent slice; integrate against real boundaries early;
and replace planned links with actual paths, symbols, migrations, and contracts.

**Capabilities**: `development.tdd` and repository-native development tools; use
`qa.browser` when user-visible browser behavior requires interactive evidence.

**Evidence**: Mergeable implementation, focused deterministic results, actual code
and contract links, and updated change/trace state.

**Complete when**: The slice satisfies its acceptance/invariant locally, integrates
across affected boundaries, and has a demonstrated recovery path.

## A10 — Review

**Activity**: Review the actual diff, contracts, origins, failure modes, tests, and
operational impact. Rank findings by user/system impact and resolve them or record
approved exceptions. Use independent context for high-risk work.

**Capabilities**: `review.code`; conditionally use `review.security`,
`review.accessibility`, `review.performance`, or `database.review` when requested or
triggered by the changed risk surface.

**Evidence**: Review findings, resolutions, approvals, and exception records.

**Complete when**: No unresolved release-blocking finding remains and every approved
exception has rationale, owner, risk, and review/expiry condition.

## A11 — PR and Change Evidence

**Activity**: Assemble the review unit linking origins, requirements, tasks, code,
contracts, migrations, tests, compatibility, security, rollout, recovery, decisions,
and documentation/ledger deltas. Follow repository PR and approval conventions.

**Capabilities**: `review.code` for review continuity and `delivery.release` for PR,
CI, artifact, and approval evidence when those systems are in scope.

**Evidence**: PR or equivalent review record with distinct code, test, build, and
approval references. Use `references/templates/verification-evidence.md` when the
tracker and CI do not already preserve equivalent evidence.

**Complete when**: A reviewer can reconstruct what changed, why it changed, how it
was verified, and how it can be recovered without relying on conversation history.

## A12 — Verification Summary

**Activity**: Reconcile acceptance and invariant coverage across static, unit,
component, contract, integration, E2E, migration, compatibility, security,
accessibility, performance, manual, and operational evidence as applicable.

**Capabilities**: Repository-native deterministic commands; conditionally
`qa.browser`, `review.security`, `review.accessibility`, and `review.performance`.

**Evidence**: Accepted, failed, blocked, stale, excepted, and `N/A` evidence indexed
by stable `TEST-*` and origin IDs. Use `references/templates/testing.md` when needed.

**Complete when**: The slice passes Merge Ready. If delivery is in scope, build,
compatibility, approvals, recovery, and signals are sufficient for Release Ready;
otherwise delivery is explicitly `N/A`.

## A13 — Release and Recovery

**Activity**: Pin source revision, baseline, included changes, build inputs, artifact
digest, target cohort/environment, deployment order, abort thresholds, approvals,
feature flags, migration sequence, communications, and recovery verification.

**Capabilities**: `delivery.release`.

**Evidence**: Immutable release manifest, deployment record, health checks, and
tested rollback or roll-forward evidence. Use the release and production-deploy
templates when the repository lacks equivalent records.

**Complete when**: The intended artifact reaches the authorized cohort/environment,
post-deploy checks pass, and the change enters `observing`; failed checks invoke the
defined recovery or stop decision.

## A14 — Observation

**Activity**: Observe requirement-linked infrastructure, application, business,
audit/security, and user-experience signals over a window justified by traffic,
batch cycles, delayed effects, and risk. Compare baseline, expected range, actual
result, and decision thresholds.

**Capabilities**: `operations.monitor`.

**Evidence**: Cohort/environment, observation window, dashboards/metrics/logs/traces,
threshold results, incidents, and release decision.

**Complete when**: The observation window supplies enough positive and negative
evidence to accept, extend, halt, or recover the release; absence of alerts alone is
not acceptance.

## A15 — Learning and Anti-Entropy

**Activity**: Review escaped defects, incidents, manual retesting, delivery friction,
stale documents, temporary flags/adapters/migration states, and repeated mistakes.
Convert reusable learning into requirements, tests, lint/structural checks,
architecture rules, runbooks, or owned follow-up origins.

**Capabilities**: `operations.retro`.

**Evidence**: Retrospective decisions, synchronized baselines/runbooks/trace links,
owned follow-ups, and cleanup/review dates for temporary mechanisms.

**Complete when**: Learning Closed passes: observation is complete and every defect,
stale edge, temporary mechanism, and follow-up has an explicit disposition. New
evidence may reopen the relevant earlier A-step.

## Gate Alignment

| Gate | Typical workflow point | Required interpretation |
|---|---|---|
| Change Ready | Across A1-A7 | Product contract, impact, verification plan, and operability are sufficient for the next slice |
| Slice Ready | End of A8 | One bounded slice has origin, dependencies, contracts, planned evidence, environment, and recovery |
| Merge Ready | End of A12 | Actual implementation, review, tests, documentation, and trace links are synchronized |
| Release Ready | A12-A13 boundary | Immutable build/deployment inputs, compatibility, approvals, recovery, and signals are ready |
| Learning Closed | End of A15 | Observation and follow-up/cleanup dispositions are complete |

## Cross-Cutting Artifacts

| Artifact | Purpose | Template/reference |
|---|---|---|
| Major-version manifest | Effective product/UX/engineering/quality/operations baseline | `references/templates/version-manifest.md` |
| Change work item | Shared four-track and A1-A15 execution state | `references/templates/change-work-item.md` |
| Verification evidence | Slice/PR evidence index when CI/tracker is insufficient | `references/templates/verification-evidence.md` |
| Traceability ledger | Normalized artifact relationships and exceptions | `references/traceability.md`; ledger templates/schema |
| Release manifest | Immutable scope and delivery/production evidence | `references/templates/release-manifest.md` |
