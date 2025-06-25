## URL Validator

Create a validator function that will check if the given String is a URL.

Assumptions: 
- All **URL's** Start with `www.`
- All **URL's** End with `.com`

Example:
```js
urlValidator(“www.elevation.com”) // will return True
urlValidator(“www.elevation.ac.il” // will return false
urlValidator(“elevation.com”) // will return false
```

Here is some code to test your answers:

```js
const firstURL = "www.workingurl.com"
const secondURL = "iamabadurl.com"
const thirdURL = "www.doireallywork.net"

const urlValidator = function(str){
  /**
   * returns true if URL starts with www. , the URL must end in .com
   * HINT : doesnt have to be a big regex expression use the methods from RegExp
   */
}

console.log(urlValidator(firstURL)) //return true
console.log(urlValidator(secondURL)) //return true
console.log(urlValidator(thirdURL)) //return false
```