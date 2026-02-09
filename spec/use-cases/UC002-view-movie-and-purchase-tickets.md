# UC002: View Movie and Purchase Tickets

Users can view movie details, see today's showings, and purchase tickets.

## Routes
- `/movie/:movieId` (public, React)

## Description

The page displays the movie's details:
- Poster image (or placeholder)
- Title
- Genre
- Duration (formatted)
- Description

Below the movie details, today's showings are listed. Each showing displays:
- Show time
- Available seats
- A "Select" button

Sold-out showings (availableSeats = 0) have the select button disabled and are visually marked as sold out.

### Purchase flow

1. User clicks "Select" on a showing
2. A dialog opens with:
   - Number of tickets (1–10, must not exceed availableSeats)
   - Customer name (required)
   - Customer email (required, validated as email)
3. User clicks "Confirm"
4. The system creates a reservation in an atomic transaction:
   - Validates availableSeats >= numberOfTickets
   - Decrements availableSeats
   - Creates the Reservation with auto-generated pickupCode
5. On success, a confirmation is shown with:
   - The pickup code (prominently displayed)
   - Instructions to present the code at the box office
6. On failure (e.g. seats no longer available), an error message is shown

Overbooking must be prevented even under concurrent requests.

## UI

Movie details are shown at the top. Today's showings are displayed in a list or table below. The purchase form is a modal dialog.
