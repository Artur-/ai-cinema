Use cases are defined in the following form

# UC001: List, add, update, delete products

Administrators can list, add, update and delete products in the the system.

Routes
- /admin/products (listing)
- /admin/products/<productId> (listing + form)

The listing shows products with:
- Name
- Description
- Price
The products can be sorted

There is an add action used to add products. All details are mandatory.

There is an edit action for each product.

There is a delete action for each product. Confirmation is asked before deleting.

## UI

The listing is implemented as a sortable grid.
The product form is shown on the right hand side when a product is being updated or added.

OR

The design for the listing view can be found in listing-view.png
