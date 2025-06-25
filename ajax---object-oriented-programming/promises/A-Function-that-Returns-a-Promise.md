Mostly we will work with functions that return promises, such as making http request.
But in our example we need the example functions to return a promise.

Here is a code that change our functions to return promises:
```js
const getRandomWord = function () {
    let words = ['Bonanza', 'Elusive', 'Hindrance', 'Astute', 'Polaroid', 'Phonic', 'Yonder']
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(words[Math.floor(Math.random() * words.length)])
        }, 1000);
    })
}

const getSynonyms = function (word) {
    let thesauraus = {
        'Absolute': ['Definitive', 'Certain', 'Sure', 'Unequivocal'],
        'Astute': ['Sharp', 'Poignant', 'Clever'],
        'Azure': ['Blue', 'Cyan', 'Sky-blue'],
        'Bright': ['Luminous', 'Brilliant'],
        'Bonanza': ['Plethora', 'Smorgasboard', 'Copious', 'Plenty'],
        'Elusive': ['Slick', 'Slippery', 'Ethereal', 'Loose'],
        'Erode': ['Destroy', 'Wear out', 'Tarnish'],
        'Hindrance': ['Bother', 'Disturbance', 'Problematic'],
        'Phonic': ['Soundful'],
        'Ploy': ['Plan', 'Ruse'],
        'Polaroid': ['Photograph'],
        'Yap': ['Bark', 'Blab', 'Chatter'],
        'Yonder': ['There', 'Away', 'Far', 'Afar']
    }
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(thesauraus[word])
        }, 1000);
    })
}

const getSentiment = function (word) {
    let wordSentiment = {
        'Definitive': 1,
        'Sharp': 1,
        'Blue': 0,
        'Luminous': 1,
        'Plethora': 1,
        'Slick': -1,
        'Destroy': -1,
        'Bother': -1,
        'Soundful': 0,
        'Plan': 0,
        'Photograph': 0,
        'Bark': -1,
        'There': -1
    }
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(wordSentiment[word])
        }, 1000);
    })
}

// No need for promises here
const getSentimentDescription = function (sentiment) {
    return sentiment === 1 ? "Positive" : sentiment === -1 ? "Negative" : "Neutral"
}
```

Use it so that you can run the code and add a `then`.

This is out side of the lesson scope.
If you are short in time move on to the next page.

# Extension 
If you have extra time, here is a basic explanation.
To write a function that returns a promise, you can do the following:

* Create a new promise using the Promise constructor, passing in a function with two arguments: resolve and reject.
* Inside the function, perform the asynchronous operation.

* If the operation succeeds, call the resolve function with the result of the operation as an argument.

* If the operation fails, call the reject function with an error as an argument.

Here is an example of a function that returns a promise that resolves with the result of an asynchronous HTTP request:

```js
function getData() {
  return new Promise((resolve, reject) => {
    fetch('https://example.com/data')
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw new Error('Request failed');
      })
      .then(data => {
        resolve(data);
      })
      .catch(error => {
        reject(error);
      });
  });
}
```

If you want to read more about it you can do it [here](https://www.freecodecamp.org/news/how-to-write-a-javascript-promise-4ed8d44292b8/), or search online.