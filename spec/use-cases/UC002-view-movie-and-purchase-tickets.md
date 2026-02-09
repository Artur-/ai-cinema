# UC002: View movie details and purchase tickets

As a **visitor**, I want to view a movie's details and purchase tickets for a showing so that I can reserve my spot.

## Routes

* `/movie/:movieId` — public, React

## Main flow

* I open the movie details page.
* I see the movie information:
  * Poster image (or a placeholder if none)
  * Title
  * Genre
  * Duration
  * Description
* Below the movie information, I see a list of today's showings with:
  * Show time
  * Available seats
  * A "Select" button

## Purchase flow

* I click "Select" on a showing.
* A dialog opens where I enter:
  * Number of tickets (1–10)
  * My name
  * My email address
* All fields are required.
* I confirm the purchase.
* The system creates a reservation and decrements available seats atomically.
* I see a confirmation with my pickup code (8 uppercase alphanumeric characters).

## Business rules

* Sold-out showings (availableSeats = 0) are shown but the "Select" button is disabled.
* The system prevents overbooking: if the requested number of tickets exceeds available seats, the reservation is rejected with an error message.
* The reservation is created in an atomic transaction to prevent race conditions.

## UI

* Movie info is displayed prominently at the top.
* Showings are listed in chronological order below the movie info.
* The purchase dialog is a modal overlay.
