# Full-Stack Skill — Dependencies

This skill orchestrates a 15-step development pipeline. It delegates to skills and agents at each step. Below is the complete dependency inventory.

## Layer 1: Required Skills

These skill packs must be installed for the pipeline to function.

### gstack

The primary skill ecosystem for product, design, deployment, QA, and operations.
**Install**: Run `~/.claude/skills/gstack/setup` after cloning/copying gstack.

Required gstack sub-skills (the pipeline references these directly):

| Skill | Used In | Purpose |
|-------|---------|---------|
| `office-hours` | Step 1 | Six-prompt requirements clarification |
| `plan-ceo-review` | Step 1 | Scope calibration (expand/keep/reduce) |
| `design-consultation` | Step 2 | Full design system generation |
| `plan-design-review` | Step 2 | Interaction design scoring |
| `design-html` | Step 2 | Production HTML/CSS from approved designs |
| `design-review` | Step 3 | Visual QA and design walkthrough |
| `plan-eng-review` | Step 4 | Architecture review (layering/data flow/testing) |
| `setup-deploy` | Step 8 | Staging environment + CI/CD configuration |
| `qa` | Step 9 | Structured integration testing + auto-fix |
| `qa-only` | Step 12 | Structured bug reports with health scores |
| `ship` | Step 11, 13 | PR creation and shipping automation |
| `land-and-deploy` | Step 11, 13 | Merge → deploy → health check |
| `review` | Step 10 | SQL safety, LLM trust boundaries, side effects |
| `cso` | Step 12 | Security audit (OWASP + STRIDE + secrets scan) |
| `canary` | Step 14 | Post-deploy canary monitoring |
| `retro` | Step 15 | Engineering retrospective + trend tracking |
| `document-release` | Step 15 | Sync docs after retro |

### Superpowers

Development discipline skills for planning, TDD, and code review.
**Install**: Via the superpowers plugin system.

Required superpowers skills:

| Skill | Used In | Purpose |
|-------|---------|---------|
| `superpowers:brainstorming` | Step 1 | Structured spec document output |
| `superpowers:writing-plans` | Step 6 | Ultra-fine-grained task decomposition |
| `superpowers:subagent-driven-development` | Step 9 | Per-task subagent with review loops |
| `superpowers:test-driven-development` | Step 9 | RED→GREEN→REFACTOR enforcement |
| `superpowers:requesting-code-review` | Step 10 | Independent subagent code review |
| `superpowers:receiving-code-review` | Step 10 | Structured feedback handling |
| `superpowers:verification-before-completion` | Step 12 | Evidence-backed test conclusions |

### OpenSpec (Optional)

Lightweight artifact and contract management. Used primarily for API contracts.

| Skill | Used In | Purpose |
|-------|---------|---------|
| `/openspec:propose` | Steps 5, 6, 7 | Spec delta management, API contracts |

---

## Layer 2: Required Agents

These agents must be available in `~/.claude/agents/`:

| Agent | Used In | Purpose |
|-------|---------|---------|
| **architect** | Steps 4, 5, 7 | System design, module boundaries, entity modeling |
| **code-reviewer** | Step 10 | General code quality and patterns |
| **security-reviewer** | Step 10 | Security vulnerabilities, OWASP Top 10 |
| **database-reviewer** | Steps 7, 8 | Index strategy, migration safety, query security |
| **e2e-runner** | Steps 9, 12 | E2E testing, visual regression screenshots |
| **a11y-architect** | Steps 9, 12 | WCAG 2.2 audit, keyboard nav, ARIA, contrast |
| **performance-optimizer** | Step 12 | API load testing, bundle analysis |
| **tdd-guide** | Step 9 | Test-driven development enforcement |
| **build-error-resolver** | Step 9 | Build and type error resolution |
| **doc-updater** | Step 15 | Documentation updates |
| **refactor-cleaner** | Step 10 | Dead code detection and removal |

### Language-Specific Reviewers (as needed)

| Agent | Use When |
|-------|----------|
| **typescript-reviewer** | TypeScript/JavaScript projects |
| **python-reviewer** | Python projects |
| **go-reviewer** | Go projects |
| **rust-reviewer** | Rust projects |
| **swift-reviewer** | Swift projects |
| **java-reviewer** | Java projects |
| **csharp-reviewer** | C# projects |
| **kotlin-reviewer** | Kotlin projects |
| **flutter-reviewer** | Flutter projects |
| **fastapi-reviewer** | FastAPI projects |
| **django-reviewer** | Django projects |
| **cpp-reviewer** | C++ projects |
| **fsharp-reviewer** | F# projects |

---

## Layer 3: MCP Tools (as needed)

| Tool | Used In | Purpose |
|------|---------|---------|
| `lighthouse_audit` (chrome-devtools MCP) | Step 12 | LCP/INP/CLS/FCP/TBT performance audit |
| `context7` MCP | Steps 4, 7, 9 | Library/API documentation lookup |
| Playwright MCP | Steps 9, 12 | Browser automation for E2E and screenshots |

---

## Quick Install Check

Run the `setup` script in this directory to check what's installed and what's missing:

```bash
bash ~/.claude/skills/full-stack/setup
```

The script will:
1. Detect installed gstack and superpowers skills
2. Detect installed agents
3. Print a colored report: ✅ installed / ❌ missing / ⚠️ partial
4. Guide you through installing missing dependencies
