
For the sharp-eyed, you will have noticed something: when we use setTimeout - we're actually using a callback function inside! Look again at the syntax of setTimeout:

  
```
setTimeout(function(){...}, 3000)
```
  

Remember, setTimeout is a function in and of itself, and what's the first parameter we're passing it...? A _function_! Therefore, the inner function ( when it's called inside of setTimeout ) will be a callback.

  

By the way, that function ( the one we're passing to setTimeout ) is called an **anonymous function** - anonymous because it doesn't have a name. We could re-write the setTimeout call like this:

  
```
const doSomething = function(){
  console.log("something")
}

setTimeout(doSomething, 3000) //will invoke doSomething in 3 seconds
```