# Feature Verification Checklist

Use this checklist to verify all Cinema App features are working correctly.

## How to Use

1. Run through each item manually
2. Check the box when verified
3. Note any issues in the Comments column

---

## Public Browsing

| # | Feature | Expected Behavior | Status | Comments |
|---|---------|-------------------|--------|----------|
| 1 | Movie index shows today's movies | Card grid displays only movies with screenings scheduled for today | [ ] | |
| 2 | Movie card content | Each card shows poster, title, genre, and duration | [ ] | |
| 3 | Missing poster | A null posterUrl renders a placeholder image | [ ] | |
| 4 | Navigate to movie details | Clicking a card navigates to `/movies/{id}` with full movie info | [ ] | |
| 5 | Showtimes display | Movie details page lists today's screenings with available seat counts | [ ] | |
| 6 | Sold-out indicator | Screenings with 0 available seats show "Sold Out" and disable the buy button | [ ] | |
| 7 | Empty state | When no movies are showing today, "No movies showing today" message is displayed | [ ] | |

---

## Ticket Purchase

| # | Feature | Expected Behavior | Status | Comments |
|---|---------|-------------------|--------|----------|
| 1 | Form pre-selection | Purchase form displays movie title, date, and time as read-only info | [ ] | |
| 2 | Name validation | Submitting with blank name shows validation error | [ ] | |
| 3 | Email validation | Submitting with invalid email shows validation error | [ ] | |
| 4 | Ticket quantity limits | Min is 1, max is the number of available seats | [ ] | |
| 5 | Successful purchase | Valid submission creates reservation and shows confirmation dialog with code, title, time, quantity | [ ] | |
| 6 | Concurrent seat exhaustion | If seats run out between form load and submit, an error is shown and availability refreshes | [ ] | |

---

## Admin Movie CRUD

| # | Feature | Expected Behavior | Status | Comments |
|---|---------|-------------------|--------|----------|
| 1 | Movie grid | Lists all movies with title, genre, duration, and poster URL columns | [ ] | |
| 2 | Create movie | "New Movie" opens empty form; saving adds movie to grid | [ ] | |
| 3 | Edit movie | Selecting a row populates form; saving updates the grid | [ ] | |
| 4 | Delete movie (no screenings) | Deleting removes the movie from the grid | [ ] | |
| 5 | Delete movie (has screenings) | Shows error: "Cannot delete movie with existing screenings" | [ ] | |

---

## Admin Screening CRUD

| # | Feature | Expected Behavior | Status | Comments |
|---|---------|-------------------|--------|----------|
| 1 | Screening grid | Lists all screenings with movie title, date, time, and total seats columns | [ ] | |
| 2 | Create screening | "New Screening" opens form with movie ComboBox, DatePicker, TimePicker, seats field; saving adds to grid | [ ] | |
| 3 | Edit screening | Selecting a row populates form; saving updates the grid | [ ] | |
| 4 | Delete screening (no reservations) | Deleting removes the screening from the grid | [ ] | |
| 5 | Delete screening (has reservations) | Shows error: "Cannot delete screening with existing reservations" | [ ] | |

---

## Admin Reservations

| # | Feature | Expected Behavior | Status | Comments |
|---|---------|-------------------|--------|----------|
| 1 | Reservation grid | Read-only grid lists all reservations | [ ] | |
| 2 | Reservation columns | Shows reservation code, movie title, date/time, customer name, email, tickets, created at | [ ] | |

---

## Admin Security

| # | Feature | Expected Behavior | Status | Comments |
|---|---------|-------------------|--------|----------|
| 1 | Unauthenticated redirect | Navigating to `/admin/*` without login redirects to `/login` | [ ] | |
| 2 | Valid login | `admin` / `admin` grants access; redirects to `/admin/movies` | [ ] | |
| 3 | Invalid login | Wrong credentials show an error message on the login form | [ ] | |
| 4 | Logout | Clicking logout returns to the login page | [ ] | |

---

## Cross-Feature End-to-End Tests

| # | Scenario | Steps | Expected | Status |
|---|----------|-------|----------|--------|
| 1 | Full purchase flow | 1. Admin creates a movie, 2. Admin creates a screening for today, 3. Visitor browses index and sees the movie, 4. Visitor opens details and sees the showtime, 5. Visitor purchases tickets, 6. Visitor sees confirmation with reservation code, 7. Admin views reservation in admin grid | Reservation appears in both confirmation dialog and admin reservation list with matching details | [ ] |
| 2 | Seat exhaustion | 1. Admin creates screening with 2 seats, 2. Visitor A purchases 2 tickets, 3. Visitor B views the same screening | Screening shows as "Sold Out" for Visitor B; attempting to purchase shows an error | [ ] |

---

## Sign-off

- [ ] All critical features verified
- [ ] No blocking issues found
- [ ] Ready for release

Verified by: _______________
Date: _______________
