# UC005 — View Movie Details & Purchase Tickets

## Summary
Public visitor views movie details, selects a screening, and purchases tickets.

## Actor
Public visitor (no login required)

## Preconditions
- The movie exists
- The movie has at least one screening today

## Main Flow

1. Visitor navigates to `/movie/:movieId` (typically by clicking a card on the home page).
2. System fetches the movie details and today's screenings.
3. System displays:
   - **Top section**: Poster image (or placeholder), title, description, genre, duration
   - **"Today's Screenings" section**: A list of time buttons/chips, sorted chronologically
4. Visitor clicks a screening time.
5. System reveals a purchase form (inline on the same page, or in a dialog) with fields:
   - **Customer Name** — text field, required
   - **Email** — text field, required, email format validated
   - **Number of Tickets** — number field, required, range 1–10, default 1
6. Visitor fills in the form and clicks "Buy Tickets".
7. System sends the order to the server.
8. Server validates input, generates an order number, creates a TicketOrder, and returns a confirmation.
9. System displays a confirmation on the same page:
   - Order number (displayed prominently)
   - Movie title
   - Screening time
   - Number of tickets
   - Message: "Show this at the cinema to pick up and pay for your tickets."
10. A "Back to movies" link is available to return to `/`.

## Alternative Flows

### AF1 — Validation Failure
- If required fields are empty or email format is invalid, inline validation errors are shown. The form is not submitted.

### AF2 — Server-Side Validation Failure
- If server validation fails (e.g. screening no longer exists), an error message is shown to the visitor.

### AF3 — Movie Not Found
- If the movieId does not correspond to an existing movie, a "Movie not found" message is shown with a link back to `/`.

### AF4 — No Screenings Today
- The movie details are shown but the screenings section displays: "No screenings today." The purchase form is not available.

## Postconditions
- A new TicketOrder is persisted with a generated order number.
- No payment is processed — the customer pays at the cinema.

## UI Description

- **Technology**: React (Hilla), no login required
- **Route**: `/movie/:movieId`
- **Layout**:
  - Top: movie details (poster, title, description, genre, duration)
  - Middle: screening time buttons/chips (chronological)
  - Bottom (on selection): purchase form → confirmation
- **Navigation**: "Back to movies" link to `/`

## Endpoints

### `MovieEndpoint.getMovieWithScreenings(Long movieId)`
- **Returns**: `@NonNull MovieWithScreeningsDTO`
- **Description**: Returns movie details and today's screenings for the given movie.
- **MovieWithScreeningsDTO fields**: `id`, `title`, `description`, `genre`, `durationMinutes`, `posterImageUrl`, `screenings` (`List<ScreeningDTO>`)
- **ScreeningDTO fields**: `id`, `startTime`

### `OrderEndpoint.createOrder(CreateOrderRequest request)`
- **Returns**: `@NonNull OrderConfirmationDTO`
- **Description**: Validates input, generates an order number, creates a TicketOrder.
- **CreateOrderRequest fields**: `screeningId` (Long, required), `customerName` (String, required), `customerEmail` (String, required, email format), `numberOfTickets` (Integer, required, 1–10)
- **OrderConfirmationDTO fields**: `orderNumber`, `movieTitle`, `screeningTime`, `numberOfTickets`
