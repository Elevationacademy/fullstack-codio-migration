
Alright, we've been teasing servers for a while. Now it's time to actually build a real one. It will still run on **localhost** (your machine) for now, but it will be a real server.

  

In particular in this lesson we'll cover:

-   The `express` package
-   Routes
-   Parameters
-   Serving files
-   Client-Server communication

  

Let's spin some servers.

----------

#### **EXPRESS**

Express is nothing more than an [NPM package](https://www.npmjs.com/package/express) that allows us to create servers easily.

  

As such, go ahead and `npm install express` for starters (you can create a new directory, or use an old one, up to you). Either way, create a `server.js` file, and right at the top of the file add the following:
```
const express = require('express')
```
  

This should come as no surprise. We need to require every NPM package we want to use.

  

If you ``console.log(express)`` and look around there, you'll see that `express` is really just a big function with some properties.

**By convention**, we invoke `express` and store its value in a variable called `app`*:

  
```
const app = express()
```
###### *Some people call this server instead, also sensible

  

Now if you take a look in `app` you'll see that that's an object with a whole bunch of properties/methods.

One of the more interesting methods is the `listen` method. We can invoke it like this:
```
const port = 3000
app.listen(port, function(){
    console.log(`Running server on port ${port}`)
})
```
  

Now - in your terminal, in the same directory where this file is - run the file: `node server.js`

This will start a server that is listening on port 3000 (notice the callback function that gets invoke after the server starts running).

  

Listening for what? For requests. Remember this, and tatoo it across your back: **servers are patient, responsive entities. They listen for requests, and only act when asked to**. The requests can come from browsers, apps, code, [Postman](https://www.getpostman.com/) - wherever. The server doesn't care who is asking. It will respond.

Generally, this piece of code goes at the **bottom** of our `server.js` file - everything we add from now one should come before that.

Now, if we go to [localhost:3000](http://localhost:3000/), we should see something like this:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/express-cannot-get.PNG)

This might seem bad, but it is better than this error:

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A1816-0.png)

The error we're seeing - ``Cannot GET /`` - is straightforward: when we try to go to localhost:3000, we (technically the browser) are making a GET request. The browser is trying to get _something_ from that address. However, our `server.js` file (which is the code running our server) looks like this:

  
```
const express = require('express')

const app = express()

const port = 3000
app.listen(port, function(){
    console.log(`Running server on port ${port}`)
})
```
  

We're not doing anything except for running a server - we haven't given it any instructions to respond to anyone!

To remedy this, add the following code to your file (remember, before the `app.listen` section):
```
app.get('/', function (request, response) {
    console.log("Someone has come into the server. Brace yourselves.")
})
```
  

Now, whenever the browser (or anyone) tries to visit localhost:3000/, they have somewhere to go.

  

The above code is literally saying _When someone makes a GET request to me*, invoke this callback function with these two parameters_ - we'll talk about these parameters and what ``/`` means in a minute.

###### * "me" in this case is app, the server

  

Save your `server.js` file, restart your server (remember, `Ctrl + C` then `node server.js` again in the terminal), and refresh the page. And now... nothing?

  

Not exactly nothing. If you look in the terminal (where you ran `node server.js`), you _will_ see "Someone has come into..." in your console log.

  

But if you look closely at the browser, you'll see that the page is forever loading. This happens because the client (the browser) has made a **request**, but the server never made a **response**! The **request-response** cycle has not ended! And so our client will wait until either:

-   The browser times out
-   The battery dies
-   Your computer fails
-   The apocalypse comes

  

It's a patient machine.

  

----------

  

The final part of building a basic server, then, is to send a response. To that end, make your code look like this:
```
app.get('/', function (request, response) {
    console.log("Someone has come into the server. Brace yourselves.")
    response.send("Ending the cycle, thanks for visiting")
})
```
Here's we're still ignoring the `request` parameter, but we're taking advantage of the `response` object to invoke the `send` method - this sends a response to the client!

  

Now, finally, if you go to [localhost:3000](http://localhost:3000/), you'll see the response from the server.

  

And that's it - that's the most basic server you can create. If you want to see this work as a 'real' server, try using [Ngrok](https://ngrok.com/) and let someone else access your server as well.