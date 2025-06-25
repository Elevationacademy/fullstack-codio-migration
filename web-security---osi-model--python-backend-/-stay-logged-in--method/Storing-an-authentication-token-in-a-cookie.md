When storing the token in the cookie, we need to take the following strategy:
- Set the cookie straight after authentication. 
- Retrieve the cookie during user validation

### Setting the cookie
Right after the user authenticates, as part of the `/token` function, we will set a cookie in the `response` object using the `response.set_cookie(key="Authentication", value="Bearer %s" % user.username)` syntax.

**Notes:**
- We’re still returning the standard bearer token syntax in JSON format at the end of the endpoint function
- We need to add a `response: Response` variable as the first parameter in the endpoint endpoint function parameter list (and import the `fastapi.Response` class as well)

### Retrieving the cookie during user validation
When validating the user, we will need to keep the current header token authentication mechanism, and add a fallback mechanism based on cookies. Now FastAPI doesn’t provide an out-of-the-box and easy to use dependency which includes both header tokens and cookie tokens, so we will have to develop our own ‘combined’ method.

For that, we will need to ditch the use of the `OAuth2PasswordBearer` dependency, and add specific code in the `get_current_user()` function.

**Note the following:**
- We add the `request: Request` variable as the first function parameter (we need to import it into the code remember?)
- We try and find an ‘Authorization’ key in the ‘Authorization’ header first
- If we can’t find, we will look for the same key in a cookie
- If both fail, we will raise an authorization error

```Python
async def get_current_user(request: Request):
    header_authorization: str = request.headers.get("Authorization")
    cookie_authorization: str = request.cookies.get("Authorization")

    header_scheme, header_param = get_authorization_scheme_param(header_authorization)
    cookie_scheme, cookie_param = get_authorization_scheme_param(cookie_authorization)

    if header_scheme.lower() == "bearer":
        authorization = True
        scheme = header_scheme
        param = header_param

    elif cookie_scheme.lower() == "bearer":
        authorization = True
        scheme = cookie_scheme
        param = cookie_param

    else:
        authorization = False

    if not authorization or scheme.lower() != "bearer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated"
        )
   …
```
