# Staging Environment Deployment Document Template

```markdown
# Staging Environment Deployment — [Project Name]

> **Version line / release target**: [v2 / 2.0.0]
> **Baseline manifest**: [Path]
> **Source NFR / OPS / SEC IDs**: [IDs]
> **Traceability ledger**: [Path or tracker URL]

## 1. Staging Architecture
- Topology diagram
| Component | Config | Address | Notes |
|-----------|--------|---------|-------|
| App server | | staging.xxx.com | |
| Database | | staging-db.xxx.com | |
| Cache | | staging-cache.xxx.com | |
| Queue | | | |
| Storage | | | |

## 2. Database Initialization
### Development Environment
```bash
# One-command local database startup
docker compose up -d db
# Run migrations
pnpm db:migrate
# Load seed data
pnpm db:seed
# Reset to clean state
pnpm db:reset
```

### Staging Environment
- Database instance info
- Migration execution method: CI auto / manual
- Seed data location: `prisma/seeds/test/`

## 3. CI/CD Configuration
```yaml
# Staging deploy pipeline
staging-deploy:
  trigger: push to feature branches
  steps:
    1. Lint & Type-Check
    2. Unit Tests
    3. Security Scan (SAST + Dependency)
    4. Build
    5. Deploy to Staging
    6. Smoke Tests
```

## 4. Environment Variables
| Variable | Development | Staging | Notes |
|----------|-------------|---------|-------|
| DATABASE_URL | localhost:5432 | staging-db:5432 | DB connection |
| API_BASE_URL | localhost:3000 | staging-api.xxx.com | API address |

## 5. Environment Reset
- How to reset staging to clean state
- How to rollback database migrations
- How to reload seed data

## 6. Access Information
- Staging URLs
- Test accounts
- VPN/firewall requirements (if any)
```
