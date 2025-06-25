Some styles are not as trivial to modify. For instance, what if we wanted a function to push the position of the ball 15px away from the left?

Because it is an `absolute` element, we should be able to use the `left` property. However, if we call this function in the console, it will do nothing:

```js
const moveRight = function(){
  document.getElementById("ball").style.left += 15
}
```
Try it out - write the code above in your `main.js` file, save, refresh the page, then call `moveRight()` **in the console**. You should see nothing changing.

That is because the value of `left` should be a `px` unit.

Then again, this will work once, but no more:

```js
const moveRight = function(){
  document.getElementById("ball").style.left += "15px"
}
```
Try this as well, use the debugger. Do you understand why this only works once?

<details><summary>
  Click here to reveal the answer.
</summary>
The first time we do `+= "15px"`, it will set the value of `left` (which initially is an empty string) to `"15px"`, which is great.
But then if we keep doing that, we're just concatenating strings - and JS will ignore that since the value of `left` cannot be `"15px15px"`

The solution, then, is to:

1.  Get the number value of `left` (i.e _parse_ the 15 out of the "15px")
2.  Increment _that_
3.  Concatenate "px" to the end of the number

If you do the above, then each time you call `moveRight`, the ball will move 15 pixels to the right.

  
  ----

To _parse_ a number, JS has a [parseInt](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt) function, which tries to identify a number in a string, like this:


```js
console.log(parseInt("15px")) // prints 15
```
  </details>