As we request a specific `resource` from our backend, it's crucial to enhance its security layer. Our topmost priority is to prevent any potential abuse, which is why we intend to validate the requester's ID by ensuring the validity of their `token`.

Let's look on our **API**
## Middleware

A common way to include these token authentication layers is using a **Middleware**.

In a **Express** server we can pass another parameters to the route which is a **middleware**, a **middleware** is a function that sits in between the server and the application's endpoints, intercepting and processing incoming requests and outgoing responses.

**Middleware** functions have access to the request and response objects, allowing them to add, modify, or delete properties from them. Middleware can be used to perform tasks such as authentication, logging, error handling, and more.

For example:

```js
const express = require('express');
const app = express();

// Middleware function
function logger(req, res, next) {
  console.log(`Received ${req.method} request for ${req.url}`);
  next();
}

// Add middleware to the application
app.use(logger);

// Add endpoint to the application
app.get('/', (req, res) => {
  res.send('Hello, World!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
```

In the above example, the logger function is a middleware function that logs information about incoming requests to the console. The app.use method is used to add the logger middleware to the application.

## Middleware Authentication with Token

If we want to create a middleware that validates that our token is correct, we would want to do the following.

```js
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) {return res.sendStatus(401);}

  jwt.verify(token, secretKey, (err, user) => {
    if (err) {
      return res.sendStatus(401);
    }
    //defnie which user is this after token authentication
    req.user = user;
    next();
  });
}

```

Now because we extracted which user it is from the `verify` method, we can save it in the `req`.
That way we can read who is the user sending the requests and possibly what are his permissions.
