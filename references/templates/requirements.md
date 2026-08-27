# Requirements Document Template

Use with `references/requirements-workflow.md`. Keep sections that apply and mark
material omissions `N/A` with a reason. Do not invent unresolved product decisions.

```markdown
# Requirements — [Product / Feature]

> **Status**: Draft / In review / Approved
> **Mode**: New / Review / Change
> **Version line**: [v1 / v2 / ...]
> **Baseline manifest**: [Path or TBD]
> **Traceability ledger**: [Path or tracker URL]
> **Owner**: [Name or role]
> **Approver(s)**: [Name or role]
> **Target release**: [Release, milestone, or TBD]
> **Baseline**: [Existing PRD, release, behavior, or N/A]
> **Last updated**: YYYY-MM-DD

## 1. Product Brief

### 1.1 Problem and Evidence

- **Target user**: [Who]
- **Problem / job**: [What they cannot do effectively]
- **Evidence**: [Research, feedback, data, incident, or stated hypothesis]
- **Current alternative**: [How the problem is handled today]
- **Why now**: [Trigger or opportunity]

### 1.2 Intended Outcomes

| Outcome | Baseline | Target | Measurement window |
|---|---:|---:|---|
| [User or business outcome] | | | |

### 1.3 Product Surface and Constraints

- **Surface**: [Web, mobile, API, admin, integration, etc.]
- **Known constraints**: [Policy, platform, budget, schedule, technology, operations]
- **Source-of-truth inputs**: [Links or repository paths]

## 2. Goals, Non-Goals, and Assumptions

### Goals

- G-01: [Outcome this release must achieve]

### Non-Goals

- NG-01: [Explicit exclusion and reason]

### Assumptions

| ID | Assumption | Confidence | Risk if false | Validation / owner |
|---|---|---|---|---|
| ASM-001 | | High / Medium / Low | | |

## 3. Users, Roles, and Permissions

| Actor / role | Need | Allowed actions | Restrictions / account states |
|---|---|---|---|
| | | | |

## 4. Capability Tree and Scope Inventory

### 4.1 Capability Tree

Use stable capability IDs. Expand every in-scope module through function and
applicable subfunction leaves.

~~~text
CAP-[DOMAIN] — [Module]
├── CAP-[DOMAIN]-01 — [Function]
│   ├── REQ-[DOMAIN]-001 — [P0 subfunction / behavior]
│   └── REQ-[DOMAIN]-002 — [P1 subfunction / behavior]
└── CAP-[DOMAIN]-02 — [Function]
    └── REQ-[DOMAIN]-003 — [Subfunction / behavior]
~~~

Tree review:

- [ ] Every committed module has its expected functional branches.
- [ ] Every P0 leaf links to exactly one detailed requirement or an identified shared requirement.
- [ ] No detailed requirement is orphaned from the tree.
- [ ] Deferred branches remain visible as P1/P2 or explicit non-goals.

### 4.2 Scope Inventory

Use stable IDs. For Change mode, set delta to Added, Modified, Removed, or
Unchanged-by-reference.

| Capability / requirement ID | Parent capability | Priority | Delta | Summary | Rationale | Dependencies |
|---|---|---|---|---|---|---|
| REQ-[AREA]-001 | CAP-[AREA]-01 | P0 / P1 / P2 | | | | |

## 5. User Flows and State Coverage

### 5.1 Primary Flow

[Numbered steps or Mermaid diagram, including important decision points.]

### 5.2 Alternate and Recovery Flows

- [Cancellation, interruption, retry, timeout, conflict, or recovery path]

### 5.3 Business State Machines

Complete for every stateful entity, workflow, or asynchronous process. Do not use
UI loading states as a substitute.

#### State Catalog

| Entity / workflow | State | Meaning | Allowed actions | Terminal? |
|---|---|---|---|---|
| | | | | Yes / No |

#### Transition Table

| Transition ID | From | Event | Actor | Guard / precondition | To | Side effects | Invalid / repeated behavior |
|---|---|---|---|---|---|---|---|
| TR-[AREA]-001 | | | | | | | |

### 5.4 UI State Matrix

| Requirement ID | Actor / precondition | Initial / empty | Loading / partial | Success | Error / denied | Recovery |
|---|---|---|---|---|---|---|
| | | | | | | |

## 6. Operational Semantics

Complete for state-changing, asynchronous, batch, or external operations. Mark
individual fields `N/A` with a reason when they do not apply.

| Requirement / operation | Concurrency and conflict policy | Idempotency identity, scope, window, replay result | Cancellation and commit point | Retry / resume / recovery | Partial success | Permission changes during execution |
|---|---|---|---|---|---|---|
| REQ-[AREA]-001 / [operation] | | | | | | |

## 7. Detailed Requirements

### REQ-[AREA]-001 — [Requirement Name]

- **Priority**: P0 / P1 / P2
- **Rationale**: [User or business value]
- **Actors and preconditions**: [Who, permissions, prior state]
- **Trigger**: [Event or user action]
- **User-visible behavior**: [Observable product contract]
- **Business rules**: [Limits, ordering, calculations, ownership, conflicts]
- **Data contract**: [Inputs, outputs, source, validation, defaults, retention]
- **Dependencies**: [Other requirements, policies, services, operations]

#### Edge Cases

| Condition | Expected behavior | Recovery / support path |
|---|---|---|
| Empty, invalid, duplicate, oversized, stale, concurrent, offline, timeout, denied | | |

#### Acceptance Criteria

- AC-[AREA]-001 — Given [precondition], when [action], then [observable result].
- AC-[AREA]-002 — Given [failure or boundary], when [action], then [safe result and recovery].

#### Observability

- **Success signal**: [Metric, event, log, audit record, or N/A]
- **Failure signal**: [Metric, event, log, support diagnostic, or N/A]

## 8. Non-Functional Requirements

| ID | Category | Requirement and measurable target | Validation method | Applies to |
|---|---|---|---|---|
| NFR-001 | Performance / Availability / Security / Privacy / Accessibility / Compatibility / Localization / Capacity | | | |

## 9. Change Impact Analysis

Complete for Change mode; otherwise mark N/A.

| Area | Current behavior | Required change | Compatibility / regression risk |
|---|---|---|---|
| UI and content | | | |
| API and integrations | | | |
| Data and migration | | | |
| Roles and permissions | | | |
| Analytics and audit | | | |
| Tests and operations | | | |

## 10. Delivery Constraints

- **Rollout / feature flags**: [Required behavior or N/A]
- **Migration / backward compatibility**: [Requirement or N/A]
- **Rollback expectations**: [User/data behavior on rollback]
- **Support and communication**: [Training, release note, support impact, or N/A]

## 11. Risks, Questions, and Decisions

### Risks

| Risk | Likelihood / impact | Mitigation | Owner |
|---|---|---|---|
| | | | |

### Open Questions

| ID | Question | Blocking / Assumption / Follow-up | Impact | Owner / decision date |
|---|---|---|---|---|
| Q-001 | | | | |

### Decision Log

| Date | Decision | Rationale | Decider | Affected IDs |
|---|---|---|---|---|
| | | | | |

## 12. Definition of Ready

- [ ] Goals and non-goals are explicit.
- [ ] Capability tree covers modules, functions, and applicable subfunctions.
- [ ] Every P0 leaf maps to a detailed requirement; no detailed requirement is orphaned.
- [ ] Every P0 requirement has a stable ID and acceptance criteria.
- [ ] Applicable actors, rules, data constraints, and edge cases are covered.
- [ ] Stateful behavior has a transition table including guards, terminal states, and invalid transitions.
- [ ] Applicable operations define concurrency, idempotency, cancellation, recovery, partial success, and permission-change behavior.
- [ ] Non-functional targets are measurable or marked N/A with a reason.
- [ ] Change mode includes baseline and cross-layer impact analysis.
- [ ] Blocking questions and conflicting sources are resolved or assigned.
- [ ] Approver and approval status are recorded.
```
