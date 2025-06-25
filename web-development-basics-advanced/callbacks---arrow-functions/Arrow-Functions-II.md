
So that's great for basic syntax, what about return? This also works the same way:
```
const add = (x, y) => {
  return x + y
}

const sum = add(1, 2) 
console.log(sum) //prints 3
```
  

........................but wait. There's more!

  

If the function block is only one line - we don't even need the return keyword!
```
const add = (x, y) => x + y

const sum = add(1, 2) 
console.log(sum) //prints 3
```
  

This is a one line function that knows how to **return** implicitly. Please take a deep breath before moving on. This is all very exciting stuff. _Wow_.

  

Note, however, that if you have a more complicated function, you still need curly braces and return:

  
```
const getHypotenuse = (a, b) => {
  const aSquared = a * a
  const bSquared = b * b
  const cSquared = aSquared + bSquared
  return Math.sqrt(cSquared)
}

const hypoteneuese = getHypotenuse(3, 4) 
console.log(hypoteneuese ) //prints 5
```