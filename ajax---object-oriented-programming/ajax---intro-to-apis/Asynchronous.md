
When we talk about AJAX and making API requests, we often mention this idea of asynchronicity. To understand what that means, take a look at this code example:

```js
let person = {name: "Kyle", age: 37}
let expectedYearsLeft = 120 - person.age

console.log(`${person.name} has ${expectedYearsLeft} years to live`) //prints Kyle has 83 years to live
```
  

This code is **synchronous** - it executes exactly one line at a time. The reason we can do `person.age` on the second line is because the we've already defined `person` and the `age` property on the previous line - this is standard code execution with which we are familiar.

  

However, when we change the first line - our data - to be generated **a**synchronously:

  
```js
let person
setTimeout(function(){
  person = {name: "Kyle", age: 37}
}, 1000)

let expectedYearsLeft = 120 - person.age

console.log(`${person.name} has ${expectedYearsLeft} to live`)
```
  

It fails! It throws the error `Uncaught TypeError: Cannot read property 'age' of undefined`  - even though we've clearly defined `person`!

  

The problem is that `person` gets defined 1 second (1000 milliseconds) later. Since `setTimeout` is an **asynchronous** function, the rest of the code continues to execute before it's done - i.e, before we actually define `person`! Hence the error.

  

The under-the-hood workings of this has to do with the JS engine, which we will talk about in the future, but for now it is enough to understand that **asynchronous code runs in "the background", allowing other code to continue normal execution**.

  

While in the above case it doesn't make sense to have our code run asynchronously (we don't want undefined), when we request data from APIs (we'll talk about that in a second) we definitely want that to be asynchronous because - just like the `setTimeout` function, **API requests take time**.

  

Even if that time is only half a second, **if we let the request happen synchronously, our whole app would freeze**. The user wouldn't be able to interact with anything, and that is bad UX (user experience). So we make these requests asynchronously so that the user may continue enjoying our application smoothly.

  

With that in mind, let's talk about what these API requests actually are.
