# Exercise: Variables, Identifiers and Operators

## Exercise 1
-
Determine whether the following are truthy or falsey:

  

-   `(5 > 2) && false`
-   `!("knife" === "sword")`
-   `(1 < 2) || (-1 > -1) || !false`
-   `""`
-   `(31 % 5) == "1"`
-   `!!true`
-   `"5th Avenue" != "5th Avenue"`
-   `52 !== "52"`
-   `(undefined || null)`

  

Think first before you test it out in code. **Ask** if you don't understand why certain results are what they are.

## Exercise 2
-
Bit of a mind-twister: what are the values of a, b, and c in the end?

  
```js
let a = 3
let c = 0
let b = a
b = a
c = a
b = c
a = b
```


