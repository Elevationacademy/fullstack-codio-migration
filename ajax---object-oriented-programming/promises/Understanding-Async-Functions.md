When running this code:

```js
const getRandomWord = function () {
    let words = ['Bonanza', 'Elusive', 'Hindrance', 'Astute', 'Polaroid', 'Phonic', 'Yonder']

    setTimeout(() => {
        return words[Math.floor(Math.random() * words.length)]
    }, 1000);
}


console.log(getRandomWord());
```

We will get `undefined`

Note that this function actually doesn't return anything, and the `console.log(getRandomWord())` will happen before the callback:

```js
() => {
    return words[Math.floor(Math.random() * words.length)]
}
```

Also, look at the return of the callback.
Who use it? and where?

In fact it is redundant. The callback will be called later but no one will use it's return value.

So how do we solve this problem?


<details>
  <summary>
     Answer
  </summary>
    Using a callback!
</details>