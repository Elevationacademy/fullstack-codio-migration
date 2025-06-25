In this lesson we will work with a simple server that manges users.
For simplification, the server will use a hard coded array of users:

```js
const users = [
    { username: "bonz", name: "Bony", country: "Nepal", age: 21 },
    { username: "marv", name: "Marvin", country: "Arizona", age: 33 },
    { username: "luc", name: "Lucil", country: "Singapore", age: 47 },
    { username: "marc", name: "Marco", country: "Greece", age: 63 },
    { username: "kev", name: "Kevin", country: "Italy", age: 31 }
]
```
We will identify each user by it's unique username.

Our API will support simple CRUD operations:
1. Getting all users
1. Adding a user
1. Deleting a user

|||
# Task
Create a simple server using express library.
Add the users array, and you are ready to go!
|||

Getting all users is very simple:
```js
app.get('/users', function (req, res) {
    res.send(users)
})
```

Deleting a user can look like this:
```js
app.delete('/users/:username', function (req, res) {
    let username = req.params.username
    let userIndex = users.findIndex(user => user.username === username)
    users.splice(userIndex, 1)
    res.status(204).end()
})
```

We find the user index in our `users array` according to the username path parameter. Next, we use splice to remove it from the array. Finally, we return a 204 status code, since the request was successful and we have no data to return. 

So far, so good. This will work well in a perfect world.
But in real life we might come across some problems.

Can you think of any errors or scenarios that might be problematic?


|||create
## Task

Try to write down at least 1 possible scenario where the code we have written will not work in the expected way.
|||