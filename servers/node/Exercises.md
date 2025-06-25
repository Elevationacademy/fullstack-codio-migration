## Exercise 1

Use VS Code's debugger to help you correct the following code. Of course, **do not change the data**.

  

Don't forget, when debugging: **test all your assumptions. Validate that all your variables have the values you expect them to have**.

  
```
const countries = [
    {
        name: "Gentina", population: 30000,
        landmarks: [
            { name: "Big bank", tourismCount: 100 },
            { name: "Wild coyotes", tourismCount: 12 },
            { name: "Purple blooming fields", tourismCount: 3 },
            { name: "Turnip Gardens", tourismCount: 1500 }
        ]
    },
    {
        name: "Ance", population: 155000,
        landmarks: [
            { name: "Zumba Plaza", tourismCount: 240 },
            { name: "Woodcutting Workshop", tourismCount: 16 },
            { name: "Lava Pits", tourismCount: 890 }
        ]
    },
    {
        name: "Noxyland", population: 80000,
        landmarks: []
    },
    {
        name: "Bouti", population: 410000,
        landmarks: [
            { name: "Underground Labyrinths", tourismCount: "Unknown" },
            { name: "Dolphinarium", tourismCount: 3400 },
            { name: "Astronomy Bunker", tourismCount: 250 },
            { name: "Zoology Tower", tourismCount: 1200 }
        ]
    },
    {
        name: "Rea", population: 827000
    },
    {
        name: "Golia", population: 54000,
        landmarks: [
            { name: "Horse Heritage Site", tourismCount: 920 }
        ]
    }
]

//Find the country with the highest population
//It should print "Rea" in the end
let biggestCountry = ""
for (let c of countries) {
    let biggestPop = countries[0].population

    if (c.population > biggestPop) {
        biggestCountry = c.name
    }
}
console.log(biggestCountry)

//Console log the name of all the touristic sites that have more than 1000 visitors
//These should be: the Zoology Tower, the Dolphinarium, and the Turnip Gardens
//Hint: the `continue` keyword will allow you to skip over an element in an array
//Alternative hint: remember the || operator
const popularAttractions = []

for (let c of countries) {
    let landmarks = c.landmarks

    for (let l in landmarks) {
        if (l.tourismCount > 1000) {
            popularAttractions.push(l.name)
        }
    }
}
console.log(popularAttractions)
```

## Exercise 2

Create three files: consts.js, complaintsHandler.js, and complaints.js

  

Inside of consts.js, export all three of these variables using a single object:
```
const FINANCE = "finance"
const WEATHER = "weather"
const EMOTIONS = "emotions"
```
  

Inside of complaintsHandler.js, write a single function called handleComplaints

-   This function receives a single paramter called complaint: an object with two keys
    -   text - some string
    -   type - a string with either "finance", "weather", or "emotions" as the value
-   If the complaint type is...
    -   "finance", the function should print "Money doesn't grow on trees, you know."
    -   "weather", the function should print "It is the way of nature. Not much to be done."
    -   "emotions", the function should print "It'll pass, as all things do, with time."
-   This function should use the FINANCE, WEATHER, and EMOTIONS properties from the consts module
    -   In other words, you should **not** hard-code: if(complaint.type === "finance")

  

Of course, this means you will have to require the consts module inside of complaintsHandler

  

Finally, in complaints.js, make the following code work:
```
let complaint1 = {
    text: "I'm not getting enough money",
    type: //use the FINANCE type from the consts module
}

let complaint2 = {
    text: "My salary hasn't come in yet",
    type: //use the FINANCE type from the consts module
}

let complaint3 = {
    text: "I'm always full of energy",
    type: //use the EMOTIONS type from the consts module
}

handleComplaint(complaint1) //should print "Money doesn't grow on trees, you know."
handleComplaint(complaint2) //should print "Money doesn't grow on trees, you know."
handleComplaint(complaint3) //should print "It'll pass, as all things do, with time."
```
  

For this to work you'll need a couple of imports - but remember, **you can only** **require** **a module that's been exported!**





