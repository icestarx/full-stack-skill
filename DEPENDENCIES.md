# Full-Stack Skill — Runtime and Providers

The lifecycle has no mandatory dependency on gstack, Superpowers, OpenSpec, named reviewer agents, or a specific MCP server. Those packages are optional providers. The main agent must use repository-native tools when a specialist is unavailable.

## Core Runtime

The host needs:

- support for the open `SKILL.md` format or equivalent instruction loading;
- read/write access to the target repository within the user's authorization;
- a terminal or equivalent build/test tools for implementation work;
- the project-specific compilers, package managers, and test runners.

Repository maintenance checks use Python 3's standard library. Python is not needed
to read the Skill, but `setup --strict`, traceability validation, and eval-suite
validation require it.

If the requested outcome requires a browser, design system, private service, deployment platform, or production telemetry, the corresponding tool and authorization become task-specific requirements.

## Supported Hosts

| Host | Skill discovery | Project guidance | Specialist work |
|---|---|---|---|
| Codex | `.agents/skills/` or user/admin skill locations | `AGENTS.md` and nested overrides | Native subagents, project agents, skills, MCP |
| Claude Code | Existing Claude skill locations | Host-specific project instructions | Legacy gstack/Superpowers/OpenSpec and named agents when installed |
| Other agents | Open Agent Skills layout where supported | Host-specific repository guidance | Natural-language roles and ordinary project tools |

Codex is a first-class target. `agents/openai.yaml` supplies Codex-facing metadata; it intentionally declares no required MCP dependency because providers are selected per project.

## Capability Providers

Provider selection follows `references/platform-adapters.md`. Common optional providers include:

| Provider | Capabilities it may satisfy | Status |
|---|---|---|
| gstack | Product discovery, design, QA, delivery, monitoring, retrospective | Optional legacy accelerator |
| Superpowers | Brainstorming, planning, TDD, independent review, verification | Optional legacy accelerator |
| OpenSpec | Versioned proposals, contract deltas, task execution | Optional and cross-workflow |
| Host-native subagents | Exploration, architecture, testing, code/security review | Optional; use for bounded work |
| Browser automation | Prototype review, E2E, visual and accessibility evidence | Task-specific |
| Documentation/search MCP | Current library or platform documentation | Task-specific |
| Design MCP | Design context, assets, or canvas operations | Task-specific |
| Observability tools | Logs, metrics, traces, production health | Production tasks only |

Provider absence is not a blocker when the main agent can produce the same outcome and evidence safely.

## Codex Adapter

For repository-scoped use, place or link this folder under:

```text
<repository>/.agents/skills/full-stack-skill/
```

For personal use across repositories, use the Codex user skill location supported by the installed client. Invoke explicitly as `$full-stack-skill`, or allow implicit selection through the frontmatter description.

Use:

```bash
codex mcp list
```

to inspect configured MCP servers. Custom project agents, when useful, belong under `.codex/agents/`; the lifecycle does not require predefined agent files.

## Claude Code Legacy Adapter

Existing installations may continue to use `~/.claude/skills`, `~/.claude/agents`, legacy slash commands, and configured MCP servers. These names and paths must not appear as unconditional requirements in the portable lifecycle. Discover them first, map them to a capability, and otherwise use the fallback.

## Degraded Operation

When a provider is missing:

1. state which capability needs to be satisfied;
2. use the portable fallback from `references/platform-adapters.md`;
3. collect deterministic evidence with project tools;
4. record any verification that could not be performed;
5. stop only when proceeding would be unsafe or materially incomplete.

## Environment Audit

Run from this directory:

```bash
bash setup
bash setup --strict
```

The default audit reports host support and optional providers. Strict mode returns non-zero when core repository files are invalid; optional provider absence remains informational.
