# Verification Environment Template

Use for the minimum environment needed by the affected slice. It may describe local,
ephemeral preview, shared integration, staging, device lab, or another target.

````markdown
# Verification Environment — [Change / Environment]

> **Version/release target**: [Value or TBD]
> **Change work item**: [CHG-* / tracker]
> **Origins**: [NFR/OPS/SEC/REQ IDs]

## Purpose and Parity

- Behaviors/risks this environment verifies:
- Relevant similarities/differences from production:
- Limitations and approved risk:

## Reproduction

- Provision/start command or pipeline:
- Required services/dependencies:
- Secrets/permission source (never secret values):
- Build/source revision:

## Data Setup and Reset

- Dataset/scenarios and sensitivity classification:
- Idempotent seed/fixture method:
- Reset/isolation method:
- Migration and recovery verification:

## Verification

| Check | Command/artifact | Expected | Result/evidence |
|---|---|---|---|
| Provision/connectivity | | | |
| Smoke/health | | | |
| Required integration/E2E | | | |

## Access and Ownership

- URLs/targets:
- Access prerequisites:
- Owner/support path:
- Cost/cleanup/expiry:
````
