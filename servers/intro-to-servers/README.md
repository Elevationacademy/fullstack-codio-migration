# Barebone Server

To see an example of a simple server, let's create one using node's built-in `http` module.

  

Start by opening a new directory called `server-intro` and inside of it create a file called `server.js`

  

Inside of this file, add the following code:
```
const http = require('http')

const server = http.createServer(function (request, response) {
    response.writeHead(200, { 'Content-Type': 'text/plain' })
    response.write('Hello, world')
    response.end();
})

const port = 3000
server.listen(port, function () {
    console.log(`Node server created at port ${port}`)
})
```
  

Now run this file (just like any other JS file in node: `node server.js` in your command line/terminal), and you should see the console log "Node server created at port 3000"

  

Now go to your browser, and head to `http://localhost:3000/`

  

And that's it. You've used your browser to make a GET request to your server, and the server replied with "Hello, world"

  

----------

  

Of course, this doesn't seem very exciting yet, but here's what's going on in that code:

-   We didn't have to `npm install http` because this module is **built-in** to node
-   One of the things this module can do is invoke the `createServer` method
    -   This method receives one parameter, a callback function, that takes two arguments: a request, and a response
    -   We'll get to `request` later, but `response` is what allows us to reply to a client that sends a request
-   The `response.writehead` is a method that sends **metadata** about the response
    -   This is information about the response the user won't see, but the browser (or whoever is making the request) can access
    -   The `200` is an [HTTP Status Code](https://www.restapitutorial.com/httpstatuscodes.html) that says "everything is OK"
    -   The ``{'Content-Type...}`` tells whoever made the request what kind of data it will receive in return
-   The `response.write` method actually "writes" something to display to whoever makes the request
-   Finally, the `response.end()` closes this **request-response cycle**

  

We have the `server.listen` code at the bottom which is what ultimately starts the server. Without this, the server does not exist.

  

The `listen` part is important: **servers are always listening for requests. Like functions, they do nothing until called upon** - this means that we can write the best server in the world, but it will do **nothing** except for **serve** whoever makes a ``request``

  

In our example, the entity making the request is the browser itself when we go to **localhost:3000** - this initiates a request, the server gets the request, the server creates and sends a response, and the cycle completes.

  

Luckily for us, when we start using `express`, the code to run a server will be **much** simpler.

  

----------

  

Now, go to your terminal and stop the server from running (press `Ctrl+C`), and refresh the page where you were at localhost:3000, you should something like this:

  

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A1614-0.png)

  

Once you shut down your server, it's no longer listening. The browser (or any client) cannot find **localhost:3000** because it doesn't exist anymore.

  

So remember:

1.  You create a server
2.  You spin/run/activate/start the server - now it is listening
3.  Clients make requests to the server
4.  The server serves a response
5.  Cycle ends

  

The way we'll build our servers, the server will be able to receive many requests simultaneously - but you must consider each one as a separate **request-response cycle** - _even if_ the same client makes 1,000 requests to the same server, each one is a separate cycle.