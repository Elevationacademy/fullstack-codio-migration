
The following two features can be slightly tricky (given what you haven’t learned yet), but we believe in you! Use Google if you need help.

  

-   Add an item to your cart:
	-   Create a function named `addToCart` which receives a product object and adds it to your `cart` array.
	-   Add an event that triggers when a user clicks the Add to cart button on a given product. This event should invoke the `addToCart` function with the current product.
	-   There are multiple ways to do this, feel free to get creative
-   Deleting an item from your cart:
	-   Create a `deleteFromCart` function which receives a product object, finds it in the cart array and deletes it from the array.
	-   Add an event that triggers when a user clicks the Delete from cart button on a given product (in your cart). This event should invoke the `deleteFromCart` function with the current product.
	-   Again, there are multiple ways to do this, try and get creative.
	-   Hint 1: Don't rely on what appears on the page to understand what's in the `cart` array. Use the debugger to see if the array updates after the the button is clicked.
	-   Hint 2: After deleting an item from your cart array, make sure to re-invoke your function that displays all the products in your cart (your Cart page). This will result in the page refreshing every time the array changes.
