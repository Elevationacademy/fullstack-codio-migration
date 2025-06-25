
The first of the new CRUD operations we'll talk about is **C**reation - to create a new item we will use a POST request. In this app, the "new item" will be a new World Wonder.

  

Note that generally, **CRUD operations are for working with Databases** - but for now we'll just pretend the `wonders` array in the `wonders.js` file, located in our `server` folder, is our DB.

  

Go ahead and add the following to your `server.js` under the first ``app.get('/wonders'...)`` route:
```
app.post('/wonder', function (req, res) {
    console.log("Someone's trying to make a post request")
})
```
  

Up to now we've seen `app.get` - these were `get` **routes**, and we needed those for our GET requests. Now we're creating a `post` route which will accept POST requests.

  

If you try to go to `localhost:1337/wonder` in your browser (make sure you've run your server first), you'll notice that we **don't** see that console log in our server.

  

That's because, as we've noted before, the browser is making a GET request. In order to make POST requests, we need to write it out in code, or use an external service like [Postman](https://www.getpostman.com/). For now, we'll write it out in code.

  

In your `main.js`, add this code to the `addWonder` function:
```
let data = { name: newWonder, location: newLocation }
$.post('/wonder', data, function (response) {
    console.log("POST complete")
})
```
  

Once the `addWonder` function is invoked, this code will send a POST request to the server's ``/wonder`` route (which, remember, is a `post` route)

  

Notice the two differences between this kind of request and a GET request:

1.  We write ``$.post` instead of ``$.get` - should make sense
2.  We've added a second parameter, `data`, to the request

    -   This is the new data we're sending to the server

  

----------

  

Now if you save, refresh your server and page, press the `Add Wonder` button, and **look in your server logs**, you should see "Someone's trying to make a post request" (make sure you are accessing `localhost:1337` from the browser).

  

In order to access the data that the user sent, we have to go through `req.body`

  

However, if you ``console.log(req.body)`` **inside of the** ``/wonder`` **route**, you'll see `undefined` unfortunately. To remedy this, we need to use the `body-parser` package.