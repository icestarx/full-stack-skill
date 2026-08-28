# Delivery and Recovery Template

Select strategy, cohort, timing, and approval from actual risk and platform policy.
Do not copy example percentages, alert thresholds, or migration order from another
system.

````markdown
# Delivery and Recovery — [Release / Change]

> **Version/release**: [Value]
> **Baseline manifest/source revision**: [Path + immutable revision]
> **Included changes**: [CHG-* / tracker]
> **Release manifest**: [Path]
> **Traceability ledger**: [Path / tracker]

## Artifact and Environment

| Component | Source revision | Build/artifact + digest | Target/cohort | Owner |
|---|---|---|---|---|
| | | | | |

## Compatibility and Migration

| Stage/order | Old/new component or data combinations supported | Verification | Abort/recovery | Cleanup condition |
|---|---|---|---|---|
| | | | | |

- Backup/restore or forward-repair plan:
- Irreversible step and required authority:
- Feature flag/adapter owner and expiry/removal trigger:

## Rollout and Decision Thresholds

| Cohort/stage | Entry evidence | Success/failure signals | Observation basis | Abort/advance authority |
|---|---|---|---|---|
| | | | [Traffic/time/batch-cycle rationale] | |

## Recovery Verification

| Failure scenario | Recovery action | Data/user effect | Verification | Expected duration/owner |
|---|---|---|---|---|
| | | | | |

## Operational Readiness

- Dashboards/signals linked to critical REQ/RULE/NFR:
- Alerts and thresholds derived from baselines/SLOs:
- Runbook/on-call/escalation:
- Support/communication plan:

## Release Decision

- Required approvals and evidence:
- Final decision/authority:
- Deployment/health evidence:
- Open exceptions and expiry:
````
