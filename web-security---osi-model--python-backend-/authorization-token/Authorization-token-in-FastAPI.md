In FastAPI we will use these two classes to enable the entire security flow with a standard login form, which accepts *username* and *password* fields:
- `OAuth2PasswordRequestForm` is the Class dependency we would use in our `/login` endpoint. It will allow us to access the fields *username* and *password* from a standard dictionary
- `OAuth2PasswordBearer` defines an token authentication scheme, which means that using this class, we will define the endpoint that will be used to generate the ‘Bearer’ token, and in return, will require us to adhere to a specific JSON format as the returned ‘token’

### Using the `OAuth2PasswordBearer` Class
In our program, we will first import this Class, and then define the endpoint for generating the token.

```Python
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

Then, we will add the `oauth2_scheme` dependency to all endpoints we wish to control using the token authentication, like so:

```Python
async def get_current_user(token: str = Depends(oauth2_scheme)):
```

And lastly, we will return the token from the defined `/token` endpoint, while adhering the required JSON structure. We must include the following two keys in the response at the end of the `/token` endpoint:

```Python
@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
…
token = create_token()
return {"access_token": token, "token_type": "bearer"}
```
