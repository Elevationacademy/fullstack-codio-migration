JWTs consist of three parts separated by dots (.), which are:
- Header
- Payload
- Signature

Therefore, a JWT typically looks like the following.

`xxxxx.yyyyy.zzzzz`

![](https://supertokens.com/static/b0172cabbcd583dd4ed222bdb83fc51a/9af93/jwt-structure.png)


## Header
The header typically consists of two parts: the type of the token, which is **JWT**, and the hashing algorithm such as **HMAC SHA256** or **RSA**. This part is `Base64` encoded and then added to the **JWT** token.

you can read up more about these algorithms during your free time.


```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
## Payload
The second part of the token is the payload, which contains the **claims**. Claims are statements about an entity (typically, the user) and additional **metadata**. This part is `Base64` encoded and then added to the **JWT** token.

```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```
## Signature
To create the signature part you have to take the **encoded header**, the **encoded payload**, a **secret**, the algorithm specified in the header, and sign that.

For example if you want to use the **HMAC SHA256** algorithm, the signature will be created in the following way. The signature is used to verify that the sender of the **JWT** is who it says it is and to ensure that the message wasn't changed in the way.

```json
HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  secret)

```

