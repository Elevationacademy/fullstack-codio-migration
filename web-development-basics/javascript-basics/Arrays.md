# Arrays
We will now cover **Arrays**, which are effectively just lists

The syntax looks like this:  

```js
let companies = ["Tesla", "Amazon", "Google", "Microsoft"]
```


We can determine the number of elements in the array using `.length`.

Note that **we can access elements from an array through indexes**. For instance:


```js
const firstCompany = companies[0]
console.log(firstCompany) // prints "Tesla"
``` 

in the same way thats how we update and add to our array at a specific  index.

---

## PUSH 
What about adding new items to an array? That's where the `push` method comes in. Like this:
```js
companies.push("Blizzard Entertainment");
``` 
Remember that **`push`** **always adds the element to the end of the array**.

---

Another operator that is usefull in Arrays is called **spread syntax**, or the spread operator `...`, and what it does is expand arrays in-place, so that the following two are virtually the same:


```js
employees.push(...candidates)
employees.push(candidates[0], candidates[1], candidates[2])
```

This _is_ useful because we often deal with arrays, and combining arrays, or duplicating them is a common task.

---

## Splice

As for removing items from arrays, it's a little more involved but still straightforward.

There is a method called `splice`, and it needs two things:

1.  Where to start removing
2.  How many to remove from that point
```js
companies.splice(1, 1)
```
That's saying "go to the 1st index, and remove 1 item from there". 
When you use `splice`, the method will **return*** the item(s) that you removed from the array. 

The `splice` can also be used to add new elements in the array at a specific index, but you can figure that out by yourself using [this documentation](https://www.w3schools.com/jsref/jsref_splice.asp) 

to learn more about Splice you can check out :
[JavaScript Splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)




