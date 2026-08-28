# Product Track

Read when the change affects observable behavior, scope, UX, or acceptance. For
requirement mechanics, also read `../requirements-workflow.md`.

## A1 — Requirements and Scope

- Inventory authoritative sources and current behavior before drafting.
- Select New, Review, or Change requirement mode.
- Define capability/requirement/rule/NFR IDs, actors, invariants, states, data lifecycle,
  operational semantics, non-goals, acceptance, and success/failure signals.
- Resolve blockers for the affected slice; an owner alone does not make a blocker ready.
- Update the active version baseline and trace edges, not unaffected documents.

Evidence: approved requirement baseline/delta and Change Ready product evidence.

## A2 — UX and Interaction Contract

Run only when users or operators interact with an affected surface.

- Map applicable `REQ/AC` items to flows, screens/components, content, permissions,
  and normal/empty/loading/error/boundary/interruption/recovery states.
- Reuse the repository's design system. Create or change system decisions only when
  the product requires them.
- Produce the cheapest reviewable evidence: annotated flow, wireframe, existing UI
  delta, runnable preview, or high-fidelity prototype according to uncertainty/risk.

Evidence: affected-state coverage and design/prototype links or justified `N/A`.

## A3 — Product Decision and Acceptance

- Present unresolved product trade-offs with impact and recommendation.
- Obtain human decision when taste, policy, scope, cost, or irreversible product
  behavior cannot be inferred safely.
- Link decisions and approval to affected IDs and record rejected alternatives when
  that knowledge matters later.

Evidence: decision/approval record sufficient for the next slice. A formal demo is
not required for non-visual or already-established behavior.

## Product Track Gate Checks

- Capability coverage exposes deferred and removed behavior.
- Every committed requirement/NFR has measurable acceptance or validation.
- Stateful and asynchronous behavior defines transitions and failure semantics.
- Product semantics changed at the source, not only in downstream implementation.
- No unresolved blocker affects the slice entering work.
