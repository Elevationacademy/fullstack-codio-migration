For this lesson we will work with the following async scenario:

1. Get a random word
1. Get the synonyms of this word
1. Get a sentiment (positive/neutral/negative) for the first synonyms
1. Print the information

Each action in this flow will be async and use setTimeout to make it async.

The code will look like this:

```js
const getRandomWord = function (callback) {
    let words = ['Bonanza', 'Elusive', 'Hindrance', 'Astute', 'Polaroid', 'Phonic', 'Yonder']
    setTimeout(() => {
        callback(words[Math.floor(Math.random() * words.length)])
    }, 1000);
}

const getSynonyms = function(word, callback) {
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

    setTimeout(()=>{
        callback(thesauraus[word])
    }, 1000)
}

const getSentiment = function(word, callback) {
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
    setTimeout(()=>{
        callback(JSON.stringify(wordSentiment[word]))
    }, 1000) 
}

const getSentimentDescription = function(sentiment){
    return sentiment == "1" ? "Positive" : sentiment == "-1" ? "Negative" : "Neutral"
}
```

For example we can:
1. ask for a random word and get "cat"
1. then ask for cat synonyms and get `["kitty", "kitten", "pusycat"]`
1. then ask for the sentiment of the first synonym "kitty" and get 1, which means positive
1. lastly we can print: 
```txt
The word cat has a synonym kitty which has a positive sentiment
```

|||Guidance
## Spot Check
After figuring out the code, try to write the code that executes this flow, and calls the functions in the right order.
|||
