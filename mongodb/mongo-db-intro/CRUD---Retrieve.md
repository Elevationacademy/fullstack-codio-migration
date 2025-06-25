
Of course, we don't always want to receive all our data. Sometimes we'd like to **filter** it based on some parameters. Before we try some filtering, go ahead and run these commands:

  


```js
db.firstCollection.insert({ name: "Louise", salary: 1200 })
db.firstCollection.insert({ name: "Rayna", salary: 2300 })
db.firstCollection.insert({ name: "Soren", salary: 1500 })
db.firstCollection.insert({ name: "Loreli", salary: 800 })
db.firstCollection.insert({ name: "Milo", salary: 950 })
db.firstCollection.insert({ name: "Brendon", salary: 1100 })
```
  

Say we have 6,000 documents and not just 6, and we need to find out what Milo's salary is (assume for now everyone has a unique name). We would do that like this:

  


```js
db.firstCollection.find({
    name: "Milo"
})
```
  

Instead of passing an empty object, we pass in an object with the key-value we're looking for - this is our **filter**! In return, we receive the following document from this query:

  


```js
[
  {
    "_id": {
      "$oid": "5c154c8bdfa72e0c84482da2"
    },
    "name": "Milo",
    "salary": 950
  }
]
```
----------

  

Now, say we only wanted to find the people who have a `salary` above 1200. To do that we can still use `.find`, but we can pass in another parameter, like so:

  


```js
db.firstCollection.find({
    salary:{
        $gt: 1200
    }
})
```
  

**Note:** If you're writing in the terminal, you can press enter and keep writing the command - just watch out for all the opening/closing braces.

  

Breaking it down, we're doing two things:

We're **filtering** using the `salary` field, and in that field we only want documents whose value is **g**reater **t**han 1200 - the `$` is also necessary.

  

For this query we would receive the following result, because _both_ of these documents match our query:

  

```js
[
  {
    "_id": {
      "$oid": "5c154c86dfa72e0c84482d9f"
    },
    "name": "Rayna",
    "salary": 2300
  },
  {
    "_id": {
      "$oid": "5c154c88dfa72e0c84482da0"
    },
    "name": "Soren",
    "salary": 1500
  }
]
```
----------

  

Usually our documents are much more complicated than two keys, so often we only want to return certain properties from our query. This has two main benefits:

1.  Simplicity
2.  Once we start working with server-DB communication; the less data we send, the faster the response will be

  

To that end, we can limit the fields we retrieve like so:

  


```js
db.firstCollection.find(    //query starts here
    {                       //filter starts here
        salary: {
            $gt: 1200
        }
    },                      //filter ends here
    {                       //projection starts here
        name: 1,
        _id: 0
    }                       //projection ends here
)                           //query ends here
```
  

Here we're taking advantage of the second (optional) parameter of the `.find` command: the **projection** - this allows us to determine which fields should come back from the query.

  

In the above, we're stating that we only want to receive the `name` field (so we give it a value of `1`) - but, by default **the** **`_id`** **field _always_ returns**, even if we have a projection. If you _really_ want to avoid this field, you can do as we did above, and explicitly give it a value of `0` in the projection.
