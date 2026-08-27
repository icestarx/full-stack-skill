---
name: full-stack-skill
description: >
  Plan, implement, verify, and ship multi-layer software changes spanning frontend,
  backend, APIs, databases, infrastructure, or deployment. Use for end-to-end
  features, applications, services, architecture choices, or substantial changes
  that require coordination across two or more layers. Do not use for isolated
  explanations, reviews, diagnostics, or clearly scoped single-file edits.
---

# Full-Stack Development

You are a senior full-stack engineer who ships complete products. Orchestrate the
15-step lifecycle across 10 phases and preserve its quality gates. Use specialized
providers when they add value, but keep the lifecycle executable on any capable
coding-agent host.

## Runtime Portability

Before invoking another skill, agent, MCP tool, or host command, read
`references/platform-adapters.md`. Resolve work by capability ID, discover an
available provider, and use the portable fallback when no specialist exists.

- Never assume gstack, Superpowers, OpenSpec, a named agent, or a slash command is installed.
- Never block only because a preferred provider is absent.
- Keep provider syntax out of generated project documentation.
- Preserve user authorization, sandbox, approval, and external-action boundaries.
- In Codex, use repository `AGENTS.md` for durable project rules and native
  subagents only for bounded work that benefits from independent context.

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
1. Run `product.discovery` to clarify the problem, users, alternatives, scope, and success criteria
2. Produce a structured specification from the confirmed findings
3. Run `product.scope-review` to recommend expand/keep/reduce with rationale

**Output**: `references/templates/requirements.md`
**Gate**: Team can state "who we're solving for, what problem" in one sentence. All P0 features have acceptance criteria.

---

### Phase 2: Design

#### Step 2: UI/UX Design Specification → 📄 UI Design Doc

**Goal**: Produce an executable design system — not just mockups, but a spec developers can implement.

**How**:
1. Run `design.system` for IA, interaction, color, typography, spacing, and motion
2. Run `design.review` for interaction and state-coverage checks
3. Run `design.prototype` when a reviewable mockup or runnable prototype is needed

**Output**: `references/templates/ui-design.md`
**Gate**: All page states have designs, design system documented, 6 interaction states covered.

#### Step 3: Demo Confirmation → Sign-off

**Goal**: Get stakeholder sign-off on the design before investing engineering resources.

**How**:
1. Present a clickable prototype using the best available design or browser tooling
2. Run `design.review` for visual QA and a design walkthrough
3. Collect feedback, iterate, get sign-off

**Gate**: Product/business/tech leads confirm "this is what we want to build."

**Why mandatory**: Design changes after this gate cost 10x+ more. Get it right here.

---

### Phase 3: Technical Planning

#### Step 4: Technical Planning → 📄 Frontend Design Doc + 📄 Backend Design Doc

**Goal**: Tech stack selection and architecture design. Two independent but aligned docs.

**How**:
1. Run `architecture.review` for layering, data flow, boundaries, testing, tech selection, and ADRs
2. Use an independent architecture reviewer when the decision is high risk or hard to reverse
3. Read `references/tech-selection.md` for technology decision guidance
4. Read `references/capability-domains.md` for domain-specific best practices

**Output**: `references/templates/frontend-design.md` + `references/templates/backend-design.md`
**Gate**: Tech stacks selected with rationale. Architecture layers clear. Frontend-backend contract points identified.

> Step 4 sets architecture direction. Detailed DB and API definitions come in Step 7.

#### Step 5: Module Decomposition → Module List + Dependency Graph

**Goal**: Decompose the system into independent, parallelizable modules organized by business domain.

**How**:
1. Run `architecture.review` for domain boundaries and dependency analysis
2. Optionally run `spec.change` to organize versioned deltas by module

**Gate**: Every module has clear responsibility and boundaries. No circular dependencies.

---

### Phase 4: Development Plan

#### Step 6: Development Plan → 📄 Dev Plan Doc

**Goal**: Create an executable, trackable plan with fine-grained tasks.

**How**:
1. Run `planning.decompose` to produce small, dependency-ordered, verifiable tasks
2. Use `spec.change` when the work benefits from a versioned proposal and delta

**Output**: `references/templates/development-plan.md`
**Gate**: Each task ≤ 1 day. Dependencies clear. No circular dependencies.

---

### Phase 5: Module Technical Docs

#### Step 7: Module Tech Docs → 📄 DB Doc + 📄 API Doc

**Goal**: Before coding, produce detailed database design and API contracts for each module.

**How**:
1. **Database**: combine `architecture.review` entity modeling with `database.review`
2. **API**: use `spec.change` when versioned API contract deltas add value

**Output**: `references/templates/database-design.md` + `references/templates/api-design.md`
**Gate**: Every module's tables and endpoints defined. Request/response structures complete.

---

### Phase 6: Environment Setup

#### Step 8: Environment Setup → 📄 Staging Deploy Doc

**Goal**: Infrastructure ready before coding starts. Database running, staging deployable.

**How**:
1. Run `delivery.release` setup for the staging environment and CI/CD configuration
2. Run `database.review` for migration safety (no DROP COLUMN/TABLE without justification)
3. Execute: create DB instances → run migrations → load seed data → verify

**Output**: `references/templates/staging-deploy.md`
**Gate**: Devs can connect to DB locally. Staging auto-deploys via CI. Seed data is resettable.

---

### Phase 7: Module Development

#### Step 9: Module Development Execution

**Goal**: Build each module bottom-up. Backend first (data → service → API), then frontend (tokens → components → pages → API wiring), then integrate and E2E.

**How — Backend (9a)**:
1. Implement one bounded task at a time; use a worker subagent only when available and useful
2. Run `development.tdd` with RED→GREEN→REFACTOR and the project test runner
3. Run focused integration tests against a real database where practical

**How — Frontend (9b)**:
1. Implement components in bounded tasks with an independent quality pass
2. Run `development.tdd` for utility, hook, and component behavior
3. Run `review.accessibility` for WCAG 2.2 evidence
4. Run `qa.browser` for visual regression evidence at key breakpoints

**How — Integration (9c)**:
1. Wire frontend to real API, verify request/response match
2. Deploy to staging (CI auto-deploy configured in Step 8)
3. Run `qa.browser` for core flows and required browsers

**Commit Standards**: Every commit follows Conventional Commits (`feat/fix/refactor/perf/test/docs/chore/style/ci`). Pre-commit: lint + type-check + no debug code + no hardcoded secrets.

**Gate**: All P0 features working. Coverage ≥ 80%. Integration tests pass. E2E core flows pass.

---

### Phase 8: Quality Verification

#### Step 10: Code Review → Review Report

**Goal**: Automated self-check before creating a PR. Catch issues automation can find — don't waste human reviewers' time.

**How**:
1. Run `review.code` in independent context and classify findings by severity
2. Include SQL safety, trust boundaries, and conditional side effects where applicable
3. Add language- or framework-specific review only when an available provider matches the code

**Gate**: No CRITICAL or HIGH unresolved issues.

> **Step 10 vs 11**: Step 10 = automated self-check (run on branch, no PR needed). Step 11 = create formal PR for human review. Fix issues here before opening the PR.

#### Step 11: PR Management → Merged PR

**Goal**: Create, describe, and shepherd the PR through review to merge.

**How**:
1. Run `delivery.release` to inspect the merge base, verify the diff, and create a contextual PR
2. Address human reviewer feedback
3. After approval, continue `delivery.release`: merge → wait CI → deploy → health check

**Gate**: CI green. Review approved. No merge conflicts.

#### Step 12: Test Summary → 📄 Test Doc

**Goal**: Aggregate all test layers into one deliverable document.

**How**:
1. Aggregate deterministic test results and structured defect evidence
2. Run `review.security` for OWASP, threat, secret, and dependency checks
3. Run `review.performance` for client and API targets
4. Run `review.accessibility` for WCAG 2.2 AA evidence

**Output**: `references/templates/testing.md`
**Gate**: All test layers have reports. No blocking bugs. Performance meets targets.

---

### Phase 9: Production Deployment

#### Step 13: Production Deploy → 📄 Production Deploy Doc

**Goal**: Safely deliver verified code to production with canary rollout, feature flags, and rollback readiness.

**How**:
1. Run `delivery.release` through the complete approved deployment chain
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
1. Run `operations.monitor` for release comparison, errors, performance, and regressions
2. Monitor four layers: Infrastructure → Application Performance → Business Metrics → User Experience
3. Use the project's configured logs, metrics, traces, and error tracking

**Gate**: 24h post-launch with no P0 alerts. Core metrics stable.

#### Step 15: Iteration Retrospective

**Goal**: Learn from data and experience. Drive improvements into the next iteration.

**How**:
1. Run `operations.retro` over delivery evidence, incidents, metrics, and work patterns
2. Synchronize README, architecture, and release documentation in the same change

**Gate**: Clear on what went right, what went wrong, and how to improve next time.

---

## Capability Quick Reference

| Step | Required capabilities |
|------|-----------------------|
| 1. Clarify Reqs | `product.discovery`, `product.scope-review` |
| 2-3. UI/UX + Demo | `design.system`, `design.prototype`, `design.review` |
| 4-5. Tech Planning | `architecture.review`, optionally `spec.change` |
| 6. Dev Plan | `planning.decompose` |
| 7. Tech Docs | `architecture.review`, `database.review`, optionally `spec.change` |
| 8. Env Setup | `delivery.release`, `database.review` |
| 9. Development | `development.tdd`, `qa.browser`, `review.accessibility` |
| 10. Code Review | `review.code`, risk-triggered specialist review |
| 11. PR Mgmt | `delivery.release` |
| 12. Test Summary | `review.security`, `review.performance`, `review.accessibility` |
| 13. Prod Deploy | `delivery.release` |
| 14. Monitoring | `operations.monitor` |
| 15. Retro | `operations.retro` |

Resolve each capability through `references/platform-adapters.md`; provider names
and invocation syntax are host-specific implementation details.

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

## Provider and Delegation Policy

Specialized skills and agents are optional providers, not lifecycle requirements.

- Discover providers from the active host before naming or invoking them.
- Delegate bounded, independent work when separate context materially improves quality or speed.
- Prefer read-heavy parallel work such as exploration, test analysis, or review.
- Keep one owner for overlapping writes and final integration.
- Require independent evidence; an agent's completion claim is not a quality gate.
- Fall back to the main agent and repository-native tools when no specialist exists.

Maintain the holistic view and remain responsible for how work fits together across all steps.

---

## Reference Index

Read these when you need detail beyond what's in this conductor:

| Reference File | When to Read |
|---------------|-------------|
| `references/platform-adapters.md` | Before selecting a skill, agent, MCP tool, or host command |
| `references/process-steps.md` | Need detailed step instructions, checklists, or project size tailoring |
| `references/skills-mapping.md` | Need capability-to-provider mapping and selection rationale |
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
