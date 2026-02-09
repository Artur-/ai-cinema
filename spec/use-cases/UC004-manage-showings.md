# UC004: Manage Showings

Administrators can list, add, update, and delete showings.

## Routes
- `/admin/showings` (listing)
- `/admin/showings/new` (add form)
- `/admin/showings/:showingId` (edit form)

## Description

### Listing
The listing shows showings with:
- Movie title
- Show date
- Show time
- Total seats
- Available seats

The listing is sortable by all columns.

Filters are available for:
- Date (date picker)
- Movie (dropdown)

There is an "Add Showing" action that navigates to the add form.

Each row has an edit action that navigates to the edit form.

### Form
The form has fields for:
- Movie (required, dropdown)
- Show date (required, cannot be in the past)
- Show time (required)
- Total seats (required, must be > 0)

When editing, total seats cannot be reduced below the number of already reserved seats (totalSeats - availableSeats). An error message is shown if this is attempted.

All required fields are validated before saving.

### Delete
Each showing can be deleted from the edit form. Confirmation is asked before deleting.

## UI

The listing is implemented as a sortable Grid with filter controls above (Java/Flow). The form is a separate view navigated to from the listing.
