# UC2: View Movie Details & Purchase Tickets

## Summary

A customer views detailed information about a movie, sees today's screening times, and can order tickets for a selected screening.

## View Type

**Public React view** — movie detail page. No login required.

## Actors

- Customer (anonymous, no account)

## Preconditions

- The movie exists in the system.

## Main Flow

### Viewing Movie Details

1. Customer navigates to the movie detail page (e.g. `/movies/{movieId}`).
2. The system displays:
   - Poster image (or placeholder)
   - Title
   - Description
   - Genre
   - Duration (formatted, e.g. "2h 15min")
3. The system lists today's screening times for this movie, sorted by start time.
4. If there are no screenings today, a message is shown: "No screenings today for this movie."

### Ordering Tickets

5. Customer selects a screening time from the list.
6. Customer enters:
   - Name (required)
   - Email (required)
   - Number of tickets: 1–10 (required, default 1)
7. Customer submits the order.
8. The system validates the input:
   - Name must not be blank.
   - Email must not be blank and must be a valid email format.
   - Number of tickets must be between 1 and 10.
9. The system creates a TicketOrder with a generated order number.
10. The system navigates to a confirmation page.

### Confirmation Page

11. The confirmation page displays:
    - Order number
    - Movie title
    - Screening date and time
    - Number of tickets
    - Customer name
12. A message reminds the customer to pay and pick up tickets at the cinema using their order number.

## Validation Errors

If validation fails, the form shows inline error messages next to the invalid fields. The form is not cleared so the customer can correct their input.

## API

- `GET /api/movies/{movieId}` — Returns movie details: id, title, description, genre, durationMinutes, posterImageUrl.
- `GET /api/movies/{movieId}/screenings/today` — Returns today's screenings for the movie: id, date, startTime.
- `POST /api/orders` — Creates a new ticket order. Request body: screeningId, customerName, customerEmail, numberOfTickets. Response: orderNumber, movieTitle, screeningDate, screeningStartTime, numberOfTickets, customerName.
