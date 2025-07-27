Now let's look again at our Flow.

![alt text](.guides/img/TokenBasedAuthentication.png)

We see that we finished **Step 2**, Let's move on to **Step 3**!

In order to generate a token, we need to use the **JWT**'s library. 

We can read up more about the [JWT Library here.](https://www.npmjs.com/package/jsonwebtoken)

## JWT Sign method
We use the `sign` method to generate a JWT string.

It will look something like this:
```js
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjEyMzQsImVtYWlsIjoidXNlckBleGFtcGxlLmNvbSIsImlhdCI6MTYxNjQ2MTY0OCwiZXhwIjoxNjE2NDY1MjQ4fQ.rWZbItYK1ajCTHkxmkEfp8WJTWjwjF9I9KZg2_RjK5c
```

The `sign` method is built like this.
```js
jwt.sign(payload, secretOrPrivateKey, [options, callback])
```

- **payload :**  This is the data that will be encoded as a **JWT**. The payload is typically a `JSON` object containing some data that you want to include in the **JWT**, such as user `ID`, `name`, `email`, or any other relevant data.

- **secretOrPrivateKey :** This is a shared `secret` or `private key` between the issuer of the **JWT** (usually a server) and the recipient of the **JWT** (usually a client). The secret key is used to generate the digital signature and to verify the authenticity of the **JWT**.


## JWT Verify method

once we have a generated token, we will be sending it to the client and demanding he will have it on every request he makes to our server if he wants to get resources he has access to.

The `verify` method is used like this:

```js
jwt.verify(token, secretOrPublicKey, [options, callback])
```
- **token :**  the received **JWT** token from the client. 
- **secretOrPublicKey :** This is a shared `secret` or `private key` between the issuer of the **JWT** (usually a server) and the recipient of the **JWT** (usually a client). The secret key is used to generate the digital signature and to verify the authenticity of the **JWT**.

