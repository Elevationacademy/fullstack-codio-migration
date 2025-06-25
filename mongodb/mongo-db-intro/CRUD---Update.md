
Alright, now that we have our basic Creation and Retrieval, let's talk about Updating.

  

To update an existing document, we can use the `.update` command - **however**, if we run it simply this will overwrite the _entire_ document:

  

```js
db.firstCollection.update(
    {
        name: "Milo"        //filter
    },
    {
        lastName: "Shakers" //update
    }
)
```
  

Sometimes we do want to overwrite the entire doc, but in the above case this would be a mistake. We want to _add_ the last name, not erase the whole document.

  

To make sure we're adding (or updating an existing field) _without_ deleting everything else, we must also use `$set`, like so:

  


```js
db.firstCollection.update(
    {
        name: "Milo"
    },
    {
        $set:
            {
                lastName: "Shakers"
            }
    }
)
```
  

Now when we query for "Milo" we'll see that he also has a last name of "Shakers".

  

  

**Spot check:** give Loreli a promotion. Make her salary 1050.

  

You can find the solution [here](https://codepen.io/ElevationPen/pen/mZPdXo?editors=0010).
