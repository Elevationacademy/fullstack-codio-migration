So far we've learned to write HTML+CSS, and JS separately. They have not interacted with one another... until _today_.

  

To make our webpages more interesting, we want to be able to **dynamically change the content** on the page - that means either removing, changing, or adding new elements to the page.

  

We also want to interact with the user; if the user clicks a button, we want to _do something_ in response to that.

  

As such, today's lesson will cover the following:

  

-   The DOM and the `document` object
-   Using JS to find HTML elements on our page
-   Accessing the values of those elements
-   Modifying/removing elements and/or their values
-   Creating new elements with JS and adding them to the page
-   Events - things the user does on our page, to which we want to react

  

This is the beginning of doing really cool things as developers! Be excited!

  

----------

  

#### **THE DOM**

  

Before we _do_ anything, we need to understand what we're dealing with. After all, we want to do all these HTML related actions using JS, but we don't write any HTML in our JS files.

  

Remember this: **the way JS accesses HTML elements is through the DOM**

  

DOM stands for **D**ocument **O**bject **M**odel - it is a _representation_ of our HTML document.

  

In particular, it is a representation in which each _node_ in our HTML is an _object_ which represents part of the `document`.

  

What is this `document`?

  

The `document` is an object accessible in JS that represents our entire page. Let's check it out.
