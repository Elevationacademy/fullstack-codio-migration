Let's take care of these errors:

```js
app.post('/users', function (req, res) {
    const newUser = req.body
    const userName = newUser.username
    if (!userName.match(/^[a-z]+$/i)) {
        res.status(400).send({ "Error": `${userName} is not a valid name` })
        return
    }
    let doesExist = users.some(w => w.username === userName)
    if (doesExist) {
        res.status(409).send({ "Error": `User ${userName} already exist` })
        return
    }
    users.push(newUser)
    res.status(201).end()
})
```

This is great! Now that every erroneous scenario has a specific status code and detailed message it will be easier for our API user to debug and understand how to work with the APi.

<hr>

In this example we implemented all the logic inside the handler. But now let's look at a different design.
In this new design there is a users module that will be in charge of the users logic, such as adding a new user, deleting a user and so on.

The skeleton of the users module will look something like that:

```js
const usersModule = function(){

    const addUser = function(newUser){}

    const deleteUser = function(username){}

    const getAll = function(){}

    return {
        add: addUser,
        delete: deleteUser,
        getAll: getAll
    }
} 
```

So what happens now, with the errors?
Can we still have the same code?

Let's look at the post method in our server file. Now it will look like that:

```js
const users = require('./users')

app.post('/users', function (req, res) {
    const newUser = req.body
    users.add(newUser)
    res.status(201).end()
})
```

How will we be able to understand which error occurred?

If we copy the code, from the server to the users model it can look like this:

```js
    const addUser = function(newUser, res){
        const newUser = req.body
        const userName = newUser.username
        if (!userName.match(/^[a-z]+$/i)) {
            res.status(400).send({ "Error": `${userName} is not a valid name` })
        }
        let doesExist = users.some(w => w.username === userName)
        if (doesExist) {
          res.status(409).send({ "Error": `User ${userName} already exist` })
          return
        }
        users.push(newUser)
    }
```

In the previous solution we returned the relevant response, but now that this logic is in a module, it does not make much sense that it will know about the server, and status code and such matters.

Can you think of a solution?