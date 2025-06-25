
What a rush. But before we wrap this up, you need to **make a very clear distinction in your mind:**

  

On the **Client** we have...

A GET **request** with an API: ``$.get('/theRoute'...)``

  

On the **Server** we have...

A get **route** defined by the server: ``app.get('/theRoute...``

  

The **client** part is the action, the actual **request** for data - this is someone asking some API for some information. This can be done with jQuery, the browser, someone else's computer - anyone can make this request.

  

The **server** part is a route that **listens** for requests - it's just waiting for someone to access it, and then it will **respond** with whatever information it knows to give. Remember, **the server is passive**.

  

Great. Now, we can practice.