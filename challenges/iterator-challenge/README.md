# The Challenge

Create an **object** which implements the **iterable protocol** so that when we iterate over the element with a `for of` loop it will print **only** the even numbers.
The object should contain 10 random numbers, you can initials them hard coded at first.


So if your obejct is called `myObject`, and it contains the numbers ``[11,13,14,66,67,69,234,456,2,1]``, 

then following code:
```
const myObject = {
// your code here
}

for (let x of myObject) {
    console.log(x)
}
```

should print:
```
14
66
234
456
2
```



Here is a [link](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols) to start you off.

Good Luck!