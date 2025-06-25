
**Completing the Game**
-
Now that you know events, you can complete the little game!

  

-   Add events to each of the arrow `divs`
-   Each event should call some function that moves the ball according to the arrow direction
-----
**Reservations**
-
Remember the reservations code?
```js
const reservations = {
  Bob: { claimed: false },
  Ted: { claimed: true }
}
```
  

The above code is a reservation system where people can claim their reservations when they arrive.

  

Use an `input` element to get the name, and put all your logic in a `checkReservation` function.

  

The function should be invoked when you click a button:

-   If the reservation exists and is unclaimed, welcome the user.
-   If the reservation exists and is already claimed, inform the user about the situation
-   If there is no reservation, tell the user there is nothing under their name

  

Use 'Bob' and 'Ted' to test your code:

  

-   When you test Bob, it should say "Welcome, Bob"
-   When you test Ted, it should say "Hmm, someone already claimed this reservation"
-   If you try a different name, it should say "You have no reservation"

  

It should work like this, but prettier:

  




  

**Note** that to extract text from an `input`, you should use `.value` instead of `.innerHTML`

--------


**Visual Overload**
-
Create the following (hover over the boxes), using the guidelines below:


  

The rule is simple: when you hover your mouse over any box, that box should change to a random color.

  

-   You should only have **one** `div` inside your **index.html** `body` - a `div` with an ID of `container`, which will hold all the boxes
-   Generate and add the other boxes to `container` using JS (you should be using a for loop)
-   In the loop, you should first create a `box`, then give it its attributes
-   To make each box respond to its own onmouseenter event, you can use the same box you created in the beginning in order to change its background color (alternatively, you can use [JS this](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this))
-   Except for the background colors, the CSS should be in a separate file

  

You can create your own function to generate a random color if you want an extra challenge, [this reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random) might help, or you can use [this code](https://codepen.io/ElevationPen/pen/eaoLjb?editors=0010).

----
**Form**
-
Most websites have some sort of way for a user to sign up - usually through some form, kind of like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/DOM-form-example.PNG)

  

But, if the user tries to submit with a missing field, the form will show an error, like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/DOM-form-example-alert.PNG)

  

Your job is to **create your own form**, with the following conditions:

  

-   Name must be longer than 2 characters
-   Salary must be greater than 10,000 but less than 16,000
-   Birthday may not be null
-   Phone must be 10 digits long

If you follow these steps, you will be able to create this form entirely on your own with what we've learned in this lesson:

  

1.  Create the HTML - it can be as simple as a few `input` fields and a `button` - **do not stress over CSS** for now
2.  Add an **event** to the button that calls a `validate` function
3.  In the function, you should retrieve the information from each field
4.  To get the element, you'll use `document.getElementById` like we talked about
5.  Once you have all the data the user entered, you need to execute some `if` statements that check the conditions
6.  Finally, if there are any errors, you should create an element and add it to the page - these should be in red

  

Make it pretty when you're done - definitely a nice little project to have in your Github. Here are some [nice colors](https://flatuicolors.com/palette/defo) you can use.

  

Do this one step at a time. Use `console.log` to check everything. You can do it!

  
---------------------------

Finished everything and ready for a challenge? This is where you get to create cool things.

  

**Form Extension**
-

If the user entered all the data correctly, make the entire form disappear ( **hint:** use display: none )

Then, show a welcome message with the user's name

  

----------

  

**Visual Overload Extension**
-

Display a message below the boxes that says "Nice job!" if all the boxes are the same color.

  

  

----------

  

  

**Ball Game Extension**
-

No one should be forced to click so much. Using [these docs](https://developer.mozilla.org/en-US/docs/Web/Events/keydown), figure out how to use keyboard presses to invoke your functions that move the ball. In future lessons we'll learn how to turn this into a proper game, but for now this is a good foundation.

  

# **lesson.onDone = rest( )**

