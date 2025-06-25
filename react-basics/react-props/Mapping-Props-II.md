
Ok so that was nice, but we can make it nicer. A whole separate method just to generate a simple list is excessive, and really all we're doing is **mapping** each letter to a different format.

In other words, we are changing `{name: "Tesla", revenue:140}` to `<Company name="Tesla" revenue=140/>`

  

To that end, let's use our old `map` friend provided by our friendly neighborhood ES6. Let's get rid of `generateCompanyTags`, and re-write our `App`'s `return` like this:

  
```
return (
  //...other code
  <div>
    {companies.map(c => <Company name={c.name} revenue={c.revenue} />)}
  </div>
)
```
  

First, that looks much nicer. Let's break it down real quick:

  

-   `map` will iterate over something (in this case our `companies` array)
-   Do something with each item (the `c =>` above indicates that) - in this case, create a `<Company...` tag _for each_ `c` (company)
-   Finally, return a new _array_ with all our tags - `map` always returns an array

  

We'll be using `map`s henceforth with React, so make sure you're comfortable with them.