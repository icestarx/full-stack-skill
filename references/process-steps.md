# 15-Step Full-Stack Process — Detailed Steps

> This is the detailed reference for each step. The SKILL.md conductor tells you which step to execute; this file tells you how.
> 
> For document templates, see `references/templates/`. For skill selection rationale, see `references/skills-mapping.md`.

## Pipeline Overview

```
Requirements (1) → Design (2) → Technical Planning (2) → Development Plan (1) →
Module Tech Docs (1) → Environment Setup (1) → Module Development (1) →
Quality Verification (3) → Production Deploy (1) → Operations (2)
```

**15 nodes, 10 phases, 10 phase documents, plus cross-cutting control records.**

```
Step 1                      Step 2              Step 3
Clarify Requirements ──→ UI/UX Design Spec ──→ Demo Confirmation
📄 Requirements Doc        📄 UI Design Doc       Design Review Passed

Step 4                      Step 5
Technical Planning ────→ Module Decomposition
📄 Frontend Design Doc      Module List + Dependency Graph
📄 Backend Design Doc

Step 6                      Step 7
Development Plan ─────→ Module Tech Docs
📄 Dev Plan Doc            📄 DB Doc + 📄 API Doc

Step 8
Environment Setup
├── 8a. Database Init (create instance / run migrations / seed data)
└── 8b. Staging Deploy (staging setup / CI/CD config)
📄 Staging Deploy Doc

Step 9
Module Development [loop per module]
├── 9a. Backend Dev (TDD → Unit Tests → Integration Tests)
├── 9b. Frontend Dev (Components → Component Tests → Visual Regression)
└── 9c. Module Integration (Frontend-Backend Wiring → Deploy to Staging → E2E)

Step 10        Step 11        Step 12
Code Review → PR Management → Test Summary
                               📄 Test Doc

Step 13                  Step 14        Step 15
Production Deploy ──→ Monitoring ──→ Retrospective
📄 Production Deploy Doc
```

---

## Mandatory Document Checklist

| # | Document | Produced At | Contents |
|---|----------|-------------|----------|
| 1 | **Requirements Doc** | Step 1 | Product brief, capability tree, stable requirement IDs, state transitions, operational semantics, acceptance criteria, quality attributes, impact and decisions |
| 2 | **UI Design Doc** | Step 2 | Design system (DESIGN.md): color, typography, spacing, motion, component states |
| 3 | **Frontend Design Doc** | Step 4 | Frontend tech stack, component architecture, state management, routing, rendering strategy, performance |
| 4 | **Backend Design Doc** | Step 4 | Backend tech stack, system architecture, auth/authz, data flow, security, ADRs |
| 5 | **Development Plan Doc** | Step 6 | Task breakdown, timeline, dependencies, ownership, milestones |
| 6 | **Database Design Doc** | Step 7 | ER diagram, DDL, index strategy, migration plan |
| 7 | **API Doc** | Step 7 | Endpoint definitions, request/response schemas, error codes, auth scheme |
| 8 | **Staging Deploy Doc** | Step 8 | Staging architecture, DB init flow, CI/CD config, env vars, seed data |
| 9 | **Test Doc** | Step 12 | Test strategy, case list, coverage report, performance baseline, known issues |
| 10 | **Production Deploy Doc** | Step 13 | Production architecture, release strategy, rollback plan, monitoring & alerting |

These 10 phase documents are accompanied by cross-cutting records rather than
counted as additional phases:

- major-version manifest — effective product/UX/engineering baseline;
- traceability ledger — normalized artifact relationships, coverage, and exceptions;
- release manifest — immutable scope and delivery evidence for one release.

Read `references/document-organization.md` for placement and
`references/traceability.md` for update rules and gates.

---

## Phase 1: Requirements Definition (Step 1)

### Step 1: Clarify Requirements ← 📄

> Before writing code, confirm we're solving the right problem. One step: problem definition + requirements doc.

| Dimension | Content |
|-----------|---------|
| **Entry** | Product idea, existing PRD, requested change, repository behavior, user feedback, business need, or data insight |
| **Core Activities** | Source inventory, mode selection (New/Review/Change), problem qualification, capability tree and scope, actor/rule/data coverage, state machines, operational semantics, acceptance criteria, change impact, readiness review |
| **Output** | **📄 Requirements Document**, baseline/ledger updates, or review findings when review-only was requested |
| **Exit Criteria** | Requirements pass `requirements-workflow.md` Definition of Ready; the capability tree has no missing/orphan P0 leaves; committed REQ/AC items are indexed in the version line; no hidden blocker remains |
| **Capabilities** | `product.discovery` → `product.scope-review` → `product.requirements-review` |

> **Workflow**: `references/requirements-workflow.md`
> **Template**: `references/templates/requirements.md`

**Key Questions:**
- What is already confirmed, where did it come from, and which sources conflict?
- Is this a new requirement, a review, or a delta to existing behavior?
- Does the capability tree cover every module, function, and applicable subfunction?
- Who can act, under which permissions, states, business rules, and data constraints?
- Which state transitions and concurrency/idempotency/cancellation/recovery semantics apply?
- What is explicitly outside this release, and what may regress when behavior changes?
- Can every P0 item be verified through positive, negative, and recovery behavior?

---

## Phase 2: Design (Steps 2-3)

### Step 2: UI/UX Design Specification ← 📄

> Information architecture → interaction design → UI design, unified into one executable design system spec.

| Dimension | Content |
|-----------|---------|
| **Entry** | Requirements doc feature list + user stories |
| **Core Activities** | Information architecture, interaction design, UI design, responsive/state coverage, and REQ/AC-to-flow/screen/state mapping |
| **Output** | **📄 UI Design Document (DESIGN.md)**, design mockups (desktop/tablet/mobile), clickable prototype |
| **Exit Criteria** | All page states have designs, design system documented, 6 interaction states covered, and every committed UX-affecting REQ/AC has a valid design link or approved N/A |
| **Capabilities** | `design.system` → `design.review` → `design.prototype` |

> **Template**: `references/templates/ui-design.md`

**6 Interaction States That Must Be Covered:**
1. Normal flow (happy path)
2. Empty state (first use / no data / search with no results)
3. Loading state (skeleton / spinner / progress bar / optimistic update)
4. Error state (network error / permission denied / data anomaly / timeout)
5. Edge cases (extra-long text / extreme data volume / concurrent operations / weak network)
6. Interruption & recovery (background switch / session expiry / network reconnect)

---

### Step 3: Demo Confirmation

> Before investing engineering resources, confirm with stakeholders using prototypes/mockups: "this is what we're building." Design → confirm → iterate → sign off.

| Dimension | Content |
|-----------|---------|
| **Entry** | UI design doc + clickable prototype |
| **Core Activities** | Prototype demo, stakeholder review, feedback collection, design iteration, sign-off |
| **Output** | Approved demo (prototype/mockups), review notes, sign-off |
| **Exit Criteria** | Stakeholders confirm "this is what we want to build," no unresolved objections remain, and approval evidence links to affected REQ/AC items |
| **Capabilities** | `design.prototype` for the clickable demo; `design.review` for the walkthrough |

**Demo Confirmation Checklist:**

```
Pre-demo preparation:
□ Clickable prototype covers all P0 flows
□ 6 interaction states have corresponding displays
□ Responsive key breakpoints have corresponding mockups
□ Dark mode (if applicable) has a plan

During demo:
□ Core user flows: interaction paths match user expectations
□ Information architecture: users can intuitively find feature entry points
□ Visual style: matches brand tone and product positioning
□ Interaction details: state transitions, animation rhythm, feedback timing
□ Edge cases: how empty states and error states are handled

Post-demo outputs:
□ Review notes (who attended, what feedback, what decisions)
□ Change item list (if any) with expected completion time
□ Sign-off: cleared to enter technical planning phase
```

**Why this step is mandatory:**
- Looking good in mockups ≠ actually usable when interactive
- Stakeholders often only discover missing scenarios when seeing an interactive prototype
- Design changes at this stage are cheap (Figma/prototype); changes after coding cost 10x+
- Provides a confirmed UI boundary for technical planning — tech choices depend on confirmed interaction patterns

---

## Phase 3: Technical Planning (Steps 4-5)

### Step 4: Technical Planning ← 📄📄

> Tech selection + architecture design. Produces separate frontend and backend design docs. The two docs are independent but aligned (API contract is their intersection point).

| Dimension | Content |
|-----------|---------|
| **Entry** | Requirements doc + UI design doc + demo confirmation passed |
| **Core Activities** | Frontend/backend tech selection and architecture, security/toolchain decisions, ADRs, and REQ/AC-to-decision/contract mapping |
| **Output** | **📄 Frontend Design Doc + 📄 Backend Design Doc** |
| **Exit Criteria** | Stack and architecture rationale are clear; frontend-backend contract points are identified; every committed requirement maps to decisions/contracts or approved N/A |
| **Capabilities** | `architecture.review`; use an independent reviewer for high-risk decisions |

> **Note**: Step 4 produces architecture-level design docs. Detailed database design and API contracts are completed in Step 7 "Module Tech Docs." Step 4 sets the overall direction and boundaries; Step 7 refines to executable DDL and OpenAPI Spec.

> **Frontend template**: `references/templates/frontend-design.md`
> **Backend template**: `references/templates/backend-design.md`

---

### Step 5: Module Decomposition

> Based on frontend/backend design docs, decompose the system into independent, parallelizable modules.

| Dimension | Content |
|-----------|---------|
| **Entry** | Frontend design doc + backend design doc |
| **Core Activities** | Domain identification, capability-to-module reconciliation, boundary definition, dependency analysis, parallel strategy formulation |
| **Output** | Module list + dependency graph |
| **Exit Criteria** | Each module has clear responsibilities, well-defined boundaries, no circular dependencies |
| **Capabilities** | `architecture.review`; optionally `spec.change` for module deltas |

**Module Decomposition Principles:**
- Organize by business domain, not technical layer
- High cohesion, low coupling: tight within modules, loose between modules
- Each module has its own: routes + services + data access + types
- No circular dependencies: determine development order by topological sort

**Module List Template:**

```markdown
# Module List

| Module | CAP / REQ IDs | Responsibility | Out of Scope | Frontend Scope | Backend Scope | Depends On |
|---|---|---|---|---|---|---|
| auth | CAP-AUTH / REQ-AUTH-* | AuthN & AuthZ | No user profiling | Login/Register/Password reset pages | JWT/Session/Permission middleware | — |
| user | CAP-USER / REQ-USER-* | User management | No auth | Profile settings/Admin panel | User CRUD/Roles | auth |
| ... | | | | | | |

## Dependency Graph
```
auth ──→ user ──→ core-business
  └──→ notification
```
Modules with no dependencies can be developed in parallel: auth + notification can start simultaneously.
```

---

## Phase 4: Development Plan (Step 6)

### Step 6: Development Plan ← 📄

> Based on module decomposition, create an executable, trackable development plan.

| Dimension | Content |
|-----------|---------|
| **Entry** | Module list + dependency graph + frontend/backend design docs |
| **Core Activities** | Task breakdown, origin mapping, dependency analysis, planned code/test evidence, estimation, ownership, milestones |
| **Output** | **📄 Development Plan Document** (task list + timeline + dependency graph + milestones) |
| **Exit Criteria** | Each task ≤ 1 day, dependencies are acyclic, P0 has completion dates, and every task has a REQ/AC, BUG, TECH, SEC, or OPS origin |
| **Capabilities** | `planning.decompose` |

> **Template**: `references/templates/development-plan.md`

---

## Phase 5: Module Technical Docs (Step 7)

### Step 7: Module Technical Docs ← 📄📄

> Before coding each module, produce database design and API contract docs. Step 4 set the architectural direction; Step 7 refines to executable DDL and endpoint definitions.

| Dimension | Content |
|-----------|---------|
| **Entry** | Frontend/backend design docs + module list + dependency graph |
| **Core Activities** | Database/index/migration design, API/event contracts, errors, and REQ/AC/ADR-to-contract/test mapping |
| **Output** | **📄 Database Design Doc + 📄 API Doc** |
| **Exit Criteria** | Tables/endpoints and schemas are complete, indexes cover core queries, and every committed requirement has valid data/API/contract links where applicable |
| **Capabilities** | `architecture.review` + `database.review` (DB); optionally `spec.change` (API) |

> **Document timing**:
> - DB Doc + API Doc: produced at Step 7 (before coding, as frontend-backend contract)
> - Test Doc: produced at Step 12 (after all testing is complete)

> **DB template**: `references/templates/database-design.md`
> **API template**: `references/templates/api-design.md`

---

## Phase 6: Environment Setup (Step 8)

### Step 8: Development Environment Setup ← 📄

> Before coding starts, get infrastructure ready — database instance running, migrations executed, seed data loaded, staging environment deployable. Environment not ready = building on sand.

| Dimension | Content |
|-----------|---------|
| **Entry** | Database design doc + API doc + development plan |
| **Core Activities** | Database/migration/seed setup, staging and CI/CD integration, and linkage to NFR/OPS/SEC origins |
| **Output** | **📄 Staging Deployment Doc**, usable staging environment, initialized database |
| **Exit Criteria** | Developers can connect locally, staging auto-deploys, seed data resets, and environment evidence traces to valid origins |
| **Capabilities** | `delivery.release` + `database.review` |

> **Template**: `references/templates/staging-deploy.md`

#### 8a. Database Initialization

```
Database Initialization Flow:
┌─────────────────────────────────────────────────┐
│ 1. Database Instance Creation                    │
│    ├── Dev: local Docker / local install         │
│    ├── Staging: cloud service / self-hosted      │
│    └── Production: HA cluster (handled Step 13)  │
│                                                   │
│ 2. Initial Migration Execution                    │
│    ├── Execute all up migration scripts          │
│    ├── Verify all tables created successfully    │
│    └── Verify indexes and constraints active     │
│                                                   │
│ 3. Seed Data                                     │
│    ├── Dev: abundant simulated data              │
│    ├── Staging: fixed datasets for E2E           │
│    └── Seed scripts idempotent (re-runnable)     │
│                                                   │
│ 4. Database Init Verification                     │
│    ├── Connection test: local + staging reachable│
│    ├── Migration rollback test: down works       │
│    └── Seed reset: one-click reset to known state│
└─────────────────────────────────────────────────┘
```

**Database Init Checklist:**
- [ ] Dev database connectable (localhost)
- [ ] Staging database connectable
- [ ] All up migration scripts executed successfully
- [ ] Rollback down scripts executable and verified
- [ ] Seed data loaded, key business scenarios covered
- [ ] `setup.sh` or `make setup` completes all above in one command
- [ ] New team member can complete env init within 5 minutes

#### 8b. Staging Environment Deployment

```
Staging Deployment Flow:
┌─────────────────────────────────────────────────┐
│ 1. Staging Environment Setup                     │
│    ├── Server/container orchestration config     │
│    ├── Database instance (isolated from dev)     │
│    ├── Cache/queue/storage middleware            │
│    └── Domain + SSL certs (staging.xxx.com)     │
│                                                   │
│ 2. CI/CD Integration with Staging                │
│    ├── Push feature branch → auto-deploy staging │
│    ├── Env var config (dev/staging isolated)     │
│    └── Auto smoke tests after deploy            │
│                                                   │
│ 3. Environment Verification                      │
│    ├── Health check endpoint accessible          │
│    ├── Core APIs reachable                       │
│    └── Frontend pages accessible                 │
└─────────────────────────────────────────────────┘
```

---

## Phase 7: Module Development (Step 9)

### Step 9: Module Development Execution

> Each module follows "backend business logic + API first → frontend builds UI against API → wiring → E2E verification." Dependency-free modules can run in parallel.

| Dimension | Content |
|-----------|---------|
| **Entry** | Environment ready + module tech docs (DB + API) |
| **Core Activities** | Backend/frontend TDD, integration/E2E, and replacement of planned trace links with actual code symbols and test evidence |
| **Output** | Runnable code, test code, passing CI |
| **Exit Criteria** | P0 works, coverage ≥80%, integration/E2E pass, and completed tasks map backward to valid origins and forward to code/test evidence |
| **Capabilities** | `development.tdd`, `qa.browser`, and risk-triggered specialist review |

**Commit Standards (enforced within each module):**

```
Commit granularity: one commit = one logical change, independently revertible
Commit message format (Conventional Commits):
  <type>(<scope>): <subject>

Types: feat / fix / refactor / perf / test / docs / chore / style / ci
Examples:
  feat(auth): add JWT refresh token rotation
  fix(order): prevent double-submit on payment callback
  test(api): add integration tests for POST /users edge cases

Pre-commit self-check (automated or manual):
  □ lint passes
  □ type-check passes
  □ relevant tests pass
  □ no console.log / debug code
  □ no hardcoded secrets
```

#### 9a. Backend Development

> Write tests first, then code. Data layer → service layer → API layer, bottom-up.

```
Backend Dev Flow (per module):
1. TDD Coding
   RED → GREEN → REFACTOR cycle

2. Unit Tests
   Coverage ≥ 80%
   Cover: normal inputs / boundary values / invalid inputs / dependency failures
   Naming: test('[module] behavior description', () => {})
   Structure: Arrange → Act → Assert

3. Integration Tests
   Use real test database (do not mock)
   Each API endpoint covers: 200/400/401/403/404/409
   Tests independent, no ordering dependency
```

**Coding Order (bottom-up):**
```
1. Data Layer (ORM models / Repository / migration scripts)
2. Service Layer (business logic / validation / error handling)
3. API Layer (routes / middleware / serialization / error responses)
```

#### 9b. Frontend Development

> Build type-safe UI components against the published API contract.

```
Frontend Dev Flow (per module):
1. Component Coding
   Design tokens → base components → layouts → pages → API integration
   Compound components / Container-Presentational separation

2. Component Unit Tests
   Utility functions and hooks: logic tests
   Complex interaction components: behavior tests
   Key UI surfaces: visual regression screenshots

3. Visual Regression Tests
   Screenshot key breakpoints: 320 / 768 / 1024 / 1440
   Test core pages and critical states
   Dark mode (if applicable)
```

**Frontend Component Checklist:**
- [ ] Uses design system tokens
- [ ] 6 interaction states complete
- [ ] Empty and loading states have design
- [ ] Responsive adaptation
- [ ] Semantic HTML + ARIA labels
- [ ] Keyboard navigation functional
- [ ] reduced-motion adaptation
- [ ] Accessibility self-check passed (`review.accessibility`)

#### 9c. Module Integration

> Once frontend and backend modules are both complete, wire them together and verify end-to-end.

```
Module Integration Flow:
1. Frontend-Backend Wiring
   Frontend connects to real API → verify request/response match → verify error handling

2. Deploy to Staging
   CI auto-deploys to staging → execute DB migrations → verify env vars

3. E2E Tests
   Core flows:
   ├── Register → Verify → Login → Onboarding
   ├── Login → Core CRUD → Logout
   ├── Permission tests
   └── Session expiry handling
   Multi-browser: Chrome / Firefox / Safari
   Tools: Playwright / Cypress
```

**Module Parallel Strategy:**
```
Dependency-free modules start in parallel
Dependent modules follow topological sort
Frontend + backend of same module can partially overlap (backend produces API contract first, frontend builds against mock in parallel)
```

---

## Phase 8: Quality Verification (Steps 10-12)

### Step 10: Code Review

> After each module is developed, run automated review tools for local self-check (pre-PR review). Fix issues before entering Step 11 to create PR for formal review.

| Dimension | Content |
|-----------|---------|
| **Entry** | Module development complete + tests passing |
| **Core Activities** | Automated security review, code quality review, design consistency review, performance review, commit convention check |
| **Output** | Review report (pass/pass-with-changes/reject), review comments, fix commits |
| **Exit Criteria** | No CRITICAL or HIGH level unresolved issues; commit messages follow Conventional Commits |
| **Capabilities** | `review.code` in independent context plus risk-triggered specialist review |

> **Step 10 vs Step 11 relationship**: Step 10 = automated self-check (run review agents locally/on branch, no PR needed) → fix issues → Step 11 = create PR → human reviewer review → merge. Self-check passing is the prerequisite for PR creation — avoids wasting reviewer time on issues automation can catch.

**Review Checklist:**

```
Security (CRITICAL — any single failure blocks merge):
□ No hardcoded secrets/passwords/tokens
□ User input validated and sanitized
□ SQL/NoSQL injection risk addressed
□ AuthN/AuthZ logic correct
□ Sensitive operations have audit logging

Code Quality (HIGH):
□ Functions < 50 lines, files < 800 lines
□ Nesting ≤ 4 levels
□ Clear, meaningful naming
□ Error handling explicit and complete
□ No debug code

Design Consistency (HIGH):
□ UI matches design mockups
□ Design system tokens used
□ Interaction states complete
□ Responsive adaptation correct

Performance (MEDIUM):
□ No N+1 queries
□ List queries have pagination
□ Heavy computation in async queues

Traceability (HIGH):
□ Changed behavior maps to a REQ/AC or classified BUG/TECH/SEC/OPS origin
□ Planned code/test links were replaced with actual evidence
□ No unexplained orphan task/test or stale link remains
□ Source requirements changed when product semantics changed
```

---

### Step 11: PR Management

> PR creation, description, review cycle, merge — traceable, revertible delivery units.

| Dimension | Content |
|-----------|---------|
| **Entry** | Code review passed branch |
| **Core Activities** | PR creation, traceability delta, test/risk evidence, review iteration, conflict resolution, merge |
| **Output** | Merged PR (with full context) |
| **Exit Criteria** | CI green, review approved, no conflicts, and PR origin/code/test/ledger links are complete |
| **Capabilities** | `delivery.release` — merge-base check, tests, diff review, and contextual PR |

```
PR Title: <type>(<scope>): <brief description>

PR Description Template:
## Background — What problem does this solve
## Traceability — Affected REQ/AC/TASK/BUG/TECH/SEC/OPS IDs
## Changes — What was done
## Code Surfaces — Actual paths and symbols
## Test Plan — Backend/Frontend/E2E test checklist
## Evidence — TEST IDs, results, reports, screenshots
## Screenshots/Recordings — Before/After (if UI changes)
## Risk Assessment — What changed / Rollback plan
## Documentation — Baseline, contracts, and ledger updates

Review Cycle:
Submit PR → Request review → Address feedback → Re-request review → Approve → Merge
```

---

### Step 12: Test Summary ← 📄

> Aggregate all test layer coverage and results into a deliverable test document.

| Dimension | Content |
|-----------|---------|
| **Entry** | All modules complete + unit tests + integration tests + E2E + perf tests + security scan |
| **Core Activities** | AC-to-TEST reconciliation, coverage/results, orphan/stale analysis, performance/security evidence, known issues |
| **Output** | **📄 Test Document** |
| **Exit Criteria** | All layers report, every committed AC has accepted evidence, no blocking bug remains, and performance meets targets |
| **Capabilities** | deterministic QA evidence + `review.security`, `review.performance`, and `review.accessibility` |

> **Template**: `references/templates/testing.md`

---

## Phase 9: Production Deployment (Step 13)

### Step 13: Production Deployment ← 📄

> Deliver verified code safely to production. Step 8's staging deploy solves "where to dev/test"; Step 13 solves "how to ship to users."

| Dimension | Content |
|-----------|---------|
| **Entry** | All tests passing + PR merged + review approved + staging verified |
| **Core Activities** | Build/package, migration, rollout, rollback, release-manifest closure, deployment and production evidence |
| **Output** | **📄 Production Deployment Document + Release Manifest**, production running application |
| **Exit Criteria** | Health/smoke checks pass, monitoring is configured, and committed scope has no missing/stale/blocked implementation, test, or release edge |
| **Capabilities** | `delivery.release` |

> **Template**: `references/templates/production-deploy.md`

---

## Phase 10: Operations (Steps 14-15)

### Step 14: Production Monitoring

> Continuously observe system health post-deployment, quickly detect and locate issues.

| Dimension | Content |
|-----------|---------|
| **Entry** | Production deployment complete |
| **Core Activities** | Monitoring/log/trace/audit analysis, alert response, and REQ-to-production-signal mapping |
| **Output** | Monitoring dashboards, alert configuration, launch observation report |
| **Exit Criteria** | 24h post-launch has no P0 alerts, core metrics are stable, and critical released requirements map to production signals or approved exceptions |
| **Capabilities** | `operations.monitor` |

**Four Monitoring Layers:**

```
Layer 1: Infrastructure (CPU / Memory / Disk / Network / Certificate expiry)
Layer 2: Application Performance (QPS / P50 P95 P99 latency / Error rate / Slow queries)
Layer 3: Business Metrics (Core feature success rate / Conversion funnel / Key data dashboards)
Layer 4: User Experience (CWV / Crash rate / Page load time / User feedback volume)
```

---

### Step 15: Iteration Retrospective

> Learn from data and experience to drive improvements in the next iteration.

| Dimension | Content |
|-----------|---------|
| **Entry** | 1-2 weeks of post-launch data accumulated |
| **Core Activities** | Data/incident analysis, retrospective, trace-gap closure, tech-debt origins, next-iteration adjustment |
| **Output** | Iteration retrospective report |
| **Exit Criteria** | Lessons and owned actions are clear; affected stale/blocked links are closed or carried forward with valid BUG/TECH/OPS/REQ origins |
| **Capabilities** | `operations.retro` |

---

## Document Output Mapping

| Step | Document | Contents |
|------|----------|----------|
| 1. Clarify Reqs | 📄 Requirements Doc | Source-grounded capability tree, stable IDs, state transitions, operational semantics, acceptance criteria, quality attributes, impacts and decisions |
| 2. UI/UX Design | 📄 UI Design Doc | Design system plus REQ/AC-to-flow/screen/state coverage |
| 3. Demo Confirm | (Review record) | Demo notes, feedback, sign-off |
| 4. Tech Planning | 📄 Frontend + Backend Design | Architecture and REQ/AC-to-decision/contract/planned-verification mapping |
| 5. Module Decomp | (Merged into design docs) | Module list, responsibility boundaries, dependency graph |
| 6. Dev Plan | 📄 Dev Plan Doc | Stable TASK IDs, origins, dependencies, planned code/test evidence, milestones |
| 7. Module Tech Docs | 📄 DB Doc + API Doc | Data/API contracts traced to REQ/AC/ADR and contract tests |
| 8. Env Setup | 📄 Staging Deploy Doc | Staging architecture, DB init flow, CI/CD config, seed data |
| 9. Module Dev | (Code + tests) | Runnable code, backend unit/integration tests, frontend component/VR tests |
| 10+11+12. Review→PR→Test | 📄 Test Doc | AC-to-TEST coverage, PR evidence, orphan/stale links, results and known issues |
| 13. Prod Deploy | 📄 Production Deploy + Release Manifest | Baseline, committed scope, PR/build/test/deployment/production evidence |

Cross-cutting: major-version manifest + traceability ledger/coverage/exceptions are
updated whenever an affected phase artifact changes.

---

## Quality Gates

```
Step 1 → 2: Requirements pass Definition of Ready; no hidden blocker remains
Step 2 → 3: Design system documented, REQ/AC mapped, prototype available → 🚪 Demo Confirmation
Step 3 → 4: Stakeholder sign-off linked → Enter technical planning
Step 7 → 8: DB + API design complete and traced → 🚪 Environment Readiness Check
Step 8 → 9: Database connectable, staging deployable → Enter development
Step 9 → 10: All modules complete + implementation/test links valid → 🚪 Code Review Gate
Step 10 → 11: No CRITICAL/HIGH issue or unexplained trace gap
Step 12 → 13: All committed ACs verified → 🚪 Production Release Approval
Step 13 → 14: Release manifest closed and smoke tests pass
```

---

## Project Size Tailoring

### Small Projects (1-2 people, 1-2 weeks) → ~9 steps

```
1. Clarify Reqs → Requirements Doc (lean)
2. UI/UX Design → UI Design Doc (lean)
3. Demo Confirm → Quick review
4. Tech Planning → Frontend + Backend design merged (lean)
5. (Skip module decomposition)
6. Dev Plan → Lean task list
7. (Skip independent module tech docs — merge into step 4)
8. Env Setup → Docker Compose one-command (lean)
9. Module Dev → Backend TDD + Frontend Dev + E2E (1-2 flows)
10+11+12. (Simplify: merge directly, CI reports replace test doc)
13. Prod Deploy (simplified single-step deploy)
14. Monitoring → Sentry or similar lightweight
15. (Skip independent retro)

Docs: phase documents may be merged and lean, but committed scope still needs a
version/release reference and a minimal origin→code→test→PR/release ledger.
```

### Medium Projects (5-10 people, 1-3 months) → Full 15 Steps

### Large Projects (10+ people, 3+ months) → 15 Steps + Extensions

```
Each step adds:
- Formal review/sign-off sessions
- Peer review
- Technical spike nodes
- Dedicated security review
- Dedicated performance load testing
- Dedicated canary planning
- User Acceptance Testing (UAT) node
```
