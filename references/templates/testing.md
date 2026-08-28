# Verification Summary Template

Index existing CI/test artifacts; do not copy full logs or require irrelevant test
layers. Targets come from committed requirements and repository policy.

````markdown
# Verification Summary — [Change / Build]

> **Version/release target**: [Value]
> **Change work item**: [CHG-* / tracker]
> **Build/source revision**: [Immutable reference]
> **Traceability ledger**: [Path / tracker]

## Acceptance and Invariant Coverage

| TEST ID | REQ/AC/RULE/NFR/origin | Evidence layer | Native path/case/artifact | Environment/build | Result |
|---|---|---|---|---|---|
| TEST-[AREA]-001 | | | | | pass/fail/blocked/excepted |

## Risk-Based Evidence

| Risk/quality attribute | Target/invariant | Check/measurement | Actual | Status |
|---|---|---|---|---|
| Functional regression | | | | |
| Contract/compatibility | | | | N/A allowed with reason |
| Migration/recovery | | | | N/A allowed with reason |
| Security/privacy | | | | N/A allowed with reason |
| Accessibility | [Project requirement/current adopted standard] | | | N/A allowed with reason |
| Performance/reliability | [Measured target] | | | N/A allowed with reason |

## Gaps, Orphans, and Exceptions

| Artifact/acceptance | Gap or stale link | Risk | Alternative evidence/approver | Owner/follow-up |
|---|---|---|---|---|
| | | | | |

## Decision

- Merge Ready: [Yes/No and approver if required]
- Release Ready: [Yes/No/Not evaluated]
- Known defects and target disposition:
````
