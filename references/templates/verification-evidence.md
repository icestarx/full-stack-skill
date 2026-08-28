# Verification Evidence Template

Use per vertical slice or PR. Prefer generated CI artifacts where available; this
record indexes evidence and gaps rather than reproducing raw logs.

````markdown
# Verification — [CHG / Slice / PR]

> **Origin and acceptance IDs**: [REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS]
> **TASK / TEST IDs**: [IDs]
> **Code under review**: [Commit / PR / paths and symbols]
> **Environment / build**: [Immutable reference]
> **Reviewer**: [Independent reviewer when required]

## Intended Behavior and Risk

- Behavior or invariant being proved:
- Regression surface:
- Highest-risk failure mode:

## Evidence

| Check | Command / case / artifact | Expected | Actual | Result |
|---|---|---|---|---|
| Fail-before / reproduction | | | | Pass / N/A |
| Unit / component | | | | |
| Contract / integration | | | | |
| End-to-end / exploratory | | | | |
| Security / accessibility / performance | | | | N/A with reason allowed |
| Migration / compatibility / recovery | | | | N/A with reason allowed |

## Review Findings

| Finding | Severity | Resolution / owner | Evidence | Status |
|---|---|---|---|---|
| | | | | |

## Gaps and Exceptions

| Missing evidence | Risk | Rationale | Approver | Expiry / follow-up |
|---|---|---|---|---|
| | | | | |

## Decision

- `merge_ready`: Yes / No
- `release_ready`: Yes / No / Not evaluated
- Ledger updates:
````
