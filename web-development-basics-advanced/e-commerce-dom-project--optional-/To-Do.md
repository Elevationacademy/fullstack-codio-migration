
Start by creating two arrays, one named `cart` (which can be initialized as an empty array) and the second called `products`. Products should be initialized with an array of products, where each product is an object with the following properties:

-   `name` - a string which represents the name of the product
-   `price` - a number which represents the price of the product
-   `img` - a url for an image- you can find something online and copy it's 'image-url'

  

* 4 or 5 dummy products is enough

  

Now, create the basic layout of how your web page is going to look. Make sure you have a `div` that acts as a `content-container`. This container is where you will be appending the different type of content (about us, all products, cart items).

  

* Note the container should start out empty.

  

Let's add some functionality to the web app:

-   Create a function in your JS that renders the about us content (which should just be a string). Have it invoked when the `About Us` button (in the nav-bar) is clicked. You can use an event listener to do this.
-   Create a function that renders all of the products (in your `products` array). Have it invoked when the `All Products` button is clicked (you can use an event listener for this).
-   Create a function that renders all of the products in your `cart` (you can start with one or two products in your cart array as dummy data). This function should be invoked when the `Cart` button is clicked.

  

You should empty the `content-container` at the beginning of each function, and append all information to the same `content-container`.

  

Great job on making it this far! You should have a website that has "three pages". You should be able to navigate to each one by clicking a button in the nav-bar.
