
In this short lesson, we will cover a few neat tricks that ES6 has provided us to work with arrays.

  

Later in the course we'll talk about how an array is actually an object, and that's why it has methods like `push` and `splice`, but for now just roll with it ~

  

In particular, we're going to talk about the following array methods:

  

-   `filter`
-   `forEach`
-   `map`
-   `find`
-   `some` & `every`

  

In general, these methods are meant to make our lives easier, and our code more concise and readable.

  
```js
let ages = [12, 41, 11, 10, 32, 27, 18, 19, 19, 14, 58, 41, 9]

let olderThan16 = []
for(let age of ages){
  if(age > 16){
    olderThan16.push(age)
  }
}
```
  

Say we had an array `ages` with numbers representing people's ages, and we wanted to find all the ages above 16. With what we know so far, we'd do something like this:

  

That is quite verbose for this relatively simple operation.

  

We'll go into more detail in a second, but check out how much simpler this becomes with the `filter` method:


```js
let ages = [12, 41, 11, 10, 32, 27, 18, 19, 19, 14, 58, 41, 9]

let olderThan16 = ages.filter(a => a > 16)
console.log(olderThan16) // prints [41, 32, 27, 18, 19, 19, 58, 41]
```
  

Yup. Just that. Let's talk about what's going on here.
