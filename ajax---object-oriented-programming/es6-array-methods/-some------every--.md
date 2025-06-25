
Sometimes, instead of just finding and extracting elements from an array, we just want to know whether certain things _exist_ in an array.

  

Say, for instance, you're a manager at a digital bar, and a group of people comes in. You need to make sure that **every** person is above the age of 18. With the `every` method, this is trivial:

  
```js
let ages = [31, 28, 23, 27, 25, 16, 24]
ages.every(a => a > 18) //returns false
```
  

Other times, it's enough to know that **some** of the items in an array match a certain criteria. For instance, you might want to validate that at least some of the food at a restaurant is vegetarian before going there:


```js
let menu = [
    { name: "Beef stew", vegetarian: false },
    { name: "Beef sandwhich", vegetarian: false },
    { name: "Carrot on a stick", vegetarian: true },
    { name: "Beef eggroll", vegetarian: false },
]

menu.some(m => m.vegetarian) //returns true
```
  

These two methods, unlike the other array methods, **always return a boolean** after checking all the items in the array.

  

**Spot check:** given the following movies:


```js
let movies = [
    { title: "Dareangel", studio: "Marvel", year: 2023 },
    { title: "Batterfly", studio: "Fox", year: 2021 },
    { title: "League of Ordinary People", studio: "Blizzard", year: 2025 },
    { title: "Thor: Ragnarok", studio: "Marvel", year: 2017 },
]
```
  

Write some code that prints out:

  

-   "Let's go watch some movies" if at least one of the movies is by "Marvel"
-   "Let's stay home" otherwise
-   "Futuristic stuff" if all the movies are from after the year 2020
-   "Yawn" otherwise

  

Check out the solution [here](https://codepen.io/ElevationPen/pen/ewOyBz?editors=0010)
