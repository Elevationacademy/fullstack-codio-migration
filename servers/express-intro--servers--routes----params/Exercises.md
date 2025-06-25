## Instructions

For these exercises, let's start fresh. Create a new directory called `furniture-store`. Inside this directory you will:

-   Create a `server.js` file
-   Open a `dist` directory with your basic HTML/CSS/JS files
-   Run `npm init`

  

----------

First thing's first, inside your `server.js` file, create a simple server with a root route.

  

Accessing this route should return a simple string: "Server is up and running smoothly"

## Exercise 2

Add this to your `server.js` file:

  
```
const store = [
    { name: "table", inventory: 3, price: 800 },
    { name: "chair", inventory: 16, price: 120 },
    { name: "couch", inventory: 1, price: 1200 },
    { name: "picture frame", inventory: 31, price: 70 }
]
```
  

Now add a ```/priceCheck``` route which has one parameter: `name`

  

When this route is accessed, it should return the price of the item that was asked for.

  

So if someone goes to `localhost:3000/priceCheck/couch`, they should receive an **object** in response: ``{price: 1200}``

  

If the item _doesn't_ exist, the route should respond with ``{price: null}``

## Exercise 3

Add some HTML and client-side JS that allows the user to input the name of a piece of furniture, then make a GET request to ``/priceCheck`` with that input - you should display the price on the page after it returns.

## Exercise 4
Create another route in your `server.js` file called ``/buy`` which has one parameter: `name`

Accessing this route should reduce the `inventory` of that item by 1.

So if someone makes a request to `localhost:3000/buy/chair`, it should reduce the `inventory` of `chair` to 15. Make sure your route responds with the updated item.

## Exercise 5


Add another input and button in your HTML to allow the user to buy something. Again, make a GET request to the ``/buy`` route with the user's input.

  

After the request is complete, the user should see a message on the page: _Congratulations, you've just bought {item} for {price}. There are {inventory} left now in the store._

## Exercise 6

Create another route in your `server.js` called ``/sale``

  

This route should accept an **optional parameter** called `admin` which takes a boolean

  

If the route is accessed with the `admin` param, it should reduce the price of only the items with an inventory greater than 10 by 50%

  

So if someone makes a request to `localhost:3000/sale/?admin=true`, it should change the price of `chair` to 60, and of `picture frame` to 35.

  

**Hint**: The query parameter can not be a boolean but string only (use if ( something === 'true' )).

**Note:** You must end the **request-response** cycle using  `response.send( store )`` - this will send the store back to the client

## Extension 1 

On the client side, create a variable called `money`, and display it on the page.

  

When the user tries to buy something, **first** make a request to the ``/priceCheck`` route to see if the user has enough money.

  

If the user has enough money, complete the ``/buy`` request (this should happen in the callback of the ``/priceCheck`` request), and reduce the appropriate amount from `money` - otherwise, display a message telling the user they should get a job.

## Extension 2

This one should be fun.

  

Use [setInterval](https://developer.mozilla.org/en-US/docs/Web/API/WindowOrWorkerGlobalScope/setInterval) to make a request to the ``/priceCheck/chair`` route every 3 seconds. You should do this in your `main.js` file in the global scope.

  

Each time this request is made, you should check whether the price of a `chair` is lower than the last time you checked.

  

If it is lower, make a request to the ``/buy/chair`` route, and in this request's callback make a ``console.log("bought chair for less")``

  

Otherwise, ``console.log("still waiting for a price drop...")``

  

Let the interval run a few times and make sure it's not buying anything.

Then in your browser go to the ``/sale`` route - this should drop the price of `chair` - and within three seconds you should see ``"bought chair for less"`` in your browser's console.


