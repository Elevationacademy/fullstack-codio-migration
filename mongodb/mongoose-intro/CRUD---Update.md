
There are two ways we can update documents in mongoose. We can either `find`, update in the callbackin the `.then` method, then `save` again, like this:


```js
Person.findById("5c16c63bc5ad73471c3ca323").then( function (person) {
    person.age += 10 //how time flies
    person.save()
})
```
  

Here we're finding the person by its ID, then - in the callback, where we have access to the person - we modify its `age` **like the regular JS object** that it is, and then we call `.save` again.

  

This is perfectly fine, but we can also use the `findByIdAndUpdate` shortcut:


```js
Person.findByIdAndUpdate("5c16c63bc5ad73471c3ca323", { age: 70 }).then( function (person) {
    console.log(person)
})
```
  

This looks more like what we had in Mongo.

  

**However**, you'll notice that the `person` that's printed out has the old `age`, even though we've updated it!
That is just the default behavior of mongoose: to show you the old object.

  

**To see the value of the update object in the callback**, you must add the `{new: true}` parameter:


```js
Person.findByIdAndUpdate("5c16c63bc5ad73471c3ca323", { age: 70 }, { new: true }).then( function (person) {
    console.log(person)
})
```
