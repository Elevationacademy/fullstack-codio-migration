
Consider this over-simplified visual of client-server communication through the amorphous cloud:

![](https://www.quozr.com/courses/folders/4/images/Pages/clientserver.png)

Until now we've only worked on client code. The client can be on your computer, or the computer of any other user. The web browser (which can also be thought of as a client) takes your HTML, CSS and (client-side) JavaScript, and in turn the user sees beautiful, interactive web pages.

  

But where did these HTML, CSS and JavaScript files come from?

  

Up to now, all these files **came directly from our file system**, which is why you always saw something like C:/Users/.../index.html in the browser's URL.

  

But now we'll be able to use Node to create servers, and _those servers_ will **host** our files. In other words, our node servers will **serve** the client-side of our apps.

  

The cool thing is you've already experienced this concept thousands if not tens-of-thousands of times. Each time you go to a site like amazon.com, the **browser is actually making a GET request to that site's server for you** - the browser requests all the HTML, CSS, and JS files necessary to let you shop online!

  

----------

  

#### **HISTORY, BROWSER VS NODE, AND SPECS**

  

Node.js, created by Ryan Dahl, was introduced in 2009 and has continued to evolve since then. It’s a popular open source and cross platform project on [GitHub](https://github.com/nodejs/node). Node's JavaScript engine is based on the V8 JavaScript engine. This is Google’s JavaScript engine and is used in Google’s Chrome browser. This engine is written in C, not JavaScript, and it is very fast.

  

![](http://roa.h-cdn.co/assets/15/34/980x652/gallery-1440085966-jprice-roadandtrack-4471.jpg)

(above is another very fast V8, don't get confused)

  

For the most part, **running JS in node or in the browser is the same** - that is, same syntax, same built-in methods, same objects available to us - **but browser-specific operations are different**. More specifically:

-   Working with the DOM
-   There is no document object in Node, as there is no browser
-   As such, jQuery as we know it does not work in node - it makes no sense
-   The _value_ of this in the global scope
-   In the browser, the global this is the window object, in Node there is no window
-   We can make HTTP requests more liberally via node that through the browser, as we avoid [CORS issues](https://medium.com/@baphemot/understanding-cors-18ad6b478e2b)

  

There are other differences, but they will become clear as we go on.

  

----------

  

On a more technical note, node uses an event-driven, single threaded, server architecture and non-blocking I/O (input/output) model.

  

We'll learn what that means over the course of... this course, but the gist is that the interpreter* doesn’t pause or sleep while waiting for results. The interpreter is available for serving other requests. When one of the results is ready, a callback is invoked.

###### Remember, the **interpreter** is the part that actually reads our JS code and translates it to computer commands

  

Again - no need to worry about all these tech details right now, we'll explore them over time.