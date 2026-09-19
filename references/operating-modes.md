# Operating Mode Playbooks

Read only the selected mode after initial routing. Every mode uses the four-track
state and gates from `references/four-track-model.md`; these playbooks define the minimum route,
not a fixed sequence or permission to perform external actions.

## New Product or Major Version

Use when no reliable product/system baseline exists or a major line changes the
product model or architecture substantially.

**A1-A15 route**: Run the complete sequence in order. Keep verification design
active from A1, bring delivery constraints into A4-A8, repeat A6-A12 for each
vertical slice, then complete A13-A15 for the authorized release. Conditional work
inside a step may still be `N/A` with rationale.

- Product: establish product brief, capability tree, committed requirements/NFRs,
  UX behavior, and version manifest.
- Engineering: choose architecture from evidence, identify contracts and vertical
  slices, and establish the minimum runnable foundation needed by the first slice.
- Verification: define acceptance and a representative walking-skeleton check early.
- Delivery & Learning: define environment, compatibility, release, recovery, and
  signals before those decisions become expensive.
- Exit: the baseline is authoritative and released scope has full evidence; future
  capabilities remain explicitly deferred.

## Feature Change

Use for V2/V3 additions, modifications, or removals within an existing product line.

**A1-A15 route**: Start at A1 with a delta against the active baseline. Run A2-A3
only for affected UX or product decisions, then execute applicable A4-A12 for each
slice and A13-A15 when delivery is in scope. Mark preserved evidence and skipped
steps explicitly instead of recreating unaffected documents.

1. Pin current behavior and affected baseline; create the requirement/design delta.
2. Mark impacted downstream trace edges stale.
3. Inspect callers, consumers, data, permissions, tests, rollout, and version skew.
4. Deliver small vertical slices, preserving compatible mixed-version operation
   where the release strategy requires it.
5. Revalidate edges, update the authoritative baseline, and link release evidence.

Do not copy the prior PRD or recreate unaffected lifecycle documents.

## Bug Fix

Use when observed behavior violates a known or newly clarified contract.

**A1-A15 route**: Use A1 to link the `BUG-*` origin and existing contract. Run A2-A3
only when UX evidence or expected behavior is unclear. Use A4 to reproduce and map
the failure, select A5-A8 by blast radius, then run A9-A12. Use A13-A15 in proportion
to the delivery and escaped-defect risk.

1. Create or link a `BUG-*` origin and record affected `REQ/AC/RULE/NFR` when known.
2. Reproduce the defect with deterministic evidence where practical.
3. If expected behavior is ambiguous, block the affected slice until the Product
   track clarifies acceptance; do not infer a new product rule silently.
4. Implement the smallest safe correction and add fail-before/pass-after regression
   evidence at the closest effective test layer.
5. Inspect sibling paths and supported versions for the same failure pattern.
6. Use a proportionate delivery/observation path and feed escaped-defect learning
   into requirements, tests, lint, or runbooks.

## Maintenance

Use for dependency upgrades, refactors, deprecations, infrastructure work, and
technical/security/operational debt without intended product behavior change.

**A1-A15 route**: Use A1 to state the `TECH/SEC/OPS` origin and invariant. A2-A3 are
normally `N/A` unless an interface or product decision changes. Run applicable
A4-A12 for impact, compatibility, implementation, and proof; run A13-A15 only for
the actual delivery and operational learning path.

1. Use a `TECH-*`, `SEC-*`, or `OPS-*` origin and state the invariant that must remain true.
2. Inspect dependents, public contracts, stored formats, generated artifacts, build
   tooling, and rollback/roll-forward constraints.
3. Establish characterization, compatibility, or equivalence evidence before change.
4. Keep migration/adaptation periods bounded with owner and removal condition.
5. Verify the invariant and affected operational behavior; update decisions/runbooks.

If observable semantics change, route the affected part through Feature Change.

## Incident

Use for active production degradation or a security/availability event.

**A1-A15 route**: Authorized reversible containment takes priority over the normal
sequence. Preserve evidence during containment, then create durable origins and
re-enter at A1 or A4 for permanent remediation. The durable fix follows applicable
A1-A15 steps and cannot close before A14-A15 observation and learning are complete.

1. Preserve user authorization and incident command. Mitigate only within granted
   authority; prefer reversible containment over speculative permanent repair.
2. Record timeline, affected release/cohort, signals, evidence locations, actions,
   decision owner, and current user/business impact.
3. Verify mitigation using health and business signals and define escalation or
   stopping thresholds. Do not erase evidence needed for diagnosis or audit.
4. After stabilization, create `BUG/SEC/OPS/TECH` origins for durable remediation,
   add regression/failure evidence, and use the ordinary gates for permanent changes.
5. Close only when runbooks/baselines, follow-ups, temporary mitigations, and
   recurrence-prevention actions have owners and review dates.

An incident mode changes priority and sequencing, not authorization boundaries.
