API stands for **A**pplication **P**rogramming **I**nterface.

  

It is **a set of protocols that defines how software components should interact**. This has many applications (beyond requests for data), but for now, the "software components" we will focus on are our client, and some server from which we will request some data.

  

So what exactly is a **request**? Just like the English word, it means an act of **asking for something**.

  

You'll be happy to know you've already made a request in the past. _Thousands_ if not _tens of thousands_ of requests, as a matter of fact.

  

When you go to any website, you're actually **requesting** that domain's server to **serve** you some HTML, and probably other data as well.

  

For instance, when you go to [google.com](https://www.google.com/) you're actually making a request to Google's server, and what they send in return is the familiar search bar and logo with which you're already familiar. You (actually, the browser) make a request to Google _every time_ you go to their site.

  

The kind of requests in which we're interested right now, though, are more focused on receiving data. For instance, go to [this link: https://www.googleapis.com/books/v1/volumes?q=isbn:0439023521](https://www.googleapis.com/books/v1/volumes?q=isbn:0439023521). You should see something like this:

  
```json
{
{
  "kind": "books#volumes",
  "totalItems": 1,
  "items": [
    {
      "kind": "books#volume",
      "id": "hlb_sM1AN0gC",
      "etag": "y50yvFkIvUk",
      "selfLink": "https://www.googleapis.com/books/v1/volumes/hlb_sM1AN0gC",
      "volumeInfo": {
        "title": "The Hunger Games",
        "authors": [
          "Suzanne Collins"
        ],
       //etc...
```
  

You've just made an API request! In particular, you made a request to the **Google Books API**. You've requested data about a book with an ISBN (special identifier for books) of `0439023521` - and you received!

  

Notice that the URL we went to in order to receive this data has `/books/v1/volumes`... - that's the **interface** we were talking about before. In order to get the data from Google's server, we must adhere to their rules: _You want books data? Go to_ _`/books/v1`...__._

  

The `q=isbn`:... is another part of the interface where Google says _if you want to find a book by its ISBN, you have to give me that ISBN number as a_ **_query string_** _called_ _`isbn`_.

A **query string** is simply some information you (optionally, depending on the API) send in your request in order to request something more specific.

  

Google could have also said that to get a book by its ISBN you could have made a request to ...`/volumes?q=**thatBookNumberThing**=04390`... - but they're sensible people, so they called it something sensible. The point is: **you need to know the rules, the interface of the API in order to use it**.

  

----------

  

#### **REQUESTS WITH JQUERY**

  

It's well and fun to make a request through the browser - heck, we barely have to do any work - but that's not very useful if we want to integrate that into our apps.

  

Every modern browser has a built-in object called `XMLHttpRequest` that has some methods we can use to send and receive data to/from a server. AJAX uses this object, and back in the day we would create requests (in code) like this:

  
```js
// Initialize the HTTP request to a server located at "someURL"
var xhr = new XMLHttpRequest();
xhr.open('get', '/someURL');

// Track the state changes of the request.
xhr.onreadystatechange = function () {
    var DONE = 4; // readyState 4 means the request is done.
    var OK = 200; // status 200 is a successful return.
    if (xhr.readyState === DONE) {
        if (xhr.status === OK) {
            console.log(xhr.responseText); // 'This is the returned text.'
        } else {
            console.log('Error: ' + xhr.status); // An error occurred during the request.

        }
    }
};

// Send the request to send-ajax-data.php
xhr.send(null);
```
  

This is some pretty heinous stuff to make a simple request for data. There are a number of simpler ways to do this, but today we'll focus on jQuery's `get` method.

  

This method wraps all that wild code up there, and bundles it into something much more manageable for us as developers. The following is about the simplest way to make a request - specifically, a **GET** request - which, unsurprisingly, gets us some data.

  

```js
$.get("https://www.google.com", function(result){
    console.log(result)
})
```
  

Notice the **callback**? Above we see jQuery - the dollar sign - invoking a `get` function to google.com.

  

Then - because this request can take a while* - we have a **callback function** with a `result` parameter which we print out **once the request is complete**.

###### *Remember, we make requests _asynchronously_

  

This is an important point you must understand: **AJAX requests, by definition, are asynchronous. Therefore you cannot do something like this:**

  

```js
let data = $.get("/some_api")
```
  

The above returns a **promise**, which is a concept we will talk about in another lesson. But the point is, in order to use the data that an API returns, we must use a callback.

  

The example from before (the `https://www.google.com` request) won't exactly work because of [CORS](https://stackoverflow.com/questions/20035101/why-does-my-javascript-get-a-no-access-control-allow-origin-header-is-present) issues (not important right now), but the following will work:

  

```js
$.get("https://www.googleapis.com/books/v1/volumes?q=isbn:0439023521", function(result){
    console.log(result)
})
```
  

The code is the same as before, except instead of going to google.com we're going to its **public API** - specifically, its _books_ API - to ask for data about the book with an ISBN code of `04390`...

  

This is **virtually the same** as what we did before through the browser - they are both **GET requests** that `request` some data from some server.

  

Notice that we print our result data inside the callback.

  

**Try this out!**

1.  Create an index.html and `main.js` file
2.  Add the jQuery CDN
3.  Connect the files
4.  Add the above `$.get(...)` code to your JS file
5.  Open `index.html` in the browser and check out your console!

  

You should see an object that looks like this:


```js
{"kind": "books#volumes", "totalItems": 1, "items": Array(1)}
```
  

You can open it up (click on the arrows) several times to see all the data (JSON about the _Hunger Games_ book) the API returned - this is the data we **requested**!

  

----------

  

**Spot check**:

Make a request (in code) to the google books API, and find data about the book with the `title` (instead of the `isbn` query string) _Name of the Wind_.

  

Console log the first description of the first item you receive.

  

See the solution [here](https://codepen.io/ElevationPen/pen/KjPZxM?editors=0010).

  

There are many other ways to search for books, we don't just have to use the ISBN or the title. The [Google Books API documents](https://developers.google.com/books/docs/v1/using#PerformingSearch) provide an excellent guide to all the methods you can use.

  

----------

  

So we understand that in order to get data from an API that we need to request it, specifically we need to make a GET request.

  

The [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) (good ol' HTTP) defines a `GET` request as a something that should only retrieve data. If you want extra functionality on your webpage, then HTTP also defines 3 other request types -

  

-   `POST`
-   `UPDATE`
-   `DELETE`

  

But we'll learn more about those in a future lesson. Today is all about the `GET` request.

  

As we saw, `GET` request can be made in more than one way (browser, code) - but one thing always remains true, **the request is always made to some server**; at the other end is just a computer waiting for someone to ask it a question!
