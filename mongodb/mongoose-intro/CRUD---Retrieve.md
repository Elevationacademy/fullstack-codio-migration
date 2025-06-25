
In order to query our DB, we will use **the model itself, not the instance**.

  

For the example below, make sure you're `connected` to the `peopleDB` again, and **comment out** any `save` operations you have. Now run this code:

  

```js
Person.find({}).then(function (people) {
    console.log(people)
})
```
  

`Person.find` is exactly what we meant when we said that we use the Model for querying operations. This should make sense, as it would be silly to do `p1.find(...` - since we would be _looking_ for `p1`!

  

At this point, the above syntax should be quite familiar. This might help: **all mongoose operations are asynchronous - as such, we must use `.then`**.

  

We use the `find` method which takes two parameters: a filter (similar to Mongo).

```js
let peoplePromise = Person.find({})

peoplePromise.then(function (people) {
    console.log(people)
})
```
  

Oddly, you'll note that when we use promises, we don't have to have the `err` parameter in our callback in `.then`, we need to use `.catch` in order to catch it.

Like this:

```js
let peoplePromise = Person.find({})

peoplePromise.then(function (people) {
    console.log(people)
})
.catch((err)=>console.log(err))
```
  
Our result will be:

  

```js
[ { _id: 5c16bbe03f02d41e78416a4d,
    firstName: 'Shoobert',
    lastName: 'Dillard',
    age: 25,
    __v: 0 } ]
```
----------

  

Go ahead and run the following code:

```js
let p2 = new Person({ firstName: "Shoo", lastName: "Bert", age: 50 })
let p3 = new Person({ firstName: "Shoob", lastName: "Ert", age: 34 })
let p4 = new Person({ firstName: "Sh", lastName: "Oobert", age: 10 })
let p5 = new Person({ firstName: "Shoober", lastName: "T", age: 44 })

let allTheShooberts = [p2, p3, p4, p5]
allTheShooberts.forEach(s => s.save())
```
  

Notice that each instance is just a plain JS object! That means there's no problem storing it an array, iterating over the array, and `save`ing each as we do above.
