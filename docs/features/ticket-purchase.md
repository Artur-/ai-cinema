# Feature: Ticket Purchase

## Overview

Public-facing feature that allows visitors to purchase tickets for a specific screening. The flow consists of a purchase form and a confirmation dialog. There is no online payment or seat selection — customers pay at the cinema.

## Current Behavior

### Purchase Form

- Accessed from the movie details page by clicking "Buy Tickets" on a showtime
- Pre-selects the chosen screening (movie title + date + time displayed)
- Collects: customer name, customer email, and number of tickets
- Number of tickets is constrained between 1 and the number of available seats
- On submit, creates a reservation and displays the confirmation

### Confirmation Dialog

- Shown after a successful purchase
- Displays: reservation code, movie title, screening date and time, number of tickets
- Provides a clear call-to-action to return to browsing

## User Workflow

```
1. User clicks "Buy Tickets" on a showtime (from movie details page)
          ↓
2. System displays the purchase form with the screening pre-selected
          ↓
3. User enters name, email, and number of tickets
          ↓
4. User submits the form
          ↓
5. System validates input and checks seat availability
          ↓
6. System creates reservation and generates reservation code
          ↓
7. System displays confirmation dialog with reservation details
          ↓
8. User dismisses the dialog and returns to browsing
```

## Edge Cases and Validation

| Scenario | Behavior |
|----------|----------|
| Blank customer name | Show validation error: "Name is required" |
| Invalid email format | Show validation error: "Enter a valid email address" |
| Number of tickets < 1 | Prevent via input constraints (minimum = 1) |
| Number of tickets > available seats | Show validation error: "Only N seats available" |
| Concurrent purchase exhausts seats | Return error: "Not enough seats remaining" and refresh availability |
| Screening becomes sold out before submit | Return error and redirect to movie details |

## UI Components Used

| Component | Purpose |
|-----------|---------|
| Text field | Customer name input |
| Email field | Customer email input |
| Number field | Ticket quantity (min 1, max available seats) |
| Button | Submit purchase |
| Dialog | Confirmation overlay with reservation details |
| Info display | Read-only screening info (movie, date, time) |

## Data Model

### Reservation (created on purchase)
- **id**: Unique identifier
- **screening**: The selected screening (FK)
- **customerName**: Name entered by the customer
- **customerEmail**: Email entered by the customer
- **numberOfTickets**: Quantity of tickets purchased
- **reservationCode**: Auto-generated unique confirmation code
- **createdAt**: Timestamp of reservation creation

## Acceptance Criteria

### AC1: Form Display and Pre-selection
- [ ] The purchase form shows the movie title, screening date, and screening time as read-only info
- [ ] Name, email, and number of tickets fields are present and empty by default
- [ ] The ticket quantity field has a minimum of 1 and a maximum equal to available seats

### AC2: Form Validation
- [ ] Submitting with a blank name shows a validation error
- [ ] Submitting with an invalid email shows a validation error
- [ ] Requesting more tickets than available shows an error message

### AC3: Successful Purchase
- [ ] A valid submission creates a Reservation record in the database
- [ ] The reservation is assigned a unique reservation code
- [ ] The confirmation dialog displays: reservation code, movie title, date, time, and ticket count

### AC4: Concurrent Purchase Handling
- [ ] If seats are exhausted between form load and submit, an error message is shown
- [ ] The user can return to the movie details page to see updated availability
