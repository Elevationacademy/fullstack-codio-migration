
Sometimes, we want to _transform_ data we're working with into something more convenient.

  

For instance, we might receive an array of weights in pounds, but we're civilized and want to work in kilograms. Instead of writing a whole for loop to convert an array, we can use `.map`:

  
```js
let poundWeights = [142, 180, 178, 121, 132]

let kiloWeights = poundWeights.map(pw => Math.round(pw / 2.2))
console.log(kiloWeights) //prints [65, 82, 81, 55, 60]
```
  

The map method works similar to the filter method, but instead of returning a boolean in the callback, you return any new "transformed" value. It's called "map" because we're "mapping" one form of data into another.

  

**Spot check:** given the following list of strings, use map to turn everything to lowercase.

```js
let messagesFromDad = ["HI HONEY", "HOW WAS SCHOOL??", "DID YOU EAT TODAY?", "I CAN'T FIND THE REMOTE CONTROL"]
```
  

You can do this with either a named or anonymous function. But remember, one of the advantages of these methods is _brevity_.

  
```js
let calmMessages = messagesFromDad.map(m => m.toLowerCase())
```
  

----------

  

Note that you can also use `map` to extract things from a complicated array of objects, into something slimmed down, like in this case:

```js
let users = [
    {
    "name": "Leanne Graham",
    "address": {
        "street": "Kulas Light", "suite": "Apt. 556", "city": "Gwenborough", "zipcode": "92998-3874",
        "geo": { "lat": "-37.3159", "lng": "81.1496" }
    }
}, {
    "name": "Ervin Howell",
    "address": {
        "street": "Victor Plains", "suite": "Suite 879", "city": "Wisokyburgh", "zipcode": "90566-7771",
        "geo": { "lat": "-43.9509", "lng": "-34.4618" }
    }
}
]
```
  

Say that instead of all that data there, we only want the name and city. We could **map** the data differently, like so:

```js
users.map(u => { return { name: u.name, city: u.address.city } })
```
  

Notice that in this case we have a `return` inside the callback function! That is because we're creating a new object, which uses `{ }`, so we need to clearly define what the callback function is, and what the object we're creating is.
