# End-to-End Traceability

Traceability is a maintained evidence graph, not a one-time matrix. Read this when
creating committed IDs and again at planning, merge, release, and learning gates.

## Graph Model

Logical intent and physical delivery use explicit nodes and edges:

```text
CAP contains REQ/RULE/NFR
REQ accepted_by AC
REQ/AC/RULE/NFR constrained_by DESIGN/PDR/ADR/CONTRACT
REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS planned_by TASK
TASK/REQ/RULE/NFR implemented_by CODE
AC/RULE/NFR/BUG/TECH/SEC/OPS verified_by TEST
TASK/CODE/TEST delivered_by PR
PR delivered_by BUILD
BUILD delivered_by RELEASE
REQ/AC/RULE/NFR observed_by OBS
```

`CODE`, `PR`, `BUILD`, `RELEASE`, and `OBS` above are artifact types, not invented
ID prefixes. Use native repository paths/symbols, PR numbers/URLs, commit SHAs,
artifact IDs/digests, release tags/deployment IDs, feature flags, dashboards,
metrics, logs, traces, alerts, and audit references.

The graph must work backward: a production signal, release, build, PR, test, or code
change identifies the requirement/NFR or classified non-product origin that
justified it. Lean projects may omit inapplicable logical intermediates only where
the relationship schema permits it. Delivery evidence must still keep PR, build,
and release nodes distinct rather than collapsing them into an ambiguous target.

## Stable Logical IDs

| Prefix | Artifact |
|---|---|
| `CAP-*` | Module, function, or subfunction capability |
| `REQ-*` | Functional/product requirement |
| `RULE-*` | Consequential domain rule or invariant |
| `NFR-*` | Measurable non-functional requirement |
| `AC-*` | Acceptance criterion |
| `PDR-*` / `ADR-*` | Product or architecture decision |
| `CHG-*` | Active change container; never a substitute origin |
| `TASK-*` | Planned implementation or verification work |
| `TEST-*` | Stable test scenario/case |
| `BUG-*`, `TECH-*`, `SEC-*`, `OPS-*` | Non-feature work origins |

Never reuse a logical ID. Preserve it while observable semantics remain compatible.
When released semantics change incompatibly, create a successor and connect it with
`supersedes` / `superseded_by`.

## Relationship Schema

| Relationship | Valid intent |
|---|---|
| `contains` | Capability contains a child capability, requirement, domain rule, or NFR |
| `accepted_by` | Requirement defines acceptable behavior through an AC |
| `verified_by` | AC/RULE/NFR/origin is verified by a TEST record, including approved manual-review evidence when applicable |
| `constrained_by` | Intent/implementation is governed by design, decision, or contract |
| `planned_by` | Intent or non-product origin is covered by a task |
| `implemented_by` | Task or intent maps to an actual code/config/data symbol/path |
| `delivered_by` | Artifact is included in the next physical delivery artifact |
| `observed_by` | Released intent maps to a production/operational signal |
| `supersedes` / `superseded_by` | Semantic replacement link |
| `blocks` | Unresolved artifact prevents a gate |

Every edge records source, relationship, target, source/target types, version line,
status, evidence, owner, and last verification. Edge statuses are `planned`,
`valid`, `stale`, `blocked`, and `deprecated`. Artifact lifecycle statuses are owned
by their source system and must not be confused with edge status.

Use the repository tracker/ALM when it provides durable fields and bidirectional
queries. Otherwise:

- small projects may use `references/templates/traceability-ledger.md`;
- medium/large projects should use the JSON companion described by
  `references/schemas/traceability.schema.json`, optionally generating Markdown coverage views;
- CI should validate the structured ledger with `scripts/validate_traceability.py`.

Do not infer gate-critical relationships from arbitrary prose.

## Track Responsibilities

### Product

- Create `CAP/REQ/RULE/NFR/AC` in the authoritative baseline.
- Link `REQ accepted_by AC`; link requirements/NFRs to applicable design/decisions,
  verification plans, and success/failure signals or explicit exceptions.

### Engineering

- Give every `TASK` a `REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS` origin.
- Record expected code/test surfaces while planning; replace them with actual paths,
  symbols, contracts, migrations, and tests during implementation.

### Verification

- Map every committed AC/RULE/NFR to accepted tests or approved manual evidence.
- Record stable TEST IDs plus native test paths/names/case URLs and immutable results.
- Audit forward gaps, backward orphans, stale edges, and circular/ambiguous evidence.

### Delivery & Learning

- Link PRs, commits, builds/artifacts, deployments/releases, and applicable
  production signals as distinct evidence.
- Incidents reference affected requirements/NFRs and releases and create durable
  `BUG/TECH/SEC/OPS/REQ/RULE/NFR` follow-ups.

## Change Propagation

When a requirement, rule/invariant, NFR, AC, or governing decision changes:

1. retain its ID only if observable semantics remain compatible;
2. otherwise create a successor and record both replacement directions;
3. mark affected downstream edges `stale` before implementation proceeds;
4. inspect UX, architecture, contracts, tasks, code, tests, rollout, and signals;
5. revalidate or deprecate every affected edge with rationale;
6. update every supported major-version baseline affected by the change.

Never delete released historical edges to improve current coverage.

## Gate Queries

| Gate | Required query outcome |
|---|---|
| Change Ready | Committed `REQ/RULE/NFR` has owner, version, capability parent, AC/validation, and no affected blocker |
| Slice Ready | Every task has a valid origin and planned verification/recovery evidence |
| Merge Ready | Actual code/test/PR edges are resolvable; no unexplained stale or blocked affected edge |
| Release Ready | PR→build→release evidence, accepted verification, compatibility, and approvals are pinned |
| Learning Closed | Critical released intent has signals or exception; incidents/temporary mechanisms have dispositions |

Exceptions record artifact/edge, rationale, risk, alternative evidence, approver,
owner, and review/expiry. Coverage percentages are diagnostic; circular or weak
evidence does not pass a gate.
