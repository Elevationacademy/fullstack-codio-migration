# Exercises

Functions are incredibly useful, and really are the cornerstone of good programming. So make sure you understand them and are able to work with them fluently!

----------------------
## Exercise 1
-
Write a function called `isEven` that accepts a number as a parameter and checks if the number is even or not. Return `true` if it is even or `false` if it is odd. Don't Google this one ;) Use modulo `%`


## Exercise 2
-
Write a function that takes in an array of numbers.

The function should loop through the numbers and (using the function from Exercise 1) print out the odd numbers.


## Exercise 3
-
Write a JavaScript function that accepts two parameters: one being an array of integers, and the other being a number. The function should return `true` or `false` depending on whether the number exists in the array.

  

**Hint:** You should loop through the array, and for each item in the array, check if it equals the number that was passed.

  

`checkExists([1, 2, 3], 2)` - should return **true**

`checkExists([1, 2, 3], 5)` - should return **false**


## Exercise 4
-
Create an object called `calculator`.

It should have two methods: `add` and `subtract`

Both methods take two parameters, and should return the sum/difference of both numbers.

  

Use this to test your code:

  
```js
const result1 = calculator.add(20, 1)
const result2 = calculator.subtract(30, 9)

console.log(calculator.add(result1, result2)) //should print 42
```

-------------
## Exercise 5 (Extra Practice)
-
Complete the following code:

  
```js
const turnToKing = function(name, money){
    name = name.toUpperCase()
    money = increaseByNameLength(money, name)
    name = makeRegal(name)

    console.log(name + " has " + money + " gold coins")
}

turnToKing("martin luther", 100) // should print "His Royal Highness, MARTIN LUTHER has 1300 gold coins"
```
  

To complete the above you will need to create both the `increaseByNameLength` and `makeRegal` functions.

  

You should be able to write the body of both functions in one line; there's no trick here - it's just practice.

