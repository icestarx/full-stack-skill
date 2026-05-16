# Development Plan Document Template

```markdown
# Development Plan — [Project Name]

## 1. Milestones
| Milestone | Date | Contents | Delivery Criteria |
|-----------|------|----------|-------------------|
| M1: Infrastructure | D+3 | Project scaffold + CI skeleton + env vars | Local runnable, CI green |
| M2: Env Setup | D+5 | Database init + staging deploy | Staging available |
| M3: Auth Module | D+9 | Register/Login/Token refresh API | Integration tests pass |
| M4: Core API | D+15 | Core business CRUD API | Integration tests pass, coverage 80% |
| M5: Frontend Skeleton | D+10 | Routes + layouts + base components + design tokens | Pages accessible |
| M6: Frontend Pages | D+18 | Core pages + API integration | Component tests pass |
| M7: Integration | D+21 | Full chain wiring + E2E tests | E2E core flows pass |
| M8: Test Completion | D+24 | Coverage达标 + perf test + security scan | Test doc complete |
| M9: Production Launch | D+26 | Prod deploy + monitoring + smoke tests | Prod stable 24h |

## 2. Task Breakdown
### Phase 1: Infrastructure (D1-D3)
| ID | Task | Type | Est. | Depends | Owner | Status |
|----|------|------|------|---------|-------|--------|
| INFRA-01 | Create monorepo + build toolchain | Backend | 2h | — | | |
| INFRA-02 | Frontend project scaffold | Frontend | 2h | INFRA-01 | | |
| INFRA-03 | Configure CI pipeline | General | 3h | INFRA-01 | | |
| INFRA-04 | Env var templates + secrets mgmt | Backend | 1h | INFRA-01 | | |

### Phase 2: Environment Setup (D4-D5)
| ID | Task | Type | Est. | Depends | Owner | Status |
|----|------|------|------|---------|-------|--------|
| ENV-01 | DB instance creation + initial migration | Backend | 2h | INFRA-01 | | |
| ENV-02 | Seed data script + execution | Backend | 2h | ENV-01 | | |
| ENV-03 | Staging deploy + CI/CD integration | DevOps | 3h | INFRA-03, ENV-01 | | |

[... subsequent phases ...]

## 3. Dependency Graph
## 4. Parallel Strategy
## 5. Risks & Buffer
## 6. Daily Checkpoints
```
