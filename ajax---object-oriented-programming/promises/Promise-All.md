That worked well.
Now let's look at a bit of a different scenario.
In this case, we will get a random word and for that word we will want to print it's sentiment and its synonyms.

We could implement it like this:
```js
let word = null
let synonyms = null

getRandomWord()
    .then((wordParam) => {
        word = wordParam
        return getSynonyms(word)
    })
    .then((synonymsParam) => {
        synonyms = synonymsParam
        return getSentiment(word)
    })
    .then((sentiment) => {
        const sentimentDescription = getSentimentDescription(sentiment)
        console.log(`The word ${word} has synonyms ${synonyms} 
        and a ${sentimentDescription} sentiment`)
    })
```

But remember, both `getSynonyms` and `getSentiment` require a `word` - they both depend on the result of our `getRandomWord` operation. They **do not** depend on one another, so it is not efficient to chain them.


In order to solve this issue, we need to introduce a new concept: 
`Promise.all`
`all` is a method of the `Promise` object that waits for any number of promises to be resolved. Once they are all resolved it will execute the promise that it got as a parameter. 

Our new code will now look like this:
  
```js
let word = null

getRandomWord()
    .then((wordParam) => {
        word = wordParam
        let synonymsPromise = getSynonyms(word)
        let sentimentPromise = getSentiment(word)
        return Promise.all([synonymsPromise, sentimentPromise])
    })
    .then((promiseResults) => {
        // The first item in the array is our synonyms array, and the second is the sentiment for the word we got.
        let [synonyms, sentiment] = promiseResults
        const sentimentDescription = getSentimentDescription(sentiment)
        console.log(`The word ${word} has a ${sentimentDescription} sentiment and synonyms ${synonyms}`)
    })
```
  

Here's the flow for the above:
1. Get a random word
1. Once this promise is resolved, we have access to the `word` we need inside the `then`'s callback
1. We store both the `getSynonyms` and `getSentiment` promises inside of variables
1. We use `Promise.all([...])` to tell JS to resolve _all_ the promises in the array before executing the next `then`
1. Inside the second `then`, we get `promiseResults` which is an **array of all our resolved values**
1. Print the information 

It's true that this might not be the _friendliest_ syntax in the world - but it is certainly better than the callback hell from before - and it's _just_ syntax.

The principles of promises are simple: **instead of using nested callbacks, we can used chained promises to resolve series of async code** - or use `Promise.all` to resolve several promises together.