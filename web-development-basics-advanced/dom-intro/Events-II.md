There is another way we can **assign events**, using only JS. Check this out:

  

**HTML**

```html
<div id="box">Click me</div>
```
  

**JS**

```js
const box = document.getElementById("box")
box.onclick = function () {
    box.innerHTML = "clicked"
}
```
  

Pure JavaScript! Once again, we see how `box` is just a regular JS object - and now we're adding a method to its `onclick` property!

  

This will work exactly the same as before. Try and see for yourself ~

  

Also, try a different property. **Add an** **`onmouseenter`** **to** **`box`** **using only JS**, and do something else in the function.

  

So while this way of adding events has the same effect as doing it through HTML, we _have_ to use this way for elements that we create dynamically - because they don't exist in the HTML in the beginning! For example:

```js
const box = document.createElement("div") // dynamically creating an element

box.setAttribute("class", "box")
box.onclick = function(){       // adding an event to the new element
    box.innerHTML = "I'm alive!"
}

document.getElementById("some-id").appendChild(box) // now the box will be on the page, and will react to a click!
```
  

Go ahead and try this on your own, though note you'll have to create an element with `some-id` for that to work.
