# API Document Template

```markdown
# API Documentation — [Project Name]

## Requirement and Contract Coverage

| Endpoint / event | REQ / AC IDs | ADR / data contract | Implementation task | Contract/integration tests |
|---|---|---|---|---|
| | | | TASK-* | TEST-* |

## 1. General Conventions
### Base URL
- Staging: https://staging-api.example.com/v1
- Production: https://api.example.com/v1

### Authentication
- Method: Bearer Token (JWT)

### Unified Response Envelope
```json
{
  "code": 200, "message": "success",
  "data": {},
  "meta": { "total": 100, "page": 1, "pageSize": 20 }
}
```

### Error Codes
| Code | HTTP Status | Meaning | Client Action |
|------|------------|---------|---------------|

## 2. Endpoint Definitions
### Auth Module
#### POST /auth/register
- REQ / AC IDs
- Description / Auth required / Rate limit / Request body / Response / Errors
- Idempotency, concurrency, compatibility, and observability contract where applicable
- Implementation TASK IDs and contract/integration TEST IDs

[... all endpoints for every module ...]
```
