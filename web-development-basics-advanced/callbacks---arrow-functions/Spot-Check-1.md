# Sample content Page 
Let's look at a simple callback example first, then fix the problem above.

  
```
const first = function () {
    setTimeout(function () {
        console.log("should be first")
    }, 3000)
}

const second = function () {
    console.log("should be second")
}

first()
second()
```
  

What will the above console log?

<details><summary>
  Click here to reveal the answer.
</summary>

"should be second", _then_ "should be first" - because of the setTimeout!

</details>

</br>
  

And the fix, as promised, with a callback:

```
const first = function (callback) { //receive the function as a parameter
    setTimeout(function () {
        console.log("should be first")
        callback() //this is the `second` function being invoked
    }, 3000)
}

const second = function () {
    console.log("should be second")
}

first(second) //pass the second function to the first, as an argument
```

  

And there you are - the above guarantees that second will only execute after "should be first" prints because it was passed as a parameter and called later - **callbacks**!

  

Notice that we're just passing the second function as a normal _parameter_ - we're not invoking it!2