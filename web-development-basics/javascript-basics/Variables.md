# Variables

In JavaScript we will use **variables** in the following way:




```js
let country = "Djibouti"
```



We can declare a **variable** and not assign a value to a **variable**
 
```js
let mysteriousCountry //not initialized, only defined
``` 



----------



It is **Best Practice** to use **camelCase** when we name our variables - first word lowercase, and each subsequent word hasUpperCasedFirstLetter.



**Note:** if you do not initialize a variable, then its default value will be **`undefined`** **- this is a special expression in JavaScript** that means exactly what it says "this variable is undefined (so far)."




----------

  

In JS, there is a difference between something that is **undefined**, and something that is **not defined**.

Consider the following code, assume it is our entire file:


```js
let userResponse

console.log(userResponse) // prints undefined
console.log(userName) // throws an error
```
  

We _have_ defined that `userResponse` exists by saying let `userResponse`, we just haven't defined its value (i.e. we haven't initialized it) - hence this is `undefined`.

  

As for `userName` - it doesn't exist anywhere!

As such, you will see this error:

  

    Uncaught ReferenceError: userName is not defined

  

**Important difference. Note it well.**


----------

  

## **TYPES**

  

Variables can hold pretty much anything. the most important ones are : 
  - Boolean
  - Numbers
  - String

 
----------

## **PRIMITIVE TYPES**

  

The variable types we've just talked about are called **primitive types**.


  
```js
let a = 6
let b = a

console.log(a) //prints 6
console.log(b) //prints 6

b = 2

console.log(a) //prints 6
console.log(b) //prints 2
```
  

This may not seem exciting right now, but notice that the value of `a` is unaffected by the change in `b`, even though originally we set `b` to be equal to `a`. Again, this may seem obvious and natural - why should a change anyway? It's fine to think like this.

  

For now it's enough to understand that **whenever we initialize a primitive type variable, JS will create a new space in its memory to remember that variable**.



  

----------

  

## **CONCATENATION**

  



Concatenation means to link or chain things together. If we have two strings, **"car"** and **"pet"**, and we concatenate them, we will get **"carpet"**.


In JS we generally concatenate strings, and the simplest way to do this is using the `+` operator:


```js
const firstString = "car"
const secondString = "pet"
const bothStrings = firstString + secondString
```
  

If you `console.log(bothStrings)`, you will see "carpet" in the output.

  

**By the way, if you concatenate a string and a number, JS will join them into a string. We will not go into it right now, but it is because of [coercion](https://developer.mozilla.org/en-US/docs/Glossary/Type_coercion).**
  

Another way to concatenate strings is using `+=` - we say "plus equals" - like this:


  
