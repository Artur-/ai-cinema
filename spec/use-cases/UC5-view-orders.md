# UC5: View Orders

## Summary

Admins can view all ticket orders. This is a read-only view used to verify orders at pickup.

## View Type

**Admin Vaadin Flow view** — requires login.

## Actors

- Admin (authenticated user)

## Preconditions

- Admin is logged in.

## Main Flow

### Listing Orders

1. Admin navigates to the orders management page.
2. The system displays a grid/table of all ticket orders with columns:
   - Order number
   - Movie title
   - Screening date
   - Screening start time
   - Customer name
   - Customer email
   - Number of tickets
   - Order timestamp
3. The grid supports sorting by column headers.

### Filtering and Searching

4. Admin can filter the grid by screening date.
5. Admin can search by order number (text input that filters as the admin types).

## Notes

- This view is read-only. Admins cannot create, edit, or delete orders.
- The primary use case is verifying an order when a customer arrives to pick up tickets — the admin searches by order number and confirms the details.
