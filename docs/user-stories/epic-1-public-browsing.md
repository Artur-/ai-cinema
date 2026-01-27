# Epic 1: Public Browsing & Ticket Purchase

## Overview

Enable visitors to browse today's movie offerings, view showtimes with seat availability, and purchase tickets without requiring authentication.

## Goals

- Provide a visually appealing movie index page showing today's screenings
- Allow users to view detailed movie information and available showtimes
- Enable ticket purchase with a simple form (no payment, no seat selection)
- Display a confirmation with a reservation code after purchase

---

## User Stories

### US-1.1: View Today's Movies

**As a** visitor
**I want** to see a list of movies showing today
**So that** I can decide what to watch

**Acceptance Criteria:**
- [ ] The index page displays a card grid of movies that have at least one screening today
- [ ] Each card shows the movie poster, title, genre, and duration
- [ ] Movies with no screenings today are not shown
- [ ] If no movies are showing today, an empty state message ("No movies showing today") is displayed
- [ ] A null poster URL renders a placeholder image

**Tasks:**
- [ ] Create Hilla endpoint to fetch movies with today's screenings
- [ ] Build React card grid component for the index page
- [ ] Implement placeholder image for missing posters
- [ ] Implement empty state display

**Notes:**
"Today" is determined by the server's date. The query should join Movie with Screening and filter by `screeningDate = today`.

---

### US-1.2: View Movie Details and Showtimes

**As a** visitor
**I want** to view a movie's details and its showtimes for today
**So that** I can choose a screening to attend

**Acceptance Criteria:**
- [ ] Navigating to `/movies/{id}` displays the movie's poster, title, genre, duration, and description
- [ ] Today's showtimes are listed with their start time and number of available seats
- [ ] Sold-out screenings are visually marked as "Sold Out"
- [ ] Each non-sold-out showtime has a "Buy Tickets" button
- [ ] Navigating to an invalid movie ID shows a not-found state

**Tasks:**
- [ ] Create Hilla endpoint to fetch movie details with today's screenings and seat availability
- [ ] Build React movie details page component
- [ ] Implement sold-out visual indicator and disabled buy button
- [ ] Implement not-found state for invalid IDs

**Notes:**
Available seats = `totalSeats - SUM(reservations.numberOfTickets)` for each screening.

---

### US-1.3: Purchase Tickets

**As a** visitor
**I want** to purchase tickets for a screening
**So that** I can reserve my seats

**Acceptance Criteria:**
- [ ] The purchase form displays the movie title, screening date, and time as read-only info
- [ ] The form collects customer name, email, and number of tickets
- [ ] The ticket quantity field has a minimum of 1 and a maximum equal to available seats
- [ ] Submitting with a blank name shows a validation error
- [ ] Submitting with an invalid email shows a validation error
- [ ] Requesting more tickets than available shows an error message
- [ ] If seats are exhausted between form load and submit, an error is shown

**Tasks:**
- [ ] Create Hilla endpoint to submit a reservation (with seat availability check)
- [ ] Build React purchase form component
- [ ] Implement client-side validation (name, email, ticket count)
- [ ] Implement server-side seat availability check with proper error handling
- [ ] Generate unique reservation code on the server

**Notes:**
No payment processing. No seat selection. The server must re-check seat availability at the time of reservation creation to handle concurrent purchases.

---

### US-1.4: Receive Reservation Confirmation

**As a** visitor
**I want** to see a confirmation after purchasing tickets
**So that** I know my reservation was successful and have a reference code

**Acceptance Criteria:**
- [ ] After a successful purchase, a confirmation dialog is displayed
- [ ] The dialog shows: reservation code, movie title, screening date, screening time, and number of tickets
- [ ] The dialog provides a way to return to browsing (e.g., a "Back to Movies" button)

**Tasks:**
- [ ] Build React confirmation dialog component
- [ ] Pass reservation details from the purchase response to the dialog
- [ ] Implement navigation back to the movie index

---

## Dependencies

- Requires data model entities (Movie, Screening, Reservation) to be implemented first
- No dependency on Epic 2 (admin views)

## Definition of Done

- [ ] All user stories completed
- [ ] Hilla endpoints tested
- [ ] React components render correctly
- [ ] Edge cases handled (empty states, sold-out, validation errors, concurrent purchases)
- [ ] Visual review completed
