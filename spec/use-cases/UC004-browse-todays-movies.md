# UC004 — Browse Today's Movies

## Summary
Public visitors browse movies that have screenings scheduled for today.

## Actor
Public visitor (no login required)

## Preconditions
- None

## Main Flow

1. Visitor opens the application root (`/`).
2. System fetches movies that have at least one screening today.
3. System displays movie cards in a responsive grid layout.
4. Each card shows:
   - Poster image (or a placeholder if no poster URL is set)
   - Title
   - Genre
   - Duration (formatted, e.g. "120 min")
5. Visitor clicks a movie card.
6. System navigates to the movie details page (`/movie/:movieId`).

## Alternative Flows

### AF1 — No Movies Showing Today
- System displays an empty-state message: "No movies showing today."

## Postconditions
- No data is modified.

## UI Description

- **Technology**: React (Hilla), no login required
- **Route**: `/` (index page)
- **Layout**: Responsive card grid (e.g. 1 column on mobile, 2–3 on tablet, 4 on desktop)
- **Card contents**: Poster image (or placeholder), title, genre, duration
- **Interaction**: Clicking a card navigates to `/movie/:movieId`

## Endpoints

### `MovieEndpoint.getMoviesShowingToday()`
- **Returns**: `@NonNull List<@NonNull MovieDTO>`
- **Description**: Returns movies that have at least one screening with today's date.
- **MovieDTO fields**: `id`, `title`, `genre`, `durationMinutes`, `posterImageUrl`
