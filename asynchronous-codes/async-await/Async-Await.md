
Let's see the exact same code as before, but with new syntax:

  

**API Request**:

  

```js
const fetchDatum = async function () {
    let data = await $.get(API_URL)
    console.log(data.items[0])
}
```
  

Sweet mother of Moses - it's lovely. No callbacks. And. It. **Works.**

  

Out of the box, no tricks, no gimmicks - the `async` and `await` keywords are now built-in to modern JS, both on major browsers and in Node.

  

Of course, **there are some rules**:

-   The `async` keyword comes before the `function` definition
	-   This forces the function to return a **promise**, no matter what
-   You cannot use the `await` keyword outside of an `async` function
-   You can only use `await` on what's known as **`then`****able operations**
	-   These are operations that return a [promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), such as a jQuery GET request
-   If you have functions calling functions, if at any point you use `async` - then **all** of the ancestor functions must be `async` as well, and all the returns must be `await`ed (when returning data)
	-   We'll see this in a moment

  

The syntax is pretty straightforward, and the point of this is to make our code _look_ more synchronous - but in reality the only thing that is synchronous is everything after the `await` keyword, **in the scope** of the function.
