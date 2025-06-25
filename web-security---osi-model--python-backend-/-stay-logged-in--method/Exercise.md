## Add Cookie support to previous project

Add support for setting and getting the cookie information based on the learnings from this chapter. You will need to take the code in this chapter and integrate it with the code from the last exercise (*Authorization token*).

Pay attention to what needs to be replaced in the code, especially in the `/users/me` endpoint and `get_current_user()` function. Good luck.


<details>
  <summary>
     Solution
  </summary>

```Python
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status, Response, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security.utils import get_authorization_scheme_param
from pydantic import BaseModel
import uvicorn

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()

def fake_hash_password(password: str):
    return "fakehashed" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

class UserInDB(User):
    hashed_password: str

def get_user(db, username: str):
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

def fake_decode_token(token):
    # This doesn't provide any security at all
    # Check the next version
    user = get_user(fake_users_db, token)
    return user

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

    return fake_decode_token(param)

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

@app.post("/token")
async def login(response: Response, form_data: OAuth2PasswordRequestForm = Depends()):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    response.set_cookie(key="Authorization", value="Bearer %s" % user.username, httponly=True)
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user

if __name__ == "__main__":
    uvicorn.run("exercise_1_solution:app", host="127.0.0.1", port=8000, log_level="info")
```

</details>