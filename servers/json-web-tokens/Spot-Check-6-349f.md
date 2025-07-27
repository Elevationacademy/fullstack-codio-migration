Let's create a **middleware** for token authentication.
Then let's add this middleware to our relevant routes, this middleware will decide if we are allowed to take a resource from the `soundsAPI`.


<details>
  <summary>
     Solution
  </summary>

Let's start by creating a middleware.
```js
function authenticateToken(req, res, next) {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];
  if (!token) {
    return res.sendStatus(401);
  }

  jwt.verify(token, secretKey, (err, user) => {
    if (err) {
      return res.sendStatus(401);
    }

    req.user = user;
    next();
  });
}
```




Now that we created a middleware, lets add it to the `/animals/:animal` route.
It should look like this

```js
router.get('/animals', authenticateToken,(req, res) => {
  try {
    const user = findUser(req.user.id,req.user.username)
    console.log(user)
    const favAnimal = {"animal":user.animal}
    console.log(favAnimal)
    res.send(favAnimal);
  } catch (error) {
    console.log(error)
    res.status(401).send({ message: 'Invalid token' });
  }
});

```

</details>