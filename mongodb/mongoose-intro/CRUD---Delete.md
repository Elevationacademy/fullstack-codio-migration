
Finally, the **D**elete of our CRUD.

  

We use the `remove` method to delete documents, and it works exactly like that `update` method.

  

We also have the `findByIdAndDelete` method - which also works the same as `findByIdAndUpdate`

Here is a simple example:

  
```js
Person.findByIdAndDelete("5c16c63bc5ad73471c3ca323").then((person)=>{
  console.log(person)
})
```
