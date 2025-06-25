This is the start of our code:

```js
getRandomWord()
    .then((word) => {
        return getSynonyms(word)
    })
    .then((synonyms) => {
        console.log(synonyms)
    })
```

Add the next phase - getting the sentiment of the first synonym. You can assume that it returns a promise.
For a final touch you can get the description of the sentiment and print it. 


<details>
  <summary>
     Solution
  </summary>

```
getRandomWord()
    .then((word) => {
        return getSynonyms(word)
    })
    .then((synonyms) => {
        return getSentiment(synonyms[0])
    })
    .then((sentiment) => {
        const sentimentDescription = getSentimentDescription(sentiment)
        console.log(sentimentDescription)
    })
```
</details>