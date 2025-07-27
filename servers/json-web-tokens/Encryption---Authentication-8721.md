
## Bcryptjs Library

This library offers a single way encrpytion of any string, this way we can secure our code without worrying that someone can encrypt it.

So let's encrypt our passwords.

## Encrpytion of passwords

Let's import the bcryptjs library by adding this code in the top of the file.

```js
const bcrypt = require('bcryptjs');
```

### Salt

In `bcryptjs`, **salt** is a random Salt is a random string value that is added to a password before hashing to make each password hash unique. it is used to add an extra layer of security to the password hashing process. The salt value is generated randomly and is unique to each password that is hashed.

We will use **bcrypt**'s `genSaltSync` method to generate a salt.

Let's add in our code the following:

```js
//we generate the salt for the password
const saltRounds = 10;
const salt = bcrypt.genSaltSync(saltRounds);
```


|||info
## SaltRounds

salt rounds refer to the number of times the hashing algorithm iterates through the password and salt combination. Each iteration takes some time, making the hashing process slower and more secure against brute-force attacks.
|||

### Hashing

In order to hash a value, we call the **bcrypt**'s `hashSync` method, which receives a `string` and a `salt`.

For example: 

```js
bcrypt.hashSync("secertpassword",bcrypt.genSaltSync(10))
```


### Authentication

In order to make sure that the data (password) we receive from the client is truly correct, We want to compare it to our encrypted password.

we can use `bcrypt.compareSync`:
```js
bcrypt.compareSync(userPassword,password)
```