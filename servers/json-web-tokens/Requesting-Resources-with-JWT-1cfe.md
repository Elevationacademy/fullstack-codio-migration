Now that we created a **JWT** based system in the **Server.**

If we want to request a resource that is within our `token` authority (Step 4).

![alt text](.guides/img/TokenBasedAuthentication.png)


So when we want to make a `request` with a `token` we want to use a `Bearer token`.

We would want to extract our **JWT** and send it in the **Header** of our request using the `Bearer token` syntax.

The token should look like this:
```
'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJsb3RlbWgiLCJpYXQiOjE2Nzg2OTI0NTZ9.Y9n3GiPFjjKFiYVcj-CUTHZPfq8bCr2HL-R2jQsXPbg'
```

If we want to add this to our header, depending on the library we are making the request with we can attach it to the **Header**.

For example, in **JQuery** we can use the `ajax` method like this:

```js
      $.ajax({
        url: `/cat`,
        method: 'GET',
        headers: {
          Authorization: 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MiwidXNlcm5hbWUiOiJsb3RlbWgiLCJpYXQiOjE2Nzg2OTI0NTZ9.Y9n3GiPFjjKFiYVcj-CUTHZPfq8bCr2HL-R2jQsXPbg'
        },
        success: function(response) {
          console.log(response);
        },
        error: function(res, status, error) {
          console.log(error)
        }
      });
```


Feel free to explore other libraries.
