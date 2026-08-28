# Domain Review Prompts

Read only the sections touched by the current change. These are questions that
surface consequential gaps, not framework, aesthetic, or architecture mandates.

## Product and UX

- Which user/operator problem, actors, permissions, states, rules, and non-goals change?
- Which existing design-system patterns and platform conventions apply?
- Are normal, empty, partial/loading, denied/error, interruption, and recovery
  states relevant, and which evidence is sufficient for each?
- What outcome and failure signals distinguish success from mere feature usage?

## Web Client

- Where does state live, and can URL/server/client/form state diverge or become stale?
- Which rendering, caching, hydration, offline, localization, and compatibility
  constraints follow from requirements and the existing framework?
- What are the adopted accessibility and performance targets, measurement method,
  supported browsers/devices, and regression surfaces?
- Which data or secrets must never reach the client, logs, analytics, or storage?

## Mobile Client

- What must work with weak/no connectivity, background suspension, process death,
  clock drift, and delayed upgrade? Do not assume full offline support without a requirement.
- How do platform permissions, deep links, notifications, local data, sync conflicts,
  app-store rollout, and old-client compatibility affect the change?
- Which real-device evidence is needed for performance, accessibility, lifecycle,
  and platform integration?

## Desktop Client

- Which operating systems/versions, packaging/signing, update channels, permissions,
  file/protocol handlers, multi-window behavior, and recovery are in scope?
- What resource/startup targets are measured requirements rather than generic ideals?
- How are auto-update compatibility, rollback, local data, and system integration tested?

## Backend and Integrations

- Which trust boundaries, identities, authorization decisions, tenants, and audit
  requirements apply at every entry point?
- What are the consistency, concurrency, idempotency, retry, cancellation, timeout,
  partial-success, rate/capacity, and backpressure contracts?
- Which consumers, schemas, stored formats, and mixed versions must coexist?
- Which unit, contract, integration, failure, and load evidence best covers the risk?

## Data

- Who owns each dataset and which readers/writers depend on it?
- What are creation, validation, correction, retention, archival, deletion, privacy,
  audit, backup/restore, and reconciliation requirements?
- Which query/access patterns justify indexes or denormalization with measured evidence?
- How will expand/migrate/switch/contract stages handle partial progress and recovery?

## Architecture

- Does the existing boundary/dependency direction support the change?
- What decision is durable enough to need an ADR, and what would reverse it?
- Which synchronous/asynchronous interaction and failure isolation follow from actual
  latency, consistency, ownership, and availability needs?
- Can structural rules be enforced through tests/lint instead of recurring prose review?

## Delivery and Operations

- What environment and artifact provenance are sufficient to reproduce and verify the change?
- Which rollout cohort/order, compatibility window, recovery mechanism, and abort
  thresholds follow from the risk and platform?
- Which infrastructure, application, business, audit/security, and UX signals map to
  committed requirements/NFRs and failure hypotheses?
- Which temporary flag, adapter, migration state, or mitigation needs an owner and removal date?
