
We know that we can easily target elements with jQuery's $:

  
```
$("#idOfElement")
```
  

That works great if I know the exact ID of an element, or if we want to grab a bunch of elements with a class, for example, and do something to all of them.

  

But what if we have some nested data?

  

For instance, say we have some posts on the page, and each post has some nested comments.

  

Since we want to keep our data and visual separate, to remove a comment we need to know its ID, but also the ID of its post. Check out this code:

  
```
<div class="post" data-id="1">
  ﻿<div>
    ﻿<span class="remove">X</span>
    ﻿<span class="comment">A comment</span>
  ﻿</div>
</div>
```
  

When the user presses the X, we need to be able to retrieve the data-id of 1 - because that is this comment's parent.

  

However, we cannot just do `$(".post").data( ).id` - because there will definitely be other posts on the page!

  

The solution to this conundrum is something called **DOM Traversal** - this means traversing (moving) through the DOM from one element to any other.

  

Specifically, in the above code, we want to start on the span with the X, and end at the div with a data-id of 1

Check out this code that does exactly that:

  
```
$(".remove").on("click", function(){
  alert($(this).closest(".post").data().id)
})
```
  

Let's break this down briefly:

  

1.  `$(this)` - we've seen this several times. The object that called the function, i.e. the element with a class of remove that was clicked
2.  `$(this).closest(".post")` - the [closest](https://api.jquery.com/closest/) method says "go up the DOM tree until you reach some element"
3.  Since we passed ".post" as an argument, closest will go up the DOM until it reaches the closest element with a class of post
4.  Note that this is going _up_ the DOM tree with a starting point of the clicked X
5.  `$(this).closest(".post").data().id` - extracts the data-id from the desired post

  

**Try the above code** yourself, on [codepen](https://codepen.io/pen/) for simplicity, and see that the "1" is alerted when you click the X - make sure you have jQuery set up in the codepen!

  

----------

  

Here's an example that's a little more involved.

  

How would we target a specific input element in this HTML?

  
```
<div class="input-area">
  ﻿<span><input type="text"></span>
  ﻿<button class="submit-data">Submit</button>
</div>
    
<div class="input-area">
  ﻿<span><input type="text"></span>
  ﻿<button class="submit-data">Submit</button>
</div>
```
  

This is a pretty standard use-case. It's no problem to add an .on("click") listener to button - if we use $(this) we can always guarantee that the button that was clicked will be the button that reacts to the click event.

  

But what if once the user clicks, we want to get the value inside of the _relevant_input? i.e. the input inside the same input-area as the button.

  

These elements have no ID, no class, and - for design reasons - they're doubly-nested.

To be clear: we want to start at a button (whichever button we clicked on), and end at its nearest input so we can retrieve _its_ specific value.

  

Check out this code that does exactly that:

  
```
$('button').on('click', function() {
  let relevantInputValue = $(this).closest("div").find("input").val()
  alert(relevantInputValue)
})
```
  

That's quite a few **chained methods**, so let's break this down:

  

1.  $(this) - we've seen this several times. The object that called the function, i.e. the button that was clicked
2.  $(this).closest("div") - similar to before
3.  The closest div to the button is the one with a class of input-area - so $(this).closest("div") == $(".input-area") (the specific input-area that is closest to the button)
4.  $(this).closest("div").find("input") - the [find](https://api.jquery.com/find) [method](https://api.jquery.com/find) says "go down the DOM tree until you find some element"
5.  Since we passed "input" as an argument, find will go down the DOM until it finds the first input element
6.  This is exactly the input in which we're interested
7.  Note that this is going down with a starting point of the div with a class of input-area we got in step 2
8.  Finally, $(this).closest("div").find("input").val() will extract the value from that input, just as we wanted

  

**Try the above code** yourself as well.

Since this one is a little trickier, here is a visual flow of how the traversal happens:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dom-traversal.PNG)

  

Note that when we go up/down, we're checking every nested element as well! So when we go down from div to input, we pass through span first.

  

----------

  

This may seem like a lot of work to target a particular element - but generally we only ever have to go up once ( using closest ) to a relevant parent, and then down once (using find ) to the element of interest.

  

Sometimes (as in the first example) it's even enough to just do closest or find - we don't always need both.

  

Still, why don't we just give all our elements an id and then select the element using like that?

  

Often we have repeating blocks of code that each look the same just with different data, and it's impractical to give them all unique identifiers.

  

Thus, we need to be able to traverse the DOM.