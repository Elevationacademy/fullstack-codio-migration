# Loops

Loops are a fundamental concept in programming.
in JavaScript we have a couple of ways to create a loop

for the sake of explaining , lets look at this array:
`companies` array again:
```js
let companies = ["Tesla", "Amazon", "Google", "Microsoft"]
```
  

---
## For... In

`for...in` iterates over all enumerable property keys of an object ,we can use `for...in`  like this:

```js
for(let companyIndex in companies){
  console.log(companies[companyIndex])
}
```

What `for...in` does for us is it **gives us each index, in order, of the array we're looping**, In other words, we can say that **the loop generates an** **`index`** **for each item** **`in`** **our** **`companies`** **array.**

  
---

## For... of
`for...of` iterates over the values of an iterable object. Examples of iterable objects are arrays, strings, we can use `for...of`  like this:
 

```js
for(let company of companies){
  console.log(company)
}
```
  
Again, you should see all your companies printed out, one line after the other.
**What's the difference?** Here we don't get an index on each iteration - instead, **for...of gives us the element itself**! - Notice that we're not doing `companies[..]` anymore.

---

## While

As for `while` loops, the syntax is even simpler:
```js
while(someCondition){
  //do something
}
``` 

In this case we're not telling the loop to run over a certain array, but rather **run until a certain condition is met**.

---

## For let i = 0;...

This last way of doing for loops is similar to `for... in` - that is, it works with indexes; but we get more granular control of the loop. Check out this loop, which just prints the numbers 0, 1, 2...9:

  
```js
for(let i = 0; i < 10; i++){
  console.log(i)
}
```
  
















