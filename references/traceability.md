# End-to-End Traceability

Read this reference before creating lifecycle documents and again at planning,
review, release, and retrospective gates. Traceability is a maintained evidence
graph, not a one-time matrix appended after development.

## Trace Model

The required forward chain is:

```text
CAP → REQ → AC → design/decision → TASK → code → TEST → PR/build → release → OBS
```

The chain must also work backward: a production signal, test, code change, or PR
must identify the requirement or explicitly classified non-product work that
justified it.

## Stable Identifiers

Use immutable IDs for logical artifacts:

| Prefix | Artifact |
|---|---|
| `CAP-*` | Module, function, or subfunction capability |
| `REQ-*` | Functional or quality requirement |
| `AC-*` | Acceptance criterion |
| `PDR-*` / `ADR-*` | Product or architecture decision |
| `CHG-*` | Active change work item that coordinates track state and evidence |
| `TASK-*` | Planned implementation or verification work |
| `TEST-*` | Stable test scenario or test-case record |
| `BUG-*`, `TECH-*`, `SEC-*`, `OPS-*` | Valid non-feature work origins |

Keep native identifiers for physical evidence: repository paths and symbols, PR
numbers, commit SHAs, build/artifact IDs, release tags, feature flags, dashboards,
metrics, logs, traces, and alerts. Do not invent `CODE-*` IDs or add requirement
comments throughout source files. Prefer `path:symbol` because line numbers drift.

Never reuse an ID. If semantics change after release, create a new ID and connect
it with `supersedes` / `superseded_by`.

`CHG-*` is a container, not a substitute origin. Its slices and tasks still point
to a valid `REQ/AC/BUG/TECH/SEC/OPS` reason for the work.

## Relationship Ledger

Maintain a normalized link ledger rather than one increasingly wide row per
requirement. Use the project's issue tracker or ALM system when it already provides
durable bidirectional links; otherwise use a repository-local ledger based on
`references/templates/traceability-ledger.md`.

For medium/large projects, keep the canonical edges in structured tracker fields or
a machine-readable companion and validate required relationships in CI. A manually
maintained Markdown-only ledger is a lean fallback for small projects, not the
preferred large-project control plane. Do not parse arbitrary prose to infer gates.

Supported relationships include:

| Relationship | Meaning |
|---|---|
| `contains` | Parent capability contains a child capability or requirement |
| `accepted_by` | Requirement defines acceptable behavior through an AC |
| `verified_by` | AC/requirement is verified by a test or approved review artifact |
| `constrained_by` | Requirement or implementation is governed by a decision/contract |
| `planned_by` | Requirement/AC/non-product origin is covered by a task |
| `implemented_by` | Task or requirement maps to code path and symbol |
| `delivered_by` | Work is included in a PR, build, or release |
| `observed_by` | Released behavior has a production signal or audit evidence |
| `supersedes` | A new artifact replaces an older semantic contract |
| `blocks` | An unresolved artifact prevents downstream readiness |

Each edge records source, relationship, target, version line, status, evidence,
owner, and last verification. Allowed statuses are `planned`, `valid`, `stale`,
`blocked`, and `deprecated`. A link without resolvable evidence is not `valid`.

## Stage Responsibilities

### Requirements and Design

- Create `CAP`, `REQ`, and `AC` IDs in the approved baseline.
- Link `REQ accepted_by AC`; link `AC verified_by TEST` or approved evidence.
- Map every committed requirement to applicable UX flows/states, design sections,
  PDR/ADR decisions, API/data contracts, or an explicit `N/A` exception.
- A shared design or contract may satisfy several requirements; link each one.

### Planning and Implementation

- Keep the active four-track state in one `CHG-*` work item or equivalent tracker
  record; do not duplicate authoritative PRD, design, or test contents there.
- Every task must have at least one source ID: `REQ/AC`, `BUG`, `TECH`, `SEC`, or `OPS`.
- Record expected code and test surfaces during planning; replace expectations with
  actual `path:symbol` and `TEST-*` evidence during implementation.
- Shared foundation tasks list every known consumer or a documented cross-cutting origin.
- Do not rely on branch names or commit messages as the only durable link.

### Tests and Review

- Every committed AC maps to at least one test or explicitly approved manual evidence.
- Tests use a stable test ID plus the framework's test path/name or case-system URL.
- Review checks forward coverage, backward orphans, stale links, and whether changed
  behavior updated its source requirement rather than only downstream artifacts.

### PR and Release

Behavior-changing PRs include affected IDs, code surfaces, test evidence, migration
or compatibility impact, and ledger updates. Use native tracker-closing syntax only
when the repository supports it; IDs remain portable.

Before release, the manifest pins all committed requirements to accepted tests,
PRs/commits, build artifacts, deployment evidence, and applicable production
signals. A release note is not verification evidence by itself.

### Operations and Learning

Map critical released requirements to success/failure metrics, logs, traces, audit
events, alerts, or a justified `N/A`. Incidents and retrospectives reference the
affected release and requirement IDs and may create new `BUG/TECH/OPS/REQ` origins.

## Change Propagation

When a requirement, AC, or governing decision changes:

1. retain the original ID only if its observable semantics remain compatible;
2. otherwise create a successor and record `supersedes`;
3. mark affected downstream edges `stale` before implementation proceeds;
4. inspect UX, architecture, contracts, tasks, code, tests, rollout, and observability;
5. revalidate each edge or deprecate it with rationale;
6. update every supported major-version baseline affected by the change.

Never delete historical released edges merely to make current coverage look clean.

## Quality Gates

| Gate | Required evidence |
|---|---|
| Requirements ready | Committed `REQ` items have `AC`, owner, version line, and capability parent |
| Design ready | Each committed `REQ/AC` maps to UX/design/decision/contracts or approved `N/A` |
| Development ready | Tasks are dependency-ordered and every task has a valid origin ID |
| PR ready | Changed IDs, actual code surfaces, tests, and ledger delta are present |
| Release ready | No committed requirement has missing, stale, or blocked implementation/test/release edges |
| Operability ready | Critical released behavior maps to signals/runbooks or approved `N/A` |

Current-release committed scope requires the complete chain. Future/deferred
capabilities need only their capability and requirement definition until admitted
to a release. Exceptions record owner, rationale, risk, expiry/review date, and
alternative evidence.

## Coverage Views

Report at least:

- committed requirements and acceptance criteria totals;
- design, task, code, test, PR/build, release, and observability coverage;
- orphan tasks/tests and behavior-changing PRs without origins;
- `stale`, `blocked`, deprecated, and excepted edges;
- released requirements without accepted verification evidence.

Coverage percentages are diagnostic. A nominal 100% with weak or circular evidence
does not pass a gate.
