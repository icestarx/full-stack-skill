# Major-Version Manifest Template

````markdown
# [V2] Documentation Baseline Manifest

> **Baseline mode**: Independent / Derived
> **Parent baseline**: [None or one immediate parent]
> **Status**: Draft / Active / Maintenance / Retired
> **Owner**: [Name or role]
> **Baseline source revision**: [Commit/tag containing the listed content, or TBD]
> **Resolved snapshot digest**: [Generated after resolution, or N/A]
> **Last verified**: YYYY-MM-DD

## Product-Line Scope

- Target users and surfaces:
- Supported platforms/integrations:
- Explicit exclusions:
- Support lifecycle:

## Shared Imports

| Shared document | Supported version statement | Owner | Verified |
|---|---|---|---|
| `../../shared/...` | | | |

## Version-Owned Documents

| Area | Authoritative document | Status | Requirement/decision IDs | Owner |
|---|---|---|---|---|
| Product | `product/...` | | | |
| UX | `ux/...` | | | |
| Engineering | `engineering/...` | | | |
| Quality | `quality/...` | | | |
| Operations | `operations/...` | | | |

## Derived-Baseline Reuse

Complete only for Derived mode. List every resolved inherited document directly;
do not require readers to traverse transitive parent manifests.

| Resolved document | Source baseline + pinned revision | Reuse / Replace / Remove | Replacement or rationale |
|---|---|---|---|
| | | | |

## Superseded Semantics

| New ID / document | Supersedes | Reason | Compatibility notes |
|---|---|---|---|
| | | | |

## Traceability

- Structured ledger: `../../traceability/ledger.json` or configured tracker
- Human coverage view: `../../traceability/ledger.md` (optional/generated)
- Baseline coverage view: `../../traceability/coverage/[version].md`
- Open blockers/exceptions:
````
