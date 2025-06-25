
By themselves, **schemas don't do anything** - to create actual documents, we'll use our schemas to create Mongoose **models**.

  

From the mongoose site:

_Models are fancy constructors compiled from our Schema definitions._ **_Instances of these models represent documents_** _which can be saved and retrieved from our database. All document_ **_creation and retrieval from the database is handled by these models_**.

  

So models allow us to do two things:

1.  Create instances that will turn into Mongo documents
2.  Query the collection that they represent

  

This will all make sense in a moment.

  

Let’s create a `Person` model from our `personSchema`. Following your schema creation, add this line:


```js
const Person = mongoose.model('person', personSchema)
```
  

Here `mongoose.model` creates a `Person` model. The first parameter, the string 'Person', is our choice for the **model name**, the second argument is our `personSchema`

Notice that **by convention, we capitalize the model name and variable**.

  

To create an instance that we can later turn to a document, we'll use the `Person` _model_, like so:

```js
let p1 = new Person({ firstName: "David", lastName: "Smith", age: 25 }) //purposefully ignoring the `address` field
```
  

The `p1` instance is now an object that is ready to be saved as a document into our DB.

  

Go ahead and **`console.log(p1)`** **to see what comes out**. Of course, to exactly execute this you'll have to **run** **`node person.js`** since this is a regular JS file.


```js
{ _id: 5c16bb0a8fa7cf59e40c8b83,
  firstName: 'Shoobert',
  lastName: 'Dillard',
  age: 25 }
```
  

A couple of things:

  

-   The `_id` field is created for us
-   The `address` was totally ignored because we didn't pass in any values for it

  

Notice that even **creating a model instance doesn't save it to the database**, to do that, we need the `save` method.
