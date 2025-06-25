
We can get a quick count of a certain query by using the `.count` command:

  

```js
db.firstCollection.count({
    salary:{
        $gt: 1200
    }
})
```
  

Filter still works the same, but instead of `find`ing we're `count`ing, with the result being a plain number.

  

----------

  

We can `limit` the results that return to us - this is the first time we're seeing a **pipe** operation; i.e. a command that comes _after_ the query:

  

```js
db.firstCollection.find({
    salary:{
        $gt: 200
    }
}).limit(2)
```
  

This command takes a number and reduces the number of results that gets sent back - also great for reducing bandwith (amount of data that goes back-forth between server-DB).

  

----------

  

The `sort` command, you guessed it, sorts your results based on one of the keys:

  


```js
db.firstCollection.find({}).sort({salary: -1}).limit(3)
```
  

This command first sorts, then limits - so this will return the top-three earning people (we use `-1` in the sort to go from high-to-low, use `1` to go from low-to-high).
