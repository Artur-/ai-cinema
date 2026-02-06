# UC1: Browse Today's Movies

## Summary

Customers visit the cinema website and see all movies that have at least one screening today, displayed as visual cards.

## View Type

**Public React view** — this is the index/landing page of the application. No login required.

## Actors

- Customer (anonymous, no account)

## Preconditions

- None

## Main Flow

1. Customer navigates to the cinema website root URL.
2. The system fetches all movies that have at least one screening scheduled for today.
3. Each movie is displayed as a card showing:
   - Poster image (or a placeholder if no poster URL is set)
   - Title
   - Genre
   - Duration (formatted, e.g. "2h 15min")
4. Customer clicks on a movie card.
5. The system navigates to the movie detail page (see UC2).

## Empty State

If there are no movies with screenings today, the page displays a friendly message such as "No movies showing today. Check back soon!"

## Sorting

Movies are displayed in alphabetical order by title.

## API

- `GET /api/movies/today` — Returns a list of movies that have at least one screening today. Each movie includes: id, title, genre, durationMinutes, posterImageUrl.
