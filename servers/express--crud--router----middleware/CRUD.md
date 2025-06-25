
Up to now, we've only worked with GET requests. This is a convenient HTTP method because we can test it easily with the browser, and it doesn't require much from us. At most we need to send some parameters in the URL, but that's all.

  

However, traditionally we use GET requests (and GET routes) to - not suprisingly - _get_ or serve information from some server. This makes sense when working with APIs/simple servers - but eventually we'll have data that we want to update/delete in our own databases.

  

That means we need methods not just for GETting data, but also for **C**reating it in the first place, **R**etrieving (we already have this: GET) it, **U**pdating it, and **D**eleting it. These four data-related operations are known as **CRUD operations**.

  

To understand CRUD, let's start off with a simple server and client. **Go ahead and fork + clone** [**this repository**](https://github.com/Elevationacademy/crud-wonders).

  

You'll find the following in the repo:

-   `server.js` - the file where we'll write our server code
-   `package.json` - don't forget to run `npm install` to install all the dependencies here
-   `dist` - the directory that holds all our client code

  

Eventually this will be a small app that allows us to track world-wonders we've visited (things like the Grand Canyon, Great Wall of China, etc.), add new world wonders, and update the statuses of those we haven't visited yet.

  

In the starter code from the repo you already have the part that GETs (a.k.a **retrieves**) the data from an array in the server, and displays it on the page.

  

You also have the client-side code for getting some data from the user, but now we're going to need to _send_ that data to the server.