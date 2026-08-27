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

## Capability Catalog

| Capability ID | Required outcome | Portable fallback |
|---|---|---|
| `product.discovery` | Problem, users, goals, scope, assumptions, acceptance criteria | Structured interview and requirements template |
| `product.scope-review` | Expand/keep/reduce recommendation with rationale | Risk/value/effort review by the main agent |
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
| `delivery.release` | PR, CI, rollout, health checks, and recovery evidence | Repository CLI, CI provider, and deployment scripts |
| `operations.monitor` | Infrastructure, application, business, and UX signals | Project observability stack and logs |
| `operations.retro` | Evidence, lessons, owned actions, documentation updates | Git/incident/metric review by the main agent |

## Host Adapters

### Codex

- Invoke discovered skills with `$skill-name` or let Codex match their `description` implicitly.
- Store repository skills under `.agents/skills/`; use `agents/openai.yaml` only for Codex UI metadata, invocation policy, and declared MCP dependencies.
- Put durable repository commands and constraints in `AGENTS.md`. Add nested `AGENTS.md` or `AGENTS.override.md` only where subtree rules differ.
- Use native subagents for bounded, independent exploration, testing, or review. Prefer read-heavy parallelism; coordinate write-heavy work to avoid conflicts.
- Discover MCP configuration with `codex mcp list`. Treat MCP as optional unless a task requires private or live external data.

### Claude Code Legacy Adapter

- Existing gstack, Superpowers, OpenSpec, and named reviewer agents may satisfy capabilities when installed.
- Translate their provider-specific slash commands or names only after discovery.
- Treat `~/.claude/skills`, `~/.claude/agents`, and Claude MCP configuration as host-specific locations, not portable requirements.

### Other Agent Hosts

- Use the open Agent Skills `SKILL.md` format when supported.
- Use natural-language capability instructions and repository-native tools when the host lacks skill or subagent primitives.
- Preserve the same outcomes, gates, permissions, and evidence requirements even when invocation syntax differs.

## Legacy Provider Map

The original provider ecosystem remains optional. Map it by capability instead of calling it unconditionally:

| Legacy providers | Capability IDs |
|---|---|
| gstack `office-hours`, `plan-ceo-review` | `product.discovery`, `product.scope-review` |
| gstack design skills | `design.system`, `design.prototype`, `design.review` |
| gstack `plan-eng-review` | `architecture.review` |
| Superpowers brainstorming and planning | `product.discovery`, `planning.decompose` |
| Superpowers TDD and subagent development | `development.tdd`, `review.code` |
| OpenSpec proposal/apply/archive | `spec.change`, `planning.decompose` |
| gstack QA/review/CSO | `qa.browser`, `review.code`, `review.security` |
| gstack ship/deploy/canary | `delivery.release`, `operations.monitor` |
| gstack retro/document-release | `operations.retro` |
| Named architect/database/a11y/E2E/performance agents | Matching architecture, database, QA, accessibility, or performance capability |

Provider-specific references may improve execution, but the core lifecycle must remain usable without this legacy ecosystem.
