
With all our CRUD operations, you can imagine how quickly our `server.js` can become bloated.

In reality, we don't want to have all our routes inside of this file - we want this file to be our `server` file - the file that only deals with high-level operations like importing the main modules, serving the core app, and starting the server.

As such, we're going to extract all our route-management to a separate file. To do that, we're going to use another piece of middleware (which - again - we'll explain soon). So for now, go ahead and

-   Create a `server` **directory** at the **root** of your project (same level as your `server.js` file)
-   Inside of this directory create _another_ directory called `routes`
-   Inside of the `routes` directory, create an `api.js` file (other developers might call this `routes.js` - either is fine)

Now go ahead and **move all your routes and the** `wonders` **array to** `api.js` - that is, all the ``app.get/post/put/delete`` - all of that goes to `api.js`.

Now we literally have an API file - **this is our server's API, our own custom Application Programming Interface***.

###### *If anyone wants to interact with our _wonder_ful data, these are the operations available to them: getting all the wonders, adding one, updating one, and deleting one. Once we host this, anyone will be able to make GET requests to _our_ servers and get data from us. Incredible.

But of course, **there's a problem**. Now `server.js` has no idea about `api.js`. To fix that, we need to do two things.

First, add this line to your `server.js` file:
```
const api = require('./server/routes/api')
```
  

Add this before any of the `app.use`, and after the other imports.

But of course, you already know that we can't import anything that isn't being exported. So in `api.s` we need to **export** something.

However, you'll also notice that `app` **isn't defined in** `api.js`**!** That means that all of our `app.get`, `app.post`, etc - they're all meaningless right now.

To fix that, add this to the top of your `api.js` file:
```
const express = require('express')
const router = express.Router()
```
  

And here we have it - our `router` object.

This object allows us to manage routes, much like `app` did in `server.js` - the **difference between** `app` **and** `router` **is that** `app` (which, remember, is the value of invoking `express()`) **can do a lot more than just manage routes.**

And `router` is good at exactly that - managing routes. You can read more about `router` [here](https://expressjs.com/en/4x/api.html#router) if you like.

So now that we have this `router` object, you can:

-   Replace all the `app.` with `router.` inside of `api.js`
    -   They work the same for the actual routing
-   Add the following line to the end of your `api.js` file
```
module.exports = router
```
  

This should comes as no surprise, as `server.js` is importing it!

  

----------

  

**One last step** to make this new file work.

In `server.js`, all we've done is _import_ the `router` object into a variable called `api`

**To actually make our server** _use_ these routes, we need to add this line (add it after all the other `app.use`) :

  
```
app.use('/', api)
```
  

What this is saying is _whenever someone makes a request to a route that begins with_ `/` _(which is all our routes), use the separate_ `router`* object to manage those requests_.

###### *This object is stored in our `api` variable

  

This was quite a lot to go through, so to verify that everything was setup correctly, your setup sould look like this now:

  

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A1849-0.png)

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/router-setup.PNG) to embiggen.

  

And your `server.js` should look like this:

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A1849-1.png)

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/router-setup-serverjs.PNG) to embiggen.

* Note, on lines 9 & 10 it should say `express` instead of `bodyParser` and line 3 is not required.

  

Huzzah for separation of concerns and modularity!