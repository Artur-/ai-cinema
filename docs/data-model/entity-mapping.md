# Entity Mapping

This document defines the data model entities and their relationships for the Cinema App.

## Entity Diagram

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│      Movie      │       │    Screening    │       │   Reservation   │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ id: Long        │       │ id: Long        │       │ id: Long        │
│ title: String   │──1:N──│ movie: FK       │──1:N──│ screening: FK   │
│ description: Str│       │ screeningDate   │       │ customerName    │
│ durationMinutes │       │ screeningTime   │       │ customerEmail   │
│ genre: String   │       │ totalSeats: Int │       │ numberOfTickets │
│ posterUrl: Str  │       └─────────────────┘       │ reservationCode │
└─────────────────┘                                 │ createdAt       │
                                                    └─────────────────┘
```

## Entities

### Movie

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK, auto-generated | Unique identifier |
| title | String | not null, max 255 | Movie title |
| description | String | max 2000 | Synopsis or description of the movie |
| durationMinutes | Integer | not null, > 0 | Runtime in minutes |
| genre | String | not null, max 100 | Genre label (e.g. "Action", "Comedy") |
| posterUrl | String | max 500, nullable | URL to the movie poster image |

**Relationships:**
- Has many Screening (a movie can have multiple screenings)
- Cannot be deleted while screenings exist

### Screening

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK, auto-generated | Unique identifier |
| movie | Movie | FK, not null | The movie being screened |
| screeningDate | LocalDate | not null | Date of the screening |
| screeningTime | LocalTime | not null | Start time of the screening |
| totalSeats | Integer | not null, > 0 | Total number of available seats |

**Relationships:**
- Belongs to Movie (many-to-one)
- Has many Reservation (a screening can have multiple reservations)
- Cannot be deleted while reservations exist

### Reservation

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | Long | PK, auto-generated | Unique identifier |
| screening | Screening | FK, not null | The screening being reserved |
| customerName | String | not null, max 255 | Name of the customer |
| customerEmail | String | not null, max 255, valid email | Customer email address |
| numberOfTickets | Integer | not null, >= 1 | Number of tickets reserved |
| reservationCode | String | not null, unique | Auto-generated confirmation code |
| createdAt | LocalDateTime | not null | Timestamp of reservation creation |

**Relationships:**
- Belongs to Screening (many-to-one)

## Validation Rules

| Entity | Field | Rule |
|--------|-------|------|
| Movie | title | Cannot be blank, max 255 characters |
| Movie | durationMinutes | Must be greater than 0 |
| Movie | genre | Cannot be blank |
| Screening | movie | Must reference an existing movie |
| Screening | screeningDate | Cannot be null |
| Screening | screeningTime | Cannot be null |
| Screening | totalSeats | Must be greater than 0 |
| Reservation | customerName | Cannot be blank |
| Reservation | customerEmail | Must be a valid email address |
| Reservation | numberOfTickets | Must be >= 1 and <= available seats for the screening |
| Reservation | reservationCode | Auto-generated, unique |

## Derived Fields

| Context | Field | Derivation |
|---------|-------|------------|
| Screening | availableSeats | `totalSeats - SUM(reservations.numberOfTickets)` |
| Screening | soldOut | `availableSeats == 0` |

## JPA Conventions

1. **ID Generation**: Use `@GeneratedValue(strategy = GenerationType.SEQUENCE)`
2. **Equality**: Based on ID only
3. **Validation**: Domain validation in setters; Bean Validation annotations on fields
4. **Timestamps**: Use `LocalDate`, `LocalTime`, and `LocalDateTime` as appropriate
5. **Cascade**: No cascade deletes — enforce referential integrity checks before deletion
