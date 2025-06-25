There are many status codes we can return.

But the first level is to understand the general purpose of each family of status codes.

Each status code has three digits, the first digit will indicate the general purpose of the status code.



## 1XX Informational Responses



## 2XX Success

This means generally that the requests has been received, understood and accepted, in short - all is good.



## 3XX Redirection



## 4XX Client errors

There is an error in the request that has been caused by the client.



## 5XX Server errors

The server did not manage to fulfil the request.





The three most important ones are the ones that tells us if the request is ok, and if not who's fault is it: 2XX, 4XX, 5XX.

With the status method we can change the default 200 status:
```
app.get("/items/:id", (req, res)=>{
    if (!req.params.id){
        return res.status(404).send("Item not found")
    } else {
        return res.send("ID OK") // will return status 200, the default one
    }
})
```