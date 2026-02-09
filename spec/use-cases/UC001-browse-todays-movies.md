# UC001: Browse today's movies

As a **visitor**, I want to see which movies are showing today so that I can decide what to watch.

## Routes

* `/` — public, React

## Main flow

* I open the home page.
* I see a responsive card grid of movies that have at least one showing today.
* Each card shows:
  * Poster image (or a placeholder if none)
  * Title
  * Genre
  * Duration (e.g. "120 min")
  * Number of showings today
* The cards are sorted alphabetically by title.
* I click a card and am taken to the movie details page (`/movie/:movieId`).

## Empty state

* If there are no movies showing today, I see a friendly message indicating that no showings are available.

## UI

* The layout is a responsive card grid that adapts from one column on mobile to multiple columns on larger screens.
