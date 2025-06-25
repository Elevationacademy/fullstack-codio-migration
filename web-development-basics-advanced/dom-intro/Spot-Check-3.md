Go ahead and try to **rewrite the** **`moveRight()`** **function** so that the ball moves right each time you call it (in the console).

  

**Hint:** the initial value of `style.left` is an empty string, which you cannot parse. You can use this code to help:

```js
parseInt(...) || 0 // will parse a number, or return 0 if it can't parse
```

  

Once you've tried this for at least 10 minutes, check out this Solution if you are stuck

<details>
<summary>Solution</summary>
<div> 

```js
const moveRight = function(){
    const ball = document.getElementById("ball")
    let left = parseInt(ball.style.left) || 0
    left += 15
    ball.style.left = left + "px"
}
```
</div>
</details>

