# Platform Adapters and Capability Contracts

Use this reference before selecting another skill, agent, MCP tool, or host-specific command. The lifecycle is portable; providers are replaceable implementations.

## Provider Resolution

For each capability:

1. Inspect the active host's available skills, agents, and tools.
2. Prefer a provider explicitly requested by the user or configured by the project.
3. Otherwise choose the best available provider whose description matches the capability.
4. If no specialized provider exists, perform the work with the main agent and ordinary repository tools.
5. Report a blocker only when the capability itself cannot be completed, not because a preferred provider is absent.

Do not emit a slash command, `$skill` invocation, agent name, or MCP tool name until that provider has been discovered. Do not install providers without user authorization.
When a curated provider would help, read `references/provider-registry.md` and apply
only the matching profile.

## Capability Catalog

| Capability ID | Required outcome | Portable fallback |
|---|---|---|
| `product.discovery` | Problem, users, goals, scope, assumptions, acceptance criteria | Structured interview and requirements template |
| `product.scope-review` | Expand/keep/reduce recommendation with rationale | Risk/value/effort review by the main agent |
| `product.requirements-review` | Completeness, consistency, testability, boundary, and change-impact findings | Apply `references/requirements-workflow.md` Definition of Ready in a separate review pass |
| `design.system` | IA, flows, states, visual system, responsive behavior | Produce the UI design template directly |
| `design.prototype` | Reviewable mockup or runnable prototype | HTML/CSS prototype or design-tool output |
| `design.review` | Evidence-based UX and visual findings | Browser screenshots plus heuristic review |
| `architecture.review` | Boundaries, data flow, dependencies, ADRs, risks | Repository analysis and architecture templates |
| `planning.decompose` | Small, dependency-ordered, verifiable tasks | Development-plan template and repository inspection |
| `spec.change` | Versioned proposal or contract delta | Repository-local Markdown/YAML change artifact |
| `database.review` | Schema, query, index, and migration safety review | SQL/schema inspection plus deterministic tests |
| `development.tdd` | Fail-before/pass-after evidence and minimal implementation | Native test runner and RED/GREEN/REFACTOR loop |
| `qa.browser` | Reproduce and verify user-visible behavior | Available browser automation or manual preview evidence |
| `review.code` | Independent correctness and maintainability review | Fresh-context subagent when available; otherwise separate review pass |
| `review.security` | Threat-aware code and dependency review | Project scanners plus manual trust-boundary review |
| `review.accessibility` | Keyboard, semantic, ARIA, and contrast evidence | axe-compatible tooling and browser inspection |
| `review.performance` | Measured client/server performance against targets | Lighthouse-compatible audit or project load tools |
| `verification.completion` | Fresh evidence that directly supports every completion claim | Re-run the relevant full commands, inspect exit status/results, and reconcile them against acceptance and risk |
| `delivery.environment` | Reproducible verification/delivery target with data, secrets, build, smoke, signal, and cleanup constraints | Repository environment scripts, containers, CI, and documented manual setup |
| `delivery.change-review` | Reconstructable PR/change unit with distinct review, CI, approval, artifact, and recovery references | Repository PR conventions, CI artifacts, or equivalent local review record |
| `delivery.deploy` | Authorized immutable artifact rollout with cohort, compatibility, migration, health, and decision evidence | Repository deployment CLI, CD pipeline, and runbook |
| `delivery.recover` | Tested rollback, roll-forward, containment, or stop path with authority and result evidence | Repository recovery scripts/runbook and deterministic health/data checks |
| `operations.monitor` | Infrastructure, application, business, and UX signals | Project observability stack and logs |
| `operations.retro` | Evidence, lessons, owned actions, documentation updates | Git/incident/metric review by the main agent |

## Host Adapters

### Codex

- Invoke discovered skills with `$skill-name` or let Codex match their `description` implicitly.
- Store repository skills under `.agents/skills/`; use `agents/openai.yaml` only for Codex UI metadata, invocation policy, and declared MCP dependencies.
- Put durable repository commands and constraints in `AGENTS.md`. Add nested `AGENTS.md` or `AGENTS.override.md` only where subtree rules differ.
- Use native subagents for bounded, independent exploration, testing, or review. Prefer read-heavy parallelism; coordinate write-heavy work to avoid conflicts.
- Discover MCP configuration with `codex mcp list`. Treat MCP as optional unless a task requires private or live external data.

### Claude Code

- Use installed skills only after discovery and map them to the same capability
  contracts used by Codex.
- Translate provider-specific slash commands or names only after discovery.
- Treat `~/.claude/skills`, `~/.claude/agents`, and Claude MCP configuration as host-specific locations, not portable requirements.

### Other Agent Hosts

- Use the open Agent Skills `SKILL.md` format when supported.
- Use natural-language capability instructions and repository-native tools when the host lacks skill or subagent primitives.
- Preserve the same outcomes, gates, permissions, and evidence requirements even when invocation syntax differs.

## Curated Providers

The core lifecycle is provider-neutral. The maintained provider profiles are
Superpowers, UI UX Pro Max, and Ponytail; read
`references/provider-registry.md` for their capability mappings, scenario bounds,
verified snapshots, and side effects. Other discovered tools may still satisfy a
capability by description, but they are not curated or recommended by this repository.
