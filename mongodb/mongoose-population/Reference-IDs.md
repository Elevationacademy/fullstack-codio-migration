
In short, the solution is to use **reference IDs**. This is a common practice from the world of Relational Databases, which we're now applying to Mongoose.

  

The idea of using references is simple: **instead of storing an entire sub-document in each schema, we will only store a _reference_ to the object**.

  

Check out these schemas:


```js
const bookSchema = new Schema({ 
  title: String,
  author: String,
  reviews: [{type: Schema.Types.ObjectId, ref: 'Review'}] //reference to an array of Review documents
})

const reviewSchema = new Schema({ 
  book: {type: Schema.Types.ObjectId, ref: 'Book'}, //reference to a Book document
  reviewText: String,
  critic: {type: Schema.Types.ObjectId, ref: 'Critic'} //reference to a Critic document
})

const criticSchema = new Schema({ 
  name: String,
  reviews: [{type: Schema.Types.ObjectId, ref: 'Review'}], //reference to an array of Review documents
})
```
  

You'll notice that these schemas are similar to what we had before except for one thing: **we're not storing sub-docs, we're using reference IDs instead**. There are two parts to this syntax:

  

1.  type: `Schema.Types.ObjectId` - this is what tells Mongoose to save an _ID_ and not the actual document
2.  This part of the syntax will be the same for each schema
3.  `ref: MODEL_NAME` - this will associate the ID with the correct collection
4.  This is important because later, when we retrieve the data, it will tell us which collection to look in
