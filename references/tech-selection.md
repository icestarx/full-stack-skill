# Technology Decision Guide

Read only when a material technology choice is actually open. Existing repository
standards, team support, compatibility, and operational constraints outweigh generic
tool popularity. Verify current support/security status in primary documentation;
do not rely on this skill for a timeless product shortlist.

## Decision Inputs

- Required behavior and measurable NFRs
- Existing architecture, languages, deployment, data, and observability
- Team ownership, support horizon, hiring/on-call capability, and migration cost
- Ecosystem maturity, release cadence, security history, licensing, and exit path
- Compatibility with supported clients, stored formats, integrations, and tooling
- Total cost: build, operate, upgrade, debug, recover, and eventually replace

## Selection Process

1. First test whether the existing stack satisfies the requirement.
2. Define knockout constraints and weighted criteria before naming candidates.
3. Verify candidate status and required versions from official sources.
4. Shortlist the smallest credible set; avoid broad comparative research without a
   decision it can change.
5. Run a bounded spike for uncertain, high-impact claims using representative load,
   integration, deployment, debugging, and failure/recovery paths.
6. Record the decision, evidence, alternatives, consequences, owner, and revisit trigger.

## Decision Record

| Criterion | Weight | Existing option | Candidate A | Candidate B | Evidence |
|---|---:|---:|---:|---:|---|
| Functional fit | | | | | |
| Reliability/operability | | | | | |
| Security/compliance | | | | | |
| Compatibility/migration | | | | | |
| Team/maintenance | | | | | |
| Cost/exit path | | | | | |

Scores support judgment; they do not replace knockout constraints or experimental
evidence. Prefer reversible choices when evidence is weak.

## Cross-Platform and Distributed Changes

- Make shared contracts explicit but keep platform-specific UX and lifecycle needs.
- Treat clients that cannot be force-upgraded as independently versioned consumers.
- Define schema/API/event compatibility windows and removal conditions.
- For distributed writes, select idempotency, publication, compensation, and failure
  isolation patterns from actual delivery guarantees rather than pattern fashion.
