
It's great that we are now saving data references, but clearly if we want to know all the information about a book, we don't want to query the `books` collection _and_ the `reviews` collection - **we want to extract all the relevant data in one query**.

  

To do that, we need to introduce the `.populate` and `.exec` methods:

  

```js
Book.findOne({})
    .populate("reviews")
    .exec(function (err, book) {
        console.log(book.reviews)
    })
```
  

Here's what's happening:

-   We're looking for `One` book - this is just for simplicity
-   For the book we find, we want to `populate` the data in this book's `reviews` property
-   This means that we want to _extract_ the reviews data using the reference ID we saw earlier
-   Mongoose knows to do this because when we created the `Book` model, we told it that the `reviews`**reference** is the `Review` collection
-   We have to run `exec` to actually **execute** our query
-   This is new, and only applies to certain helper methods like `populate`
-   You can read more about `exec` over [here](https://stackoverflow.com/questions/31549857/mongoose-what-does-the-exec-function-do)

  

Now, instead of seeing an array of reference IDs in the console, we'll see this:

  

```js
[
  {
    "_id":"5c17bacf4d28a75dd44fb30c",
    "book":"5c17bacf4d28a75dd44fb30a",
    "critic":"5c17bacf4d28a75dd44fb30b",
    "reviewText":"Excellent Book",
    "__v":0
  }
]
```
  

Notice that only the `reviewText` property was populated - because we only told it to populate `reviews`!

  

In population, **mongoose goes to the other collection for us and queries it accordingly** behind the scenes - this is convenient, but can lead to slower queries overall. So watch out when using this.
