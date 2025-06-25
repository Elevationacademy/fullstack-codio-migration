
We now have all of our data in our App state, our single source of truth, and have the relevant components watching the state. Now, we can write functions to change the state!

  

In your `Item.js` component, **change each item from being just a div, to including an input with a checkbox inside the div.**

  

If your item has `completed = true`, then you should change the class name of the div returned from your Item component to some conditional CSS, like a strikethrough (make sure to check out the included CSS to see what classes are provided).

  

Check out the solution [here](https://codepen.io/ElevationPen/pen/armZgb?editors=0010)