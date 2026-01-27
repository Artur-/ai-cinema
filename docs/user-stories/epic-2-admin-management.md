# Epic 2: Admin Management

## Overview

Provide an authenticated admin area for managing movies, screenings, and viewing reservations. Built with Java and Vaadin Flow, protected by form-based login.

## Goals

- Secure the admin area with form-based authentication and role-based access
- Allow admins to perform full CRUD on movies and screenings
- Allow admins to view reservations in a read-only list
- Provide a consistent admin layout with sidebar navigation

---

## User Stories

### US-2.1: Admin Login

**As an** admin
**I want** to log in with my credentials
**So that** I can access the management area

**Acceptance Criteria:**
- [ ] Navigating to any `/admin/*` route without authentication redirects to `/login`
- [ ] The login page has username and password fields and a submit button
- [ ] Logging in with `admin` / `admin` grants access and redirects to `/admin/movies`
- [ ] Invalid credentials display an error message on the login form
- [ ] A logout action is available from within the admin area
- [ ] Logging out returns the user to the login page

**Tasks:**
- [ ] Configure Spring Security with form login
- [ ] Create in-memory user with username `admin`, password `admin`, role `ADMIN`
- [ ] Create login view at `/login`
- [ ] Secure all `/admin/**` routes with `@RolesAllowed("ADMIN")`
- [ ] Implement logout functionality

---

### US-2.2: Manage Movies

**As an** admin
**I want** to create, edit, and delete movies
**So that** I can maintain the cinema's movie catalog

**Acceptance Criteria:**
- [ ] The movie grid at `/admin/movies` lists all movies with columns: title, genre, duration, poster URL
- [ ] Clicking "New Movie" opens an empty form with fields: title, description, duration, genre, poster URL
- [ ] Selecting a grid row populates the form with that movie's data
- [ ] Saving a new movie adds it to the grid
- [ ] Saving an edited movie updates the grid
- [ ] Deleting a movie with no screenings removes it from the grid
- [ ] Deleting a movie that has screenings shows an error: "Cannot delete movie with existing screenings"
- [ ] Required fields (title, duration, genre) show validation errors when blank
- [ ] Duration must be greater than 0

**Tasks:**
- [ ] Create Movie Vaadin Flow CRUD view with Grid and form
- [ ] Implement save logic (create and update)
- [ ] Implement delete logic with screening existence check
- [ ] Add Bean Validation annotations to Movie entity
- [ ] Wire up form validation display

**Notes:**
Use Vaadin's `Grid` with single-select mode. The form sits beside or below the grid.

---

### US-2.3: Manage Screenings

**As an** admin
**I want** to create, edit, and delete screenings
**So that** I can schedule when movies are shown

**Acceptance Criteria:**
- [ ] The screening grid at `/admin/screenings` lists all screenings with columns: movie title, date, time, total seats
- [ ] Clicking "New Screening" opens an empty form with fields: movie (ComboBox), date (DatePicker), time (TimePicker), total seats (IntegerField)
- [ ] The movie ComboBox lists all available movies
- [ ] Selecting a grid row populates the form with that screening's data
- [ ] Saving a new screening adds it to the grid
- [ ] Saving an edited screening updates the grid
- [ ] Deleting a screening with no reservations removes it from the grid
- [ ] Deleting a screening that has reservations shows an error: "Cannot delete screening with existing reservations"
- [ ] All fields are required and validated

**Tasks:**
- [ ] Create Screening Vaadin Flow CRUD view with Grid and form
- [ ] Implement ComboBox for movie selection with item label generator
- [ ] Implement save logic (create and update)
- [ ] Implement delete logic with reservation existence check
- [ ] Add Bean Validation annotations to Screening entity
- [ ] Wire up form validation display

---

### US-2.4: View Reservations

**As an** admin
**I want** to view all reservations
**So that** I can see who has booked tickets

**Acceptance Criteria:**
- [ ] The reservation grid at `/admin/reservations` lists all reservations
- [ ] Columns: reservation code, movie title, screening date/time, customer name, customer email, number of tickets, created at
- [ ] The grid is read-only — no create, edit, or delete actions are available
- [ ] Data is sortable by column

**Tasks:**
- [ ] Create Reservation Vaadin Flow view with read-only Grid
- [ ] Configure grid columns with appropriate renderers (e.g., date/time formatting)
- [ ] Ensure no edit/delete controls are present

---

### US-2.5: Navigate Admin Area

**As an** admin
**I want** a consistent layout with navigation
**So that** I can easily switch between management views

**Acceptance Criteria:**
- [ ] All admin views use a shared `AppLayout` with a `SideNav` sidebar
- [ ] The SideNav contains links to: Movies, Screenings, Reservations
- [ ] The currently active view is highlighted in the SideNav
- [ ] A logout button is visible and functional in the layout

**Tasks:**
- [ ] Create admin layout class extending `AppLayout`
- [ ] Add `SideNav` with navigation items for each admin view
- [ ] Add logout button to the layout header or nav
- [ ] Apply the layout to all admin views via `@Route(layout = ...)`

---

## Dependencies

- Requires data model entities (Movie, Screening, Reservation) to be implemented first
- No dependency on Epic 1 (public browsing)

## Definition of Done

- [ ] All user stories completed
- [ ] Spring Security configured and login functional
- [ ] All CRUD operations work correctly
- [ ] Referential integrity checks prevent invalid deletions
- [ ] Form validation displays errors appropriately
- [ ] Visual review of admin layout completed
