# UC001: Browse Today's Movies

Users can browse movies that have showings scheduled for today.

## Routes
- `/` (public, React)

## Description

The home page displays a responsive card grid of all movies that have at least one showing today.

Each card shows:
- Poster image (or a placeholder if posterUrl is not set)
- Title
- Genre
- Duration (formatted, e.g. "1h 45min")
- Number of showings today

Cards are sorted alphabetically by title.

Clicking a card navigates to `/movie/:movieId` (UC002).

When there are no movies with showings today, a friendly empty state is shown (e.g. "No movies showing today. Check back soon!").

## UI

The listing is implemented as a responsive card grid that adapts to the screen width.
