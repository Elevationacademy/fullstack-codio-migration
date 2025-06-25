
When we talk about objects, it's different. Objects are a different **data structure**, they store data differently from an array.

```
let people = {}
```
  
## Spot check
What are the complexities for **insert**, **find**, **update**, and **remove** for an object?
```
const doSomething = function(arr){
  console.log(arr[0] + arr[37])
}
```
<details><summary>
  Click here to reveal the answer.
</summary>
  
They're all **O( 1 )**!

See [solution](https://codepen.io/ElevationPen/pen/mZrYKr?editors=0010).
</details>


----------

Given the above, it may seem like we would always prefer to use an object rather than an array.

  

However, some operations are simpler to execute with an array. For instance, **using the people <ins>object</ins>** - how would you find all the people who are over 18 years old?

  

You'd have to use something like `Object.keys(people)` in order to iterate over them - and that's **O( n )** anyway. In that case, it is simpler to use the **people array**:

```  
const findOver18 = function () {
    return people.filter(p => p.age > 18)
}
```

----------

As such, **when considering which data structure to use, you should ask yourself what your main usecase will be** - what will we be doing with the data?

  

Are we mainly filtering, extracting quickly, removing tasks? In short, **there is never a "best" data structure** to use - only one that fits the use case.