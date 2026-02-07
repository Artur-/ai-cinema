# UC003 — View Orders

## Summary
Admin views all ticket orders in a read-only list with search and filtering.

## Actor
Admin (authenticated user)

## Preconditions
- Admin is logged in

## Main Flow

1. Admin navigates to the Orders admin view.
2. System displays a Grid with columns: Order Number, Movie, Screening Date, Screening Time, Customer Name, Email, Ticket Count, Created At.
3. All columns are sortable (click column header to toggle sort direction).
4. Admin uses search/filter controls to narrow results:
   - **Order Number** — text filter (partial match)
   - **Customer Name** — text filter (partial match)
   - **Date Range** — from/to DatePickers to filter by screening date
5. Grid updates as filters are applied.

## Alternative Flows

### AF1 — No Orders
- The Grid is empty. No special empty-state message is required (an empty Grid is sufficient).

### AF2 — No Filter Matches
- The Grid shows no rows matching the filter criteria.

## Postconditions
- No data is modified. This view is read-only.

## UI Description

- **Technology**: Java (Flow), login required
- **Layout**: Filter controls above the Grid, Grid below
- **Grid columns**: Order Number, Movie (title from the screening's movie), Screening Date, Screening Time, Customer Name, Email, Ticket Count, Created At
- **Behavior**: Read-only — no edit or delete actions
- **Sorting**: All columns sortable
- **Filtering**: Text fields for order number and customer name; DatePicker pair for screening date range
