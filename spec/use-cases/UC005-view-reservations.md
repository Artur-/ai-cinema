# UC005: View Reservations

Administrators can view reservations to verify pickup codes at the box office.

## Routes
- `/admin/reservations` (listing)

## Description

The listing shows reservations with:
- Pickup code
- Movie title
- Show date
- Show time
- Customer name
- Customer email
- Number of tickets
- Reservation date

The listing is sortable by all columns.

A prominent search field for pickup code is shown at the top for quick lookup.

Additional filters are available for:
- Date range (show date)
- Movie (dropdown)

Reservations are read-only (no edit, no delete from this view).

## UI

The listing is implemented as a sortable Grid with a prominent pickup code search field and filter controls above (Java/Flow).
