
Today we will start crossing over to the other side: **server**-side development.

  

So far all the work we've been doing has been strictly on the **client**-side - i.e. only the **frontend** part of our application with which the user interacts. Now it's time to start setting up our **backend**, and to do that we'll be using **Node JS**.

  

In this lesson we will cover the following introductory concepts to Node JS:

-   What Node is
-   JS vs. Node
-   Running Node code
-   Debugging using VS Code
-   Modules in Node: exporting and requireing them

  

So let's go.

  

----------

  

#### **NODE JS**

  

Node JS (a.k.a Node.js, node.js, node js) is another **JavaScript runtime environment** - this just means that it's somewhere we can run JS code that's not the browser. We'll just call it Node* for simplicity.

###### *A lot of developers will say that they know _node_, or they _write_ node, but what they mean is that they work in a node _environment_ - the actual coding language is still _JavaScript_

  

So far we've used our JS to write code that runs only the client's device - in our specific case, the browser. This is called **frontend** code.

  

Node code is referred to as **backend** code because the user has virtually zero interaction with it. Among other things, Node allows us to:

-   Create servers
-   Serve data to users
-   Communicate with external APIs
-   Communicate with databases simply

  

Before we dive into all of that, let's have a quick refresher on the concept of clients vs. servers.