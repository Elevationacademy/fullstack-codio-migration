
Even though we said that Mongo DB documents have no "structure", when we use Mongoose we will be adding structure using a **schema**.

  

A **schema** in Mongoose is similar to a `class` in OOP - it is a blueprint of how a document will look.

  

Building a schema is straight forward. Check this out:


```js
const Schema = mongoose.Schema

const personSchema = new Schema({
  firstName: String,
  lastName: String,
  age: Number
})
```
  

For starters, we're getting the `Schema` function directly from `mongoose`

This function allows us to define a **schema**. However, **don't be confused by the** **`new`** **syntax**! A schema is still just a blueprint.

  

Generally, we create one schema definition for each **collection** we want to have in our DB.

  

As you see that in the object above, the format is quite simple - `fieldName : SchemaType` - this is what will give **structure** to our documents.

We can also write this differently to _guarantee_ that some fields have a value:

```js
const personSchema = new Schema({
    firstName: { type: String, required: true },
    lastName: String,
    age: Number
})
```
  

This is known as a **validator**. You don't have to use it, but it can save a headache down the road. There are other validators you can read about [here](https://mongoosejs.com/docs/validation.html) if you like.

  

**The possible Schema Types are:**

-   String – mapped to javascript String
-   Number – mapped to javascript Number
-   Boolean - mapped to javascript Boolean
-   Array – mapped to javascript Array(object)
-   Date – mapped to javascript object (date object)
-   ObjectId | Oid – mapped to javascript object
-   Mixed – mapped to javascript object

  

The Mixed type has the flexibility to store variety of data types within the same fields, and we use it when we do not want any structure for this field (if we prefer to go a bit schema-less with our schema - go figure.)
