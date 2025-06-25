An async operation is an action that steps out of the **line by line** synchronous code.

We saw `setTimeout` as an example:

```JavaScript
    console.log("before setTimeout")
    setTimeout(function () {
        console.log("in the callback")
    }, 1000)
    console.log("after setTimeout")
```

`setTimeout` will be invoked after the first print, but it's callback will be called later on.

Other async operations might be DOM events or API calls using ajax. In this lesson we will use `setTimeout` to show async code flows.

If we look at this function that returns a random word:
```js
const getRandomWord = function () {
    let words = ['Bonanza', 'Elusive', 'Hindrance', 'Astute', 'Polaroid', 'Phonic', 'Yonder']
    return words[Math.floor(Math.random() * words.length)]
}
```

We can see that it is a synchronous function.
Let's make it async by adding a `setTimeout`:

```js
const getRandomWord = function () {
    let words = ['Bonanza', 'Elusive', 'Hindrance', 'Astute', 'Polaroid', 'Phonic', 'Yonder']

    // using setTimeout to simulate an async operation that takes time
    setTimeout(() => {
        return words[Math.floor(Math.random() * words.length)]
    }, 1000);
}
```

Now we will get the random word after a second.

What will this function print if we call it?
```JavaScript
console.log(getRandomWord());
```
Try to answer the question without running the code, then run the code and see the result. 

Move to the next page to see the result.
