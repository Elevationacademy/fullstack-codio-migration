Now that we have understood the problem we can handle it.
We all heard about throwing and catching errors, and when we here the term **Error Handling** the try catch technique immediately comes to mind, but in this case it will not help us. The reason is that no error is being thrown so we can’t catch it.
Actually, this error can be easily handled with an if condition that will will check the return value:
```js
app.delete('/users/:username', function (req, res) {
    let username = req.params.username
    let userIndex = users.findIndex(user => user.username === username)

    if (userIndex === -1) {
        res.status(404).send({ "Error": `User ${username} does not exist` })
    } else {
        users.splice(userIndex, 1)
        res.status(204).end()
    }
})
```
Here we take care of the error by discovering it and returning a relevant `404` status code and a detailed message.
