
In this lesson's intro, we saw something like this:
```
const elem = $("#id")
```
  

The syntax is straightforward: we use the $ - we'll talk about this in a moment - then basically use CSS selector syntax.

  

If we have an element in our HTML with an ID, we use the pound/hashtag symbol to target it, as above.

  

If we had a class, we'd do this instead:
```
const elems = $(".class-name")
```
  

[Here](https://www.w3schools.com/jquery/jquery_selectors.asp) is a full guide to jQuery selectors.

  

Note that in a similar way to CSS, if we select using a class or element name then we will get an _array_ of elements.

  

And what exactly does this get us? Virtually the same as if we had done document.getEleme...- the element(s) itself!

  

You will notice, however, that while vanilla JS returns the element as-is, jQuery gives us a slightly altered version - it's still exactly the same element(s), but now we will be able to do jQuery things to it. We'll see what very soon.