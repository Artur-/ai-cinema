# UC005: View reservations

As an **administrator**, I want to view reservations so that I can verify pickup codes at the box office.

## Routes

* `/admin/reservations` — view the reservation listing

## Main flow

* I open the reservation listing.
* I see a grid of reservations showing:
  * Pickup code
  * Customer name
  * Customer email
  * Movie title
  * Show date
  * Show time
  * Number of tickets
  * Reservation date
* I can sort the grid by any column.

## Search and filter

* There is a prominent search field for looking up a reservation by pickup code.
* I can also filter by:
  * Date range (reservation date)
  * Movie

## Business rules

* Reservations are read-only. There is no create, edit, or delete from the admin side.

## UI

* The listing view uses a sortable Grid.
* The pickup code search is prominently placed above the grid for quick box-office lookups.
