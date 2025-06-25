Now that we have `down` in a variable, we can access some of its properties pretty easily. For instance, try this out:

  
```js
console.log(down.innerHTML)
```
  

The `innerHTML` property is how we extract content from inside our elements.

  

Not only that, we can use it to _modify_ our content. Try this out:

```js
down.innerHTML = "Down"
```
  

Neat.

  

What do you expect to see when you console log the `innerHTML` of `playingField`?

  

<details><summary>
  Click here to reveal the answer.
</summary>
The `div` with an ID of `ball`! That is the _inner_ content of `playingField` - make sure you try this out ;)
</details> 
  

----------

  

We don't have access to some properties right away. For instance, this will be an empty string:

```js
playingField.style.backgroundColor
```
  

Even though we know this `div` definitely has a background color.

  

The thing is, the `.style` property only retrieves styling that was placed _directly_ on the element, like this:

  
```html
<div style="background-color: red"></div>
```
  

But our styling is in our `style.css` file - which is good practice. We don't often need to access the styles of an element (it's usually enough to know how to modify them), but if you're very interested you can read about how [here](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle).

  

Anyway, we _can_ modify styles directly likes this (which is what we saw earlier):

```js
playingField.style.backgroundColor = "blue"
```
  

Notice, by the way, that even though in CSS the property is called `background-color`, in JS it is the same but with camelCase. That is because we cannot use dashes in JS variables or properties.
