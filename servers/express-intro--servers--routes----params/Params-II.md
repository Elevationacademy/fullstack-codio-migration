
Parameters that are part of the route (like ``:/userID`` or ``:username`` from above) are **required** parameters. If you got to ``/users/:userID`` without supplying a `userID`, it will not work.

  

  

However, we can also accept **optional parameters**.

  

  

APIs tend to work like this too. For instance, when we access the Google Books API, we send a request that looks like this: ``googleapis.com/books/v1/volumes?q=title:the alchemist``

  

  

If you recall, the part in bold is called a **query string** - this is where we can send the optional parameters. Check this out:

  

  
```
app.get('/routeWithOptionalParameters', (request, response) => {
    let params = request.query
    response.send(params)
})
```
  

  

  

Notice that this route doesn't have anything after the route name. Not required ``/:parameters``

  

  

However, we are accessing `request.query` - the `query` key is where our optional parameters will be stored, as objects themselves. For instance, if we (save, restart server) go to `localhost:3000/routeWithOptionalParameters/?name=robert`, we should see this:

  

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/express-routes-optional-param.PNG)

  

To _send_ the parameters, as you can see, we add a ``/?{KEY}={VALUE}`` pair after the route itself.

  

  

And of course, we can add as many parameters as we want in our route. We just need to separate each key-value pair with an ampersand: ``&``

  

  

**Note:** the above is a silly example where the server responds with the same data it was given - this is just to underscore the point that we can access the query string using `request.query`