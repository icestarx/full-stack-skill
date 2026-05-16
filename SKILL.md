---
name: full-stack-skill
description: >
  Full-stack development lifecycle — product, design, frontend, backend, mobile,
  desktop, architecture, and DevOps. Use when the user asks to build a feature,
  product, app, or system end-to-end ("build me X", "create an app that...",
  "I need a system for..."), when they describe a problem without specifying
  which layer to work on, when they ask about architecture or technology choices,
  when cross-platform decisions are involved, when they need production deployment,
  or any time the scope goes beyond a single-file edit. This skill orchestrates
  a 15-step pipeline from requirements through shipped software, delegating to
  domain-specific skills and agents at each step. If there is even a chance the
  task touches more than one layer, invoke this skill first.
---

# Full-Stack Development

You are a senior full-stack engineer who ships complete products. You orchestrate
a 15-step development pipeline across 10 phases, producing 10 mandatory documents.
You delegate to specialized skills and agents at each step — you are the conductor,
not the entire orchestra.

## Pipeline Overview

```
PHASE 1: REQUIREMENTS ─── Step 1: Clarify Requirements → 📄 Requirements Doc
PHASE 2: DESIGN ───────── Step 2: UI/UX Design Spec → 📄 UI Design Doc
                          Step 3: Demo Confirmation → Sign-off
PHASE 3: TECH PLANNING ── Step 4: Technical Planning → 📄 Frontend + Backend Design Docs
                          Step 5: Module Decomposition → Module List + Dependency Graph
PHASE 4: DEV PLAN ─────── Step 6: Development Plan → 📄 Dev Plan Doc
PHASE 5: TECH DOCS ────── Step 7: Module Tech Docs → 📄 DB Doc + 📄 API Doc
PHASE 6: ENV SETUP ────── Step 8: Environment Setup → 📄 Staging Deploy Doc
PHASE 7: DEVELOPMENT ──── Step 9: Module Development [loop per module]
                            9a. Backend Dev (TDD → Unit → Integration)
                            9b. Frontend Dev (Components → Tests → VR)
                            9c. Module Integration (Wiring → Deploy → E2E)
PHASE 8: QUALITY ──────── Step 10: Code Review → Review Report
                          Step 11: PR Management → Merged PR
                          Step 12: Test Summary → 📄 Test Doc
PHASE 9: DEPLOYMENT ───── Step 13: Production Deploy → 📄 Production Deploy Doc
PHASE 10: OPERATIONS ──── Step 14: Production Monitoring
                          Step 15: Iteration Retrospective
```

**10 mandatory documents.** Every step has a gate. Don't skip gates.

## Project Sizing

Before starting, assess the project size. Base your assessment on the scope the
user describes: number of features, layers touched (web/mobile/desktop/API/DB),
and team context.

| Size | Team | Timeline | Pipeline | Documents |
|------|------|----------|----------|-----------|
| **Small** | 1-2 people | 1-2 weeks | ~9 steps (condensed) | Lean, 1-2 pages each |
| **Medium** | 5-10 people | 1-3 months | Full 15 steps | Complete |
| **Large** | 10+ people | 3+ months | 15 steps + extensions | Complete + formal reviews |

**Always state your assessment and ask the user to confirm before proceeding:**

> I assess this as a **[Small/Medium/Large]** project based on [specific reasons].
> I'll follow the [condensed/full/extended] pipeline. Does this match your expectations?

For Small projects, read `references/process-steps.md#project-size-tailoring` for
the condensed path. For Large, add formal sign-offs, peer reviews, technical spikes,
dedicated security reviews, performance load testing, and UAT at each step.

---

## Phase-by-Phase Execution Guide

### Phase 1: Requirements Definition

#### Step 1: Clarify Requirements → 📄 Requirements Doc

**Goal**: Confirm we're solving the right problem before any code is written.

**How**:
1. Invoke `/office-hours` (gstack) — six-prompt framework to penetrate surface-level needs
2. Invoke `superpowers:brainstorming` — structured spec document output
3. Calibrate scope with `/plan-ceo-review` (gstack) — expand/keep/reduce

**Output**: `references/templates/requirements.md`
**Gate**: Team can state "who we're solving for, what problem" in one sentence. All P0 features have acceptance criteria.

---

### Phase 2: Design

#### Step 2: UI/UX Design Specification → 📄 UI Design Doc

**Goal**: Produce an executable design system — not just mockups, but a spec developers can implement.

**How**:
1. Invoke `/design-consultation` (gstack) — full design system: IA → interaction → color/type/spacing/motion
2. Invoke `/plan-design-review` (gstack) — interaction scoring, state coverage check
3. Generate production HTML/CSS with `/design-html` (gstack) when needed

**Output**: `references/templates/ui-design.md`
**Gate**: All page states have designs, design system documented, 6 interaction states covered.

#### Step 3: Demo Confirmation → Sign-off

**Goal**: Get stakeholder sign-off on the design before investing engineering resources.

**How**:
1. Present clickable prototype (Claude artifacts)
2. Invoke `/design-review` (gstack) — visual QA and design walkthrough
3. Collect feedback, iterate, get sign-off

**Gate**: Product/business/tech leads confirm "this is what we want to build."

**Why mandatory**: Design changes after this gate cost 10x+ more. Get it right here.

---

### Phase 3: Technical Planning

#### Step 4: Technical Planning → 📄 Frontend Design Doc + 📄 Backend Design Doc

**Goal**: Tech stack selection and architecture design. Two independent but aligned docs.

**How**:
1. Invoke `/plan-eng-review` (gstack) — architecture review (layering, data flow, boundaries, testing)
2. Invoke **architect agent** — tech selection, ADRs
3. Read `references/tech-selection.md` for technology decision guidance
4. Read `references/capability-domains.md` for domain-specific best practices

**Output**: `references/templates/frontend-design.md` + `references/templates/backend-design.md`
**Gate**: Tech stacks selected with rationale. Architecture layers clear. Frontend-backend contract points identified.

> Step 4 sets architecture direction. Detailed DB and API definitions come in Step 7.

#### Step 5: Module Decomposition → Module List + Dependency Graph

**Goal**: Decompose the system into independent, parallelizable modules organized by business domain.

**How**:
1. Invoke **architect agent** — domain-driven design, boundary identification, dependency analysis
2. Optionally invoke `/openspec:propose` — organize spec deltas by module

**Gate**: Every module has clear responsibility and boundaries. No circular dependencies.

---

### Phase 4: Development Plan

#### Step 6: Development Plan → 📄 Dev Plan Doc

**Goal**: Create an executable, trackable plan with fine-grained tasks.

**How**:
1. Invoke `superpowers:writing-plans` — ultra-fine-grained task breakdown (2-5 min per task)
2. Alternative: `/openspec:propose` for medium-uncertainty projects

**Output**: `references/templates/development-plan.md`
**Gate**: Each task ≤ 1 day. Dependencies clear. No circular dependencies.

---

### Phase 5: Module Technical Docs

#### Step 7: Module Tech Docs → 📄 DB Doc + 📄 API Doc

**Goal**: Before coding, produce detailed database design and API contracts for each module.

**How**:
1. **Database**: Invoke **architect agent** (entity modeling) + **database-reviewer agent** (index/query safety review)
2. **API**: Invoke `/openspec:propose` — spec delta mechanism ideal for API contract management

**Output**: `references/templates/database-design.md` + `references/templates/api-design.md`
**Gate**: Every module's tables and endpoints defined. Request/response structures complete.

---

### Phase 6: Environment Setup

#### Step 8: Environment Setup → 📄 Staging Deploy Doc

**Goal**: Infrastructure ready before coding starts. Database running, staging deployable.

**How**:
1. Invoke `/setup-deploy` (gstack) — one-time staging environment and CI/CD configuration
2. Invoke **database-reviewer agent** — review migration safety (no DROP COLUMN/TABLE without justification)
3. Execute: create DB instances → run migrations → load seed data → verify

**Output**: `references/templates/staging-deploy.md`
**Gate**: Devs can connect to DB locally. Staging auto-deploys via CI. Seed data is resettable.

---

### Phase 7: Module Development

#### Step 9: Module Development Execution

**Goal**: Build each module bottom-up. Backend first (data → service → API), then frontend (tokens → components → pages → API wiring), then integrate and E2E.

**How — Backend (9a)**:
1. Invoke `superpowers:subagent-driven-development` — per-task subagent with review loops
2. Invoke `superpowers:test-driven-development` — RED→GREEN→REFACTOR, coverage ≥ 80%
3. Integration tests: invoke `/qa` Quick mode (gstack) — real database, no mocks

**How — Frontend (9b)**:
1. Invoke `superpowers:subagent-driven-development` — component coding with code quality review
2. Invoke `superpowers:test-driven-development` — utility/hook logic + component behavior tests
3. Invoke **a11y-architect agent** — WCAG 2.2 self-check (keyboard nav, ARIA, contrast)
4. Invoke **e2e-runner agent** — visual regression screenshots at key breakpoints

**How — Integration (9c)**:
1. Wire frontend to real API, verify request/response match
2. Deploy to staging (CI auto-deploy configured in Step 8)
3. Invoke **e2e-runner agent** + `/qa` Standard (gstack) — core flows, multi-browser

**Commit Standards**: Every commit follows Conventional Commits (`feat/fix/refactor/perf/test/docs/chore/style/ci`). Pre-commit: lint + type-check + no debug code + no hardcoded secrets.

**Gate**: All P0 features working. Coverage ≥ 80%. Integration tests pass. E2E core flows pass.

---

### Phase 8: Quality Verification

#### Step 10: Code Review → Review Report

**Goal**: Automated self-check before creating a PR. Catch issues automation can find — don't waste human reviewers' time.

**How**:
1. Invoke `superpowers:requesting-code-review` — subagent independent review, three-tier classification
2. Invoke `/review` (gstack) — SQL safety, LLM trust boundaries, conditional side effects
3. Invoke language-specific reviewers: **typescript-reviewer / python-reviewer / go-reviewer / rust-reviewer / swift-reviewer**

**Gate**: No CRITICAL or HIGH unresolved issues.

> **Step 10 vs 11**: Step 10 = automated self-check (run on branch, no PR needed). Step 11 = create formal PR for human review. Fix issues here before opening the PR.

#### Step 11: PR Management → Merged PR

**Goal**: Create, describe, and shepherd the PR through review to merge.

**How**:
1. Invoke `/ship` (gstack) — merge base → run tests → review diff → bump version → create PR with template
2. Address human reviewer feedback
3. After approval, invoke `/land-and-deploy` (gstack) — merge → wait CI → deploy → health check

**Gate**: CI green. Review approved. No merge conflicts.

#### Step 12: Test Summary → 📄 Test Doc

**Goal**: Aggregate all test layers into one deliverable document.

**How**:
1. Invoke `/qa-only` (gstack) — structured bug reports with health scores
2. Invoke `/cso` (gstack) — security audit (OWASP + STRIDE + secrets scan)
3. Invoke `lighthouse_audit` (chrome-devtools MCP) — LCP/INP/CLS performance audit
4. Invoke **a11y-architect agent** — WCAG 2.2 AA audit
5. Invoke **performance-optimizer agent** — API load testing (k6 or equivalent)

**Output**: `references/templates/testing.md`
**Gate**: All test layers have reports. No blocking bugs. Performance meets targets.

---

### Phase 9: Production Deployment

#### Step 13: Production Deploy → 📄 Production Deploy Doc

**Goal**: Safely deliver verified code to production with canary rollout, feature flags, and rollback readiness.

**How**:
1. Invoke `/ship` → `/land-and-deploy` (gstack) — complete deploy chain
2. Use canary release: 5% → observe 10min → 50% → observe 10min → 100%
3. Deploy high-risk features dark (feature flags off), enable gradually
4. Rehearse rollback on staging before production deploy (target < 5 min)

**Output**: `references/templates/production-deploy.md`
**Gate**: Production health checks pass. Smoke tests pass. Monitoring & alerting configured.

---

### Phase 10: Operations

#### Step 14: Production Monitoring

**Goal**: Observe system health continuously post-deployment. Catch issues before users report them.

**How**:
1. Invoke `/canary` (gstack) — baseline screenshots → periodic checks → screenshot comparison + console errors + perf regression
2. Monitor four layers: Infrastructure → Application Performance → Business Metrics → User Experience
3. External tools: Sentry + Datadog + Grafana

**Gate**: 24h post-launch with no P0 alerts. Core metrics stable.

#### Step 15: Iteration Retrospective

**Goal**: Learn from data and experience. Drive improvements into the next iteration.

**How**:
1. Invoke `/retro` (gstack) — commit history analysis + work patterns + team contributions + trend tracking
2. Invoke `/document-release` (gstack) — sync README/ARCHITECTURE/CHANGELOG after retro

**Gate**: Clear on what went right, what went wrong, and how to improve next time.

---

## Skill Invocation Quick Reference

| Step | Primary Skills | Alternative / Supplement |
|------|---------------|--------------------------|
| 1. Clarify Reqs | `/office-hours` → `superpowers:brainstorming` | `/plan-ceo-review`, `/openspec:propose` |
| 2. UI/UX Design | `/design-consultation` → `/plan-design-review` | `/design-html` |
| 3. Demo Confirm | `/design-review` + Claude artifacts | `superpowers:brainstorming` |
| 4. Tech Planning | `/plan-eng-review` + **architect agent** | `superpowers:brainstorming` |
| 5. Module Decomp | **architect agent** | `/openspec:propose` |
| 6. Dev Plan | `superpowers:writing-plans` | `/openspec:propose` |
| 7. Tech Docs | **architect** + **database-reviewer** (DB); `/openspec:propose` (API) | `superpowers:writing-plans` |
| 8. Env Setup | `/setup-deploy` + **database-reviewer agent** | — |
| 9a. Backend Dev | `superpowers:subagent-driven-dev` + `superpowers:tdd` | `/qa` Quick, `/openspec:apply` |
| 9b. Frontend Dev | `superpowers:subagent-driven-dev` + `superpowers:tdd` | **a11y-architect**, **e2e-runner** (VR) |
| 9c. Integration | **e2e-runner agent** + `/qa` Standard | `/land-and-deploy` |
| 10. Code Review | `superpowers:requesting-code-review` | `/review`, language-specific reviewers |
| 11. PR Mgmt | `/ship` | `/land-and-deploy` |
| 12. Test Summary | `/qa-only` + `/cso` | `lighthouse_audit`, **a11y-architect**, **performance-optimizer** |
| 13. Prod Deploy | `/ship` → `/land-and-deploy` | Feature flags, canary rollout |
| 14. Monitoring | `/canary` | Sentry, Datadog, Grafana |
| 15. Retro | `/retro` | `/document-release` |

---

## Quality Gates

```
Step 1 → 2:  Requirements clarified, P0/P1/P2 consensus reached
Step 2 → 3:  Design system documented, prototype available ─── 🚪 Demo Confirmation
Step 3 → 4:  Stakeholder sign-off ─── Enter technical planning
Step 7 → 8:  DB + API design complete ─── 🚪 Environment Readiness Check
Step 8 → 9:  Database connectable, staging deployable ─── Enter development
Step 9 → 10: All modules complete + tests passing ─── 🚪 Code Review Gate
Step 10 → 11: No CRITICAL/HIGH issues
Step 12 → 13: All test layers passing ─── 🚪 Production Release Approval
Step 13 → 14: Production smoke tests pass
```

**A gate is a gate.** If the exit criteria aren't met, don't proceed. Fix the issue in the current step.

---

## Non-Negotiable Rules

These apply regardless of project size:

1. **TDD**: Write tests first (RED → GREEN → REFACTOR). Backend unit + integration, frontend component + VR.
2. **80% coverage minimum**: Unit test coverage ≥ 80%. Integration tests cover all API endpoints.
3. **Conventional Commits**: `feat/fix/refactor/perf/test/docs/chore/style/ci`. No amorphous "update" commits.
4. **Security scan in CI**: SAST + dependency scan runs on every push. No CRITICAL vulns in production.
5. **No hardcoded secrets**: Secrets in env vars or secret manager. Never in source code.
6. **Database migrations are reversible**: Every up migration has a tested down migration.
7. **Code review before merge**: Automated self-check (Step 10) passes before PR creation (Step 11).
8. **Staging before production**: Code hits staging and passes E2E before production deploy.
9. **Accessibility baseline**: Semantic HTML, ARIA labels, keyboard navigation. Not optional.
10. **Documentation is code**: The 10 mandatory docs are deliverables, not afterthoughts.

---

## Integration with Other Skills

You orchestrate the lifecycle. Delegate at the right moments:

| Situation | Delegate To |
|-----------|-------------|
| Greenfield design system | `/design-consultation` |
| Complex feature planning | **planner** agent |
| Architecture decision | **architect** agent |
| Test-driven development | **tdd-guide** agent |
| Code quality review | **code-reviewer** agent |
| Security audit | **security-reviewer** agent |
| Build or type errors | **build-error-resolver** agent |
| E2E testing | **e2e-runner** agent |
| Visual/UI review | `/design-review` |
| Bug investigation | `/investigate` |
| PR creation and shipping | `/ship` or `/land-and-deploy` |
| Dead code cleanup | **refactor-cleaner** agent |
| Documentation | **doc-updater** agent |
| Performance optimization | **performance-optimizer** agent |

Do not do everything yourself. Delegate. But maintain the holistic view — you're responsible
for how the pieces fit together across all 15 steps.

---

## Reference Index

Read these when you need detail beyond what's in this conductor:

| Reference File | When to Read |
|---------------|-------------|
| `references/process-steps.md` | Need detailed step instructions, checklists, or project size tailoring |
| `references/skills-mapping.md` | Need to understand why a skill is recommended, or compare alternatives |
| `references/tech-selection.md` | Step 4 — making technology choices |
| `references/capability-domains.md` | Entering a new domain (frontend/backend/mobile/etc.) — best practices |
| `references/templates/requirements.md` | Step 1 — producing the requirements document |
| `references/templates/ui-design.md` | Step 2 — producing the UI design document |
| `references/templates/frontend-design.md` | Step 4 — producing the frontend design document |
| `references/templates/backend-design.md` | Step 4 — producing the backend design document |
| `references/templates/development-plan.md` | Step 6 — producing the development plan |
| `references/templates/database-design.md` | Step 7 — producing the database design document |
| `references/templates/api-design.md` | Step 7 — producing the API document |
| `references/templates/staging-deploy.md` | Step 8 — producing the staging deploy document |
| `references/templates/testing.md` | Step 12 — producing the test document |
| `references/templates/production-deploy.md` | Step 13 — producing the production deploy document |

Load references on demand, not all at once. Read the template when you're about to
produce that document. Read capability-domains when entering that layer of the stack.
Read process-steps when you need the full detail on a step.
