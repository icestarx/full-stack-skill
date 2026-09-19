# Delivery & Learning Track

Read when environment, compatibility, release, production, incident, or learning
work applies. External deploy/merge/notification actions still require the user's
scope and authorization.

## A8 — Environment and Delivery Readiness

- Identify the minimum reproducible environment required for the current slice:
  local, ephemeral preview, shared integration, staging, hardware lab, or other.
- Define data setup/reset, secrets, permissions, dependencies, build provenance, and
  smoke/health evidence.
- Add CI/CD or a shared staging environment only when the repository and risk require
  it; do not block coding on unrelated infrastructure.

Evidence: commands/configuration and a reachable verification environment, or a
recorded limitation with risk decision.

Capability: `delivery.environment`.

## A13 — Release and Recovery

- Pin version baseline/source revision, included changes/origins, PR/commits, build
  inputs/artifact digest, test/approval evidence, and intended cohort/environment.
- Select deployment order and cohort increments from compatibility, migration,
  traffic, data, and rollback/roll-forward characteristics. Avoid universal
  percentages or observation durations.
- Define abort thresholds, operator/automation authority, feature-flag lifecycle,
  migration cleanup, communication, and recovery verification.

Evidence: immutable release record and successful risk-appropriate health checks.

Capabilities: `delivery.deploy` for the authorized rollout and `delivery.recover`
for the tested rollback, roll-forward, containment, or stop path.

## A14 — Observation

- Observe infrastructure, application, business, audit/security, and user-experience
  signals that correspond to committed requirements/NFRs and failure modes.
- Use an observation window justified by traffic, batch cycles, delayed effects, and
  risk. Absence of alerts alone is not success.
- Record cohort, baseline, expected range, actual result, and decision threshold.

Evidence: production/target-environment signals and release decision.

## A15 — Learning and Anti-Entropy

- Review escaped defects, incidents, manual retesting, delivery friction, stale docs,
  temporary flags/adapters, and repeated agent mistakes.
- Convert reusable learning into requirements, regression tests, lint/structural
  checks, architecture rules, runbooks, or owned `BUG/TECH/SEC/OPS/REQ/RULE/NFR` work.
- Assign removal/review conditions to temporary compatibility mechanisms.

Evidence: closed or owned follow-ups and synchronized baseline/runbooks.

## Delivery & Learning Gate Checks

- Delivery evidence is immutable enough to reconstruct what reached each cohort.
- Compatibility and data recovery match the actual deployment order.
- Signals test success and failure hypotheses for critical behavior.
- Cleanup and follow-up work has an owner and review/expiry condition.
