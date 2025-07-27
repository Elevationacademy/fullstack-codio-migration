We will showcase how token-based authentication works. We will begin with a simple scenario: 

Many websites require users to sign up before they can perform any actions in the site. There are many different benefits to having user-account based websites, from managing permissions to offering a unique experience.



1. We start with a simple **Login page**, in this login page we will enter our `username` and `password`.

![](https://i.ytimg.com/vi/eeHqZeJ9Vqc/maxresdefault.jpg)

2. As we enter our `username` and `password` and make a request to our `server`, the `server` receives the request and would want to **authenticate** the user.

3. Once there is a successful **authentication** the server will request a generation of a `token`, this generation could be from a 3rd-party service or a library depending on how we implement it. The generated `token` is **encrypted** and sent back to the `client`.

4. The `client` will request any `resource` that it may need and send the `token` with his request.

5. The `server` then will be able to serve the `client` a resource.

6. `resource` is sent back to the client.

You can look at this flow for reference.

![alt text](.guides/img/TokenBasedAuthentication.png)

