## Regex Dynamic Searcher

Create a function SearchMatchingRegex(string) that will look through an array of Regex’s for a matching Regex for the string. It will return true if it found a matching Regex or false if it failed to.

Example:
```js
regexArr = [/at/,/a/,/a$/,^b]

SearchMatchingRegex(‘cat’) //will return true
SearchMatchingRegex(‘bike’) //will return true
SearchMatchingRegex(‘mouse’) //will return false 
```

Here is some code to test your answers:

```js
const regexArr = [/a/, /b/, /^d/, /e$/]
const str = "Bike"
const str1 = "the room is on fire"
const str2 = "Fergalicious"
const str3 = "Fox in sheep clothing"
const searchMatchingRegex = function (str) {
  /**
   * should return true if one match is found with the array
   */
}

console.log(searchMatchingRegex(str)) //return true (contains b)
console.log(searchMatchingRegex(str1)) //return true (ends with e)
console.log(searchMatchingRegex(str2)) //return true (contains a)
console.log(searchMatchingRegex(str3)) //return false
```