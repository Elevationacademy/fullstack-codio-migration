# Body Parser

When we make a POST request from the browser, behind the scenes **the browser is turning the data we're sending into a JSON** - this is a good thing because it allows us to forgo the `JSON.stringify` bit.

  

However, since we are sending JSON, the server needs to know that it needs to **parse** that JSON.

To do that, we need to add the following to our `server.js`:
```
app.use(express.json())
app.use(express.urlencoded({ extended: false }))
```
  

* You can add the above code under all the `require`s but above the other lines of `app.use`.

  

We'll dive into what `use` is later in this lesson, but for now it's enough to understand that this code allows our server to receive and parse JSON.

  

----------

  

Now if you restart your server, refresh your page, type in a Wonder and Location, and press the `Add Wonder` button:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/post-from-client-gui.PNG)

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/post-from-client-gui.PNG) to emibggen.

  

You should see this in your server logs:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/post-from-client-server-log.PNG)

  

Excellent! We've sent some data to our server through a POST request - note that this is **different** than sending data through GET parameters!

  

When we send data through GET, we're doing it through the **route**, i.e. the URL - this is not always safe or what we want. Plus, it is not convenient when we want to send lots of data - especially if it's more complex data.

  

Sending data with a **POST request allows us to send any JS object**. This is great.

  

And now, of course, we want to _add_ this object to our `wonders` array in the server.