Now that we know how to generate a `token`, let's adjust our `/login` route to return a generated `token`.

for now we will return the token in the body of the response


<details>
  <summary>
     Solution
  </summary>


First thing we want to do is add a `secert` key that only the server and client know.
```js
const secretKey = 'my_secret_key';
```

Now that we have a secret key, we can make 
```js
function generateAccessToken(user) {
  return jwt.sign(user, secretKey);
}
```


|||important
## Generated Token Data

Notice in here we pass a `user`.
`user` is an object that contains details about the user. 
depending on what we want to save in our token it can change.

For example, if we want to save who is this user and what shopping cart he has it will look like this
```js
const user = {id:1, username:"ameerj" , shoppingCart: ['cookies', 'cat treats']
}
```
|||



So now we will adjust the `/login` route to be the following:

```js
router.post('/login', (req, res) => {
  const { username, password } = req.body;
  const user = authenticateUser(username, password);
  if (!user) {
    return res.status(401).send({ message: 'Invalid username or password' });
  }
  const accessToken = generateAccessToken(user);
  res.send({ accessToken });
});
```


</details>

</br>
With this, we finished **Step 3** in our diagram.