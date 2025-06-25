Comprehension Exercises
--

## Exercise 1
What does the following code return/print?

```js
let facts = {numPlanets: 8, yearNeptuneDiscovered: 1846};
let {numPlanets, yearNeptuneDiscovered} = facts;

console.log(numPlanets); // ?
console.log(yearNeptuneDiscovered); // ?
```

<details>
<summary>Solution</summary>
<div> 

```js
let facts = {numPlanets: 8, yearNeptuneDiscovered: 1846};
let {numPlanets, yearNeptuneDiscovered} = facts;

console.log(numPlanets); // 8
console.log(yearNeptuneDiscovered); // 1846
```
</div>
</details>



## Exercise 2
What does the following code return/print?


```js
let planetFacts = {
  numPlanets: 8,
  yearNeptuneDiscovered: 1846,
  yearMarsDiscovered: 1659
};

let {numPlanets, ...discoveryYears} = planetFacts;

console.log(discoveryYears); // ?
```

<details>
<summary>Solution</summary>
<div> 

```js
let planetFacts = {
  numPlanets: 8,
  yearNeptuneDiscovered: 1846,
  yearMarsDiscovered: 1659
};

let {numPlanets, ...discoveryYears} = planetFacts;

console.log(discoveryYears);
// {yearNeptuneDiscovered: 1846, yearMarsDiscovered: 1659}
```
</div>
</details>

## Exercise 3
What does the following code return/print?

```js
function getUserData({firstName, favoriteColor="green"}){
  return `Your name is ${firstName} and you like ${favoriteColor}`;
}

getUserData({firstName: "Alejandro", favoriteColor: "purple"}) // ?
getUserData({firstName: "Melissa"}) // ?
getUserData({}) // ?
```

<details>
<summary>Solution</summary>
<div> 

```js
function getUserData({firstName, favoriteColor="green"}){
  return `Your name is ${firstName} and you like ${favoriteColor}`;
}

getUserData({firstName: "Alejandro", favoriteColor: "purple"})
// Your name is Alejandro and you like purple

getUserData({firstName: "Melissa"})
// Your name is Melissa and you like green

getUserData({})
// Your name is undefined and you like green
```
</div>
</details>

## Exercise 4
What does the following code return/print?

```js
let [first, second, third] = ["Maya", "Marisa", "Chi"];

console.log(first); // ?
console.log(second); // ?
console.log(third); // ?
```

<details>
<summary>Solution</summary>
<div> 

```js
let [first, second, third] = ["Maya", "Marisa", "Chi"];

console.log(first); // Maya
console.log(second); // Marisa
console.log(third); // Chi
```
</div>
</details>


## Exercise 5

What does the following code return/print?

```js
let [raindrops, whiskers, ...aFewOfMyFavoriteThings] = [
  "Raindrops on roses",
  "whiskers on kittens",
  "Bright copper kettles",
  "warm woolen mittens",
  "Brown paper packages tied up with strings"
]

console.log(raindrops); // ?
console.log(whiskers); // ?
console.log(aFewOfMyFavoriteThings); // ?
```

<details>
<summary>Solution</summary>
<div> 

```js
let [raindrops, whiskers, ...aFewOfMyFavoriteThings] = [
  "Raindrops on roses",
  "whiskers on kittens",
  "Bright copper kettles",
  "warm woolen mittens",
  "Brown paper packages tied up with strings"
]

console.log(raindrops); // "Raindrops on roses"
console.log(whiskers); // "whiskers on kittens"
console.log(aFewOfMyFavoriteThings);
// ["Bright copper kettles", "warm woolen mittens", "Brown paper packages tied up with strings"]
```
</div>
</details>
