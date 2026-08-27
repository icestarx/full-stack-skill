# Four-Track Operating Model

Read this reference when routing work, deciding which lifecycle activities are
needed, or coordinating a change across product, engineering, quality, and
operations. The tracks are responsibility streams, not team names or mandatory
parallel agents.

## The Four Tracks

| Track | Question | Owns | Continuous output |
|---|---|---|---|
| Product | Are we building the right behavior? | Problem, capability scope, UX, domain rules, acceptance criteria, product decisions | Approved product baseline or delta |
| Engineering | Can we change the system safely? | Reconnaissance, architecture, contracts, tasks, code, migrations, technical decisions | Small, integrated vertical slices |
| Verification | What evidence proves it works and remains safe? | Test design, deterministic checks, exploratory review, security/accessibility/performance evidence, trace coverage | Accepted or blocked evidence |
| Delivery & Learning | Can we release, operate, and improve it? | Environments, rollout, compatibility, release records, observability, incidents, feedback | Releasable artifacts and production learning |

Verification starts when acceptance criteria are written. Delivery starts when
compatibility, environments, and observability affect the design. Do not postpone
either track until coding is complete.

## Shared Change Control

Create one change work item from `references/templates/change-work-item.md` for
substantial work. It is the shared control plane for all tracks and references the
canonical baseline, traceability ledger, tasks, evidence, and release records.

Use these states:

```text
proposed → ready → in_progress → merge_ready → releasable → observing → closed
                    ↘ blocked     ↘ cancelled
```

State is evidence-based. A track's narrative claim cannot advance the shared state
without the required links or approved exception.

## Operating Modes

| Mode | Default route |
|---|---|
| New product / major version | Establish all four tracks and a version baseline; execute the full relevant activity set |
| Feature change | Record requirement/design deltas, inspect impact, deliver vertical slices, verify regressions, update the active baseline |
| Bug fix | Reproduce and create `BUG-*`; clarify the product contract only if ambiguous; add regression evidence; use a proportionate release path |
| Maintenance | Use `TECH-*`, `SEC-*`, or `OPS-*` origin; focus on impact, compatibility, deterministic verification, and recovery |
| Incident | Mitigate first within incident authority; preserve evidence; then create durable fix, regression test, baseline/runbook updates, and learning actions |

Do not regenerate every lifecycle document for each change. Update only the
authoritative baseline, affected contracts, work item, evidence, and release record.

## Risk Determines Depth

Assess blast radius, reversibility, data sensitivity, external contracts, migration
complexity, operational novelty, and uncertainty. Team size affects coordination and
document form; it does not determine risk.

| Risk | Expected control depth |
|---|---|
| Low | Lean work item, focused design notes, deterministic tests, ordinary review and release |
| Medium | Explicit impact analysis, contract/regression coverage, independent review, staged rollout and monitored acceptance |
| High | Formal product/architecture/security decisions, compatibility rehearsal, failure injection or load evidence where applicable, named approvals, canary and tested recovery |

Raise risk when evidence is missing. Lowering risk requires a recorded rationale.

## Synchronization Gates

### Change Ready

- Product: origin, scope, non-goals, and acceptance are clear.
- Engineering: affected surfaces, dependencies, decisions, and unknowns are known.
- Verification: planned evidence covers positive, negative, boundary, and recovery behavior.
- Delivery & Learning: compatibility, rollout, rollback/roll-forward, and signals are addressed or explicitly `N/A`.

### Slice Ready

The next vertical slice has an origin, bounded outcome, affected paths/contracts,
acceptance evidence, dependencies, and recovery approach. It can be merged or
reverted without waiting for unrelated slices.

### Merge Ready

Actual code and test evidence replace planned links; deterministic checks pass;
review findings are resolved; affected baselines, contracts, work item, and ledger
are updated in the same change.

### Release Ready

Committed scope has no unexplained missing, stale, or blocked evidence; build and
deployment artifacts are pinned; compatibility and migration checks pass; approval,
rollback/roll-forward, and production signals are ready.

### Learning Closed

The observation window completed; escaped defects and incidents have owners and
regression actions; stale links and temporary flags/adapters have dispositions;
reusable learning has updated requirements, tests, architecture rules, or runbooks.

## Vertical-Slice Loop

For each independently valuable or risk-reducing slice:

1. Select the smallest ready slice from the change work item.
2. Refine only the product and technical decisions needed for that slice.
3. Define verification before implementation; capture fail-before evidence when
   fixing a defect or changing observable behavior where practical.
4. Implement and integrate the slice, keeping compatibility with in-flight versions.
5. Run focused deterministic checks, then risk-triggered independent review.
6. Update actual trace links and pass Merge Ready.
7. Merge or release according to the change strategy; do not accumulate a giant
   end-of-project integration batch.

## Mapping the 15 Activities

The numbered activities remain a reusable detail catalog in
`references/process-steps.md`; they are not a mandatory waterfall.

| Activities | Primary track | Supporting tracks |
|---|---|---|
| 1-3 Requirements, UX, confirmation | Product | Verification, Engineering |
| 4-7 Architecture, decomposition, planning, contracts | Engineering | Product, Verification, Delivery & Learning |
| 8 Environment setup | Delivery & Learning | Engineering, Verification |
| 9 Development and integration | Engineering | Product, Verification |
| 10-12 Review, PR, test evidence | Verification | Engineering, Delivery & Learning |
| 13 Deployment | Delivery & Learning | Verification, Engineering |
| 14-15 Monitoring and retrospective | Delivery & Learning | Product, Verification, Engineering |

An activity may recur for every slice. Skip an activity only when its outcome is
already proven or genuinely inapplicable, and record the evidence or rationale.

## Long-Running Work and Handoffs

At the end of a working session, update the work item with completed slices, actual
verification commands/results, decisions, blockers, repository state, and the next
smallest ready action. On resume, inspect repository status and re-run the cheapest
relevant smoke check before trusting the handoff. Do not use chat history as the
only durable state.
