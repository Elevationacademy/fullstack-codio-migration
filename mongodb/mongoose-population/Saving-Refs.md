
Ok, now that we have our schemas set up properly, we need to **save documents**. That would look like this:


```js
let b1 = new Book({
    title: "Name of the Wind",
    author: "Patrick Rothfuss",
    reviews: []
})

let c1 = new Critic({
    name: "William Jeffery",
    reviews: []
})

let r1 = new Review({
    book: b1,
    critic: c1,
    reviewText: "Excellent Book"
})
```
  

We start by creating the document objects. Notice two things:
1.  We initially set the `reviews` in `b1` and `c1` to be _empty arrays_
2.  Since a review _must have_ a book and a critic, we give it the `b1` and `c1` objects right away

  

And now for the actual saving:

  

```js
b1.reviews.push(r1)
c1.reviews.push(r1)

b1.save()
c1.save()
r1.save()
```
  

See how convenient mongoose is? We're just working with objects! As such:

-   Before we save the book and critic documents (`c1` and `b1`), we add the review to their `reviews` array
-   The order of the saves **does not** really matter since the objects mongoose creates for us hold the same ID as they will have in the DB

  

Now let's look at our DB. Run this command:

  

```js
Book.find({}, function(err, books){
    console.log(books)
})
```
  

In the console, you should see this:


```js
[ { reviews: [ 5c17bacf4d28a75dd44fb30c ],
    _id: 5c17bacf4d28a75dd44fb30a,
    title: 'Name of the Wind',
    author: 'Patrick Rothfuss',
    __v: 0 } ]
```
  

That's our book document with its `title`, `author`, **and an array of IDs**! (only one ID, but still)

  

Even though we did `books.reviews.push(r1)` - i.e. we pushed the _entire_ review object, **Mongoose only saved the ID**.

  

The reason that happened is because of the way we defined our schema, using the `Schema.Types.ObjectId` - excellent!
