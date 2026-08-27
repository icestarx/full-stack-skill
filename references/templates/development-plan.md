# Development Plan Document Template

```markdown
# Development Plan — [Project Name]

> **Version line**: [v1 / v2 / ...]
> **Release target**: [Release or TBD]
> **Change work item**: [CHG-* path / tracker URL]
> **Traceability ledger**: [Path or tracker URL]

## 1. Milestones
| Milestone | Date | Contents | Delivery Criteria |
|-----------|------|----------|-------------------|
| M1: Infrastructure | D+3 | Project scaffold + CI skeleton + env vars | Local runnable, CI green |
| M2: Env Setup | D+5 | Database init + staging deploy | Staging available |
| M3: Auth Module | D+9 | Register/Login/Token refresh API | Integration tests pass |
| M4: Core API | D+15 | Core business CRUD API | Contract/integration checks and risk-based coverage pass |
| M5: Frontend Skeleton | D+10 | Routes + layouts + base components + design tokens | Pages accessible |
| M6: Frontend Pages | D+18 | Core pages + API integration | Component tests pass |
| M7: Integration | D+21 | Full chain wiring + E2E tests | E2E core flows pass |
| M8: Test Completion | D+24 | Coverage达标 + perf test + security scan | Test doc complete |
| M9: Production Launch | D+26 | Prod deploy + monitoring + smoke tests | Prod stable 24h |

## 2. Task Breakdown

Every task needs a stable `TASK-*` ID and at least one origin: `REQ/AC`, `BUG`,
`TECH`, `SEC`, or `OPS`. Replace planned code/test surfaces with actual evidence
during implementation.

### Phase 1: Infrastructure (D1-D3)
| Task ID | Origin IDs | Task | Planned code / test evidence | Type | Est. | Depends | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| TASK-INFRA-001 | TECH-* / OPS-* | Create monorepo + build toolchain | [Paths/checks] | Backend | 2h | — | | |
| TASK-INFRA-002 | TECH-* | Frontend project scaffold | [Paths/checks] | Frontend | 2h | TASK-INFRA-001 | | |
| TASK-INFRA-003 | OPS-* | Configure CI pipeline | [Pipeline/check] | General | 3h | TASK-INFRA-001 | | |
| TASK-INFRA-004 | SEC-* | Env var templates + secrets mgmt | [Paths/security check] | Backend | 1h | TASK-INFRA-001 | | |

### Phase 2: Environment Setup (D4-D5)
| Task ID | Origin IDs | Task | Planned code / test evidence | Type | Est. | Depends | Owner | Status |
|---|---|---|---|---|---|---|---|---|
| TASK-ENV-001 | OPS-* / REQ-* | DB instance creation + initial migration | [Migration/check] | Backend | 2h | TASK-INFRA-001 | | |
| TASK-ENV-002 | TEST-* / REQ-* | Seed data script + execution | [Seed/check] | Backend | 2h | TASK-ENV-001 | | |
| TASK-ENV-003 | OPS-* | Staging deploy + CI/CD integration | [Pipeline/smoke test] | DevOps | 3h | TASK-INFRA-003, TASK-ENV-001 | | |

[... subsequent phases ...]

## 3. Dependency Graph
## 4. Parallel Strategy
## 5. Risks & Buffer
## 6. Daily Checkpoints
```
