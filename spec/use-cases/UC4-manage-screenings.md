# UC4: Manage Screenings

## Summary

Admins can create, view, edit, and delete screenings for movies.

## View Type

**Admin Vaadin Flow view** — requires login.

## Actors

- Admin (authenticated user)

## Preconditions

- Admin is logged in.
- At least one movie exists in the system (to create a screening).

## Main Flow

### Listing Screenings

1. Admin navigates to the screenings management page.
2. The system displays a grid/table of screenings with columns:
   - Movie title
   - Date
   - Start time
3. The grid is filterable by date (defaults to today).
4. The grid supports sorting by column headers.

### Adding a Screening

5. Admin clicks an "Add Screening" button.
6. A form is presented with fields:
   - Movie (required, select/dropdown from existing movies)
   - Date (required, date picker)
   - Start time (required, time picker)
7. Admin fills in the form and clicks "Save".
8. The system validates the input and saves the screening.
9. The grid refreshes to include the new screening.

### Editing a Screening

10. Admin selects a screening from the grid.
11. The form is populated with the screening's current data.
12. Admin modifies fields and clicks "Save".
13. The system validates and updates the screening.
14. The grid refreshes to show the updated data.

### Deleting a Screening

15. Admin selects a screening from the grid.
16. Admin clicks a "Delete" button.
17. The system asks for confirmation.
18. On confirmation, the screening and its associated ticket orders are deleted.
19. The grid refreshes.

## Validation

- Movie must be selected.
- Date must not be empty.
- Start time must not be empty.

## Notes

- Deleting a screening cascades to its ticket orders. This is acceptable given the limited scope of the application.
