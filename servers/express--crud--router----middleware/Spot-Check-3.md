
The final part of CRUD is to delete something, and for that we have the (no surprise) DELETE request.

  

Like PUT, there is no built-in ``$.delete` in jQuery - but you already know how to handle this.

So go on, on your own: **create a** `delete` **route in your server (called** ``/wonder``**) that also accepts a** `name`**, and removes that wonder from the array.**

  

See [solution](https://codepen.io/ElevationPen/pen/jjmBPp?editors=0010).

  

As for accessing this route - that's going to require some extra HTML - you can do this at the end of this lesson. The interesting part is in the server anyway ~

  

For now, you can test your route with this code:
```
$.ajax({
    url: '/wonder/Colosseum',
    method: "DELETE",
    success: function () { }
})
```
  

Just add that code to the bottom of your `main.js`, then check in your server that the "Colosseum" wonder was removed.

  

----------

  

And there you have it! A fully CRUD-compliant app. Of course, all the data is in an array on our server which is **awful** - but until we learn to work with databases this is the best we've got.