
There are only two differences between arrow functions and normal functions:

1.  Syntax
2.  How this works

That is all - otherwise they are exactly the same.

  

Arrow functions come from **ES6**, and the biggest syntactical change is that the developers decided that writing function was too painful. So here's how we write arrow functions:

  
```
const greet = () => {
  console.log("Hello there")
}
```
  

Poof. The function keyword is gone and replaced by what's known as (totally serious) **fat arrow**syntax.

  

If you call the greet function above, it will be exactly the same as calling this function:

  
```
const greet = function() {
  console.log("Hello there")
}
```
  

You can probably guess that as far as parameters are concerned, it also works in a similar way: parameters go in the parentheses:

  
```
const greet = (name) => {
  console.log("Hello there, " + name)
}

greet("Jolene") //prints "Hello there, Jolene"
```
  

But wait there's more!

  

Arrow functions have an even _shorter_ version for when the function body is one line:

  
```
const greet = (name) => console.log("Hello there, " + name)

greet("Jolene") //prints "Hello there, Jolene"
```
  

A one line function! Wow. We don't even need the curly braces, { or } at all if it's just one line.

  

And you know what else? It can get _even shorter_:

  
```
const greet = name => console.log("Hello there, " + name)

greet("Jolene") //prints "Hello there, Jolene"
```
  

When we only have 1 parameter, we don't even need the parentheses around it! Oh, we hope your heart is fine.