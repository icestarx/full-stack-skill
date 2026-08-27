# Production Deployment Document Template

```markdown
# Production Deployment — [Project Name]

> **Version line / release**: [v2 / 2.0.0]
> **Baseline manifest**: [Path]
> **Change work item**: [CHG-* path / tracker URL]
> **Release manifest**: [Use `references/templates/release-manifest.md`]
> **Traceability ledger**: [Path or tracker URL]

## 1. Production Architecture
- Deployment topology diagram
- High availability plan
| Component | Config | Address | Backup Strategy |
|-----------|--------|---------|-----------------|
| App server | | | |
| Database | | | Daily automatic backup |
| Cache | | | |
| CDN | | | |

## 2. CI/CD Pipeline
1. Lint & Type-Check
2. Backend Unit Tests
3. Backend Integration Tests
4. Frontend Component Tests
5. Build (Frontend + Backend)
6. Deploy Staging (automatic)
7. E2E Tests on Staging (automatic)
8. Deploy Production — **Manual approval required**
9. Smoke Tests (automatic)
10. Health Check + Monitoring Confirmation

## 3. Database Migrations (Production)
- Migration execution method: auto before deploy
- Recovery: tested rollback or roll-forward; use forward repair when destructive down migration is unsafe
- Large table change strategy (>1M rows): online DDL / maintenance window
- Migration execution order: run migrations first → then deploy new code (backward compatible)

## 4. Environment Variables
| Variable | Description | Production Source | Sensitive |
|----------|-------------|-------------------|-----------|
| DATABASE_URL | DB connection string | Vault/KMS | Yes |
| JWT_SECRET | JWT signing key | Vault/KMS | Yes |

## 5. Release Strategy
### Standard Release
1. Merge PR to main → CI auto-triggers
2. Auto-deploy to staging → E2E auto-executes
3. Manual approval (production gate)
4. Production deploy: canary 5% → observe 10min → 50% → observe 10min → 100%
5. Smoke tests auto-execute

### Feature Flags
- Deploy high-risk features to production dark (flag off), verify infra compatibility
- Gradually enable for % of users: internal → 5% → 25% → 100%
- Disable flag on anomaly (no rollback needed), effective in seconds
- Centralized flag management (LaunchDarkly / Flagsmith / self-built)
- Regularly clean up old flags that have been 100% enabled for N+ days

### Canary Release
- Deploy new version to 1-2 instances first
- Observe 15 minutes: error rate / latency / business metrics
- Metrics normal → full rollout
- Metrics abnormal → auto-rollback

### Rollback Testing
- Before each release, rehearse rollback on staging
- Verify: deploy new version → trigger rollback → confirm DB down migration executable → smoke tests pass
- Record rollback duration (target < 5 minutes)

### Emergency Rollback
1. Trigger rollback: `gh run rerun <previous-version-run-id>` or revert commit
2. Database rollback (if needed): execute down migration
3. Smoke test verification
4. Notify team + record incident

## 6. Monitoring & Alerting
- Dashboard links
- Key alert rules:
  - Error rate > 1% → P1 alert
  - API P95 latency > 500ms → P2 alert
  - DB connection count > 80% → P2 alert
  - Disk usage > 85% → P1 alert
- Oncall rotation
- Escalation path

## 7. Traceability Closure

- All committed REQ/AC items map to accepted TEST evidence.
- PRs, commits, build artifacts, deployment IDs, and approvals are pinned in the release manifest.
- Critical released behavior maps to production signals or an approved `N/A` exception.
- No missing, stale, or blocked delivery edges remain without release-owner approval.
```
