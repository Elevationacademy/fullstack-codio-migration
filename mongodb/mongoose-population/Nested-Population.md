
In the previous example we only received the `reviews` - because that's all populated. If we want to also get information about the _critic_ of each review, we have to do some **nested population**.

  

We have to nest because a `Book` only has a `title`, `author`, and `reviews` - the data about the `critic` is per _review_, hence we're populating the `critic` of the _reviews_ that get extracted:

```js
Book.findOne({})
    .populate({
        path: 'reviews',
        populate: {
            path: 'critic'
        }
    })
    .exec(function (err, book) {
        console.log(book.reviews)
    })
```
  

Our `populate` method has changed a bit. Now it takes an object with two keys: `path` and `populate`

  

The path tells it what to populate (in this case, `reviews`), and the `populate` key tells it _what else_ to populate.

  

The second `populate` _also_ receives an object, with one key: `path` - this does the same as the previous path.

  

After all that, here is the result:


```js
[
    {
        "_id": "5c17bacf4d28a75dd44fb30c", "book": "5c17bacf4d28a75dd44fb30a",
        "critic": {
            "reviews": ["5c17bacf4d28a75dd44fb30c"],
            "_id": "5c17bacf4d28a75dd44fb30b",
            "name": "William Jeffery",
            "__v": 0
        },
        "reviewText": "Excellent Book",
        "__v": 0
    }
]
```
  

Notice that we only printed `book.reviews` - so this is our `reviews` array. Right now it only has one object, a review document with the `critic` and `reviewText` keys - both of which are now populated!

  

In theory, **we could keep nesting populations forever**, but eventually it becomes impractical.
