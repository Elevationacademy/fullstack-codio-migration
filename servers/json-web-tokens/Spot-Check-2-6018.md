Now let's add Authentication in our code, anyone who wants to try to **Login** will have to get verified using the `bcryptjs` library.

Adjust the code in the `/login` route.



<details>
  <summary>
     Solution
  </summary>

In order to keep it clean code, we will have multiple helper functions.

```js
function authenticateUser(username, password) {
  const user = users.find(u => u.username === username);
  if (!user) {
    return null;
  }
  const isPasswordValid = bcrypt.compareSync(password, user.password);
  if (!isPasswordValid) {
    return null;
  }
  return { id: user.id, username: user.username };
}
```

Now we will edit the `/login` route and return a fitting message if he is a valid user and authenticated successfully.

```js
router.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = authenticateUser(username, password);
  if (!user) {
    return res.status(401).send({ message: 'Invalid username or password' });
  }
  res.send({message:"user has successfully logged in"});
});
```

</details>