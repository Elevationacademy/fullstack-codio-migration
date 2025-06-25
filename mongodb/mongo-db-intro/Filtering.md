
We've already seen how to do some basic filters, but we have some other built-in commands as well.

  

If we want to have multiple conditions, we can use the `$and` operator. This key needs an _array_ where each value is another filter:

  


```js
db.firstCollection.find({
    $and:[
        {salary: {$gt: 1000}},
        {salary: {$lt: 1500}}
    ]
})
```
  

The above query will find anyone with a salary that is greater than 1,000 but less than 1,500 - it may seem like a lot of syntax but it makes sense if you think of it as a **list of conditions**, where each condition needs to know what _field_ the condition is on, and _what the actual condition_ is.

  

In this case, both _fields_ are `salary`, and the conditions are `$gt` and `$lt`

There is also an `$or` command, but you can figure that out ;)

  

----------

  

We can also filter based on array values quite simply. For this example, run these commands first:

  

```js
db.firstCollection.insert({name: "Spore", hobbies: ["Running", "Hip Hop", "Basketball", "Soccer"]})
db.firstCollection.insert({name: "Daniel", hobbies: ["Hip Hop", "Ballet", "Salsa", "Running"]})
db.firstCollection.insert({name: "Beckie", hobbies: ["Reading", "Running", "Hip Hop", "Writing", "Debate", "Philosophy"]})
db.firstCollection.insert({name: "Dugg", hobbies: ["Philosophy", "Psychology"]})
```
  

In order to find all the people that like Philosophy, we could do this:

  

```js
db.firstCollection.find({
    hobbies: "Philosophy"
})
```
  

That command would return the `Beckie` and `Dugg` documents.

  

Unfortunately, there is a slight limitation to raw mongo that makes it quite tricky to filter off of _multiple_ array values that are strings. But no worries, we'll get to that in another lesson.
