
Let's query the `Review` collection for a second:

  
```js
Review.find({}, function (err, reviews) {
    console.log(reviews)
})
```
  

Because of the way our schemas are set up with **reference IDs**, the result would be this:

  

COPY
```js
[ { _id: 5c17bacf4d28a75dd44fb30c,
    book: 5c17bacf4d28a75dd44fb30a,
    critic: 5c17bacf4d28a75dd44fb30b,
    reviewText: 'Excellent Book',
    __v: 0 } ]
```
  

Notice that book and critic are _separate_ references. In order to populate _both_ of them, we could do this:


```js
Review.find({})
    .populate('book critic')
    .exec(function (err, reviews) {
        console.log(reviews)
    })
```
  

That's all - to populate multiple fields, **separate the properties to be populated with a space** and populate as normal. This would be the result:

  

```js
[ { _id: 5c17bacf4d28a75dd44fb30c,
    book:
     { reviews: [Array],
       _id: 5c17bacf4d28a75dd44fb30a,
       title: 'Name of the Wind',
       author: 'Patrick Rothfuss',
       __v: 0 },
    critic:
     { reviews: [Array],
       _id: 5c17bacf4d28a75dd44fb30b,
       name: 'William Jeffery',
       __v: 0 },
    reviewText: 'Excellent Book',
    __v: 0 } ]
```
  

That's it! Our entire reviews object, fully populated with all the data: the review text, data about the critic, and data about the book. Excellent.
