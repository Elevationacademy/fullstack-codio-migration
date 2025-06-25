## Not Found 

When we try to delete a user, the user might not be in our list of users. What will happen if we try to delete a user with username 'koko'?

You can check the array of users or believe us that there is no such user. If we look at the code we might spot a problem.
Can you tell what is the problem? 

Here is the code for reference:
```js
app.delete('/users/:username', function (req, res) {
    let username = req.params.username
    let userIndex = users.findIndex(user => user.username === username)
    users.splice(userIndex, 1)
    res.status(204).end()
})
```

Well, let's investigate!
First we get the username from the path - No problem here.
Next, we call `findIndex` trying to find the relevant index, but since there is no such user we will not get an index from the array.
What will we get back? what will be the value of `userIndex` variable?
null? undefined?
will the program throw an error?


|||debugging
## Discovering Errors

Maybe you know the answer, but if not there are (at least) 2 ways to approach this challenge:
1. Read the documentation (of `findIndex` in our case)
1. Debug

We recommend that you will debug and find out what happens
|||

So now you know what is the return value, is it over?
Not really. We will continue to the next line:
```js
users.splice(userIndex, 1)
```

What will happen now?
You know what to do :)

Did you debugged and manage to understand what happens in the code?


<details>
  <summary>
     Check the explanation here
  </summary>
    <code>findIndex</code> will return -1, and then we will call splice with -1 like this:
    <code>users.splice(-1, 1)</code>
    This will cause the last user in the array to be deleted. If you are not sure why, read about the use of negative indexes in the <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice#syntax">documentation</a>
</details>

