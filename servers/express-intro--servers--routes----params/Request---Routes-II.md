
Now, in your HTML, remove the div element and add the following instead:
```
<input type="text" id="book-input" placeholder="What's the book ID?">
<button onclick=fetchBookData()>Search</button>
```
  

Also, NPM install `jquery`, and add this script tag above your `main.js` script:
```
<script src="./jquery/dist/jquery.js"></script>
````
  

The reason we don't need to do ``./node_modules/jquery...`` is because we're going to **serve** the entire ``node_modules` directory, the same way we served the `dist` directory - so we have direct access to it. As such...

  

**Spot check:** serve the `node_modules` directory using ``app.use(...`` like we did for the `dist` directory.

  

See [solution](https://codepen.io/ElevationPen/pen/XLRNdp?editors=0010).

  

Now add the following to your `main.js`` file:
```
const fetchBookData = function () {
    let input = $("#book-input").val()

    $.get(`books/${input}`, function (bookData) {
        $("body").append(`<div>${bookData.title} - ${bookData.author}`)
    })
} 
```
  

The above should be straightforward: this is the function that gets invoked when our `button` is clicked.

  

The function makes a GET request to ``/books/the-id-the-user-input`` - yes, we are creating our route **dynamically** - and yes, **we are making a GET request to our own server!**

  

This is the exciting part!

We're running a server that does two things:

1.  Serve our HTML/CSS/JS to whoever goes to the root route (``express.static(...)`` does this)
2.  Serve data about books to whoever goes to ``/books/:bookID``

  

The second part acts _exactly_ like any API would, in that we can make requests to it. This is known as an **internal or custom API** - one that _we the developers_ have defined.

  

The main difference between this API request and the others we've been doing so far, is that for others - known as **external API requests** - we've had to write out the whole address, something like: ``https://google.books/api/v2....`` - in these we're going to some remote server for data.

  

But here, **because our server is serving the client files, the client can directly access the server's routes using only the route name**.

  

As such, if the user types `1081` in the `input` and presses the `Search` button, it will send a request to ``/books/1081`` - this is the **same** as going to [localhost:3000/books/1081](http://localhost:3000/books/1081) in the browser - you get some JSON back in both cases!

  

Go ahead and ``console.log(bookData)`` in the callback of the API request - you'll see a simple object with data about the book with an ID of 1081. Same as you'd see in the browser.