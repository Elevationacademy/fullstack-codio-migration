
Mongo has several commands - you can google anything that comes to mind, from renaming keys to increasing a value by a certain amount.

  

We're going to introduce a few other useful ones. For instance, **adding to an array**:

  

```js
db.firstCollection.update(  
    {name: "Razu"}, 
    {$push: {
        hobbies: "Razu-Ball"
    }}
)
```
  

Notice that this is just a different type of `update` command - here we're using the `$push` operator. We also **have to tell Mongo which array to update**, of course (the `hobbies` array).
