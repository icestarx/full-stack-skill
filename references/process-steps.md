# Full-Stack Activity Index

The 15 activity numbers are stable lookup keys retained for compatibility. They are
not phases, a fixed order, or a requirement to generate every document. Route the
change with `references/four-track-model.md` and `references/operating-modes.md`, then read only the track
reference containing the needed activity.

## Activity Map

| ID | Activity | Primary track | Run when | Reference / usual artifact |
|---|---|---|---|---|
| A1 | Requirements and scope | Product | Observable behavior, scope, or acceptance changes | `references/tracks/product.md`; `references/templates/requirements.md` |
| A2 | UX and interaction contract | Product | An affected human/operator interface needs design evidence | `references/tracks/product.md`; `references/templates/ui-design.md` |
| A3 | Product decision and acceptance | Product | Product trade-off or review evidence is needed | `references/tracks/product.md` |
| A4 | Reconnaissance and technical decisions | Engineering | Repository impact or consequential design is unclear | `references/tracks/engineering.md`; affected design/ADR |
| A5 | Boundaries and dependency map | Engineering | Modules/consumers or slice ordering need clarification | `references/tracks/engineering.md` |
| A6 | Slice plan | Engineering | More than one coherent task/slice is required | `references/tracks/engineering.md`; `references/templates/development-plan.md` |
| A7 | Data and interface contracts | Engineering | Persistence/API/event/integration contracts change | `references/tracks/engineering.md`; API/DB templates |
| A8 | Environment and delivery readiness | Delivery & Learning | A runnable integration/preview/staging path is needed | `references/tracks/delivery-learning.md`; staging template |
| A9 | Implementation and integration | Engineering | Code/config/data changes are authorized | `references/tracks/engineering.md` |
| A10 | Review | Verification | A slice/PR needs correctness and risk review | `references/tracks/verification.md` |
| A11 | PR evidence | Verification | A PR or equivalent review unit is in scope | `references/tracks/verification.md`; verification template |
| A12 | Verification summary | Verification | Merge/release evidence must be reconciled | `references/tracks/verification.md`; testing template |
| A13 | Release and recovery | Delivery & Learning | Delivery to a target cohort/environment is in scope | `references/tracks/delivery-learning.md`; release/deploy templates |
| A14 | Observation | Delivery & Learning | Delivered behavior needs operational acceptance | `references/tracks/delivery-learning.md` |
| A15 | Learning and anti-entropy | Delivery & Learning | Observation, incident, or repeated friction yields improvements | `references/tracks/delivery-learning.md` |

## Selection Rules

- Select activities by required outcome and evidence, not by number.
- Repeat selected activities as needed per vertical slice; an earlier activity may
  run after a later one when production learning changes the product contract.
- Skip an activity when its outcome is already proven or genuinely inapplicable.
  Record the evidence or `N/A` rationale at the applicable gate.
- For low-risk changes, several artifacts may be fields in one tracker item. For
  high-risk changes, separate owned documents and approvals may be appropriate.
- Existing repository conventions and generated specifications remain authoritative;
  do not create a parallel document merely because a template exists.

## Cross-Cutting Artifacts

| Artifact | Purpose | Template/reference |
|---|---|---|
| Major-version manifest | Effective product/UX/engineering/quality/operations baseline | `references/templates/version-manifest.md` |
| Change work item | Shared four-track state for substantial active work | `references/templates/change-work-item.md` |
| Verification evidence | Slice/PR evidence index when CI/tracker is insufficient | `references/templates/verification-evidence.md` |
| Traceability ledger | Normalized artifact relationships and exceptions | `references/traceability.md`; ledger templates/schema |
| Release manifest | Immutable scope and delivery/production evidence | `references/templates/release-manifest.md` |

## Gate Summary

| Gate | Required outcome |
|---|---|
| Change Ready | Product contract, impact, verification plan, and operability are sufficient for the next slice; no affected blocker remains |
| Slice Ready | One bounded slice has origin, dependencies, expected surfaces, verification, and recovery |
| Merge Ready | Actual implementation/evidence is valid and affected docs/trace state are synchronized |
| Release Ready | Scope, immutable build and deployment evidence, compatibility, approvals, recovery, and signals are ready |
| Learning Closed | Observation completed and defects, stale evidence, temporary mechanisms, and follow-ups have dispositions |

Detailed transition rules live in `references/four-track-model.md`.
