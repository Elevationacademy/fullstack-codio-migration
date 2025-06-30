# Exercises: Objects

## Exercise 1
-
And now, your turn

![](https://media.tenor.com/images/0db7c91067dfe5e190c9fcb2fed9ab17/raw)

  

----------

  

Create two 'people' objects, `p1` and `p2`. Each should have the following properties:

  

-   name
-   age
-   city

  

Write some code with the following logic:

  

-   If the people are the same age
-   If the people live in the same city
-   Print "Jill wanted to date Robert"
-   If they're not in the same city
-   Print "Jill wanted to date Robert, but couldn't"

  

Note that the only data should be **in the objects** - in your `if` conditions, make sure to use the objects' properties (keys).



## Exercise 2
-
-   Create an object called `library` that has a `books` **key**
-   The **value** of `books` should be an array of book objects
-   Each book should have a `title` and `author` key

  
  

----------

_* If you've finished all the exercises above and have more lessons ahead, please head to the next lesson and get started. Otherwise continue to the next exercises :)_


Exercise 3 (Extra Practice)
-
You have this setup code:
```js
const reservations = {
  Bob: { claimed: false },
  Ted: { claimed: true }
}

const name = prompt('Please enter the name for your reservation');
```
  

Note that `prompt` will show a popup on your screen and allow you to input some text - that text will be stored inside `name`

  

The above code is a reservation system where people can claim their reservations when they arrive.

  

After receiving the name from the `prompt`,

  

-   If the reservation exists and is unclaimed, welcome the user (console log or use [alert](https://www.w3schools.com/jsref/met_win_alert.asp))
-   If the reservation exists and is already claimed, inform the user about the situation
-   If there is no reservation, tell the user there is nothing under their name

  

Use 'Bob' and 'Ted' to test your code:

  

-   When you test Bob, it should say "Welcome, Bob"
-   When you test Ted, it should say "Hmm, someone already claimed this reservation"
-   If you try a different name, it should say "You have no reservation"

  

**Note:** Definitely upload this code to Github, you might want to use it later on ;)

-----
## Exercise 3.1
It so happens that our restaurant has a bunch of open tables.

  

﻿Therefore, if someone doesn't have a reservation, add it to the reservations object and set "claimed" to true for that person.

----
## Exercise 3.2
As of now, 'Ted' and 'ted' are two different names in our system. Change your code so that 'ted' and 'Ted' or even 'TeD' is all the same.

  

You might be interested in [toLowerCase](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/toLowerCase).



Extensions
-
This one is not hard, it's just involved. Take a breath, take your time.

Given these two variables:

  
```js
const date = 3

const kitchen = {
    owner: "Geraldine",
    hasOven: true/false, // choose one
    fridge: {
        price: 500,
        works: true/false, // choose one
        items: [
            { name: "cheese", expiryDate: 7 },
            { name: "raddish", expiryDate: 2 },
            { name: "bread", expiryDate: 1 }
        ]
    }
}
```
  

You're going to console log these four options _conditionally_, based on the values you selected for `hasOven` and `works`:

  

-   `hasOven`: true and `works`: true
-   Geraldine's raddish expired 1 day ago. Weird, considering her fridge works. Luckily, she has an oven to cook the raddish in.
-   `hasOven`: false and `works`: true
-   Geraldine's raddish expired 1 day ago. Weird, considering her fridge works. Too bad she doesn't have an oven to cook the raddish in.
-   `hasOven`: true and `works`: false
-   Geraldine's raddish expired 1 day ago. Probably because her fridge doesn't work. Luckily, she has an oven to cook the raddish in. And she'll have to pay 250 to fix the fridge.
-   `hasOven`: false and `works`: false
-   Geraldine's raddish expired 1 day ago. Probably because her fridge doesn't work. Too bad she doesn't have an oven to cook the raddish in. And she'll have to pay 250 to fix the fridge.

  

Note that the _expired 1 day ago_ should be calculated based off the `date` variable and `expiryDate` property.

  

Also, _she'll have to pay 250 to fix the fridge_ should be calculated based off the `price` property in `fridge` - it should be half the price.

  

**Make sure** to only use information from the variables you've been given.

**Do not** write out "raddish". Instead, use `kitchen.fridge.items`...

  

**Hint:** Use **helper variables** to make your life easier. For instance:

  
```js
const hasOven = kitchen.hasOven
//...

if(hasOven){
  //...//this will be cleaner than doing: //if(kitchen.hasOven){...
  ```
