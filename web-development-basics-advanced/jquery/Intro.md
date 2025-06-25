
We've been working with the DOM a bit, and eventually you've got to get tired of writing document.getElementById... - it's very verbose.

  

So today we're introducing the **jQuery library** - effectively this will give us several shortcuts to working with the DOM. Don't get confused: **jQuery is just JavaScipt**. Specifically, it is a [wrapper](https://en.wikipedia.org/wiki/Wrapper_function) for **vanilla JS** that makes our lives easier.

  

For instance, instead of writing this in vanilla (plain, regular) JS:
```
document.getElementById("container")
```
  

We'll write this with jQuery:
```
$("#container")
```
  

In terms of getting an element by an ID, they do the exact same! But that jQuery sure is more convenient.

  

jQuery does more than give us shortcuts for things that vanilla JS already does. It also gives us extra methods that do specific things for us. Like this:

  
```
//vanilla JS
document.getElementById("container").style.display = "none" 

//jQuery
$("#container").hide() //when we select elements with jQuery, we also get methods that can work on the element, on top of the element itself
```
  

We'll talk more about jQuery methods soon.

----------

  

There's a lot to explore in jQuery, but for this lesson we'll focus on the following:

  

-   Targeting/selecting elements
-   Understanding $
-   Common jQuery methods
-   css and addClass
-   val
-   data
-   Handling user events
-   Good ol' this - in jQuery
-   Creating & adding/removing elements to/from the DOM
-   Dynamic event listeners

  

It may seem like a lot, but really it's mostly the same things we did in vanilla JS, with more convenience.

Call it DOM++ if you like.