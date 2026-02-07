# UC002 — Manage Screenings

## Summary
Admin manages screenings (showings of movies at specific dates and times) via CRUD operations.

## Actor
Admin (authenticated user)

## Preconditions
- Admin is logged in
- At least one movie exists (for creating a screening)

## Main Flow

1. Admin navigates to the Screenings admin view.
2. System displays a Grid with columns: Movie Title, Date, Start Time, Actions.
3. Admin clicks "Add Screening".
4. System shows an inline form (or side panel) with fields:
   - **Movie** — ComboBox, required (lists all movies by title)
   - **Date** — DatePicker, required
   - **Start Time** — TimePicker, required
5. Admin fills in the form and clicks "Save".
6. System validates input, persists the screening, refreshes the Grid, and clears the form.

### Edit
7. Admin clicks "Edit" on a screening row.
8. System populates the form with the screening's current data.
9. Admin modifies fields and clicks "Save".
10. System validates, updates the screening, and refreshes the Grid.

### Delete
11. Admin clicks "Delete" on a screening row.
12. System checks whether the screening has associated ticket orders.
    - If **no orders**: system deletes the screening and refreshes the Grid.
    - If **orders exist**: system shows a confirmation dialog: "This screening has existing ticket orders. Deleting it will also delete all associated orders. Continue?"
      - Admin confirms → system cascade-deletes the orders and the screening, then refreshes the Grid.
      - Admin cancels → no action is taken.

## Alternative Flows

### AF1 — Validation Failure
- If required fields are empty, inline validation errors are displayed. The form is not submitted.

### AF2 — No Movies Exist
- The "Add Screening" button is disabled. A message is shown: "Create a movie first before adding screenings."

### AF3 — Cancel
- Admin clicks "Cancel" (or selects a different row). The form is cleared without saving.

## Postconditions
- The screening schedule reflects the admin's changes.
- If a screening with orders was deleted, the associated orders are also deleted.

## UI Description

- **Technology**: Java (Flow), login required
- **Layout**: Grid on the left/top, form on the right/bottom
- **Grid columns**: Movie Title, Date, Start Time, Actions (Edit / Delete buttons)
- **Validation**: Inline field-level validation with Vaadin Binder
