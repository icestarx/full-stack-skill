# Data Contract and Migration Template

Use for affected stored data. Select rollback or roll-forward from actual data-loss
and compatibility risk; do not require a destructive down migration.

````markdown
# Data Design — [Change / Domain]

> **Change work item**: [CHG-* / tracker]
> **Authoritative schema source**: [Path / generated artifact]

## Coverage and Ownership

| REQ/AC/RULE/NFR/ADR | Entity/schema | Owner | Readers/writers | Sensitivity/lifecycle | TEST |
|---|---|---|---|---|---|
| | | | | | |

## Current and Target Model

- Current schema/format reference:
- Target delta and invariants:
- Query/access patterns and measured capacity assumptions:
- Retention, archival, deletion, audit, and legal/privacy constraints:

## Migration and Compatibility

| Stage | Schema/code behavior | Mixed-version compatibility | Verification | Abort/recovery | Owner |
|---|---|---|---|---|---|
| Expand/prepare | | | | | |
| Migrate/backfill | | | | | |
| Switch/activate | | | | | |
| Contract/cleanup | | | | | |

- Backup/restore or forward-repair plan:
- Data reconciliation and loss/corruption checks:
- Locking/load/online-change considerations:
- Temporary dual-read/write/adapters and removal condition:
````
