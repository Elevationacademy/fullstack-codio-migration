# Functions

![.guides/img/func-in-output](.\img\func-in-output.PNG)

A JavaScript function is a block of code designed to perform a particular task. A JavaScript function is executed when "something" invokes it (calls it).
 
In this lesson we'll talk about the following:

-   Function syntax
-   Calling/invoking functions
-   Function parameters & arguments
-   Default parameters
-   Reference pitfalls
-   The `return` statement
-   Methods

SYNTAX
---

A simple syntax to use functions is : 

  
```js
const greet = function(){
  console.log("Hello there")
}
```
  
Generally, we will want our functions to be `const`s, because there is no reason for them to change.

So as usual, we start by defining a variable with a name: `const greet` - here `greet`* is our `function` name.
###### *Naming convention for functions dictates that **function names should be some sort of _action_, or a verb**. We'll see examples of this throughout the lesson.

The way we invoke the function is by `()`, the moment we invoke it, the function is called 

```js
 greet() //will print "Hello there"
```

