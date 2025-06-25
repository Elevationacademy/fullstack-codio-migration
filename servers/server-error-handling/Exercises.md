# Ex 1
What happens if someone tries to add the following user?

```js
{ 
  username: "lil", 
  country: "Greece", 
  age: "forty" 
}
```

Look! the name field is missing.
The age property is a string and not a number.

Handle these cases, and any other invalid data that you might receive. 

# Ex2
Add a route to get a specific user by its username.
For example `/users/marv` will get the details of a user with a 'marv' username.

Think what error might occur in this request and handle them.
Make sure to return a relevant status code and error message.