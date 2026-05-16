# Full-Stack Process × Skills Mapping Matrix

> Read this reference when you need to understand **why** a specific skill is recommended for a step, or when you need to choose between alternative skills.

## Three Skill Ecosystems

| Dimension | Superpowers | gstack | OpenSpec |
|-----------|-------------|--------|----------|
| **Core Philosophy** | Methodology discipline — formal checkpoints at every step | Product-driven — complete loop from idea to operations | Change management — structured artifact-driven |
| **Best At** | Development discipline (planning/TDD/review/verification) | Product discovery + design system + deployment + retro | Lightweight artifact management + contract spec deltas |
| **Key Blindspots** | No product discovery, no design system, no deployment/ops | Heavier preamble, more interactive questions | No QA, no deployment, no monitoring, no retro |

**Conclusion: The three are complementary, not competitive.** Best practice for the full-stack pipeline is combining them.

---

## Per-Step Skill Mapping

### Step 1: Clarify Requirements

| Preferred | `/office-hours` (gstack) + `superpowers:brainstorming` |
|-----------|--------------------------|
| **Rationale** | office-hours uses six-prompt framework (need authenticity, current alternatives, wedge focus, user observation, future adaptation) to penetrate surface-level needs; brainstorming outputs structured spec docs |
| **Alternative** | `/openspec:propose` — produces proposal.md (what & why = core requirements doc) |
| **Scope Calibration** | `/plan-ceo-review` (gstack) — evaluates whether scope is right-sized, four modes (expand/keep/reduce) |
| **Output** | 📄 Requirements Document |

### Step 2: UI/UX Design Specification

| Preferred | `/design-consultation` (gstack) |
|-----------|--------------------------|
| **Rationale** | Most complete design system solution: information architecture → interaction evaluation → color/typography/spacing/motion + preview pages + AI mockups. Has anti-slop rules |
| **Supplement** | `/plan-design-review` (gstack) — interaction dimension 0-10 scoring, covers state coverage and flow completeness |
| **Implementation** | `/design-html` (gstack) — converts approved design to production HTML/CSS |
| **Output** | 📄 UI Design Document (DESIGN.md) |

### Step 3: Demo Confirmation

| Preferred | `/design-review` (gstack) + Claude artifacts |
|-----------|--------------------------|
| **Rationale** | design-review does visual QA and design walkthrough; Claude artifacts generate clickable prototypes for stakeholder interaction |
| **Supplement** | `superpowers:brainstorming` — aids decision-making when feedback is conflicting |
| **Key Activity** | Prototype demo → stakeholder review → feedback collection → iteration → sign-off |
| **Exit Criterion** | Product/business/tech leads confirm "this is what we want to build" |

### Step 4a: Frontend Design Document

| Preferred | **architect agent** |
|-----------|--------------------------|
| **Rationale** | Frontend tech stack selection, component architecture design, state management strategy, rendering strategy selection, performance strategy |
| **Supplement** | `/plan-eng-review` (gstack) — focuses on frontend architecture layering, data flow, testing strategy |
| **Output** | 📄 Frontend Design Document |

### Step 4b: Backend Design Document

| Preferred | `/plan-eng-review` (gstack) + **architect agent** |
|-----------|--------------------------|
| **Rationale** | plan-eng-review does architecture review (layering/data flow/boundaries/testing/performance), architect agent does tech selection and ADRs |
| **Supplement** | `superpowers:brainstorming` — for architecture option comparison and decision discussion |
| **Output** | 📄 Backend Design Document |

### Step 5: Module Decomposition

| Preferred | **architect agent** |
|-----------|--------------------------|
| **Rationale** | Domain-driven design, module boundary identification, dependency analysis, parallel strategy formulation |
| **Supplement** | `/openspec:propose` — can organize spec deltas by module |
| **Output** | Module list + dependency graph |

### Step 6: Development Plan

| Preferred | `superpowers:writing-plans` |
|-----------|--------------------------|
| **Rationale** | Ultra-fine-grained task breakdown (2-5 min per task), with complete code, commands, and expected outputs. Auto-reviews coverage and type consistency |
| **Alternative** | `/openspec:propose` — produces tasks.md (implementation steps), coarser granularity but better for medium-uncertainty projects |
| **Output** | 📄 Development Plan Document |

### Step 7a: Database Design

| Preferred | **architect agent** + **database-reviewer agent** |
|-----------|--------------------------|
| **Rationale** | architect agent does entity identification and relationship modeling; database-reviewer reviews index strategy and query security |
| **Output** | 📄 Database Design Document (ER diagram + DDL + index strategy) |

### Step 7b: API Documentation

| Preferred | `/openspec:propose` |
|-----------|--------------------------|
| **Rationale** | Spec delta mechanism naturally suited for API contract management. Delta specs under `openspec/changes/<name>/specs/` auto-compare with main specs, sync on archive |
| **Alternative** | `superpowers:writing-plans` — can write API contracts into tasks, but lacks spec sync mechanism |
| **Output** | 📄 API Document (OpenAPI / GraphQL Schema / tRPC Router) |

### Step 8: Development Environment Setup

| Dimension | Preferred Skill |
|-----------|----------------|
| **Database Init** | **database-reviewer agent** — review migration script safety; manual/Docker execution |
| **Staging Deploy** | `/setup-deploy` (gstack) — one-time deploy platform and staging environment configuration |
| **CI/CD Integration** | `/setup-deploy` (gstack) — configure auto-deploy pipeline (with security scan step) |
| **Output** | 📄 Staging Environment Deployment Document |

**Key Checks:**
- database-reviewer: migration scripts have no destructive operations (DROP COLUMN / DROP TABLE)
- setup-deploy: staging environment and production environment config structures match (scale differs)
- Seed data covers all business scenarios needed for P0 features
- CI pipeline includes Security Scan step (SAST + dependency scan)

### Step 9a: Backend Development

| Activity | Preferred Skill |
|----------|----------------|
| **TDD Implementation** | `superpowers:subagent-driven-development` — per-task subagent → spec compliance review → code quality review → fix → re-review |
| **Unit Tests** | `superpowers:test-driven-development` — iron rule RED→GREEN→REFACTOR. Coverage ≥ 80% |
| **Integration Tests** | `/qa` Quick mode (gstack) — structured testing + auto-fix + re-verify. Use real database, do not mock |
| **Alternative Coding** | `/openspec:apply` — execute per-task from tasks.md, well-designed pause mechanism for evolving requirements |

### Step 9b: Frontend Development

| Activity | Preferred Skill |
|----------|----------------|
| **Component Implementation** | `superpowers:subagent-driven-development` — per-task subagent + code quality review |
| **Component Unit Tests** | `superpowers:test-driven-development` — utility/hook logic tests + component behavior tests |
| **Accessibility Self-Check** | **a11y-architect agent** — WCAG 2.2 review, keyboard navigation, ARIA labels, color contrast |
| **Visual Regression** | **e2e-runner agent** Playwright screenshots — key breakpoint screenshot comparison |

> **Commit Convention**: After each coding session, commits follow Conventional Commits (`feat/fix/refactor/test/docs/chore/perf/ci`), pre-commit checks lint + type-check + no debug code.

### Step 9c: Module Integration

| Activity | Preferred Skill |
|----------|----------------|
| **Frontend-Backend Integration** | Manual + API contract verification |
| **Deploy to Staging** | `/land-and-deploy` (gstack) — deploy to staging (configured in step 8) |
| **E2E Testing** | **e2e-runner agent** + `/qa` Standard/Exhaustive (gstack) — core flows multi-browser validation |

### Step 10: Code Review

| Preferred | `superpowers:requesting-code-review` |
|-----------|--------------------------|
| **Rationale** | Subagent independent review + three-tier classification (Critical/Important/Minor) + precise diff scope. Combine with `superpowers:receiving-code-review` for feedback handling |
| **Supplement** | `/review` (gstack) — focuses on SQL safety, LLM trust boundaries, conditional side effects |
| **Supplement** | Language-specific reviewers: **typescript-reviewer / python-reviewer / go-reviewer / rust-reviewer / swift-reviewer** |

### Step 11: PR Management

| Preferred | `/ship` (gstack) |
|-----------|--------------------------|
| **Rationale** | Complete PR automation: merge base branch → run tests → review diff → bump version → update CHANGELOG → create PR with templated description |
| **Follow-up** | `/land-and-deploy` (gstack) — merge PR → wait CI → deploy → health check |

### Step 12: Test Summary

| Preferred | `/qa-only` (gstack) + `/cso` (gstack) |
|-----------|--------------------------|
| **Rationale** | qa-only produces structured bug reports (health score + screenshots + repro steps). cso does security audit (OWASP + STRIDE + secrets scan) |
| **Supplement** | `superpowers:verification-before-completion` — every test report conclusion needs evidence |
| **Performance Testing** | `lighthouse_audit` (chrome-devtools MCP) — LCP/INP/CLS/FCP/TBT audit; k6 or **performance-optimizer agent** — API load testing |
| **Accessibility** | **a11y-architect agent** — WCAG 2.2 AA audit, axe scan |
| **Output** | 📄 Test Document |

### Step 13: Production Deployment

| Preferred | `/ship` → `/land-and-deploy` (gstack) |
|-----------|--------------------------|
| **Rationale** | Only system covering complete deployment chain: pass CI → review → bump version → PR → merge → deploy → health check. Step 13 focuses on production (step 8 handled testing environment) |
| **Key Distinction** | Canary/gradual rollout strategy, Feature Flags for dark launching, production DB migrations (needs approval), HA verification, rollback testing |
| **Output** | 📄 Production Deployment Document |

### Step 14: Production Monitoring

| Preferred | `/canary` (gstack) |
|-----------|--------------------------|
| **Rationale** | Only post-deploy monitoring: baseline screenshots → periodic checks → screenshot comparison + console errors + performance regression |
| **Supplement** | Superpowers and OpenSpec blind spot. External tools: Sentry + Datadog + Grafana |

### Step 15: Iteration Retrospective

| Preferred | `/retro` (gstack) |
|-----------|--------------------------|
| **Rationale** | Only retrospective tool: commit history analysis + work patterns + team contributions + trend tracking + action items, persistent history for cross-cycle comparison |
| **Supplement** | `/document-release` (gstack) — sync documentation after retro (README/ARCHITECTURE/CHANGELOG) |

---

## Coverage Density by Phase

```
                        Superpowers    gstack      OpenSpec    Agent
Clarify Reqs (S1)       ★★★★☆      ★★★★★       ★★★☆☆      ★★☆☆☆
UI/UX Design (S2)       ★★☆☆☆      ★★★★★       ☆☆☆☆☆      ★★☆☆☆
Demo Confirm (S3)       ★★★☆☆      ★★★★☆       ☆☆☆☆☆      ★★★☆☆
Tech Planning (S4)      ★★★☆☆      ★★★★★       ★★★★☆      ★★★★★
Module Decomp (S5)      ★★☆☆☆      ★★★☆☆       ★★★★☆      ★★★★★
Dev Plan (S6)           ★★★★★      ★★☆☆☆       ★★★★☆      ★★☆☆☆
Tech Docs (S7)          ★★☆☆☆      ★★★☆☆       ★★★★★      ★★★★★
Env Setup (S8)          ★★☆☆☆      ★★★★★       ☆☆☆☆☆      ★★★☆☆
Backend Dev (S9a)       ★★★★★      ★★★☆☆       ★★★★★      ★★★☆☆
Frontend Dev (S9b)      ★★★★★      ★★★☆☆       ★★★★☆      ★★★★☆
Integration (S9c)       ★★★☆☆      ★★★★★       ☆☆☆☆☆      ★★★★★
Code Review (S10)       ★★★★★      ★★★★☆       ☆☆☆☆☆      ★★★★☆
PR Mgmt (S11)           ★★★☆☆      ★★★★★       ☆☆☆☆☆      ★★☆☆☆
Test Summary (S12)      ★★★☆☆      ★★★★★       ☆☆☆☆☆      ★★★★☆
Prod Deploy (S13)       ★★★☆☆      ★★★★★       ☆☆☆☆☆      ★★☆☆☆
Monitoring (S14)        ☆☆☆☆☆      ★★★★★       ☆☆☆☆☆      ★★☆☆☆
Retro (S15)             ☆☆☆☆☆      ★★★★★       ☆☆☆☆☆      ★★☆☆☆
```

---

## Best Combination Strategy

```
Step 1  ─Clarify Reqs────── /office-hours + superpowers:brainstorming ──→ 📄 Requirements Doc
Step 2  ─UI/UX Design────── /design-consultation + /plan-design-review ──→ 📄 UI Design Doc
Step 3  ─Demo Confirm────── /design-review + Claude artifacts ──→ Review Passed
Step 4a ─Frontend Arch───── architect agent + /plan-eng-review ──→ 📄 Frontend Design Doc
Step 4b ─Backend Arch────── /plan-eng-review + architect agent ──→ 📄 Backend Design Doc
Step 5  ─Module Decomp───── architect agent ──→ Module List + Dependency Graph
Step 6  ─Dev Plan────────── superpowers:writing-plans ──→ 📄 Dev Plan Doc
Step 7a ─DB Design───────── architect + database-reviewer ──→ 📄 DB Design Doc
Step 7b ─API Design──────── /openspec:propose ──→ 📄 API Doc
Step 8  ─Env Setup───────── /setup-deploy + database-reviewer ──→ 📄 Staging Deploy Doc
Step 9a ─Backend Dev─────── superpowers:subagent-driven-dev + superpowers:tdd + /qa Quick
Step 9b ─Frontend Dev────── superpowers:subagent-driven-dev + superpowers:tdd + e2e-runner(VR)
Step 9c ─Integration─────── e2e-runner + /qa Standard (gstack)
Step 10 ─Code Review─────── superpowers:requesting-code-review + /review (gstack)
Step 11 ─PR Mgmt─────────── /ship (gstack)
Step 12 ─Test Summary────── /qa-only + /cso (gstack) ──→ 📄 Test Doc
Step 13 ─Prod Deploy─────── /ship → /land-and-deploy (gstack) ──→ 📄 Prod Deploy Doc
Step 14 ─Monitoring──────── /canary (gstack)
Step 15 ─Retro───────────── /retro (gstack)
```

## Three-Ecosystem Contribution Share

| Phase | Dominant System | Share |
|-------|----------------|-------|
| Requirements (S1) | gstack + Superpowers | 45% each |
| Design (S2-S3) | gstack | 80% |
| Tech Planning (S4-S5) | gstack + Agent + OpenSpec | ~30% each |
| Dev Plan (S6) | Superpowers | 80% |
| Module Tech Docs (S7) | OpenSpec + Agent | 40% each |
| Env Setup (S8) | gstack + Agent | 40% each |
| Backend Dev (S9a) | Superpowers + gstack | 40% each |
| Frontend Dev (S9b) | Superpowers + Agent | 40% each |
| Integration (S9c) | gstack + Agent | 40% each |
| Quality (S10-S12) | Superpowers + gstack | 40% each |
| Production Deploy (S13) | gstack | 90% |
| Operations (S14-S15) | gstack | 95% |

**gstack covers the two ends (product + operations), Superpowers covers the middle (development discipline), OpenSpec fills API contracts and artifact management. The three combined = complete full-stack pipeline.**
