
# Validating credentials and raising exceptions
Now that we know how to add basic authentication, let’s add a validation check to make sure that only the right *username* and *password* gets to execute the API endpoint.

Here we use a new dependency called `get_current_username()` which includes the `HTTPBasic()` dependency in its definition. By doing so, we will leverage the built-in dependency to check for the existence of the *username* and *password* parameters, and inside the `get_current_username()` dependency, we will validate if these two parameters match our existing credentials.

Here we introduce a new class `HTTPException`, which will be used to raise the standard API exception, and the `status` module, to use an enum of defined statuses.

**Note:**
- In a production system the *username* and *password* parameters are stored in a database, and the password is encrypted (more on that later)

```Python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn

app = FastAPI()
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if not (credentials.username == "johnsmith") or not (credentials.password == "swordfish"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    
    return credentials.username

@app.get("/profile")
async def main(username: str = Depends(get_current_username)):
    return {"username": username}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
```
