# Backend

## Functionalities
create a server that will do the following logic / functionalities :

- Retrieving all the transactions.
- Adding a transaction.
- Deletion a transaction.
- Getting a breakdown of the sum of transactions per category.


## Guidelines
1.  Make sure your server is running on a **different** port from your react app.
2.  When making requests from the client side to the server, **write out the full path**
    -  i.e, instead of making a GET request to `/transactions`, you'll make it to `http://localhost:<server-port>/transactions`
3.  Since react is "hosting" our app, there is **no need** to serve any `dist` or `node_modules` from the server
4.  Because we want our server to accept "foreign" requests, we have to explicitly allow this. For simplicity, use the following code:

  

```
app.use(function (req, res, next) {
    res.header('Access-Control-Allow-Origin', '*')
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With')

    next()
})
```
  

Add the above code before your route definitions.

  

**Note:** the above steps are only required when we are in _development_ mode. In production mode (i.e when you'll deploy to Heroku, for example) it's different.

  

In particular, <span style="color: red">**never ever add the above** **Access-Control...** **code snippet in your production code**</span> - it allows _anyone_ to access your server with _all_ permissions.

  

It is **only safe for development purposes**.