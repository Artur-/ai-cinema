# Domain Model

## Movie

| Field           | Type    | Notes                |
|-----------------|---------|----------------------|
| id              | Long    | Auto-generated       |
| title           | String  | Required             |
| description     | String  | Required             |
| posterUrl       | String  | Optional             |
| genre           | String  | Required             |
| durationMinutes | Integer | Required, positive   |

## Showing

| Field          | Type      | Notes                                      |
|----------------|-----------|--------------------------------------------|
| id             | Long      | Auto-generated                             |
| movie          | Movie     | Many-to-one, required                      |
| showDate       | LocalDate | Required                                   |
| showTime       | LocalTime | Required                                   |
| totalSeats     | Integer   | Required, positive                         |
| availableSeats | Integer   | Decremented atomically on reservation      |

- A showing belongs to exactly one movie.
- `availableSeats` starts equal to `totalSeats` and is decremented atomically when a reservation is created.

## Reservation

| Field           | Type      | Notes                                                        |
|-----------------|-----------|--------------------------------------------------------------|
| id              | Long      | Auto-generated                                               |
| showing         | Showing   | Many-to-one, required                                        |
| numberOfTickets | Integer   | Required, 1–10                                               |
| pickupCode      | String    | Auto-generated, unique, 8 uppercase alphanumeric characters  |
| customerName    | String    | Required                                                     |
| customerEmail   | String    | Required, valid email                                        |
| reservationDate | LocalDate | Auto-set to current date on creation                         |

- Create-only from the public side (no edit or delete).
- The `pickupCode` is generated automatically and must be unique across all reservations.
