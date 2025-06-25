## Add a ‘register’ endpoint

Add a new capability to the app developed in this chapter. Add a `/users` endpoint with the `@post` method, which accepts a *username* and *password*, either as standard URL parameter or form fields, and creates a new *db* entry (in the `users_db` dictionary.

The db entry will include the *username* and the hashed *password*. You can hash the password using the `pwd_context.hash(password)` statement. You need to be able to test that you can access the protected `/profile` endpoint by entering both the existing *username/password* *johnsmith/swordfish* and both the pair you add when you use the `/post` endpoint.


<details>
  <summary>
     Solution
  </summary>

```Python
from typing import Union
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from passlib.context import CryptContext
import uvicorn
from pydantic import BaseModel

app = FastAPI()
security = HTTPBasic()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Fake user db containing a single user with a hashed password
users_db = {
    "johnsmith": {
        "username": "johnsmith",
        "full_name": "John Smith",
        "email": "johnsmith@example.com",
        "hashed_password": "$2a$12$CgpQ6EX4ukkKmTROa245OeplIB2kraEV6wuPJAM7G1gqX.Im.KBQC"
    }
}

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None

# Function that authenticates the user
def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    is_authorized = True

    # First check if the username exists in the users db and if the password was provided
    if credentials.username not in users_db or not credentials.password:
        is_authorized = False

    # Secondly, check if the provided password matches the stored hashed password
    elif not pwd_context.verify(credentials.password, users_db[credentials.username]["hashed_password"]):
        is_authorized = False

    if not is_authorized:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    # Populate a 'User' object with the database results, except for the hashed password
    return User(**users_db[credentials.username])

@app.get("/profile")
async def main(user: User = Depends(authenticate_user)):
    return user

@app.post("/users")
async def create_user(username: str, password: str):
     users_db[username] = {
        "username": username,
        "hashed_password": pwd_context.hash(password)
     }

     print(users_db[username]["hashed_password"])

     return {"username": username}

if __name__ == "__main__":
    uvicorn.run("exercise_1_solution:app", host="127.0.0.1", port=8000, log_level="info")
```

</details>