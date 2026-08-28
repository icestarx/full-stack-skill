# Release Manifest Template

````markdown
# Release Manifest — [2.0.0]

> **Version line**: [v2]
> **Baseline manifest**: `docs/versions/v2/manifest.md`
> **Included change work items**: [CHG-* paths / tracker URLs]
> **Baseline source revision**: [Immutable commit/tag containing the referenced baseline content]
> **Manifest revision**: [Filled by release tooling after publication, or N/A]
> **Source tag / commit**: [Tag and SHA]
> **Build / artifact**: [Immutable ID and digest]
> **Release status**: Planned / Verifying / Released / Rolled back

## Committed Scope

| Requirement / rule / NFR ID | Acceptance/validation | Change type | Owner | Status |
|---|---|---|---|---|
| REQ-[AREA]-001, RULE-[AREA]-001, or NFR-[AREA]-001 | AC-[AREA]-001 or TEST-[AREA]-001 | Added / Modified / Deprecated | | |

## Delivery Evidence

| Requirement / task | PR | Commit | Tests / report | Build artifact | Approval |
|---|---|---|---|---|---|
| | | | | | |

## Deployment Evidence

| Environment / cohort | Deployment ID | Time | Smoke/health evidence | Result |
|---|---|---|---|---|
| | | | | |

## Feature Flags and Compatibility

| Flag / migration | Requirements | Initial state | Enable/rollback rule | Owner |
|---|---|---|---|---|
| | | | | |

## Production Verification

| Requirement | Metric / log / trace / audit / alert | Baseline | Expected | Observation window | Result |
|---|---|---:|---:|---|---|
| | | | | | |

## Traceability Closure

- Ledger update: [Path/commit]
- Missing/stale/blocked edges: [None or list]
- Approved exceptions: [None or links]
- Final release decision and approver:
````
