# Four-Track Capability Mapping

This file maps outcomes to portable capability IDs. Read `references/platform-adapters.md`
before selecting a concrete skill, tool, command, or agent.

## Selection Rules

1. Preserve user-selected providers and repository conventions.
2. Use deterministic project tools for build, test, lint, migration, and state checks.
3. Select the smallest provider set that produces the required evidence.
4. Trigger specialist review from user request or actual risk, not merely because a
   technology appears in the change.
5. Use independent context for consequential review when available and authorized.
6. Fall back to the main agent instead of blocking on a missing optional provider.

## Track Mapping

| Track | Core capabilities | Conditional capabilities |
|---|---|---|
| Product | `product.discovery`, `product.scope-review`, `product.requirements-review` | `design.system`, `design.prototype`, `design.review` for affected UX |
| Engineering | `architecture.review`, `planning.decompose`, `development.tdd` | `database.review`, `spec.change`, domain specialist |
| Verification | Deterministic project commands, `review.code` | `qa.browser`, `review.accessibility`, `review.security`, `review.performance` |
| Delivery & Learning | `delivery.release`, `operations.monitor`, `operations.retro` | `database.review`, platform/incident specialist |

## Activity Mapping

| Activity | Required outcome | Typical capabilities |
|---|---|---|
| A1 Requirements | Source-grounded baseline/delta with ready acceptance | `product.discovery`, `product.requirements-review` |
| A2 UX contract | Affected interaction/state evidence | `design.system`, optionally prototype/review |
| A3 Product decision | Linked decision/approval where material | `product.scope-review`, `design.review` |
| A4 Reconnaissance/decisions | Repository-grounded impact and durable decisions | `architecture.review`, optionally specialist |
| A5 Boundaries | Consumer/module/dependency map | `architecture.review` |
| A6 Slice plan | Bounded dependency-ordered tasks with origins/evidence | `planning.decompose` |
| A7 Contracts/data | Executable contracts and compatibility/recovery | `architecture.review`, `database.review`, optionally `spec.change` |
| A8 Environment | Reproducible risk-appropriate verification target | `delivery.release`, project tools |
| A9 Implementation | Integrated slice with actual code/test links | `development.tdd`, project tools |
| A10 Review | Impact-ranked independent findings | `review.code`, risk-triggered specialists |
| A11 PR evidence | Contextual review unit with trace/evidence delta | `delivery.release` |
| A12 Summary | Accepted/gapped/excepted verification index | deterministic commands, risk-triggered reviewers |
| A13 Release | Immutable artifact/deployment/recovery evidence | `delivery.release` |
| A14 Observation | Requirement-linked production/target signals | `operations.monitor` |
| A15 Learning | Owned improvements and anti-entropy updates | `operations.retro` |

## Degraded Operation

Missing providers reduce automation, not required outcomes. Record the fallback and
evidence not collected. Stop when proceeding would be unsafe or materially
incomplete—for example, a private system is inaccessible, an irreversible action
lacks authority, or required verification cannot run.
