## Instructions

 let's put our CRUD and `router` knowledge to practice.

  

For the following exercises, you must first make sure you understand how to use [Postman](https://www.getpostman.com/) - these will be purely backend exercises. No frontend code.

  


  

## Exercise 1

This will be a straightforward Word Counting backend that allows us to send `words/sentences`, and then make a request to see how many times those words have appeared in previous requests.

You can write each exercise in its corresponding section in the `server.js` file.

First, in your `server.js` file, create a `/sanity` route that simply responds with
```html
Server is up and running
```

## Exercise 2

create an empty object called `wordCounter` in your server.

This object's keys will be words (any word), and each word's value will be a number.

For starters, set up another `get` route that receives one parameter: `word` - this should be a string with a single word in it.

If the `word` is inside of `wordCounter`, respond with an object that looks like `{count: wordCount}`. Otherwise, respond with `{count: 0}`

For example: If the word you asked for was found in `wordCounter` and it had a count of 4, you should respond with an object that looks like this `{count: 4}`

## Exercise 3

Now create a `post` route. It accepts an object with the key: `word`*- and its value should be a string with a single word in it.

  

This route should add the word to `wordCounter` with a count of `1` if it doesn't exist, or increment its count if it does.

  

The response from the server should be an object that looks like this `{text: "Added {word}", currentCount: {count} }`

  

_*In other words, you should be able to make a POST request to this route and send a {word: "..."} object to it_

## Exercise 4
Now create another `post` route that receives one parameter: `sentence` - still a string, but it should be a string with many words.

This route should do the same thing as the `.post(/word)` route does, but for each word in the inside of `sentence`

The response from the server should be `{text: "Added {numNewWords} words, {numOldWords} already existed", currentCount: -1}`

To clarify: `numNewWords` is the number of new words (if any) that came in from this POST request, and `numOldWords` is how many words came in that you already had in your `wordCounter` object.

## Exercise 5
Add a `delete` route that receives one route parameter: `word`. It should delete the given word from the object.
Think about any errors that might occur. How would you handle them?
In your response make sure to return the relevant **status code** and an informative message.



## Extension 1
If you send `"This is a sentence, this the *best* sentence"`, and then send `"Cake is the best"`, then `"This"` will be considered different from `"this"`, and `"*best*"` will be considered different from `"best"`

  

Modify your routes so that they ignore casing, special characters, and any numbers.

  

## Extension 2
Create one more `get` route that responds with an object with the most popular word and its count.

  

The response from the server should be `{text: {word}, count: {count} }`

## Extension 3
Create a final `get` route that responds with an array of the top 5 most popular words, sorted by count.

  

The response from the server should be `{ranking: [ {word1: count1}, {word2: count2}, ... {word5: count5} ]`



## Extension 4
Add another `get` route that responds with the current total count of words (i.e. sum all the values inside of `wordCounter`, or a more creative solution.)

The response from the server should be an object that looks like this `{text: "Total count", count: {sum} }`  

----------

  

#### **ROUTER.DONE( )**





