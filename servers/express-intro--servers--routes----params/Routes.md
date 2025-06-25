
In the simple example we just saw, a user can only go to `http://localhost:3000/`` - that's like if people could only ever go to `google.com` - but often our site will be much more complex and have many **routes**.

  

  

For instance, [google.com](https://google.com/) will take you to Google's landing page with the familiar search bar, but google.com/maps will take you to their [maps](https://google.com/maps) app, and you can guess where [google.com/calendar](https://google.com/calendar) will take you.

These /somewhere are known as **routes**, and we can add some to our app as well:
```
app.get('/', function (request, response) {
    console.log("Someone has come into the server. Brace yourselves.")
    response.send("Ending the cycle, thanks for visiting")
})

app.get('/maps', function (request, response) {
    response.send("Here's some stuff related to maps")
})

app.get('/shoobi', function (request, response) {
    response.send("This here is the shoobi *route*")
})
```
The "base" ``/`` is known as the **root** route - it has no specific name.

  

But if you change your code to look like the one above, save your file, then restart your server, you should be able to go to [localhost:3000/maps](http://localhost:3000/maps) or [localhost:3000/shoobi](http://localhost:3000/shoobi) - and get each separate response.

  

  

Right now these routes are just returning simple strings (i.e. **data**), but soon we'll see how to return entire files/directories/json - and then each route will be more meaningful.