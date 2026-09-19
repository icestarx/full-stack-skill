# A1-A15 Capability Mapping

This file maps every workflow step to portable capability IDs. Read
`references/platform-adapters.md` before selecting a concrete skill, tool, command,
or agent. Capability IDs specify required outcomes; provider names are replaceable
implementations discovered from the active host.

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
| Verification | Deterministic project commands, `review.code`, `verification.completion` | `qa.browser`, `review.accessibility`, `review.security`, `review.performance` |
| Delivery & Learning | `delivery.environment`, `delivery.change-review`, `delivery.deploy`, `delivery.recover`, `operations.monitor`, `operations.retro` | `database.review`, platform/incident specialist |

## A1-A15 Workflow Mapping

| Step | Required outcome | Core capabilities | Conditional capabilities / fallback |
|---|---|---|---|
| A1 Requirements and scope | Source-grounded baseline/delta, origins, and testable acceptance | `product.discovery`, `product.requirements-review` | `product.scope-review`; main-agent requirements workflow for missing providers |
| A2 UX contract | Affected flows, responsive behavior, and interaction-state evidence | `design.system` | `design.prototype`; repository design system and direct UI specification |
| A3 Product acceptance | Linked scope/design decision and approval where material | `product.scope-review`, `design.review` | `design.prototype`; structured human decision record |
| A4 Reconnaissance/decisions | Repository-grounded impact and durable technical decisions | `architecture.review` | Technology/domain specialist; repository inspection and focused decision record |
| A5 Boundaries | Consumer, module, ownership, and dependency map | `architecture.review` | Main-agent dependency analysis from code/contracts |
| A6 Slice plan | Bounded dependency-ordered tasks with origins, evidence, and recovery | `planning.decompose` | Main-agent change-work-item/development-plan update |
| A7 Contracts/data | Authoritative contracts plus compatibility, migration, and recovery | `architecture.review` | `database.review`, `spec.change`; schema/API inspection and native contract tests |
| A8 Environment | Reproducible, risk-appropriate verification and delivery target | `delivery.environment` | Repository-native environment, build, CI/CD, and smoke tooling |
| A9 Implementation | Integrated vertical slice with actual code/test/contract links | `development.tdd` | `qa.browser`; native test runner and RED/GREEN/REFACTOR loop |
| A10 Review | Impact-ranked findings with resolutions or approved exceptions | `review.code` | Security, accessibility, performance, or database review when triggered |
| A11 PR evidence | Reconstructable review unit with trace, CI, approval, and recovery evidence | `review.code`, `delivery.change-review` | Repository PR template, CI artifacts, or equivalent local review record |
| A12 Verification summary | Accepted, failed, blocked, stale, excepted, and `N/A` evidence index backed by fresh completion checks | `verification.completion` plus deterministic project commands | `qa.browser` and risk-triggered reviewers; manual evidence with approval metadata |
| A13 Release | Immutable artifact, deployment, compatibility, and recovery evidence | `delivery.deploy`, `delivery.recover` | Repository CLI, CI provider, deployment/recovery scripts, and runbooks |
| A14 Observation | Requirement-linked target/production signals and threshold decision | `operations.monitor` | Project observability stack, logs, metrics, traces, and audit records |
| A15 Learning | Owned anti-entropy improvements and temporary-mechanism cleanup | `operations.retro` | Git, incident, metric, and support-evidence review by the main agent |

## Conditional Review Triggers

| Capability | Select when |
|---|---|
| `database.review` | Schema, query, index, stored format, migration, backup, or data recovery changes |
| `qa.browser` | User-visible browser behavior, interactive reproduction, or visual evidence is required |
| `review.security` | Trust boundaries, authentication, authorization, sensitive data, secrets, dependency exposure, or audit behavior changes |
| `review.accessibility` | An affected user interface changes semantics, keyboard behavior, focus, content, or visual contrast |
| `review.performance` | A measurable performance/reliability target or credible regression risk exists |
| Domain specialist | The change enters a specialized platform or application domain whose constraints are not represented by repository evidence |

## Curated Provider Resolution

After selecting capabilities, read `references/provider-registry.md` only when a
curated specialist or execution overlay would help. The curated set is intentionally
limited to Superpowers, UI UX Pro Max, and Ponytail. Ponytail shapes the minimum safe
solution but never satisfies a capability or lowers its evidence requirement.

## Degraded Operation

Missing providers reduce automation, not required outcomes. Record the fallback and
evidence not collected. Stop when proceeding would be unsafe or materially
incomplete—for example, a private system is inaccessible, an irreversible action
lacks authority, or required verification cannot run.
