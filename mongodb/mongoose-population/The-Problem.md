
Before we talk about a new concept, let's talk about what we already know, and why it's sometimes not enough.

  

Say we wanted to create three collections: `books`, `critics`, and `reviews` - how would these schemas look like?

If you think about it,

-   Each book has some data about itself and a list of reviews about the book
-   Each critic should have a name and a list of reviews the critic has written
-   Each review should have the review text, and which book and critic it's reviewing

  

So maybe we could write out the schemas like this, using **sub-documents** (i.e. nested schemas):

  

```js
const bookSchema = new Schema({ 
  title: String,
  author: String,
  reviews: [reviewSchema]
})

const reviewSchema = new Schema({ 
  book: bookSchema,
  reviewText: String,
  critic: criticSchema
})

const criticSchema = new Schema({ 
  name: String,
  reviews: [reviewSchema],
})
```
  

As for the models, they would look something like this:

  

```js
const Book = mongoose.model("Book", bookSchema)
const Review = mongoose.model("Review", reviewSchema)
const Critic = mongoose.model("Critic", criticSchema)
```
  

But then when we go to save this data, **we're going to be repeating ourselves** quite a bit. Think about which collection will store data about reviews:

  

1.  The `books` collection - a list of reviews about each book
2.  The `reviews` collection - obviously, this is where we store all our `review` documents
3.  The `critics` collection - each critic has a list of reviews they've written

  

Storing the same data in separate place is a big no-no in the world of Database Management. This defies a principle known as **data integrity**, which states that **data should be stored in a single place** and act as our **single source of truth**.

  

One of the main reasons data should be stored in the same place is because otherwise, **any change in data in one place would make the data inconsistent in other places we've saved it**. This means that for any _one_ update to our data, we'd have to go to _two other places_ to update it! Very bad.

  

Now that we understand the problem, let's talk about a possible solution.
