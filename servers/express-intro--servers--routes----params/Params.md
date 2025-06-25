
Sometimes we need to send information from the client to the server when we make requests. For instance: we might want to send the user a custom welcome message depending on which user has come to our site.

  

To that end, check out this code:
```
app.get('/landing/:username', function (request, response) {
    response.send(`Hi there, ${request.params.username}`)
})
```
  

A few things:

-   We're using the `request` object to access the `params`* property
-   This property allows us to access anything that is sent _through the route_
-   We can access this route by going to [localhost:3000/landing/Tilda](http://localhost:3000/landing/Tilda), for example - though the name is variable!
-   If this reminds you a bit of functions - good! It's the same concept
-   The ``/:username` is just a placeholder for anything that comes after ``/landing``
-   Any part of the route that starts with ``/:`` will be a variable that has to come in through the route

###### ***params** is short for **parameters**