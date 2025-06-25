
With any database, the most important thing is being able to complete the four basic CRUD operations: Create, Retrieve, Update, Delete.

  

The nice thing about working with Mongo is that its syntax is quite similar to how we work with regular JS objects, so it should be familiar for you.

  

You should already have a `firstCollection` collection setup inside of a `test-db` database, so now let's see what **document creation** looks like:

  


```json
db.firstCollection.insert({name: "You"})
```
  

We use the keyword `db` (it's already defined for us once we run the `use` command) to access our `firstCollection` collection, and then we use the `insert` command* to pass in our document: a simple key-value pair.

  

**Virtually all Mongo commands follow this formula:** `db.collectionName.operation(parameters)`

*Notice we said _command_ and **not** "function" or "method" - though it may look like it, **this is not JavaScript** - we are writing **Mongo commands** - you cannot define variables/arrays/functions here. We can only use the commands given to us.

  

Another note, **our Mongo commands do not have to be JSON-compliant** - but we'll see in a moment that our documents are stored as JSON.

  

Of course, since we're `insert`ing plain objects, we can insert any arbitrarily complex object we would like:

  


```json
db.firstCollection.insert({
    name: "Razu",
    hometown: {
        city: "Razuville",
        country: "Razuland"
    },
    hobbies: ["Razu-ing", "Razu Surfing", "Razu Cooking"]
})
```
  

Please insert this doc into your collection, as Razu will show up later on in the lesson.

  

Obviously, this is tricky to write out if you're using the terminal - so feel free to copy-paste this time.

  

----------

  

In order to **retrieve documents**, we can use the `find` command, like so:

  


```json
db.firstCollection.find({})
```
  

The `find` commands accepts one required parameter, and one optional parameter (we'll talk about that later). The required parameter above is an **empty object, signifying that we want to retrieve all our data**. In return, we should see something like this:

  

```json
[
  {
    "_id": {
      "$oid": "5c153ca0dfa72e0c84482d9c"
    },
    "name": "Razu",
    "hometown": {
      "city": "Razuville",
      "country": "Razuland"
    },
    "hobbies": [
      "Razu-ing",
      "Razu Surfing",
      "Razu Cooking"
    ]
  },
  {
    "_id": {
      "$oid": "5c1531d1dfa72e0c84482d99"
    },
    "name": "You"
  }
]
```
  

You'll notice that even though we never defined it, **Mongo creates an** **`_id`** **field for us, and assigns a unique ID to each document** - this is excellent since ID-management can be a pain.

We could, of course, store data with our own ID, like so:

  

```json
db.firstCollection.insert({
    _id: 99143,
    name: "Shoobert"
})
```
  

And sometimes we might want to do that. When you retrieve the above you should see your own ID, like this:

  


```js
  {
    "_id": 99143,
    "name": "Shoobert"
  }
  ```
