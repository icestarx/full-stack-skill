# Database Design Document Template

```markdown
# Database Design — [Project Name]

> **Change work item**: [CHG-* path / tracker URL or N/A]

## Requirement and Decision Coverage

| REQ / AC IDs | ADR / rule | Entities / tables / migrations | Verification |
|---|---|---|---|
| | | | TEST-* / review |

## 1. Entity Relationship Diagram (ERD)
- [Mermaid/PlantUML ER diagram]

## 2. Entity Inventory
| Entity | Table | Source REQ / ADR IDs | Description | Est. Data Volume | Growth Rate |
|---|---|---|---|---|---|

## 3. Table Definitions
### Table: users
| Column | Type | Constraints | Default | Description |
|--------|------|-------------|---------|-------------|
| id | UUID | PK | gen_random_uuid() | Primary key |
| email | VARCHAR(255) | UNIQUE, NOT NULL | | Email address |
| created_at | TIMESTAMPTZ | NOT NULL | now() | Creation time |
| updated_at | TIMESTAMPTZ | NOT NULL | now() | Update time |
| deleted_at | TIMESTAMPTZ | | NULL | Soft delete |

## 4. Index Strategy
| Table | Index Name | Columns | Type | Purpose |
|-------|------------|---------|------|---------|

## 5. Migration Plan
- Migration tool: Prisma Migrate / Alembic / golang-migrate
- Strategy: one independent migration file per change, versioned, reversible

| Migration / task | Source IDs | Compatibility requirement | Up/down verification | Release |
|---|---|---|---|---|
| | | | TEST-* | |

## 6. Data Security
- Fields requiring encryption (PII)
- Encryption method
- Audit logging strategy
```
