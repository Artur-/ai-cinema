# Domain Model

## Movie

| Field           | Type    | Required | Notes                    |
|-----------------|---------|----------|--------------------------|
| id              | Long    | auto     | Primary key              |
| title           | String  | yes      |                          |
| description     | String  | yes      |                          |
| posterUrl       | String  | no       | URL to poster image      |
| genre           | String  | yes      |                          |
| durationMinutes | Integer | yes      | Must be > 0              |

## Showing

| Field          | Type      | Required | Notes                                    |
|----------------|-----------|----------|------------------------------------------|
| id             | Long      | auto     | Primary key                              |
| movie          | Movie     | yes      | Many-to-one                              |
| showDate       | LocalDate | yes      |                                          |
| showTime       | LocalTime | yes      |                                          |
| totalSeats     | Integer   | yes      | Must be > 0                              |
| availableSeats | Integer   | yes      | Initialized to totalSeats, decremented atomically on reservation |

## Reservation

| Field           | Type      | Required | Notes                                         |
|-----------------|-----------|----------|-----------------------------------------------|
| id              | Long      | auto     | Primary key                                   |
| showing         | Showing   | yes      | Many-to-one                                   |
| numberOfTickets | Integer   | yes      | 1–10                                          |
| pickupCode      | String    | auto     | Unique, 8 uppercase alphanumeric, auto-generated |
| customerName    | String    | yes      |                                               |
| customerEmail   | String    | yes      | Must be valid email                           |
| reservationDate | LocalDate | auto     | Set to current date on creation               |

### Reservation rules
- Reservations are create-only from the public side (no edit, no delete)
- Creating a reservation atomically decrements `showing.availableSeats` by `numberOfTickets`
- If `availableSeats < numberOfTickets`, the reservation must be rejected
