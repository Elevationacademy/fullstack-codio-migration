
You may sometimes want to populate the properties of one document (as opposed to an entire array).

  

To do so we can use the [doc.populate](http://mongoosejs.com/docs/api.html#document_Document-populate) mongoose method. For example:


```js
Critic.findOne({}, function(err, critic) {
  //now we have a single critic
  critic.populate('reviews', function() {
    console.log(critic.reviews)
  })
})
```
  

Note that here we don't use the `exec` method.

  

Not much more to say about this, you get it ;)
