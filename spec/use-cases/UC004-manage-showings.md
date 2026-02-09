# UC004: Manage showings

As an **administrator**, I want to manage showings so that I can schedule when movies are available to the public.

## Routes

* `/admin/showings` — view the showing listing
* `/admin/showings/new` — add a new showing
* `/admin/showings/:showingId` — edit an existing showing

## Main flow

* I open the showing listing.
* I see a grid of showings displaying:
  * Movie title
  * Show date
  * Show time
  * Total seats
  * Available seats
* I can sort the grid by any column.
* I can filter the grid by:
  * Date
  * Movie

## Add showing

* I choose to add a new showing.
* I am taken to the showing form view.
* I enter the showing details: movie (dropdown), show date, show time, total seats.
* All fields are required.
* Available seats is automatically set equal to total seats.
* I save the showing and am returned to the listing where the new showing appears.

## Update showing

* I select an existing showing from the listing.
* I am taken to the showing form view with the current details filled in.
* I modify the showing details.
* I save the changes and am returned to the listing with the updated information.

## Delete showing

* From the form view, I choose to delete a showing.
* The system asks me to confirm the deletion.
* After confirming, the showing is removed and I am returned to the listing.

## Business rules

* Show date cannot be set to a past date.
* Total seats cannot be reduced below the number of already-reserved tickets (totalSeats - availableSeats).
* A showing that has existing reservations cannot be deleted. The system shows an error explaining why.

## UI

* The listing view uses a sortable, filterable Grid.
* Add and edit use a separate form view (not a side panel).
