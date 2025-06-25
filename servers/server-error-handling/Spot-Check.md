Try to think what errors might happen in a post request, when we want to create a new user.

You can use the following implementation to help you think:

```js 
app.post('/users', function (req, res) {
    const newUser = req.body
    users.push(newUser)
    res.status(201).end()
})
```

Try to think of at least 1 error and handle it.

