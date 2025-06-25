Another way to control access is through the use of ‘middlewares’. Middlewares work with every request before it is processed by any specific path operation, and also with every response before returning it.

As FastAPI is lacking functionality and documentation for middleware-based authentication, the `fastapi_auth_middleware` package comes to the rescue. It’s a simple FastAPI middleware implementation. Let’s go ahead and install it and learn how to use it.

```Python
pip install fastapi_auth_middleware
```


|||important
## Note 
You will need Python >=3.8
|||

Now, let’s see how this works. Let’s create the ‘authorization’ function, which we’ll attach to the FastAPI server as a middleware in just a moment. Note that the function receives a `string` variable holding the token, basic or jwt, so the `auth_header` below will only contain the token itself)

```
def verify_authorization_header(auth_header: str) -> Tuple[List[str], BaseUser]:
```

Don’t forget to add the right imports at the top of the file:
```Python
from starlette.authentication import requires
from fastapi_auth_middleware import AuthMiddleware, FastAPIUser
```

Further down the file you’ll notice that the function returns two variables, one is a list of `scopes`, and the other is the `user` object.
```Python
    return scopes, user
```

The goal here is that we can authenticate using the `auth_header` parameter, and authorize (see explanation later in this course), using the `scope` variable. Below is the complete example of the ‘authorization’ function.

```Python
# Takes a string that will look like 'Bearer eyJhbGc...'
def verify_authorization_header(auth_header: str) -> Tuple[List[str], BaseUser]: # Returns a Tuple of a List of scopes (string) and a BaseUser
    user = FastAPIUser(first_name="Code", last_name="Specialist", user_id=1)  # Usually you would decode the JWT here and verify its signature to extract the 'sub'
    scopes = []  # You could for instance use the scopes provided in the JWT or request them by looking up the scopes with the 'sub' somewhere
    return scopes, user
```

We then add this custom middleware to the FastAPI server by adding the following line right after setting the app.
```Python
app = FastAPI()
app.add_middleware(AuthMiddleware, verify_header=verify_authorization_header)
```

Then, we can restrict access to the endpoints based on scopes in the following way using the `@require` decorator. This instruction tells FastAPI to look for the scope ‘admin’ to be able to execute it, otherwise, a 401 authorization exception will be raised.
```Python
@app.get('/home')  # Sample endpoint (secured)
@requires("admin")  # Requires the role 'admin' (Will succeed)
def home(request: Request):
    return request.user
```

### Full application code
Below is a full working code for an app with middle-ware authentication using the ‘admin’ scope for securing the `/` endpoint.

```Python
from typing import Tuple, List
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.authentication import requires
from fastapi_auth_middleware import AuthMiddleware, FastAPIUser

# The method you have to provide
def verify_authorization_header(auth_header: str) -> Tuple[List[str], FastAPIUser]:
    user = FastAPIUser(first_name="Code", last_name="Specialist", user_id=1)  # Usually you would decode the JWT here and verify its signature to extract the 'sub'
    scopes = ["admin"]  # You could for instance use the scopes provided in the JWT or request them by looking up the scopes with the 'sub' somewhere
    return scopes, user

app = FastAPI()
app.add_middleware(AuthMiddleware, verify_header=verify_authorization_header)  # Add the middleware with your verification method to the whole application

@app.get('/')  # Sample endpoint (secured)
@requires("admin")
def home(request: Request):
    return request.user

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8080)  # Starts the uvicorn ASGI
```
