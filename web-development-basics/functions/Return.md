# Return

In JavaScript , inorder to for the function to return values we use , *drum rolls...* , Return!


```js
const add = function(x, y){
  return x + y
}

const sum = add(1, 2)
console.log(sum) // prints 3
 ```


Let's see a more interesting example:

```
const meow = function(){
    console.log("Meow")
}

const woof = function(){
    console.log("woof")
}


const getAnimalSoundFunc = function(animal){
    if(animal=="cat"){
            return meow
        }
    if(animal=="dog"){
            return woof
    }
}

getAnimalSoundFunc("cat")() //will print meow
```
we can see that we can return a function from a function.

Here's another diagram that should help:
 

![.guides/img/functions-return](.\img\functions-return.PNG)


Remember, functions are input-output machines. The input is straightforward: parameters & arguments.

Another small note on the return function - **return** **always exits the function, no matter what**. 

 