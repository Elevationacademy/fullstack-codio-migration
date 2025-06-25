
In fact, we can **chain** consecutive calls forever, thereby allowing us to avoid callback hell:

  

In the following code we'll start small: 
we'll Get a random word, then **chain** the next operation - get the synonyms of this word :

```
getRandomWord()
    .then((word) => {
        return getSynonyms(word)
    })
    .then((synonyms) => {
        console.log(synonyms)
    })
```
  

What we're seeing here is invoking the `getRandomWord`, then, inside the callback of the first `then` we are **returning the promise of the next operation** - `getSynonyms(word)`.

Remember, the value of `getRandomWord` is a **promise object**,- and who resolves that promise? The second `then`!
So the second `then` will only happen after the `getSynonyms(wordParam)` operation will be fulfilled.

In the second `then`'s callback we have the value we're looking for: the `synonyms` for the random word we got from the first operation.

**Note**, that in the first `then` we return a promise from the callback. This means that the second then's callback will only be invoked after the promise is resolved.


By the way, handling errors when using `then` is quite trivial. **We can use the** `catch` **method to handle errors**:

  
```
getRandomWord()
    .then((word) => {
        return getSynonyms(word)
    })
    .catch(error => console.log(error))
    .then((synonyms) => {
        console.log(synonyms)
    })
    .catch(error => console.log(error))
```
  

As you can see, each `then` can be followed by a `catch` (to handle its errors, if any), and each `catch` can be followed by the next `then` - and everything works as usual.

  

