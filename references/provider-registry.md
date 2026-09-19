# Curated Provider Registry

Read this reference only after selecting a capability from
`references/skills-mapping.md` and deciding that a specialist could materially
improve the result. Capability IDs remain the contract; these profiles are optional,
replaceable implementations or execution overlays.

This registry intentionally curates only Superpowers, UI UX Pro Max, and Ponytail.
Discover the installed provider before invocation, follow its installed instructions,
and never install or upgrade it without user authorization. A verified version below
is a review snapshot, not a required or automatically trusted version.

## Resolution Rules

1. Preserve a provider selected by the user or repository.
2. Confirm the exact installed skill name and instructions in the active host.
3. Match the provider to the current capability and scenario; do not run an entire
   suite merely because one of its skills applies.
4. Keep project-native commands authoritative for build, test, migration, CI,
   deployment, and production evidence.
5. Apply side-effect and authorization boundaries at the action level. Provider
   discovery never authorizes workspace, Git, remote, or production mutation.
6. Use the portable fallback when the provider is absent, stale, mismatched, or
   would add more process than the change warrants.

## Superpowers

| Field | Profile |
|---|---|
| Role | Engineering-method provider for design refinement, executable planning, TDD, independent review, and completion verification |
| Best-fit steps | A1 when the problem/design is unresolved; A6; A9; A10; A12 |
| Capability mapping | `brainstorming` → `product.discovery`; `writing-plans` → `planning.decompose`; `test-driven-development` → `development.tdd`; `requesting-code-review` / `receiving-code-review` and the review stages of `subagent-driven-development` → `review.code`; `verification-before-completion` → `verification.completion` |
| Use when | The change benefits from a strict design-to-plan-to-test-to-review loop, the plan is stable enough to execute, or a completion claim needs an explicit evidence gate |
| Avoid or narrow when | Requirements and design are already approved; the change is trivial; a throwaway prototype or generated/config-only change does not fit strict TDD; subagent overhead exceeds the risk |
| Side effects | Selected skills may write design/plan documents, tests, code, commits, branches, or worktrees; inspect the installed skill before use |
| Hosts | Codex App/CLI and other hosts documented by the provider; exact discovery and invocation vary by host |
| Verified snapshot | Release `v6.4.1`, commit `5bf4e78011075bcfc0dc295f0724994cd123ee71`, reviewed 2026-09-19 |
| Source | <https://github.com/obra/superpowers> |

Superpowers strengthens process discipline; it does not replace product authority,
UI design expertise, project-native checks, deployment tooling, or production
telemetry. Invoke only the matching installed skill, not the suite as a mandatory
waterfall.

## UI UX Pro Max

| Field | Profile |
|---|---|
| Role | Searchable UI/UX design-intelligence provider for visual systems and stack-specific implementation guidance |
| Best-fit steps | A2; supplementary input to A3 and UI-focused A10/A12 reviews |
| Capability mapping | Primary input to `design.system`; heuristic input to `design.review`, `review.accessibility`, and UI implementation decisions |
| Use when | A UI change needs grounded style, palette, typography, component, responsive, accessibility, animation, chart, or target-stack guidance |
| Avoid or narrow when | The repository design system already decides the question; no human/operator UI changes; the task requires a prototype, stakeholder approval, or browser evidence rather than design guidance |
| Side effects | Search/guidance is read-only; implementation may write UI files. It does not itself authorize design-tool, Git, remote, or deployment actions |
| Hosts | Includes Codex support in provider metadata; discover the installed skill name and local search commands before use |
| Verified snapshot | Release tag `v2.15.0`, commit `a38d04c3d5c298c851dbe5e6ee1965ee3de42cb5`, reviewed 2026-09-19 |
| Source | <https://github.com/nextlevelbuilder/ui-ux-pro-max-skill> |

Treat its output as design guidance. A3 acceptance still requires a human decision
when material, and A12 still requires rendered/browser and project-native evidence
for claims about the implemented interface.

## Ponytail

| Field | Profile |
|---|---|
| Role | Minimal-solution execution overlay: YAGNI, reuse, standard-library/native-first choices, and the shortest safe diff after full reconnaissance |
| Best-fit steps | A4-A10 when designing, planning, implementing, refactoring, fixing, or reviewing code |
| Capability mapping | Influences `architecture.review`, `planning.decompose`, `development.tdd`, and `review.code`; it does not satisfy any capability by itself |
| Use when | The task risks speculative abstraction, boilerplate, dependency growth, duplicated helpers, or an unnecessarily broad change |
| Avoid or narrow when | The request is non-coding; simplification would remove explicit scope, trust-boundary validation, data-loss prevention, security, accessibility, recovery, or required evidence |
| Intensity | Respect the installed skill and user selection; `full` is its default, `lite` exposes the simpler alternative, and `ultra` should be explicit because it challenges scope aggressively |
| Side effects | Depends on the wrapped coding/review activity; no external mutation is implied |
| Hosts | Use only when the exact `ponytail` skill is discoverable in the active host |
| Verified snapshot | Unversioned local skill snapshot, SHA-256 `1316a2f3f95741d2300b116fe0c2d81ce4a9568656ed0a62643f54aaf09957f2`, reviewed 2026-09-19 |
| Source | Active-host skill catalog; no portable upstream source or declared version was available in the verified snapshot |

Ponytail runs after the problem and affected flow are understood. It may reduce the
solution, files, dependencies, and prose; it may not reduce the required outcome or
evidence. When paired with Superpowers, use Ponytail to prune speculative tasks and
implementation while retaining Superpowers' test, review, and verification gates.

## Recommended A1-A15 Use

| Step | Curated provider use |
|---|---|
| A1 | Superpowers `brainstorming` only when problem or design discovery remains unresolved |
| A2 | UI UX Pro Max for design-system and target-stack guidance |
| A3 | UI UX Pro Max as decision input; it does not replace prototype evidence or human acceptance |
| A4 | Ponytail after repository reconnaissance to prefer existing/native solutions and avoid speculative architecture |
| A5 | Ponytail to keep boundaries and shared foundations no broader than current consumers require |
| A6 | Superpowers `writing-plans` for consequential multi-step work; Ponytail removes speculative tasks and excess granularity |
| A7 | Ponytail may simplify contracts and dependencies but cannot omit compatibility, migration, validation, or recovery semantics |
| A8 | Ponytail may minimize environment code/configuration but cannot weaken reproducibility, secrets handling, recovery, or smoke evidence |
| A9 | Superpowers TDD/subagent workflow when proportionate; Ponytail keeps the implementation minimal after the failing evidence is established |
| A10 | Superpowers review workflow for independent review; Ponytail adds an over-engineering and dependency pass |
| A11 | No curated provider is sufficient by itself; use repository PR/CI systems and `delivery.change-review` fallback |
| A12 | Superpowers `verification-before-completion`; UI UX Pro Max is guidance only, never verification evidence |
| A13 | No curated provider; use authorized project deployment and recovery tooling |
| A14 | No curated provider; use project observability and `operations.monitor` fallback |
| A15 | No curated provider; use repository/incident/release evidence and `operations.retro` fallback |
