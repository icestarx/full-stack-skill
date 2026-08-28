# Slice Plan Template

Use when the tracker/change record does not already provide equivalent fields. Do
not invent dates or split work by technical phase when vertical slices are possible.

````markdown
# Slice Plan — [Change / Project]

> **Version / release target**: [Version or TBD]
> **Change work item**: [CHG-* path / tracker]
> **Traceability ledger**: [Path / tracker]
> **Planning horizon**: [Current slice / milestone; avoid false precision]

## Outcomes and Constraints

- Committed origins (`REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS`):
- Delivery/recovery constraints:
- Known dependencies and blocked decisions:

## Vertical Slices

Each slice should be independently useful or retire a named risk and should be
mergeable, verifiable, and recoverable without unrelated work.

| Slice | Outcome | Origin IDs | Affected surfaces/contracts | Planned verification | Recovery | Depends on | Owner | State |
|---|---|---|---|---|---|---|---|---|
| SLICE-[AREA]-01 | | | | | | | | planned |

## Tasks

| TASK ID | Slice | Origin IDs | Bounded task | Planned paths/contracts | Planned TEST/evidence | Depends on | Owner | State |
|---|---|---|---|---|---|---|---|---|
| TASK-[AREA]-001 | SLICE-[AREA]-01 | REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS-* | | | TEST-* / check | | | planned |

## Dependency and Parallelism Notes

- Critical path:
- Independently executable read-heavy or write-isolated work:
- Shared files/owners that prevent parallel writes:

## Risks and Decisions

| Risk/decision | Trigger or deadline | Mitigation/choice | Owner | Status |
|---|---|---|---|---|
| | | | | |

## Checkpoints

| Checkpoint | Evidence required | Target/trigger | Owner | Status |
|---|---|---|---|---|
| Slice Ready | Origin, impact, verification, recovery | | | |
| Merge Ready | Actual code/test/docs/trace evidence | | | |
| Release Ready | Build, deployment, compatibility, and signal evidence | If applicable | | |
````
