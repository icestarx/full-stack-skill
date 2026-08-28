# Requirements Workflow

Read this reference for Product activity A1. It defines how to create, review, or change
requirements without inventing missing product decisions.

## Operating Principles

- Read existing product and repository sources before asking questions or drafting.
- Treat confirmed source material as evidence; expose conflicts instead of silently choosing.
- Ask only questions that remove a material ambiguity. Group related questions and
  distinguish blocking answers from assumptions that can be reviewed later.
- Describe product behavior and constraints. Keep solution design in later technical documents.
- Make scope, exclusions, unhappy paths, and unknowns as explicit as the happy path.
- Use stable requirement IDs once an item enters committed scope. Later delivery
  artifacts may reference these IDs without depending on document headings.
- Select the major-version baseline using `references/document-organization.md` and maintain
  requirement/acceptance links using `references/traceability.md`.

## Select a Mode

These are requirement-document operations nested inside the lifecycle modes from
`references/operating-modes.md`. For example, a Feature Change normally uses requirement
Change mode; a Bug Fix uses Review or Change only when the expected contract is
missing or must change.

| Mode | Use when | Primary output |
|---|---|---|
| **New** | A product or feature has no reliable PRD | Confirmed product brief plus PRD |
| **Review** | A PRD exists and the user wants gaps or risks identified | Findings plus an optional revised PRD |
| **Change** | Existing behavior or requirements must be extended, modified, or retired | Delta-oriented PRD and impact analysis |

Do not force a new-product interview onto a well-documented change. Do not rewrite
an existing PRD when the user asked only for review.

## 1. Inventory Current Truth

Inspect sources the user provided and relevant repository material. Depending on
the task, this can include existing PRDs, decision records, routes, screens,
components, APIs, schemas, permission rules, analytics, tests, incidents, and
support feedback.

Summarize:

- confirmed facts and their sources;
- current behavior for an existing product;
- conflicting statements that require a decision;
- assumptions and their confidence;
- unanswered questions and who can answer them.

If the relevant product or repository context is unavailable, state the limitation
before making detailed claims.

## 2. Confirm the Product Brief

Before expanding detailed requirements, establish:

- target user and job or problem;
- evidence that the problem matters;
- desired user and business outcomes;
- current alternatives and meaningful differentiation;
- product surface and operating constraints;
- goals, non-goals, and MVP boundary;
- approver and intended release context.

For uncertain new products, present this as a short concept brief and obtain
directional confirmation. A separate concept file is optional: use it when risk,
stakeholder count, or ambiguity justifies an explicit gate.

## 3. Build the Scope and Coverage Model

Create a capability tree before writing prose for individual features:

- **Module**: a cohesive product or business area;
- **Function**: a user- or system-visible capability within the module;
- **Subfunction**: the smallest independently scoped behavior worth accepting.

Give every tree node a stable capability ID and every committed leaf a requirement
ID such as `REQ-AUTH-001`. Link requirements back to their leaf capability. Review
the tree top-down to catch missing branches and bottom-up to catch orphan or
duplicate requirements. For an API, platform, or internal system, name capabilities
by business outcome rather than forcing a screen-oriented hierarchy.

After the tree is complete, create the scope inventory. Record priority, rationale,
dependencies, and—when changing an existing product—whether an item is added,
modified, removed, or unchanged.

For every P0 requirement, evaluate the applicable coverage dimensions:

| Dimension | Questions to resolve |
|---|---|
| Actors | Which roles, permissions, account states, tenants, or regions differ? |
| Preconditions | What must exist or be true before the behavior starts? |
| Flow | Entry, happy path, cancellation, interruption, retry, recovery, and exit |
| Business states | Durable states, allowed and invalid transitions, guards, terminal states, side effects |
| UI states | Initial, empty, loading, partial, success, error, stale, offline, denied |
| Domain rules/invariants | Ordering, limits, calculations, ownership, constraints that must always hold, violation behavior |
| Data | Source, required fields, validation, defaults, retention, deletion, sensitivity |
| Operational semantics | Concurrency, idempotency, cancellation, retry/resume, partial success, permission changes |
| Dependencies | APIs, third parties, policies, operations, feature flags, other requirements |
| Quality | Performance, availability, accessibility, compatibility, localization, security |
| Observability | Success/failure signals, analytics, audit events, support diagnostics |
| Delivery | Migration, backward compatibility, rollout, rollback, and regression scope |

Mark a dimension `N/A` with a reason rather than silently omitting it.

### State Machines

Define a business state machine for any entity, workflow, or asynchronous process
with more than one meaningful state. List states separately from transitions. Each
transition must identify source state, event, actor, guard/precondition, destination
state, observable side effects, and failure behavior. Identify terminal states and
the response to invalid or repeated transitions. UI loading/error states do not
replace the business state machine.

### Operational Semantics

For every applicable state-changing, asynchronous, batch, or external operation,
define the product contract for:

- competing operations on the same target and the conflict policy;
- idempotency identity, scope, validity window, and replay result;
- cancellation before and after the commit point, including compensation;
- retry and resume behavior after timeout, disconnect, or partial completion;
- partial-success reporting for multi-item work;
- permission re-evaluation when access changes after an operation starts.

State `N/A` with a reason for genuinely stateless/read-only behavior. Add acceptance
criteria for the selected semantics instead of leaving them as implementation notes.

## 4. Write Testable Requirements

Separate the user-visible contract from implementation suggestions. Each detailed
requirement should contain its rationale, actors and preconditions, behavior,
business rules, relevant data constraints, edge cases, and acceptance criteria.

Give consequential cross-cutting domain rules and invariants stable `RULE-*` IDs.
State what the rule protects, where it applies, when it may be temporarily violated
(if ever), and the reject/repair/audit behavior on violation. Link each rule to its
affected requirements and verification evidence rather than duplicating prose.

Use Given/When/Then when sequence or state matters. Include at least one negative
or recovery criterion when failure is plausible. Avoid subjective terms such as
"fast", "intuitive", or "secure" unless accompanied by a measurable target or
an explicit validation method.

Unknowns must be recorded as one of:

- **Blocking**: development or acceptance cannot begin until resolved;
- **Assumption**: work may proceed using the stated default and risk;
- **Follow-up**: intentionally deferred outside the current scope.

Give blocking questions an owner and decision date when those are known. The
affected slice remains blocked until the question is resolved or deliberately
reclassified as an approved assumption with explicit risk.

## 5. Apply Mode-Specific Review

### Review Mode

Classify findings as blocker, major, or minor. Review for:

- completeness of scope, states, rules, and quality attributes;
- internal consistency across flows, feature inventory, and detailed requirements;
- testability and measurable acceptance;
- explicit non-goals and absence of hidden scope;
- feasibility risks and unresolved dependencies;
- readiness for downstream implementation linkage.

Report findings first. Modify the source only when the user asked for improvement.
Use a compact findings table with: finding ID, severity, affected requirement IDs,
evidence, delivery or user risk, recommended correction, and decision status. If
the lifecycle will continue, the reviewed and accepted PRD—not the review report—
remains the Product-track source of truth.

### Change Mode

Identify the baseline behavior and express the requested delta. Preserve unchanged
behavior by reference instead of restating the entire previous PRD. Analyze impact
across UI, API, data, permissions, analytics/audit, tests, operations, rollout, and
backward compatibility. Surface conflicts for a decision; do not silently overwrite
prior requirements.

This mode defines requirement content, not the repository's version-directory
layout. Follow the project's documentation convention until an iteration strategy
is explicitly chosen.

When a versioning strategy exists, update every affected supported baseline and
mark downstream traceability edges stale until they are revalidated.

## Definition of Ready

Change Ready passes for the affected product scope only when:

- the target user, problem, evidence, goals, and non-goals are explicit;
- the version line/baseline is selected and committed REQ/AC items are indexed in
  the traceability ledger or configured ALM system;
- the capability tree covers modules, functions, and applicable subfunctions, and
  every P0 leaf maps to a detailed requirement without orphan requirements;
- every P0 requirement has a stable ID and testable acceptance criteria;
- applicable actors, domain rules/invariants, violation behavior, data constraints,
  and edge cases are covered;
- affected data defines ownership/source, creation/correction, retention/archive/deletion,
  access/sensitivity, audit, restore/export, and support diagnostics as applicable;
- stateful entities and workflows define states, transitions, guards, terminal and invalid behavior;
- applicable operations define concurrency, idempotency, cancellation, recovery,
  partial-success, and permission-change semantics;
- measurable quality requirements are present or explicitly marked `N/A`;
- existing-product changes include baseline and impact analysis;
- no unresolved contradiction remains hidden;
- no unresolved blocking question affects the slice; ownership alone is insufficient;
- assumptions, risks, approver, and approval status are recorded.

Passing this gate means the requirement is ready for the affected design and engineering work,
not that implementation details have already been chosen.
