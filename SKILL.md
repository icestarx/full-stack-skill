---
name: full-stack-skill
description: >
  Plan, implement, verify, and ship multi-layer software changes spanning frontend,
  backend, APIs, databases, infrastructure, or deployment. Use for end-to-end
  features, applications, services, architecture choices, or substantial changes
  that require coordination across two or more layers. Do not use for isolated
  explanations, reviews, diagnostics, or clearly scoped single-file edits.
---

# Full-Stack Development

Deliver complete, maintainable product changes through four coordinated tracks:
Product, Engineering, Verification, and Delivery & Learning. Use A1-A15 as the
default end-to-end route and stable activity identifiers, not a mandatory waterfall.

## Runtime Portability

Before invoking another skill, agent, MCP tool, or host command, read
`references/platform-adapters.md`. Resolve work by capability ID and use the
portable fallback when no specialist exists. Read
`references/provider-registry.md` only when selecting a curated provider.

- Never assume a named skill, agent, slash command, CLI, or MCP server is installed.
- Keep provider syntax out of generated project documentation.
- Preserve user authorization, sandbox, approval, and external-action boundaries.
- In Codex, use repository `AGENTS.md` for durable rules. Delegate only bounded,
  independent work that benefits from separate context.

## Start by Routing the Change

Read `references/four-track-model.md`, then:

1. Inspect repository instructions, status, architecture, tests, current behavior,
   active version baseline, and related recent changes before proposing edits.
2. Classify the operating mode: new product/major version, feature change, bug fix,
   maintenance, or incident. Read the selected playbook in
   `references/operating-modes.md`.
3. Assess risk from blast radius, reversibility, sensitive data, external contracts,
   migration complexity, operational novelty, and uncertainty. Team size affects
   coordination, not risk.
4. For substantial work, initialize or update one change work item using
   `references/templates/change-work-item.md`. Do not create a parallel source of
   truth when the repository's tracker already preserves the required fields.
5. Identify the smallest vertical slice that can produce user value or retire risk
   and can be independently verified, merged, and recovered.
6. Read `references/process-steps.md`. Mark A1-A15 applicable, already satisfied,
   or `N/A` with rationale; select capabilities through
   `references/skills-mapping.md` before resolving concrete providers.

State the selected mode, risk, and execution depth. Ask for confirmation only when
the classification would materially change scope, cost, external actions, or an
irreversible decision; otherwise proceed and record assumptions.

## Four Tracks

The tracks are continuous responsibilities. One agent may own all four; several
agents do not imply four tracks, and four tracks do not require parallel execution.

### Product Track

**Question**: Are we building the right observable behavior?

- Own the problem, capability scope, actors, domain rules, states, UX, acceptance
  criteria, priorities, non-goals, and product decisions.
- For New/Review/Change requirements, read `references/requirements-workflow.md`.
- For UI behavior, cover normal, empty, loading, error/denied, boundary, interruption,
  and recovery states. Obtain human product/design decisions when genuinely needed.
- Update only the affected major-version baseline or explicit delta. Never redefine
  a released requirement ID when its semantics change.

Use `product.discovery`, `product.scope-review`, `product.requirements-review`,
`design.system`, `design.prototype`, and `design.review` as available.

**Track evidence**: approved `CAP/REQ/RULE/NFR/AC` scope, UX/design links, decisions, and
success/failure signals.

### Engineering Track

**Question**: Can we change the system safely and coherently?

- Explore the repository before planning: dependencies, call paths, similar code,
  governing decisions, contracts, migrations, tests, and relevant history.
- Define only the architecture, data/API contracts, compatibility strategy, and
  tasks required by the current change and its known consumers.
- Decompose work into dependency-ordered vertical slices with stable `TASK-*` IDs
  and `REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS` origins.
- Implement one bounded slice at a time. Keep changes mergeable and recoverable;
  avoid a long-lived backend-first then frontend-first integration batch.
- Replace planned trace links with actual `path:symbol`, contract, migration, and
  commit/PR evidence as work completes.

Read `references/tracks/engineering.md` for detailed reconnaissance, planning,
contract, migration, and implementation activities. Use `architecture.review`,
`planning.decompose`, `database.review`, `spec.change`, and `development.tdd` as
applicable.

**Track evidence**: decisions, impact analysis, tasks, code/contracts, migrations,
and integrated slices.

### Verification Track

**Question**: What evidence proves the change works and remains safe?

- Start test design with the acceptance criteria, not after implementation.
- Define positive, negative, boundary, concurrency, permission, cancellation,
  recovery, compatibility, and operational evidence according to risk.
- For bug fixes and observable behavior changes, capture fail-before/pass-after
  evidence where practical.
- Prefer deterministic repository checks and CI artifacts. Use independent review
  for high-risk or hard-to-reverse work; an agent's confidence is not evidence.
- Verify the affected regression surface. Record uncovered acceptance criteria,
  orphan tests, stale links, and approved exceptions explicitly.
- Use `references/templates/verification-evidence.md` per slice/PR when existing CI
  and tracker output do not already provide an equivalent record.

Use project-native commands first, then `qa.browser`, `review.code`,
`review.accessibility`, `review.security`, or `review.performance` when triggered.
Before claiming a slice or change complete, use `verification.completion` to run
fresh checks that directly support the claim.

**Track evidence**: stable `TEST-*` references, commands and results, reports,
review findings, screenshots where material, and exception decisions.

### Delivery & Learning Track

**Question**: Can we release, operate, recover, and learn from the change?

- Address environments, seed/test data, compatibility, migrations, feature flags,
  rollout, rollback or roll-forward, and observability early enough to influence
  design.
- Keep build, artifact, deployment, approval, and production evidence in the release
  record; do not copy product/UX/architecture baselines into release folders.
- Use staged rollout proportional to risk. Verify health and business signals during
  an explicit observation window.
- Preserve incident evidence, create regression origins, update runbooks/baselines,
  and assign cleanup for temporary flags, adapters, and migration states.
- Feed repeated human-test findings and escaped defects back into requirements,
  deterministic tests, lint, architecture rules, or operational checks.

Use `delivery.environment`, `delivery.change-review`, `delivery.deploy`,
`delivery.recover`, `operations.monitor`, and `operations.retro` as applicable.

**Track evidence**: environment readiness, immutable release manifest, deployment
and recovery records, production signals, and owned learning actions.

## A1-A15 Execution and Slice Loop

The default complete route is A1 Requirements through A15 Learning. Run it in
order for a new product or major version. In other modes, preserve the identifiers
while selecting only applicable steps. Existing evidence may satisfy a step; an
inapplicable step requires a recorded rationale. Never manufacture an artifact
only to make the sequence appear complete.

A6-A12 form the repeatable delivery loop for each vertical slice. A later step may
reopen an earlier one when implementation, review, release, or production evidence
changes the product contract, architecture, verification plan, or recovery design.

For each vertical slice:

1. Bring all applicable tracks to **Slice Ready**: bounded origin and outcome,
   affected surfaces, acceptance evidence, dependencies, and recovery approach.
2. Implement and integrate the slice while Verification runs focused checks.
3. Update the change work item and traceability ledger with actual evidence.
4. Pass **Merge Ready**: deterministic checks green, findings resolved, documents
   synchronized, and no unexplained stale or blocked link.
5. Merge or release according to the change strategy; then select the next slice.

Do not wait for every feature to finish before integration, review, or verification.
Pause at a gate only for missing evidence, a recorded decision, an authorization
boundary, or an external dependency that prevents meaningful progress.

## Synchronization Gates

| Gate | Required outcome |
|---|---|
| Change Ready | Product contract, impact, verification plan, and delivery/operability concerns are sufficient to start a slice |
| Slice Ready | One bounded slice has origin, dependencies, expected code/contracts, tests, and recovery |
| Merge Ready | Actual implementation and fresh completion evidence are valid; review and documentation/ledger deltas are complete |
| Release Ready | Committed scope maps to accepted tests and distinct PR, build, deployment, compatibility, approval, and signal evidence |
| Learning Closed | Observation completed; defects, stale evidence, temporary mechanisms, and follow-ups have owners/dispositions |

If a required outcome is inapplicable, record `N/A` with rationale. Do not satisfy a
gate with circular links or prose assertions.

## Documentation and Traceability

Read `references/document-organization.md` when initializing documentation, starting
a major version, or preparing a release. Major-version baselines describe effective
product/UX/engineering/quality/operations truth; release records describe delivery
events; change work items coordinate active work.

Read `references/traceability.md` before changing committed behavior. Maintain the
bidirectional graph:

```text
CAP → REQ/RULE/NFR → TASK → CODE → PR → BUILD → RELEASE
       REQ → AC ─────→ TEST ────────┘
       REQ/AC/RULE/NFR → DESIGN/PDR/ADR/CONTRACT
       REQ/AC/RULE/NFR → OBS
```

Code, tests, PRs, and production evidence must also trace backward to a valid
`REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS` origin. Use the project's durable tracker when it supports
the required relationships; otherwise use the repository ledger template.

## Quality Invariants

Apply these to every mode, at depth proportional to risk:

1. Observable behavior has testable acceptance or a valid non-product origin.
2. Changed behavior has focused deterministic verification; defects gain regression
   evidence. Coverage percentages are diagnostic, not a substitute for behavior and
   risk coverage.
3. Secrets never enter source or logs. Security, privacy, permissions, and audit
   controls are reviewed when affected.
4. Data changes define compatibility, backup/recovery, and a tested rollback or
   roll-forward strategy. Do not require a destructive down migration when forward
   repair is safer.
5. Production changes pass an equivalent pre-production or controlled cohort check
   and have health signals plus a recovery path.
6. Accessibility is part of acceptance for affected user interfaces.
7. Review precedes merge; high-risk work receives independent review and named
   approval where required.
8. Completion claims use fresh command/result evidence against the stated
   acceptance and risk surface.
9. Baselines, contracts, decisions, work state, evidence, and release records change
   with the implementation rather than as a later cleanup task.
10. Use Conventional Commits when consistent with repository policy; never override
   a repository's established contribution rules.

## Long-Running Work

Do not rely on conversation history as the only state. Before ending a session,
record completed slices, decisions, commands/results, blockers, repository state,
and the next smallest ready action in the change work item. On resume, inspect the
repository state and re-run the cheapest relevant smoke check before continuing.

## Provider and Delegation Policy

Specialized skills, agents, and tools are optional providers.

- Discover providers from the active host before invoking them.
- Delegate bounded, independent work only when separate context improves quality or
  latency; prefer read-heavy exploration and independent verification.
- Keep one owner for overlapping writes and final integration.
- Require artifacts or deterministic results, not completion claims.
- Fall back to the main agent and repository-native tools when no specialist exists.

## Reference Router

Load references only when the current work requires them:

| Reference | Read when |
|---|---|
| `references/four-track-model.md` | Routing a change, selecting gates, or coordinating tracks |
| `references/operating-modes.md` | After selecting New/Major, Feature Change, Bug Fix, Maintenance, or Incident mode |
| `references/platform-adapters.md` | Selecting a skill, agent, MCP tool, or host command |
| `references/provider-registry.md` | Selecting a curated Superpowers, UI UX Pro Max, or Ponytail profile after capability selection |
| `references/document-organization.md` | Initializing docs, a major-version baseline, change record, or release |
| `references/requirements-workflow.md` | Creating, reviewing, or changing product requirements |
| `references/traceability.md` | Creating IDs, links, coverage views, exceptions, or release evidence |
| `references/process-steps.md` | Running the default A1-A15 flow, selecting applicable steps, and checking completion criteria |
| `references/tracks/product.md` | Product requirements, UX contract, and acceptance activities |
| `references/tracks/engineering.md` | Reconnaissance, architecture, planning, contracts, implementation |
| `references/tracks/verification.md` | Verification design, review, PR evidence, and summary |
| `references/tracks/delivery-learning.md` | Environment, release, observation, incident learning, and cleanup |
| `references/skills-mapping.md` | Capability selection, conditional reviewers, and provider fallback for each A1-A15 step |
| `references/tech-selection.md` | Making a material technology choice |
| `references/capability-domains.md` | Entering a specialized application/domain layer |
| `references/templates/` | Producing an affected lifecycle artifact; use only the needed template |
