# Backend Design Template

Document only consequential choices and affected boundaries. Reuse established
repository architecture rather than filling every section mechanically.

````markdown
# Backend Design — [Change / System]

> **Change work item**: [CHG-* / tracker]
> **Current architecture source**: [Path / diagram / ADR]

## Traceability and Impact

| REQ/AC/RULE/NFR | Current path/contract | Proposed decision/delta | TASK | Verification |
|---|---|---|---|---|
| | | | | |

## Context and Boundaries

- Affected services/modules and owners:
- Call/dependency/data flow:
- Consumers and version-skew concerns:
- Trust boundaries and authorization:

## Decisions

| ADR | Decision | Context/constraints | Alternatives | Consequences | Reversal trigger |
|---|---|---|---|---|---|
| | | | | | |

## Contracts and Data

- API/event/file contract links:
- Data ownership, lifecycle, consistency, and migration:
- Concurrency/idempotency/retry/cancellation semantics:
- Failure isolation, recovery, and operability:

## Quality and Verification

| NFR/risk | Target/invariant | Design response | TEST/measurement |
|---|---|---|---|
| | | | |

## Open Risks

| Risk/unknown | Impact | Owner | Decision/evidence needed by |
|---|---|---|---|
| | | | |
````
