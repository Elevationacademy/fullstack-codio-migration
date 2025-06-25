
Add a `children` property to `Animal`.

However, instead of initializing the value of `children` from the constructor parameters, simply set its value to an empty array.

Then, change the `giveBirth` method to add the `name` to the `children` array.

Remember how you access an object's own properties?

  

To see if you did it right (before looking at the solution), you can check with this code:


```js
cat.giveBirth("Dolly")
console.log(cat.children) // should print an array with 1 item: ["Dolly"]﻿
```
  

See the solution [here](https://codepen.io/ElevationPen/pen/QXLmyx?editors=0010).
