Dependencies, aka "Dependency Injection", is a **FastAPI** mechanism that allows you to inject functionality in-line, while keeping the syntax clean and readable. The injected, or embedded, functionality will exist in the same context as it’s called from, allowing it to access all parameters.

A decorator is simply a Python function, and you use it in the code, using the `Depends({function_name})` syntax, e.g. `Depends(security)`. During runtime, the Python interpreter injects the function and executes it ‘in-place’.

It allows you to write reusable components that you can easily embed in different parts of the code, and in this instance, as part of the entry point of the ‘path operation function’ (the function that implements the FastAPI path decorator).

The below example shows how to use a decorator to set default values for query parameters. We define an `async` function called `common_parameters()` which is invoked in each path operation function.

```Python
from typing import Union
from fastapi import Depends, FastAPI
import uvicorn

app = FastAPI()

async def common_parameters(q: Union[str, None] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
```

We will use dependencies to add ‘security’ functionality to our API endpoints, controlling which endpoints require authentication and which do not.
