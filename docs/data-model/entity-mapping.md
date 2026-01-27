# Entity Mapping

This document defines the data model entities and their relationships.

## Entity Diagram

```
┌─────────────────┐       ┌─────────────────┐
│     Entity1     │       │     Entity2     │
├─────────────────┤       ├─────────────────┤
│ id: Long        │       │ id: Long        │
│ name: String    │───────│ entity1: FK     │
│ created: Date   │ 1   n │ value: String   │
└─────────────────┘       └─────────────────┘
```

## Entities

### Entity1

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK, auto-generated | Unique identifier |
| name | String | not null, max 255 | Display name |
| created | LocalDateTime | not null | Creation timestamp |

**Relationships:**
- Has many Entity2 (cascade delete)

### Entity2

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK, auto-generated | Unique identifier |
| entity1 | Entity1 | FK, not null | Parent reference |
| value | String | not null | Data value |

**Relationships:**
- Belongs to Entity1

## Validation Rules

| Entity | Field | Rule |
|--------|-------|------|
| Entity1 | name | Cannot be blank |
| Entity2 | value | Maximum 1000 characters |

## JPA Conventions

Following the patterns from `examplefeature/Task.java`:

1. **ID Generation**: Use `@GeneratedValue(strategy = GenerationType.SEQUENCE)`
2. **Equality**: Based on ID only (see Task.equals/hashCode pattern)
3. **Validation**: Domain validation in setters
4. **Timestamps**: Use `LocalDateTime` for timestamps
