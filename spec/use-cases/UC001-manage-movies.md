# UC001 — Manage Movies

## Summary
Admin manages the movie catalog via CRUD operations.

## Actor
Admin (authenticated user)

## Preconditions
- Admin is logged in

## Main Flow

1. Admin navigates to the Movies admin view.
2. System displays a Grid with columns: Title, Genre, Duration, Actions.
3. Admin clicks "Add Movie".
4. System shows an inline form (or side panel) with fields:
   - **Title** — text field, required, max 255 characters
   - **Description** — text area, optional, max 2000 characters
   - **Genre** — text field, optional, max 100 characters
   - **Duration (minutes)** — integer field, required, minimum 1
   - **Poster Image URL** — text field, optional, max 500 characters
5. Admin fills in the form and clicks "Save".
6. System validates input, persists the movie, refreshes the Grid, and clears the form.

### Edit
7. Admin clicks "Edit" on a movie row.
8. System populates the form with the movie's current data.
9. Admin modifies fields and clicks "Save".
10. System validates, updates the movie, and refreshes the Grid.

### Delete
11. Admin clicks "Delete" on a movie row.
12. System checks whether the movie has associated screenings.
    - If **no screenings**: system deletes the movie and refreshes the Grid.
    - If **screenings exist**: system shows an error notification: "Cannot delete a movie that has screenings. Delete its screenings first."

## Alternative Flows

### AF1 — Validation Failure
- If required fields are empty or constraints are violated (e.g. duration < 1), inline validation errors are displayed next to the relevant fields. The form is not submitted.

### AF2 — Cancel
- Admin clicks "Cancel" (or selects a different row). The form is cleared without saving.

## Postconditions
- The movie catalog reflects the admin's changes.

## UI Description

- **Technology**: Java (Flow), login required
- **Layout**: Grid on the left/top, form on the right/bottom
- **Grid columns**: Title, Genre, Duration, Actions (Edit / Delete buttons)
- **Validation**: Inline field-level validation with Vaadin Binder
