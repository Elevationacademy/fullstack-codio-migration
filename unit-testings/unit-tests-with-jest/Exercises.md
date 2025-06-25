
That's the basics of testing - and unless you get to async/mocking, there's really not much more to it!

  

In these exercise you get an opportunity to **practice reading and understanding docs** - thankfully for you, [the Jest docs](https://jestjs.io/docs/en/expect) are quite good.

  

For simplicity's sake, all the exercises will use one class: `Exercises` - you should write add all your methods to this class, and write the tests using an instance of this class.

  

**Note:** unless otherwise stated, **do not change the code given to you!**

  

**Also:** do **not** erase any of your tests - you will need them all in a later exercise.

----------

  

**Exercise 1**

  

Write a test for the following method:

```
//should return true if n is even, false otherwise
isEven(n) {
    return n % 2 == 0 ? true : false
}
```
  

**Note:** do **not** use `.toBe(true)` - read the docs ;)

  

----------

  

**Exercise 2**

  

Write a test for the following method:

```
//should remove at least one element from the array `arr`
removeAtLeastOne(arr) {
    let numItemsToRemove = Math.floor(Math.random() * (arr.length - 1)) + 1
    arr.splice(0, numItemsToRemove)
    return arr
}
```
  

**Hint:** Because the above method is using `.random` - you can't know how many items will be after the splice - only that there _should_ be _less than_ the original array.

----------

  

**Exercise 3**

  

Write a test for the following method:

```
//should return a clean string without these symbols: "!", "#", ".", ",", "'"
simplify(str) {
    let symbols = ["!", "#", ".", ",", "'"]
    return str.split("").filter(c => symbols.indexOf(c) == -1).join("")
}
```
  

Notice that this is purposefully written in a somewhat complex way - this is to highlight the fact that **you don't really have to understand the code to write a good test for it!**

----------

  

**Exercise 4**

  

Now let's **practice TDD**.

  

Here is the task you received from your manager, **write the test(s) first** and only then write the method:

-   Write a method called `validate`
-   The method should receive an array of booleans
-   It should verify that there is at least one **boolean** in the array
    -   If there isn't, it should return `{error: "Need at least one boolean"}`
-   If there are more `true`s than `false`s in the array, the method should return `true`
-   Otherwise, it should return `false`

  

**Hint:** `typeof` could be useful here.

----------

  

**Exercise 5**

  

For **each** of the previous exercises, write **at least one more test** - this might seem tricky at first, but _think_ of all the edge cases:

  

-   What if we didn't receive a parameter at all?
-   What if the parameter is the wrong type?
-   Did you take care of `null`, `undefined`?
-   Too many values, too few?

  

In testing, there is almost _always_ more to check. With these additional tests, **you might find that the code was actually not perfect to begin with** - and that's why we have tests, to discover these cases.

----------

  

#### **EXTENSION**

  

Aside from just testing I/O (input/output) of methods, we can also use Jest to **test whether a method has been called at all** - or whether it has been called a certain amount of times, or with a certain parameter.

  

Read about [toHaveBeenCalled](https://jestjs.io/docs/en/expect#tohavebeencalled) **and** about [spy](https://jestjs.io/docs/en/jest-object#jestspyonobject-methodname).

  

Once you've got a grasp of those, write a test that checks whether `push` has been used in this method:

  
```  
add(x, y){
    let stuff = []
    stuff.push(x, y)
}
```
  

**Hint:** you might need to use `Array.prototype`