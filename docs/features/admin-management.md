# Feature: Admin Management

## Overview

Admin-only area for managing the cinema's data: movies, screenings, and reservations. Built with Java and Vaadin Flow. Protected by form-based login with role-based access control.

## Current Behavior

### Admin Layout

- All admin views share an `AppLayout` with a `SideNav` sidebar
- Navigation items: Movies, Screenings, Reservations
- A logout button is available in the layout
- The layout is only accessible to authenticated users with the `ADMIN` role

### Security

- Form-based login at `/login`
- In-memory user: username `admin`, password `admin`
- All `/admin/**` routes require `@RolesAllowed("ADMIN")`
- Unauthenticated access redirects to the login page

### Movie CRUD (`/admin/movies`)

- **Grid**: Lists all movies with columns for title, genre, duration, and poster URL
- **Form**: Fields for title (TextField), description (TextArea), duration (IntegerField), genre (TextField), poster URL (TextField)
- **Create**: Click "New Movie" to open an empty form; fill in and save
- **Edit**: Select a row in the grid to populate the form; modify and save
- **Delete**: Select a row and click "Delete"; prevented if the movie has associated screenings

### Screening CRUD (`/admin/screenings`)

- **Grid**: Lists all screenings with columns for movie title, date, time, and total seats
- **Form**: Fields for movie (ComboBox), screening date (DatePicker), screening time (TimePicker), total seats (IntegerField)
- **Create**: Click "New Screening" to open an empty form; fill in and save
- **Edit**: Select a row in the grid to populate the form; modify and save
- **Delete**: Select a row and click "Delete"; prevented if the screening has associated reservations

### Reservation List (`/admin/reservations`)

- **Grid**: Read-only list of all reservations
- Columns: reservation code, movie title, screening date/time, customer name, customer email, number of tickets, created at
- No create, edit, or delete actions

## User Workflow

### Login
```
1. User navigates to /admin/*
          ↓
2. System redirects to /login
          ↓
3. User enters admin / admin
          ↓
4. System authenticates and redirects to /admin/movies
```

### Movie Management
```
1. Admin views movie grid
          ↓
2. Admin clicks "New Movie" or selects a row
          ↓
3. Admin fills/edits the form and clicks "Save"
          ↓
4. System validates and persists the movie
          ↓
5. Grid refreshes with updated data
```

### Screening Management
```
1. Admin views screening grid
          ↓
2. Admin clicks "New Screening" or selects a row
          ↓
3. Admin fills/edits the form (selects movie from ComboBox)
          ↓
4. Admin clicks "Save"
          ↓
5. System validates and persists the screening
          ↓
6. Grid refreshes with updated data
```

## Edge Cases and Validation

| Scenario | Behavior |
|----------|----------|
| Delete movie with screenings | Show error: "Cannot delete movie with existing screenings" |
| Delete screening with reservations | Show error: "Cannot delete screening with existing reservations" |
| Invalid login credentials | Show error on login form |
| Session expires | Redirect to login page |
| Blank required fields on movie form | Show validation errors |
| Blank required fields on screening form | Show validation errors |
| Total seats set to 0 or negative | Show validation error |
| Duration set to 0 or negative | Show validation error |

## UI Components Used

| Component | Purpose |
|-----------|---------|
| AppLayout | Main layout shell for admin area |
| SideNav | Navigation between admin views |
| Grid | Data tables for movies, screenings, reservations |
| TextField | Title, genre, poster URL, customer name fields |
| TextArea | Movie description |
| IntegerField | Duration, total seats |
| ComboBox | Movie selection in screening form |
| DatePicker | Screening date |
| TimePicker | Screening time |
| Button | Save, Delete, New, Logout actions |
| Notification | Success/error feedback messages |

## Data Model

### Movie
- **id**: Unique identifier
- **title**: Movie title (required)
- **description**: Synopsis
- **durationMinutes**: Runtime in minutes (required, > 0)
- **genre**: Genre label (required)
- **posterUrl**: URL to poster image (optional)

### Screening
- **id**: Unique identifier
- **movie**: Parent movie reference (required)
- **screeningDate**: Date of screening (required)
- **screeningTime**: Start time (required)
- **totalSeats**: Total capacity (required, > 0)

### Reservation (read-only in admin)
- **id**: Unique identifier
- **screening**: Parent screening reference
- **customerName**: Customer name
- **customerEmail**: Customer email
- **numberOfTickets**: Number of tickets
- **reservationCode**: Unique confirmation code
- **createdAt**: Reservation timestamp

## Acceptance Criteria

### AC1: Authentication and Authorization
- [ ] Navigating to `/admin/*` without authentication redirects to `/login`
- [ ] Login with `admin` / `admin` grants access to admin views
- [ ] Invalid credentials show an error message on the login form
- [ ] Logout returns the user to the login page

### AC2: Movie CRUD
- [ ] The movie grid displays all movies with title, genre, duration, and poster URL columns
- [ ] Creating a new movie adds it to the grid after save
- [ ] Editing a movie updates the grid after save
- [ ] Deleting a movie with no screenings removes it from the grid
- [ ] Deleting a movie with screenings shows an error message

### AC3: Screening CRUD
- [ ] The screening grid displays all screenings with movie title, date, time, and seats columns
- [ ] The movie ComboBox lists all available movies
- [ ] Creating a new screening adds it to the grid after save
- [ ] Editing a screening updates the grid after save
- [ ] Deleting a screening with no reservations removes it from the grid
- [ ] Deleting a screening with reservations shows an error message

### AC4: Reservation List
- [ ] The reservation grid displays all reservations as read-only
- [ ] Columns include: reservation code, movie title, date/time, customer name, email, tickets, created at
- [ ] No create, edit, or delete actions are available

### AC5: Admin Layout and Navigation
- [ ] All admin views use a shared AppLayout with SideNav
- [ ] SideNav contains links to Movies, Screenings, and Reservations
- [ ] A logout button is present and functional
