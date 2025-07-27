The term `Bearer` is used in the context of using **JWTs** as **authentication tokens** in HTTP requests.

 When a **JWT** is used as a **Bearer token**, it is included in the HTTP request header using the **"Authorization" header field** with the value **"Bearer"** followed by the **JWT**.

So when we want to send a request to the server it should look like this:

```js

$.ajax({
  url: 'https://example.com/api/meow',
  type: 'GET',
  headers: {
    'Authorization': `Bearer ${token}`
  },
  success: function(response) {
    console.log(response);
  },
  error: function(error) {
    console.log(error);
  }
});
```

We can see that we send the **Token** in the header of the request.

