
Let's say we have a `personSchema` and in it, we need to store an address field. The address, as we saw above, is a bit more complex than a simple String. We could do something like this:

```js
const personSchema = new Schema({
  firstName: String,
  lastName: String,
  age: Number,
  address : {
    city : String,
    street: String,
    apartment : Number
  }
})
```
  

Or we can use the `addressSchema` from before like this:

```js
const personSchema = new Schema({
  firstName: String,
  lastName: String,
  age: Number,
  address : addressSchema
})
```
  

Both are legal, but the second is tidier.
