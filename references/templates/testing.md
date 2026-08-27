# Test Document Template

```markdown
# Test Documentation — [Project Name]

> **Version line / release target**: [v2 / 2.0.0]
> **Traceability ledger**: [Path or tracker URL]

## Acceptance Traceability

| TEST ID | REQ / AC IDs | Test layer | Test path/name or case URL | Environment/build | Result | Evidence |
|---|---|---|---|---|---|---|
| TEST-[AREA]-001 | | | | | Pass / Fail / Blocked | |

Every committed AC has at least one accepted automated test or approved manual
evidence. Record orphan tests, uncovered ACs, and stale mappings explicitly.

## 1. Test Strategy Overview
| Test Layer | Tool | Coverage Target | Actual Coverage | Status |
|------------|------|-----------------|-----------------|--------|
| Backend Unit | Vitest/Jest/pytest | ≥80% | XX% | ✅/❌ |
| Backend Integration | Supertest/httpx | 100% API | XX% | ✅/❌ |
| Frontend Component | Vitest + Testing Library | ≥80% | XX% | ✅/❌ |
| Visual Regression | Playwright screenshots | Key pages | X/X | ✅/❌ |
| E2E | Playwright | Core flows | X/X pass | ✅/❌ |
| Performance | Lighthouse/k6 | LCP<2.5s | X.Xs | ✅/❌ |
| Security Scan | Trivy/ZAP | 0 HIGH | X HIGH | ✅/❌ |
| Accessibility | axe | WCAG 2.1 AA | X errors | ✅/❌ |

## 2. Backend Tests — Coverage details, integration test case list
## 3. Frontend Tests — Component test coverage, visual regression comparison
## 4. E2E Tests — Scenario list, multi-browser results matrix
## 5. Performance Tests — Lighthouse / API load test / comparison with previous
## 6. Security Tests — Dependency scan, OWASP Top 10 check
## 7. Known Issues
| BUG ID | Affected REQ / AC / TEST IDs | Description | Severity | Status | Target Fix Version |
|---|---|---|---|---|---|
```
