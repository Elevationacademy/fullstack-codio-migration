# Intro

After a user successfully authorizes themselves, they can access a single resource or page. But what if they want to access multiple pages? Or come back to the same page a few times over the next few days? Do they need to login each time? No they don’t. They just need to store the token on the client side.

The next question we need to answer is where do we store? We have a few options, but really only one really makes sense.

- **HTML5 Web Storage (localStorage or sessionStorage)**. We might be tempted to store the token in localstorage, but as you can imagine, this is not safe, as Web Storage (localStorage/sessionStorage) is accessible through JavaScript on the same domain. This means that any JavaScript running on your site will have access to web storage, and because of this can be vulnerable to cross-site scripting (XSS) attacks.
- **Cookie**. The next usual suspect are the cookies, and cookies is the best option, and especially if used with the `HttpOnly` cookie flag, are not accessible through JavaScript, and are immune to XSS. You can also set the `Secure` cookie flag to guarantee the cookie is only sent over HTTPS