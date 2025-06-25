
One of the best things about databases is that it can do complex computation for us.

  

As a simple example, say we were interested in the `sum` of all the salaries we're paying. We can use `aggregate` to figure that out easily:

  


```js
db.firstCollection.aggregate([
                     { $group: 
                        { _id: null, 
                        totalSalaries: { $sum: "$salary" } } }
                   ])
```
  

In order to use these **aggregator operators**, we must use the `$group` command.

  

In this case, we don't want to group by any field - i.e, we just want to get the total salaries of everyone, so we use an identifier (the `_id`) of `null`

  

Note as well that `totalSalaries` is a key we've created, and that we've added a `$` before the `salary` field - these are the rules of `aggregate`

  

----------

  

To make the `aggregator` clearer, go ahead and run this command first - it will **get rid of all your documents** so we can start fresh:

  


```js
db.firstCollection.remove({})
```
  

Now run this command to get some more interesting data in your collection:

  


```js
db.firstCollection.insert({ name: "Louise", dept: "Finance", salary: 1200 })
db.firstCollection.insert({ name: "Rayna", dept: "R&D", salary: 2300 })
db.firstCollection.insert({ name: "Soren", dept: "Finance", salary: 1500 })
db.firstCollection.insert({ name: "Loreli", dept: "Sales", salary: 800 })
db.firstCollection.insert({ name: "Milo", dept: "Sales", salary: 950 })
db.firstCollection.insert({ name: "Brendon", dept: "Finance", salary: 1100 })
```
  

Here's where DBs come in very handy. To find the total salaries for each department, all we have to do is the following:

  


```js
db.firstCollection.aggregate([
                     { $group: 
                        { _id: "$dept", 
                        totalSalaries: { $sum: "$salary" } } }
                   ])
```
  

All we've changed is the `_id` field - this is what tells the aggregator what to **group by** - i.e., on which fields should it execute the `$sum` command.

  

The result for the above query is the following JSON:

  

```js
{ "_id" : "R&D", "totalSalaries" : 2300 }
{ "_id" : "Sales", "totalSalaries" : 1750 }
{ "_id" : "Finance", "totalSalaries" : 3800 }
```
  

**Important note:** because we want the _sum_ of the `salary` fields, then we're using `$salary` - this will add each salary to one another.

  

If instead we just wanted the total _count_ of people getting a salary per department, we would use `1` instead of `$salary`, and that would add 1 for each department. **Try this out and see the result**.

  

There are other aggregator operators such as `$max`, `$min`, and `$avg` - but they work the same as `$sum`
