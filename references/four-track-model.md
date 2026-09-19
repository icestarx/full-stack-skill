# Four-Track Operating Model

Read this reference when routing work, selecting gates, or coordinating product,
engineering, verification, and delivery responsibilities. Tracks are responsibility
streams, not team names or a requirement to use four agents.

## Track Contracts

| Track | Question | Owns | Accepted evidence |
|---|---|---|---|
| Product | Are we building the right behavior? | Problem, capability scope, UX, domain rules, acceptance, product decisions | Approved baseline/delta and `CAP/REQ/RULE/NFR/AC` links |
| Engineering | Can the system change coherently? | Reconnaissance, architecture, contracts, slices, code, migrations | Decisions, impact map, actual code/contracts, integrated slices |
| Verification | What proves the change works and remains safe? | Test design, deterministic checks, review, risk evidence | Stable tests, results, findings, exceptions |
| Delivery & Learning | Can it be delivered, operated, recovered, and improved? | Environments, compatibility, rollout, observability, incidents, feedback | Distinct build and deployment evidence, production signals, owned learning |

Verification begins when acceptance is defined. Delivery concerns begin when
compatibility, migration, environment, or observability choices can affect design.

## Shared Change State

For substantial work, keep one `CHG-*` record or equivalent tracker item as the
shared control plane. It links to canonical artifacts rather than copying them.

Canonical states use lowercase snake case:

```text
proposed → ready → in_progress → merge_ready → release_ready → observing → closed
    └──────────────→ cancelled       │              │
                  any nonterminal → blocked → prior_state
```

| Transition | Required gate/evidence | Authority |
|---|---|---|
| `proposed → ready` | Change Ready | Change owner; named approval when risk requires it |
| `ready → in_progress` | At least one Slice Ready | Change owner |
| `in_progress → merge_ready` | Every committed slice is Merge Ready | Engineering and Verification evidence owners |
| `merge_ready → release_ready` | Release Ready, or delivery explicitly `N/A` for non-released work | Release/change owner |
| `release_ready → observing` | Artifact delivered to its intended cohort/environment | Delivery owner |
| `observing → closed` | Learning Closed | Change owner |
| `* → blocked` | Missing decision, evidence, authorization, or external dependency recorded | Any track owner |
| `blocked → prior_state` | Blocking condition resolved and cheapest relevant check rerun | Owner of the blocking condition |
| `proposed/ready/in_progress → cancelled` | Cancellation rationale and cleanup/disposition recorded | User or authorized change owner |

For work with no production delivery, record delivery as `N/A` with rationale,
transition through `release_ready`, and close after merge/acceptance evidence. Never
use `closed` to hide stale links or unfinished committed scope.

Track-local status uses: `not_applicable`, `planned`, `active`, `blocked`,
`evidence_ready`, `accepted`. A shared-state transition requires every applicable
track to have the evidence named by that gate; it does not require identical local
statuses.

## Risk Determines Depth

Assess blast radius, reversibility, sensitive data, external contracts, migration
complexity, operational novelty, and uncertainty. Team size affects coordination
and document form, not risk.

| Risk | Expected depth |
|---|---|
| Low | Lean record, focused design, deterministic affected checks, ordinary review and delivery |
| Medium | Explicit impact/compatibility analysis, regression and contract evidence, independent review, staged delivery |
| High | Formal product/architecture/security decisions, named approvals, recovery rehearsal, controlled cohort, applicable failure/load/privacy evidence |

Missing evidence raises uncertainty and therefore risk. Lowering risk requires a
recorded rationale; it cannot be justified only by schedule pressure.

## Synchronization Gates

### Change Ready

- Product: origin, scope, non-goals, and acceptance are clear enough for the next slice.
- Engineering: affected surfaces, dependencies, decisions, and unknowns are recorded.
- Verification: planned evidence covers applicable positive, negative, boundary,
  permission, concurrency, compatibility, and recovery behavior.
- Delivery & Learning: rollout, recovery, signals, and operational ownership are
  addressed or explicitly `N/A`.
- No unresolved blocker affects the slice. Assigning a blocker an owner does not
  satisfy this gate.

### Slice Ready

One independently useful or risk-reducing slice has a valid origin, bounded outcome,
affected paths/contracts, dependencies, acceptance evidence, and recovery approach.
It can be merged or reverted without waiting for unrelated slices.

### Merge Ready

Actual code/test evidence replaces plans, deterministic affected checks pass,
review findings are resolved or approved as exceptions, and affected baselines,
contracts, change state, and trace edges are synchronized. The completion claim is
backed by a fresh run of the commands that prove the accepted scope and risk surface.

### Release Ready

Committed scope has no unexplained missing, stale, or blocked evidence. Immutable
build inputs and artifacts, compatibility/migration evidence, approvals, recovery,
and production signals are ready or explicitly inapplicable.

### Learning Closed

The risk-appropriate observation window has completed. Escaped defects, incidents,
stale links, and temporary flags/adapters/migration states have owners and explicit
dispositions. Reusable learning has updated a requirement, test, architecture rule,
runbook, or backlog origin.

## Vertical-Slice Loop

1. Select the smallest ready slice from the change record.
2. Refine only the product and technical decisions required for that slice.
3. Define verification before implementation; reproduce defects first when practical.
4. Implement and integrate using the safest dependency order for this slice.
5. Run focused deterministic checks, then risk-triggered independent review.
6. Replace planned links with actual evidence and pass Merge Ready.
7. Merge or deliver according to strategy, then select the next slice.

Do not accumulate a large end-of-project integration batch. Do not force staging,
browser tests, a prototype, or production delivery when the affected behavior and
risk do not require them.

## Long-Running Handoffs

Before ending a session, update the change record with completed slices, decisions,
commands/results, blockers, repository state, and the next smallest ready action.
On resume, inspect repository state and rerun the cheapest relevant smoke check
before trusting the handoff. Conversation history is not durable project state.
