Now we will add a callback 
```js
const getRandomWord = function (callback) {
    let words = ['Bonanza', 'Elusive', 'Hindrance', 'Astute', 'Polaroid', 'Phonic', 'Yonder']
    setTimeout(() => {
        callback(words[Math.floor(Math.random() * words.length)])
    }, 1000);
}


getRandomWord((randomWord)=> {
    console.log(randomWord);
})

```

Now `getRandomWord` receives a callback as it's parameter.
This callback will be called after the 1 second timeout, get the random word and do what ever it wants with it, in our case - print it.

