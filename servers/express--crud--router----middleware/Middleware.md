
Finally, we've been teasing this enough. Let's talk about **middleware**.

  

From our usage of middleware so far - and from its name - you should have a general concept of what middleware is: **middleware functions are functions that can run in the _middle_ of our request-response cycle.**

  

The simplest example is when we did the following:
```
app.use(express.json())
```

The `express.json()` method is a function that is running between when a request comes in to the server, and before it actually arrives at whichever route it's looking for.

  

When we `use(express.json())` we're actually asking express to first run the `express.json()` method on the data inside of the incoming requests (this parses our JSON into managable JS objects), and only then let it continue to our routes.

  

So in fact, when someone does `$.post(/wonder...)`, this is **not** exactly what's happening:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/middleware-wrong-flow.PNG)

But in fact, this is more similar to the **actual flow**:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/middleware-correct-flow.PNG)

* Note, `bodyParser.json()` in the image above has been changed to `express.json()`.

  

Express actually has more middleware functions going on behind the scenes, but we won't go into them right now.

  

If you want to dive deeper into middleware, [this is a good article](https://medium.com/@agoiabeladeyemi/a-simple-explanation-of-express-middleware-c68ea839f498), and [these are the official docs](https://expressjs.com/en/guide/using-middleware.html) - but for the most part it's enough to understand that something can happen "in between" our request and our request arriving at our routes.