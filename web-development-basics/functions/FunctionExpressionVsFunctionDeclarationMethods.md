# Function Expression vs. Function Declaration, Methods

So far we've written what's known as **function expressions** - that is, each function is stored in a variable. This is good practice.

There is another, slightly wild-west way of writing function called **function declarations**, and that looks like this:

```js
function greet(){
  console.log("Hello there, from the wild, wild West")
}
```  

The only difference between the two is that **function declarations can be called from anywhere** because JS will **hoist** them (send them up to) the top of the JS file.
Hoisting is also done for variables that were declared with `var`. You can read more about hoisting [here](https://developer.mozilla.org/en-US/docs/Glossary/Hoisting).

On the other hand, **function expressions can only be used after they're initialized**. Check this:
```js
greet() //works without a problem
greetExpression() //throws an error

function greet(){
  console.log("Hello there, from the wild, wild West")
}

const greetExpression = function(){
  console.log("Uh oh")
}
```  

Try out the above yourself and see what we mean. Read the error, it makes sense.

----------
 

## **METHODS**

Now that we understand functions, here's something really cool we can do with objects - check this out:

```js
const person = {
  name: "Julius",
  speak: function() {
    console.log("Et tu, Brutus?")
  }
}
```
  

Remember how we said we can store anything as the value of a key? Serious business here. _Anything_.


When we define a function likes this (as part of an object), it's called a **method**, and it can be used just like a normal object property/function call:

```js
console.log(person.name) //you know what this will do

person.speak() //and this? Try it out!
```  

Note that we still have to **invoke** the method, and it can have parameters too!