## 1. Fix the code
Fix the issues in this code based on the learning from this class.
### Hint
Use the code in this chapter to help you figure out what needs fixing.

```Python
from typing import Tuple, List
import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.authentication import requires
from fastapi_auth_middleware import AuthMiddleware, FastAPIUser


def verify_authorization_header(auth_header: str) -> Tuple[List[str], FastAPIUser]:
    user = FastAPIUser(first_name="Code", last_name="Specialist", user_id=1)  # Usually you would decode the JWT here and verify its signature to extract the 'sub'
    scopes = []  
    return scopes, user

app = FastAPI()

# Sample endpoint (secured)
@app.get('/')  
def home(request: Request):
    return request.user

if __name__ == '__main__':
    uvicorn.run('exercise_1:app', host="127.0.0.1", port=8000)  # Starts the uvicorn ASGI
```

<details>
<summary>Solution</summary>
<div> 

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
    uvicorn.run('exercise_1:app', host="127.0.0.1", port=8000)  # Starts the uvicorn ASGI
```

</div>
</details>

## 2. Add a new endpoint and a new scope

Extend the previous code and add another endpoint called `/profile`. This endpoint requires a `standard` role (e.g. scope). Hard code-it for now. We’ll extend it in the next exercise. Make sure the new endpoint returns the user (which should be created by the middleware, similar to how it’s implemented currently).

<details>
<summary>Solution</summary>
<div> 

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
    scopes = ["standard"]  # You could for instance use the scopes provided in the JWT or request them by looking up the scopes with the 'sub' somewhere
    return scopes, user

app = FastAPI()
app.add_middleware(AuthMiddleware, verify_header=verify_authorization_header)  # Add the middleware with your verification method to the whole application

@app.get('/')  # Sample endpoint (secured)
@requires("admin")
def home(request: Request):
    return request.user

@app.get('/profile')  # Sample endpoint (secured)
@requires("standard")
def home(request: Request):
    return request.user

if __name__ == '__main__':
    uvicorn.run('exercise_2_solution:app', host="127.0.0.1", port=8000)  # Starts the uvicorn ASGI
```

</div>
</details>