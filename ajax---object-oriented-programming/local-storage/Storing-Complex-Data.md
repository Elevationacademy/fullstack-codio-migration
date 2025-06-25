
We said that LS works like an elaborate object, but if you try to do something like this (in Chrome, at least):
```
localStorage.personalData = {
  averageTimeOnSite: {unit: "hr", amt: 9},
  probabilityOfFriends: 0.02,
  commonKeywords: ["salsa for one", "1 vs. none Chess"]
}
```
  

And then you try to extract that using localStorage.personalData, you might see this as a result:
```
"[object Object]"
```
  

Good old [object Object], always showing up where we don't want it. Anyway.

  

Thankfully, the solve is pretty simple. The expectation is that you store your data as a _string_, no matter what the data is (even an object as complex as the personalData key above.)

  

We can use JS' built-in JSON object, and take advantage of its stringify method, like so:
```
localStorage.personalData = JSON.stringify({
  averageTimeOnSite: {unit: "hr", amt: 9},
  probabilityOfFriends: 0.02,
  commonKeywords: ["salsa for one", "1 vs. none Chess"]
})
```
  

Note that we can use JSON.stringify anywhere, not just with Local Storage:
```
let x = {name: "Shoobert"}
x = JSON.stringify(x)
console.log(x) //prints a string-version of the object
```
  

The problem with storing things in LS as a string, though, is that then when we access them we cannot use them as objects. In other words, this won't work:

  
```
let userStuff = localStorage.personalData //the object we stored earlier

console.log(userStuff.probabilityOfFriends) //prints undefined
```
  

It doesn't work because localStorage.personalData returns a string - and strings don't have a probabilityOfFriends property.

  

However, we _can_ extract the object using another popular method of JSON called parse:
```
let userStuff = JSON.parse(localStorage.personalData)

console.log(userStuff.probabilityOfFriends) //prints 0.02
```
  

Now our userStuff variable is an actual object, and not a string - and that wraps up our LS cycle.