
Events in jQuery are very similar to what we saw when working with the VanillaJS DOM API.

  

There are many kinds of user events that can be handled, for example: click, scroll, hover, etc.

For a full list of jQuery events [check out the docs](https://api.jquery.com/category/events/).

  

To set up an event listener on a particular element or elements we first need to select them, using the same technique from earlier in the lesson.

  

As we saw earlier, selecting an element with jQuery exposes a bunch of methods including on

The [documentation](https://api.jquery.com/on/) tells us that on is the jQuery method that we can use for event handling. Look at this code:

  
```
$('button').on('click', function () {
  alert('clicked!')
})
```
  

What do you think it does?

<details><summary>
  Click here to reveal the answer.
</summary>

The above code adds a click handler function to every button on the page! Therefore when any button is clicked, "clicked" will be alerted.
</details>

</br>


  

There is also a short hand method called just click:
```
$('button').click(function () {
  alert('clicked!')
})
```
  

These both do the same thing. Let's note exactly what's going on in both cases. Two things:

  

1.  They are each **binding** a click event to the button element(s) on the page. It could be said that once this code runs, the button(s) will begin "listening" for clicks and respond accordingly
2.  They both take a function as an argument, and invoke it when a click event happens on the button. This is a **callback** function in action!

  

Each of these examples could also be written like this:
```
const clicked = function () {
  alert('clicked!')
}

$('button').on('click', clicked)
```
  

or...
```
const clicked = function () {
  alert('clicked!')
}

$('button').click(clicked)
```
  

Callbacks are great.