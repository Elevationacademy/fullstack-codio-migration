
Before we start building our own servers with express, we need to understand what a server really _is_, and understand how building one works.

  

Equally important is to understand the difference between a client and a server - because they are different.

  

This is mainly a conceptual lesson, but the concepts here are **critical**, you will **definitely be expected to understand these ideas** in interviews, and as a developer in general.

  

Let's begin.

  

----------

  

#### **A SERVER, CONCEPTUALLY**

  

Ultimately, a server is a physical machine. For all the talk about the "cloud" and "cloud computing" - any data (as of 2018, at least), any code, and program, is stored or executing on a physical machine somewhere on the ground (or [underwater](https://thenextweb.com/microsoft/2018/06/07/microsoft-just-dropped-864-servers-into-the-sea-to-run-an-underwater-data-center/)) - nothing in the sky so far.

  

We use **servers to serve data, files, images, videos, etc** - most of what you see when you enter any webpage is being served to you from some server, somewhere.

  

It should come as no surprise then, that if we want the apps we've been building to be accessible to other people, we'll have to **serve** those as well - and we will, pretty soon. Take a look at this graphic:

![](https://assets-global.website-files.com/620d42e86cb8ec4d0839e59d/6230ef96eb40de02b0e3fbd0_61c9fc4838f10a5389c9cbca_Client-Server-Diagram.jpeg)



This is a nice representation of what's known as the **client-server** model. **One server serving many clients.**

  

Today it's a little different, there can be thousands of servers serving the same data/files - but there will virtually always be more clients than servers, and the server will always serve some information to the clients.

  

Another important concept to understand is that **servers should be stateless** - loosely, this means that **the server itself does not keep any information about the client**. The server may _receive_ data from the client, then _store_ that data in a database - but it should never "keep a state" or "remember" anything about the client.

  

In other words, **any communication between the server and client is a one-time deal, and should include all the necessary information to complete a transaction**.

  

If you imagine the client as person A, and the server as person B, this would be considered **bad** communication:

  

**A:** Hey, I need to save some data about a person named "Richmond"

**B:** Ok, does he have an identifier?

**A:** Yes, it's 13001

**B:** Ok, saved ``{id: 13001, name: "Richmond"}`` //in this case, the server remembers the name "Richmond" from the last interaction

  

Instead, it should be:

  

**A:** Hey, save this data: ``{id: 13001, name: "Richmond"}``

**B:** Ok, saved ``{id: 13001, name: "Richmond"}``

  

This is known as a valid **request-response cycle**: the client requests for something (data, an operation), and the server (optionally) does something, and then (mandatory) sends a response in return.