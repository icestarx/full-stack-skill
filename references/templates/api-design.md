# Interface Contract Template

Use for affected APIs, events, files, webhooks, or service interfaces. Prefer the
repository's generated specification when it is authoritative.

````markdown
# Interface Contract — [Name / Change]

> **Change work item**: [CHG-* / tracker]
> **Source revision / generated spec**: [Path, commit, or N/A]

## Coverage and Consumers

| Interface | REQ/AC/RULE/NFR/ADR | Producers | Consumers/versions | TASK | Contract TEST |
|---|---|---|---|---|---|
| | | | | | |

## Conventions

- Protocol/style and rationale:
- Authentication/authorization:
- Versioning and compatibility window:
- Error representation and retryability:
- Pagination/streaming/backpressure where applicable:
- Rate/capacity limits:
- Idempotency/concurrency rules:
- Observability/audit contract:

## Interface Definitions

### [Operation / event / schema]

- Purpose and origin IDs:
- Preconditions and authorization:
- Input/schema/validation:
- Output/schema:
- Errors and caller action:
- Side effects and state transitions:
- Compatibility/deprecation:
- Implementation TASK/code:
- TEST/evidence:

## Change and Rollout Matrix

| Consumer/version combination | Supported during rollout? | Adaptation/migration | Removal condition/owner |
|---|---|---|---|
| | | | |
````
