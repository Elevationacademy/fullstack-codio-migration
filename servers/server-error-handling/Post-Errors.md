# Duplicated resources
A classical error, especially when trying to create a new resource, is that the resource already exist. 
In our case we might add a user with a username that is already being used.
In that case we would not want to allow the creation of a duplicated username.
In order to avoud this, we might want to check first that the new username is not in use in our users list:
```js
app.post('/users', function (req, res) {
    const newUser = req.body
    const userName = newUser.username
    let doesExist = users.some(w => w.username === userName)
    if (doesExist) {
        res.status(409).send({ "Error": `User ${userName} already exist` })
        return
    }
    users.push(newUser)
    res.status(201).end()
})
```

Another thing that might happen, is that the username will be not valid. In our case we will assume that the username can contain only letters. In the username contains invalid characters such as numbers or special characters we will want to return a relevant start code, and a clear error message.

Try to handle these scenarios, if you haven't already!
And move to the next page to see our suggestion. 