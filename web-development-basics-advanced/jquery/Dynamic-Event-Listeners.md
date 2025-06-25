
When we do something like $(...).on(...) - the underlying assumption is that this element is **on the DOM at when the listener is added**.

  

Take this example:

  

**HTML**
```
<button>Add Div</button>
```
  

**CSS**
```
.box{
  width: 100px;
  height: 100px;
  background-color: blue;
  margin: 10px;
  display: inline-block;
}
```
  

**JS**
```
const addDiv = function() {
  $("body").append("<div class=box></div>")
};

$("button").on("click", function() {
  addDiv()
});

$(".box").on("click", function() {
  alert("hi")
});
```
  

There are two event listeners here - a click for a button element, and a click for any element with a class of box

  

The button is on the DOM (physically in the HTML) _before_ we add its click listener.

Therefore, whenever we click the button, the addDiv( ) function will be invoked.

  

That's great.

  

However, there are no elements with the class of box on the DOM when the second listener gets added! These elements get added _dynamically_, so we need a dynamic way to add listeners to them.

  

In other words, when we add the $(".box").on("click", ...) listener (line 9), it's pretty much pointless! That code runs _once_ - and at the point when it runs, there is no .boxes to which we can add that click listener.

  

**Try out the code yourself** (on [codepen](https://codepen.io/pen/) for simplicity) and see that though we are able to add blue boxes to the page, nothing happens when we click them.

  

----------

  

There are two main ways to fix this issue.

1.  Add the listener after the element is created
2.  The smart way

  

Here's the first way:
```
const addDiv = function() {
  $("body").append("<div class=box></div>");
  
  $(".box").on("click", function() {
    alert("hi");
  });
};

$("button").on("click", function() {
  addDiv();
});
```
  

Now we only add the click listener for elements with the box class _after_ we add them to the page.

  

If you do the above, you will run into a _different_ issue - each time we create an element we add another listener...to _all_ the elements with a class of box - try adding a few boxes, then click on a few, and you're going to see a whole lot more alerts than you expected.

  

The solve for this issue is to use jQuery's [off](http://api.jquery.com/off/) function- but it's a bit of a hassle when we have a better option.

  

Here's the smart fix to our issue:
```
const addDiv = function() {
  $("body").append("<div class=box></div>");
};

$("button").on("click", function() {
  addDiv();
});

$("body").on("click", ".box", function() {
  alert("hi");
});
```
  

The changes are:

-   Instead of adding the listener to .box we're adding it to body
-   We've added another argument to the on function

  

The second argument is optional, and together with our first change, here's what we're saying:

For any element with a class of box inside of body, add a click listener to it.

  

In other words, the extra argument - the ".box" - is called a **selector** and it restricts the click event to only the .box descendants of body.

  

This works no **matter when the descendants are created** because body _is_ on the DOM when this code runs - so body will know to keep adding click listeners to any .box child it will have in the future.

  

Of course, we don't have to use body - in fact we shouldn't; we should use the most direct parent that is on the DOM when the function runs.

  

Make sure to **test the above code** to see it working.