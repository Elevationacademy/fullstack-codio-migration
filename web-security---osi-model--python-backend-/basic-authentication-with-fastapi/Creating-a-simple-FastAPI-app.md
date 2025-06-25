In this class we will base our learning on a simple FastAPI app, and we’ll use the `uvicorn` web server as the baseline for our event loop and await/async mechanism, providing high-performance networking for Python.

We'll install the relevant packages:
```Python
pip install fastapi
pip install "uvicorn[standard]"
```

Let’s create the app by using the following code. Here we set up a simple web server with single RestAPI endpoint `/profile` which returns a simple JSON `{"name": "John Smith"}`. The server will use `localhost` with port 8000.

```Python
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/profile")
async def main():
    return {"name": "John Smith"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
```
