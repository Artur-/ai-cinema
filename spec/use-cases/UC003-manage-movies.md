# UC003: Manage movies

As an **administrator**, I want to manage movies so that I can keep the movie catalog up to date.

## Routes

* `/admin/movies` — view the movie listing
* `/admin/movies/new` — add a new movie
* `/admin/movies/:movieId` — edit an existing movie

## Main flow

* I open the movie listing.
* I see a grid of movies showing:
  * Title
  * Genre
  * Duration
* I can sort the grid by any column.

## Add movie

* I choose to add a new movie.
* I am taken to the movie form view.
* I enter the movie details: title, description, poster URL (optional), genre, duration in minutes.
* All fields except poster URL are required.
* I save the movie and am returned to the listing where the new movie appears.

## Update movie

* I select an existing movie from the listing.
* I am taken to the movie form view with the current details filled in.
* I modify the movie details.
* I save the changes and am returned to the listing with the updated information.

## Delete movie

* From the form view, I choose to delete a movie.
* The system asks me to confirm the deletion.
* After confirming, the movie is removed and I am returned to the listing.

## Business rules

* A movie that has showings in the future (today or later) cannot be deleted. The system shows an error explaining why.

## UI

* The listing view uses a sortable Grid.
* Add and edit use a separate form view (not a side panel).
