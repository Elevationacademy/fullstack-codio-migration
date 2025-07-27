Modify our code in the `users.js` file in ways that we secure our passwords with `bcryptjs`.

**Please use forEach**


<details>
  <summary>
     Solution
  </summary>

```js
const bcrypt = require('bcryptjs')

//we generate the salt for the password
const saltRounds = 10;
const salt = bcrypt.genSaltSync(saltRounds);

//rest of code

users.forEach(user => {
  const hashedPassword = bcrypt.hashSync(user.password, salt);
  user.password = hashedPassword;
});
  
```

</details>