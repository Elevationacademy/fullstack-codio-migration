## Email Validator

Create a validator function that will check if the given String is an email.

Assumptions: 
- All emails will end in ``.com``
- Email may contain only letters

Example:
```js
emailValidator(“cat@meow.com”) // will return True
emailValidator(“bad1npuT!@gmail.com” // will return false
emailValidator(“meow@gmail.net”) // will return false
```

Here is some code to test your answers:

```js
const email1 = "cat@meow.com"
const email2 = "bad1npuT!@gmail.com"
const email3 = "meow@gmail.net"

const emailValidator = function(str){
  /**
   * returns true if email prefix and domain is made strictly out of letters , the email must end in .com
   * HINT : doesnt have to be a big regex expression use the methods from RegExp
   */
}

console.log(emailValidator(email1)) //return true
console.log(emailValidator(email2)) //return true
console.log(emailValidator(email3)) //return false
```