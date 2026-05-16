# API Document Template

```markdown
# API Documentation — [Project Name]

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
- Description / Auth required / Rate limit / Request body / Response / Errors

[... all endpoints for every module ...]
```
