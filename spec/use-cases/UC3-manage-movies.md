# UC3: Manage Movies

## Summary

Admins can create, view, edit, and delete movies in the system.

## View Type

**Admin Vaadin Flow view** — requires login.

## Actors

- Admin (authenticated user)

## Preconditions

- Admin is logged in.

## Main Flow

### Listing Movies

1. Admin navigates to the movies management page.
2. The system displays a grid/table of all movies with columns:
   - Title
   - Genre
   - Duration (minutes)
3. The grid supports sorting by column headers.

### Adding a Movie

4. Admin clicks an "Add Movie" button.
5. A form is presented with fields:
   - Title (required)
   - Description (optional)
   - Genre (optional)
   - Duration in minutes (required)
   - Poster image URL (optional)
6. Admin fills in the form and clicks "Save".
7. The system validates the input and saves the movie.
8. The grid refreshes to include the new movie.

### Editing a Movie

9. Admin selects a movie from the grid.
10. The form is populated with the movie's current data.
11. Admin modifies fields and clicks "Save".
12. The system validates and updates the movie.
13. The grid refreshes to show the updated data.

### Deleting a Movie

14. Admin selects a movie from the grid.
15. Admin clicks a "Delete" button.
16. The system asks for confirmation.
17. On confirmation, the movie and its associated screenings and ticket orders are deleted.
18. The grid refreshes.

## Validation

- Title must not be blank.
- Duration must be a positive integer.

## Notes

- Deleting a movie cascades to its screenings and their ticket orders. This is acceptable given the limited scope of the application.
