In case of multiple errors we can throw a relevant error for each case.

So the code can look something like that:

```js
    const addUser = function(newUser){
        const newUser = req.body
        const userName = newUser.username
        if (!userName.match(/^[a-z]+$/i)) {
            throw new TypeError() 
        }
        let doesExist = users.some(w => w.username === userName)
        if (doesExist) {
            throw new SyntaxError()
        }
        users.push(newUser) 
    }
```

Note that for the case where the the username is not valid we throw a `TypeError` , and for the case where the usernmae already exist we throw `SyntaxError`.
We can try to find which js builtin errors that might be closest to ours - but do they really describe the errors?  

If we are honest than, not really.

How can we solve this issue?

Custom Errors to the rescue!!

We can create our own errors like this:

```js
class InvalidUsernameError extends Error {}

class DuplicatedResourceError extends Error {}

module.exports = {InvalidUsernameError, DuplicatedResourceError}
```

Now we can import them and throw relevant errors in the user module:

```js
    const addUser = function(newUser){
        const userName = newUser.username
        if (!userName.match(/^[a-z]+$/i)) {
            throw new InvalidUsernameError() 
        }
        let doesExist = users.some(w => w.username === userName)
        if (doesExist) {
            throw new DuplicatedResourceError()
        }
        users.push(newUser) 
    }
```

and of course we will have to update the handler in the server:
```js
app.post('/users', function (req, res) {
    const newUser = req.body
    const username = newUser.username
    try{
        users.add(newUser)
        res.status(201).end()
    } catch (error) {
        if (error instanceof InvalidUsernameError){
            res.status(400).send({ "Error": `${username} is not a valid name` })
        } else if (error instanceof DuplicatedResourceError){
            res.status(409).send({ "Error": `User ${username} already exist` })
        }
    }
})
```