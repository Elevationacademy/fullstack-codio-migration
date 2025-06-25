
To check your work from the previous spot check, you might have done something like this:

  

```js
for (let vegetable of orangeVegetables) {
    console.log(vegetable.name) //expect to see Carrot, Squash, and Sweet Potato
}
```
  

And that's fine, if you're working in **_ES5_**.

  

But we're more advanced now, so we're going to use the `forEach` method, like so:

```js
orangeVegetables.forEach(ov => console.log(ov.name))
```
  

One lovely line that does exactly what it says.

  

Again, **the** **`forEach`** **method takes a function, and invokes the function on each item it iterates over** - unlike `filter`, this function doesn't have to return anything.

  

**Spot check:** given the following array, write a _named function_ outside of a `forEach` method. The function should receive one parameter, `person`, and should increase the person's `salary` by 300 if their performance was good.

  
```js
let people = [
    { salary: 1300, goodPerformance: false },
    { salary: 1500, goodPerformance: true },
    { salary: 1200, goodPerformance: true },
    { salary: 1700, goodPerformance: false },
    { salary: 1600, goodPerformance: true },
]
```
  

Test your code using the following:

  
```js
people.forEach(p => console.log(p.salary)) //should print 1300, 1800, 1500, 1700, 1900 (on separate lines)
```
  

Give this a good ten minutes before peeking at [the solution](https://codepen.io/ElevationPen/pen/xoKpKg?editors=0010).
