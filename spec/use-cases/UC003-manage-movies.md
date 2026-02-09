# UC003: Manage Movies

Administrators can list, add, update, and delete movies.

## Routes
- `/admin/movies` (listing)
- `/admin/movies/new` (add form)
- `/admin/movies/:movieId` (edit form)

## Description

### Listing
The listing shows movies with:
- Title
- Genre
- Duration
- Number of showings

The listing is sortable by all columns.

There is an "Add Movie" action that navigates to the add form.

Each row has an edit action that navigates to the edit form.

### Form
The form has fields for:
- Title (required)
- Description (required)
- Poster URL (optional)
- Genre (required)
- Duration in minutes (required, must be > 0)

All required fields are validated before saving.

### Delete
Each movie can be deleted from the edit form. Confirmation is asked before deleting.

A movie cannot be deleted if it has showings with a date today or in the future. An error message is shown if deletion is attempted.

## UI

The listing is implemented as a sortable Grid (Java/Flow). The form is a separate view navigated to from the listing.
