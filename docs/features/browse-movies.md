# Feature: Browse Movies

## Overview

Public-facing feature that allows visitors to browse today's movie offerings and view details including showtimes and seat availability. Built with React and Hilla.

## Current Behavior

### Movie Index Page

- Displays a responsive card grid of all movies with screenings scheduled for today
- Each card shows: poster image, title, genre, and duration
- Clicking a card navigates to the movie details page
- If no movies are scheduled for today, an empty state message is displayed

### Movie Details Page

- Shows full movie information: poster, title, genre, duration, and description
- Lists all of today's showtimes for the movie
- Each showtime displays the screening time and the number of available seats
- Sold-out screenings are visually marked and the purchase action is disabled
- A "Buy Tickets" action on each showtime navigates to the ticket purchase flow

## User Workflow

```
1. User visits the index page
          ↓
2. System loads and displays today's movies as cards
          ↓
3. User clicks a movie card
          ↓
4. System navigates to the movie details page
          ↓
5. System displays movie info and today's showtimes with available seats
          ↓
6. User clicks "Buy Tickets" on a showtime
          ↓
7. System navigates to the ticket purchase form
```

## Edge Cases and Validation

| Scenario | Behavior |
|----------|----------|
| No movies with screenings today | Show empty state: "No movies showing today" |
| Movie has null posterUrl | Display a placeholder image |
| Invalid movie ID in URL | Show a not-found message or redirect to index |
| All screenings for a movie are sold out | Show showtimes but mark each as "Sold Out" with purchase disabled |
| Movie exists but has no screenings today | Do not show the movie on the index page |

## UI Components Used

| Component | Purpose |
|-----------|---------|
| Card grid (React) | Display movie cards on the index page |
| Image | Movie poster display |
| Badge / Tag | Genre and duration labels |
| List | Showtime entries on the details page |
| Button | "Buy Tickets" action per showtime |
| Empty state | Message when no movies are available |

## Data Model

### Movie
- **id**: Unique identifier
- **title**: Movie title
- **description**: Synopsis
- **durationMinutes**: Runtime in minutes
- **genre**: Genre label
- **posterUrl**: URL to poster image (nullable)

### Screening (filtered to today)
- **id**: Unique identifier
- **movie**: Parent movie reference
- **screeningDate**: Date of screening
- **screeningTime**: Start time
- **totalSeats**: Total capacity
- **availableSeats** (derived): `totalSeats - SUM(reservations.numberOfTickets)`

## Acceptance Criteria

### AC1: Movie Index Displays Today's Movies
- [ ] Index page shows only movies that have at least one screening today
- [ ] Each card displays the poster, title, genre, and duration
- [ ] Cards are laid out in a responsive grid

### AC2: Navigation to Details
- [ ] Clicking a movie card navigates to `/movies/{id}`
- [ ] The details page shows full movie information
- [ ] Today's showtimes are listed with available seat counts

### AC3: Sold-Out Handling
- [ ] Sold-out screenings display a "Sold Out" indicator
- [ ] The "Buy Tickets" button is disabled for sold-out screenings

### AC4: Empty and Error States
- [ ] When no movies are showing today, an empty state message is displayed
- [ ] A null poster URL renders a placeholder image
- [ ] Navigating to an invalid movie ID shows a not-found state
