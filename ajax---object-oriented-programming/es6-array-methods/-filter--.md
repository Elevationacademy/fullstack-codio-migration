
Generally, all the array methods take one thing: a function. **It can be anonymous or named**.

  

In the `.filter` example above, we used an anonymous arrow function. Recall that arrow functions implicitly return if there is only one line.

  

So when we do `(a => a > 16)`, what we are saying is "for every `a` inside of `ages`, return `true` or `false` for the expression `a > 16`"

  

We could re-write that `ages.filter` from above like this, using a **named function**:

  

```js
const isGreaterThan16 = function (age) {
    return age > 16
}

let olderThan16 = ages.filter(isGreaterThan16) //notice that passing in the function will implicitly pass it the `a` parameter that the function expects
```
  

Or, taking advantage of arrow functions (still named), like this:

```js
const isGreaterThan16 = (a) => a > 16
let olderThan16 = ages.filter(isGreaterThan16)
```
  

But the point is the same, **the filter method should receive a function that returns a boolean**, and in return **it will return an array with elements that match the filter.**

  

And what do we call a function that is called by another function? A **callback function**! Yes, ES6 array methods are nothing more than simple functions that take a callback and work some logic with those callbacks.

  

Let's break down the syntax real quick:

  

```js
let olderThan16 = ages.filter(a => a > 16)
```
  

-   On the left-hand side of the equals, we're declaring a variable in which we will store the ages that are greater than 16
-   On the right-hand side of the equals, we invoke the `filter` method on the `ages` array, which holds _all_ the ages
-   Here we use an **anonymous** function inside the `filter` method
-   The first `a` inside the method is a variable which will represent each item in the array
-   In other words, the `filter` method will **iterate** over each item in `ages`, and we decide what it should do on each iteration with the a variable we declared
-   Finally, we have our filtering logic: only keep the items which are greater than 16

  

Note that **by convention, the iteration variable is a single letter**, generally the first letter of the array's name. Of course, you can give it a fuller name, but we tend to use these methods to simplify our code, so if we're doing it right, it should be obvious that `a > 16` means `age > 16`.

  

----------

  

**Spot check:** given the array below, use `filter` to get an array of objects of all the orange vegetables:

  

```js
let vegetables = [
    { name: "Eggplant", color: "purple" },
    { name: "Carrot", color: "orange" },
    { name: "Squash", color: "orange" },
    { name: "Tomatoe", color: "red" },
    { name: "Onion", color: "white" },
    { name: "Sweet Potato", color: "orange" }]
```
  

<details><summary>  
Click here to reveal the answer.  
</summary>
  
```js
let orangeVegetables = vegetables.filter(v => v.color === "orange")
```
</details>
