# Crud   Create

Now that we have a `p1` that represents a document based off our schema, we can run this command:

```js
p1.save()
```
  

And that, finally, saves data to our Mongo DB - the **C** in **C**RUD: Create.

  

To check that this actually exists in the DB, go ahead and run the **Mongo command** (remember to use the correct collection!):

  

```js
db.people.find({})
```
  

Of course, **run that in the mongo shell** - do **not** try that in your `.js` file as you will get an error.

  

You should see something similar to this output:

  

```js
[
  {
    "_id": {
      "$oid": "5c16bbe03f02d41e78416a4d"
    },
    "firstName": "Shoobert",
    "lastName": "Dillard",
    "age": 25,
    "__v": 0
  }
]
```
  

At this point you should be wondering, _where the heck did the_ `_people_` _collection come from?_

  

The answer is that **mongoose will create a collection for us, and name it based off our Model Name** - since we called our model `Person`, mongoose was clever enough to create a `people` collection for us, and store our document there.

  

If, instead, you want to name your collection on your own, you can create a model like this instead:

  
```js
const Person = mongoose.model('person', personSchema, 'persons'); //<== persons will be the name of the collection
```