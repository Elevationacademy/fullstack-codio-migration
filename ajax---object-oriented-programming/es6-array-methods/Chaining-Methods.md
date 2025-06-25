
Another nice thing about (some) array methods is that, because of their nature (methods that work on arrays that return arrays), we can **chain** methods. That is, we can first filter, then map in one go. Check this out:

```js
let countries = [
    { name: "Greece", population: 500 },
    { name: "Namibia", population: 1200 },
    { name: "Finland", population: 100 },
    { name: "Switzerland", population: 300 },
    { name: "Peru", population: 200 }
]

let smallCountries = countries.filter(c => c.population < 500).map(c => c.name)
```
  

Now `smallCountries` we will be `["Finland", "Switzerland", "Peru"]` because we first filtered out only the countries with a population of less than 500, and then mapped _those that match the filter_ to only have the country's names.

  

Chaining methods tends to become hard to read, so we generally like to write the chains like this:


```js
let smallCountries =
    countries
        .filter(c => c.population < 500)
        .map(c => c.name)
```
  

This is much more readable, and shows a clear logical flow of what we're doing.
