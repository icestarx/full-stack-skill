# Engineering Track

Read for repository impact analysis, architecture/contracts, planning, implementation,
or migration work. Select only the activities required by the current slice.

## A4 — Repository Reconnaissance and Technical Decisions

- Inspect repository instructions, current architecture, dependency/call paths,
  similar implementations, contracts, tests, and relevant decision/change history.
- Identify affected consumers, stored formats, permissions, operational boundaries,
  and unknowns before choosing a solution.
- Record an ADR only for a consequential or durable choice; prefer existing
  conventions when they satisfy the change.

Evidence: impact map, material decisions, and affected `REQ/AC/RULE/NFR` links.

## A5 — Boundaries and Dependency Map

- Define or confirm business/domain ownership, public interfaces, data ownership,
  and dependency direction.
- Identify independently mergeable vertical slices and shared foundation work.
- Avoid circular dependencies; do not force a particular folder/layer structure on
  an established repository.

Evidence: affected module/consumer map and slice dependencies.

## A6 — Slice Plan

- Give each task a stable `TASK-*` ID and valid `REQ/AC/RULE/NFR/BUG/TECH/SEC/OPS` origin.
- Include outcome, affected surfaces, dependencies, planned verification, recovery,
  owner/status, and a size that one agent/team can complete and verify coherently.
- Prefer small mergeable batches. Do not impose universal hour/day estimates or
  milestone dates without project planning inputs.

Evidence: dependency-ordered slices in the change record or project tracker.

## A7 — Data and Interface Contracts

Run for affected persistence, API, event, file, integration, or client contracts.

- Define current/delta schema, validation, errors, authorization, concurrency,
  idempotency, consumers, compatibility window, observability, and contract tests.
- For data changes, plan expand/migrate/switch/contract or another repository-safe
  sequence. Define backup, rollback or roll-forward, verification, and cleanup.
- Generate specifications from code when that is the repository's source of truth;
  do not create competing hand-maintained documentation.

Evidence: executable/authoritative contracts and compatibility/recovery plan.

## A9 — Implementation and Integration

- Choose contract-first, backend-first, frontend-with-fake, migration-first, or
  another sequence from the slice dependencies and risk.
- Establish fail-before or characterization evidence where practical, implement the
  smallest coherent change, and integrate against real boundaries early.
- Use project-native style and commands. Replace planned links with actual paths,
  symbols, migrations, contracts, and commits/PRs.

Evidence: mergeable implementation plus focused deterministic results.

## Engineering Track Gate Checks

- The plan is repository-grounded and no material consumer is silently omitted.
- Each slice is independently verifiable and recoverable.
- Compatibility and migration strategy covers in-flight versions where applicable.
- Actual implementation evidence replaces plans before Merge Ready.
