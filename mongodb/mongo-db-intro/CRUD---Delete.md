
Finally, to round up our CRUD: Delete. Always a dangerous operation, but somtimes necessary.

  

For this, we have the `.remove` command. Note that as-is, **remove will delete any document that matches the query**:

  


```js
db.firstCollection.remove({
    name: "Rayna"
})
```
  

This is fine sometimes, but if for whatever reason you only want **to delete the first occurence, use the second (optional) parameter**: a `true` that indicates Mongo should only delete one doc, not all matching docs:

  

```js
db.firstCollection.remove(  
    {
        name: "Rayna"
    }, 
    true
)
```
