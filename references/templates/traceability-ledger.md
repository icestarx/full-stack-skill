# Traceability Ledger Template

Use this Markdown fallback for small projects. Medium/large projects should copy
`traceability-ledger.json`, validate it against `../schemas/traceability.schema.json`,
and generate human coverage views from structured data.

````markdown
# Traceability Ledger — [Product / Version Line]

> **Owner**: [Name or role]
> **Last verified**: [Date / commit]
> **Structured ledger**: [Path or N/A for approved small-project fallback]

## Artifact Index

| ID / native reference | Type | Title/location | Version | Lifecycle status | Owner |
|---|---|---|---|---|---|
| CAP-[AREA]-01 | CAP | [Capability tree anchor] | | approved | |
| REQ-[AREA]-001 | REQ | [Requirement anchor] | | approved | |
| RULE-[AREA]-001 | RULE | [Domain rule/invariant anchor] | | approved | |
| NFR-[AREA]-001 | NFR | [Requirement anchor] | | approved | |
| AC-[AREA]-001 | AC | [Acceptance anchor] | | approved | |
| TASK-[AREA]-001 | TASK | [Tracker/plan] | | planned | |
| `src/path:Symbol` | CODE | [Repository location] | | planned | |
| TEST-[AREA]-001 | TEST | [Test path/name/case] | | planned | |
| PR-[native] | PR | [URL] | | planned | |
| BUILD-[native] | BUILD | [Artifact/digest] | | planned | |
| RELEASE-[native] | RELEASE | [Tag/deployment] | | planned | |
| OBS-[local-ref] | OBS | [Metric/dashboard/audit] | | planned | |

## Relationship Edges

Keep physical delivery artifacts separate; do not combine `PR`, `build`, and
`release` in one target.

| Source | Source type | Relationship | Target | Target type | Version | Edge status | Evidence | Owner | Verified |
|---|---|---|---|---|---|---|---|---|---|
| CAP-[AREA]-01 | CAP | contains | REQ-[AREA]-001 | REQ | | valid | [Baseline] | | |
| CAP-[AREA]-01 | CAP | contains | RULE-[AREA]-001 | RULE | | valid | [Baseline] | | |
| REQ-[AREA]-001 | REQ | accepted_by | AC-[AREA]-001 | AC | | valid | [PRD] | | |
| REQ-[AREA]-001 | REQ | planned_by | TASK-[AREA]-001 | TASK | | planned | [Plan] | | |
| RULE-[AREA]-001 | RULE | planned_by | TASK-[AREA]-001 | TASK | | planned | [Plan] | | |
| TASK-[AREA]-001 | TASK | implemented_by | `src/path:Symbol` | CODE | | planned | [Commit] | | |
| AC-[AREA]-001 | AC | verified_by | TEST-[AREA]-001 | TEST | | planned | [Result] | | |
| RULE-[AREA]-001 | RULE | verified_by | TEST-[AREA]-001 | TEST | | planned | [Result] | | |
| `src/path:Symbol` | CODE | delivered_by | PR-[native] | PR | | planned | [Commit] | | |
| TEST-[AREA]-001 | TEST | delivered_by | PR-[native] | PR | | planned | [Checks] | | |
| PR-[native] | PR | delivered_by | BUILD-[native] | BUILD | | planned | [CI] | | |
| BUILD-[native] | BUILD | delivered_by | RELEASE-[native] | RELEASE | | planned | [Deploy] | | |
| REQ-[AREA]-001 | REQ | observed_by | OBS-[local-ref] | OBS | | planned | [Dashboard] | | |

## Coverage and Gaps

| Scope | Total | Design | Tasks | Code | Tests | PR | Build | Release | Signals | Stale/blocked |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Current committed scope | | | | | | | | | | |

| Artifact/edge | Missing relationship/evidence | Risk | Owner | Resolution |
|---|---|---|---|---|
| | | | | |

## Exceptions

| Artifact/edge | Rationale | Risk | Alternative evidence | Approver | Owner | Review/expiry | Status |
|---|---|---|---|---|---|---|---|
| | | | | | | | |
````
