Use cases focus on user actions and outcomes and are defined in the following form

Here’s a rewritten version in an **active, user-centric use case style**, addressing the comment while keeping the same scope and content:

---

# UC001: List, add, update, and delete products

As an **administrator**, I want to manage products so that I can keep the product catalog up to date.

## Routes

* `/admin/products` — view the product listing
* `/admin/products/<productId>` — view the product listing with a product form

## Main flow

* I open the product listing.
* I see a list of products showing:
  * Name
  * Description
  * Price
* I can sort the list by the available columns.

## Add product

* I choose to add a new product.
* I enter the product details (name, description, price).
* All fields are mandatory.
* I save the product and see it appear in the listing.

## Update product

* I select an existing product from the listing.
* I modify the product details.
* I save the changes and see the updated information in the listing.

## Delete product

* I choose to delete a product.
* The system asks me to confirm the deletion.
* After confirming, the product is removed from the listing.

## UI

* I interact with the product listing through a sortable grid.
* When I add or update a product, I see the product form on the right-hand side of the listing.

OR

* The visual design of the listing view is in **listing-view.png**
