# Backend Design Document Template

```markdown
# Backend Design — [Project Name]

## Traceability

| REQ / AC IDs | ADR / API / data contract | Backend decision | Planned code surface | Verification |
|---|---|---|---|---|
| | | | `src/path:Symbol` | TEST-* / planned |

## 1. Backend Tech Stack
| Layer | Choice | Version | Rationale |
|-------|--------|---------|-----------|
| Runtime/Language | Node.js / Python / Go / Rust | | |
| Framework | FastAPI / Hono / Express / Gin / ... | | |
| Database | PostgreSQL / MongoDB / ... | | |
| Cache | Redis / ... | | |
| Message Queue | BullMQ / Celery / ... | | |
| Object Storage | S3 / MinIO / ... | | |
| ORM/Query | Prisma / Drizzle / SQLAlchemy / ... | | |
| Build/Deploy | Docker + ... | | |

## 2. System Architecture
- Architecture diagram (C4 model: Context → Container → Component)
- System layers:
  ```
  Gateway Layer (Gateway/Reverse Proxy)
    → Application Layer (Routes/Middleware/Controllers)
      → Service Layer (Business Logic)
        → Data Layer (ORM/Repository)
          → Infrastructure Layer (DB/Cache/Queue/Storage)
  ```
- Each layer's responsibilities and boundaries

## 3. Authentication & Authorization
- Auth scheme: JWT / Session / OAuth2 / OIDC
- Token management: access token + refresh token, httpOnly cookie
- Authorization model: RBAC / ABAC / ReBAC
- Multi-tenant isolation strategy (if applicable)

## 4. Data Flow Design
### Read Path
```
Client → Gateway → Controller → Service → Cache(Hit?) → DB → Response
```
### Write Path
```
Client → Gateway → Controller → Validation → Service → DB → Event Publish → Response
```
### Async Path
```
Event → Queue → Consumer → External Service / Heavy Compute
```

## 5. API Architecture
- API style: REST / GraphQL / tRPC / gRPC
- Versioning strategy: URL prefix (/v1/) or Header
- Unified response envelope format
- Pagination convention (cursor-based / offset-based)
- Rate limiting strategy

## 6. Background Jobs
- Queue selection
- Job type inventory
- Idempotency strategy
- Retry strategy (exponential backoff)
- Dead letter queue handling

## 7. Caching Strategy
| Cache Layer | Tool | TTL | Invalidation Strategy |
|-------------|------|-----|-----------------------|

## 8. Security Architecture
- Secrets management (env vars / Vault / KMS)
- CORS policy
- CSRF protection
- SQL injection prevention (parameterized queries)
- Input validation (schema-based)
- Audit logging strategy
- Sensitive data encryption (PII)

## 9. Backend Project Structure
```
api/
├── src/
│   ├── routes/        # Route definitions
│   ├── controllers/   # Request handling
│   ├── services/      # Business logic
│   ├── repositories/  # Data access
│   ├── middleware/     # Middleware
│   ├── jobs/          # Background jobs
│   ├── utils/         # Utility functions
│   └── types/         # Type definitions
├── tests/
│   ├── unit/
│   └── integration/
└── docs/
```

## 10. Architecture Decision Records (ADR)
| ID | Governs REQ / AC IDs | Decision | Context | Alternatives | Rationale | Date |
|---|---|---|---|---|---|---|

## 11. Risks & Trade-offs
| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
```
