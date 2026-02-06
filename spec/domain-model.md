# Domain Model

## Overview

The cinema app manages movies, screenings, and ticket orders. The scope is intentionally limited: no payment processing, no seat selection, no customer accounts, and no capacity tracking. Customers pay at the cinema when picking up tickets.

## Entities

### Movie

| Field            | Type    | Constraints       | Description                        |
|------------------|---------|-------------------|------------------------------------|
| id               | Long    | PK, auto-generated | Unique identifier                 |
| title            | String  | Required, max 255 | Movie title                        |
| description      | String  | Optional, max 2000 | Movie description / synopsis      |
| genre            | String  | Optional, max 100 | Free-text genre (e.g. "Action", "Comedy, Drama") |
| durationMinutes  | Integer | Required, min 1   | Runtime in minutes                 |
| posterImageUrl   | String  | Optional, max 500 | URL to the poster image            |

### Screening

A screening represents a specific showing of a movie at a given date and time.

| Field     | Type      | Constraints        | Description                          |
|-----------|-----------|--------------------|--------------------------------------|
| id        | Long      | PK, auto-generated | Unique identifier                    |
| movie     | Movie     | Required, FK       | The movie being screened             |
| date      | LocalDate | Required           | The date of the screening            |
| startTime | LocalTime | Required           | The start time of the screening      |

### TicketOrder

A ticket order represents a customer's reservation of tickets for a screening. There is no capacity tracking — the system does not limit total tickets sold per screening.

| Field           | Type           | Constraints                  | Description                                      |
|-----------------|----------------|------------------------------|--------------------------------------------------|
| id              | Long           | PK, auto-generated           | Unique identifier                                |
| screening       | Screening      | Required, FK                 | The screening the tickets are for                |
| customerName    | String         | Required, max 255            | Name of the customer                             |
| customerEmail   | String         | Required, max 255            | Email of the customer                            |
| numberOfTickets | Integer        | Required, min 1, max 10      | Number of tickets ordered (abuse-prevention cap) |
| orderNumber     | String         | Required, unique, generated  | Human-readable order number used for pickup      |
| createdAt       | LocalDateTime  | Required, auto-set on create | Timestamp of when the order was placed           |

## Relationships

```
Movie 1 ──── * Screening
Screening 1 ──── * TicketOrder
```

- A Movie has many Screenings
- A Screening belongs to one Movie
- A Screening has many TicketOrders
- A TicketOrder belongs to one Screening

## Design Decisions

- **No capacity tracking**: The system does not enforce a maximum number of tickets per screening. This keeps the scope minimal.
- **Max 10 tickets per order**: A simple abuse-prevention limit per individual order.
- **Order number**: A generated, human-readable identifier (not the database ID) used by customers to pick up tickets at the cinema.
- **No customer accounts**: Customers provide name and email per order. There is no login or order history for customers.
- **No payment processing**: Payment happens in person at the cinema.
- **No seat selection**: Tickets are general admission.
