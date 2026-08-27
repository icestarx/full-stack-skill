# Traceability Ledger Template

Use with `references/traceability.md`. The same schema may be implemented in a
project issue tracker; preserve these fields and bidirectional queries.

```markdown
# Traceability Ledger — [Project / Product Line]

> **Version line**: [v1 / v2 / ...]
> **Baseline manifest**: [Path]
> **Owner**: [Name or role]
> **Last verified**: YYYY-MM-DD / [commit]

## Artifact Index

| ID / native reference | Type | Title / location | Version line | Status | Owner | Supersedes |
|---|---|---|---|---|---|---|
| REQ-[AREA]-001 | Requirement | [PRD path/anchor] | | approved | | |
| AC-[AREA]-001 | Acceptance criterion | [PRD path/anchor] | | approved | | |
| TASK-[AREA]-001 | Task | [Plan/tracker URL] | | planned | | |
| TEST-[AREA]-001 | Test | [Test path/name or case URL] | | planned | | |

## Relationship Ledger

| Source | Relationship | Target | Version line | Status | Evidence | Owner | Last verified |
|---|---|---|---|---|---|---|---|
| CAP-[AREA]-01 | contains | REQ-[AREA]-001 | | valid | [Capability tree] | | |
| REQ-[AREA]-001 | accepted_by | AC-[AREA]-001 | | valid | [PRD] | | |
| REQ-[AREA]-001 | planned_by | TASK-[AREA]-001 | | planned | [Plan/tracker] | | |
| TASK-[AREA]-001 | implemented_by | `src/path:fileSymbol` | | planned | [PR/commit] | | |
| AC-[AREA]-001 | verified_by | TEST-[AREA]-001 | | planned | [Result/report] | | |
| REQ-[AREA]-001 | delivered_by | [PR/build/release] | | planned | [Native URL/ID] | | |
| REQ-[AREA]-001 | observed_by | [Metric/log/alert or N/A] | | planned | [Dashboard/runbook] | | |

## Coverage Summary

| Scope | Total | Design | Tasks | Code | Tests | PR/build | Release | Observability | Stale / blocked |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Current committed requirements | | | | | | | | | |

## Orphans and Gaps

| Artifact | Type | Missing relationship | Risk | Owner | Resolution |
|---|---|---|---|---|---|
| | | | | | |

## Exceptions

| Artifact / relationship | Rationale | Risk | Alternative evidence | Owner | Review / expiry date | Status |
|---|---|---|---|---|---|---|
| | | | | | | |
```
