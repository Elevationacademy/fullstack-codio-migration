# Parameters & Arguments

In JavaScript the way we define parameters for a function is by passing it in the `()` of the function. 
we do not need to define the type of parameter that a function receives.

```js
const greet = function(name){
  console.log("Hello there, " + name)
}
```

the **parameter** of name that is passed to our function can be used as an **argument**.

But where does the **value** of `name` come from? That's where **arguments** come in:

```js
greet("Dexter")
```

This visual should help:
![.guides/img/functions-arg-to-param](.\img\functions-arg-to-param.PNG)


Whenever we call a function with some arguments, those arguments _initialize_ the parameters of the function. Great stuff.

Default Paramaters
---
Sometimes, we want to avoid weird issues or errors by not sending in the right amount of arguments. The solution (provided by our good friend [**ES6**](https://dev.venntro.com/2013/09/es6-part-1/)) is to set some defaults for our function parameters. Here is a plain example for simplicity:

```js
const multiply = function(x, y = 2){
  console.log(x * y)
}

multiply(3, 4) // prints 12
multiply(3) // prints 6
```  

If we want to give a parameter a **default value**, we use the `=` symbol right after the parameter name.

Reference Pittfalls
---
Remember the difference between **primitive types** and **reference types**? Well, it can cause us some trouble here, too, if we're not careful.

The function below receives some array, then creates a new array initialized to the array it receives, then changes the new array only:
  
```js
const changeArray = function(arr){
  let innerArray = arr
  innerArray[0] = 50
}

const numbers = [1, 2, 3]

changeArray(numbers)
console.log(numbers) // prints [50, 2, 3]
```
  
Alas, even though we've only changed `innerArray` inside of `changeArray` - the `numbers` array changes as well!
  
Again with the reference madness. Just make sure you're aware of this. And of course, this applies to objects as well.

