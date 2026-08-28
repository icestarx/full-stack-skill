# Verification Track

Read when defining acceptance evidence, reviewing a slice/PR, or deciding merge and
release readiness. Deterministic project checks take precedence over agent opinion.

## Verification Design

- Map each committed `AC/RULE/NFR` or non-product invariant to the cheapest effective
  evidence layer: static/type/lint, unit/component, contract, integration, E2E,
  migration/compatibility, security/privacy, accessibility, performance, manual UAT,
  or production signal.
- Cover applicable positive, negative, boundary, permission, concurrency,
  cancellation, recovery, and version-skew behavior.
- Use coverage metrics as diagnostic signals. Set targets from repository policy and
  changed-risk analysis; do not substitute a universal percentage for behavior.

## A10 — Review

- Review the actual diff, affected contracts, origins, failure modes, and evidence.
- Apply project rules rather than universal function/file-size or framework rules.
- Use independent context for high-risk/hard-to-reverse changes when available and
  authorized. Trigger specialist security, accessibility, performance, or database
  review only when requested or risk-relevant.
- Classify findings by user/system impact and provide resolvable evidence.

Evidence: findings and resolutions; no unresolved release-blocking issue.

## A11 — PR Evidence

For behavior-changing PRs, record:

- origin and affected `REQ/AC/RULE/NFR/TASK/BUG/TECH/SEC/OPS` IDs;
- actual code/contracts/migrations;
- commands, stable TEST IDs, artifacts, and material screenshots;
- compatibility, data, security, rollout, and recovery impact;
- baseline, decision, change-state, and trace-ledger delta.

Use repository PR conventions and approval rules. Do not require a PR or external
mutation when the user's requested workflow stops before that action.

## A12 — Verification Summary

- Index generated CI/test artifacts rather than copying logs into prose.
- Report accepted, failed, blocked, stale, excepted, and not-applicable evidence.
- Identify uncovered acceptance, orphan tests/tasks, and validation not performed.
- A manual assertion requires approver, rationale, risk, and follow-up/expiry when it
  substitutes for expected deterministic evidence.

Evidence: slice/PR verification record or equivalent tracker/CI result.

## Verification Track Gate Checks

- Every committed behavior/invariant has accepted evidence or approved exception.
- A defect fix has regression evidence where practical.
- Checks cover the changed regression surface, not merely new lines.
- Test, code, PR, build, and release links are distinct, resolvable, and non-circular.
