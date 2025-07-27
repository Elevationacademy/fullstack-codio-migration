We can see that in this file we have a `users` variable which contains two `users` (their password and username).
Usually this information is in the database but for the sake of simplicity we will contain it in the server directly.

There is a simple `/login` route that all it does is redirect us to another page (even if the login details are incorrect).

First thing we would want to do is secure our passwords, right now they are exposed (even if they are in the database), this is why we want to use `bcryptjs`.

![alt text](.guides/img/TokenBasedAuthentication.png)

if we re-visit the **JWT Flow** We will remember that once we want to attempt to login we want to **authenticate** and give **authorization** to generate a token.

so first, lets **encrypt** and create an **authentication** mechanic in our server.

