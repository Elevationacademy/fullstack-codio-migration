## Exercise 1
    
To complete our stardom, write a function called `printStarSeries` that receives two parameters: `num`, and `count`
    
This function should continue to print the stars normally then backwards for as many times as count, for example:
    
```
printStarSeries(5, 3)
//should print the following:
    
*
**
***
****
*****
****
***
**
*
    
*
**
***
****
*****
****
***
**
*
    
*
**
***
****
*****
****
***
**
*
```    
      
Target complexity: O(mn)
    
    
## Exercise 2

Write some code that takes a string and reverses it:
    
```
const reverse = function(str){
        
  let reversed = //your code
  //more code..or not - it's possible to do this in one line ;)
  return reversed
}
    
reverse("dog") //should return "god"
reverse("race car") //should return "rac ecar"
```    
      
Obviously, do not use JavaScript's built in reverse function ;)
    
Target complexity: O(n)
    
## Exercise 3

---

Write a function that receives a **string** and finds **the first non-repeating character** in the string.

for example :

- "aabbccdee" will return "d"
- "abca" will return "b"

    
Target complexity: O(n)
    
## Exercise 4
    
Write a function called `encrypt` that receives a string and encrypts it by shifting every letter in the string by one to the right (in the English alphabet).
    
For instance, `encrypt(cat)` should return `dbu` because
    
-   The letter `d` comes after **c**
-   The letter `b` comes after **a**
-   The letter `u` comes after **t**
    
Target complexity: O(n)


## Exercise 5

Write a function called `jumble` that receives two arrays, and returns a third that is a jumbled form of the first two:
    
```
const colors = ["red", "indigo", "white", "teal", "yellow"];
const foods = ["bread", "cheese", "cucumber"];
    
const jumble = function (arr1, arr2) {
  let jumbledArr = //work with arr1 and arr2
  return jumbledArr
}
    
jumble(colors, foods) 
// could return: ["cheese",teal","cucumber","red","bread","yellow","white","indigo"]
```
 
Note that the new array should have **no** duplicates.
    
Target complexity: O(n)
    

## Exercise 6
    

Given the following data:
    
```
const rawDist = {
        A: 60,
        B: 10,
        C: 10,
        D: 20
}
``` 
      
    
Write a function `getLetter` such that there is a 60% chance of getting `A`, 10% chance of getting `B`, etc.
         
    
**Hint:** Math.random is your friend.
    
Target complexity: O(n)

## Exercise 7

Remove duplicates from a linked list.
Given the head of a singly linked list,  remove duplicates from the linked list.
Offer a way to implement a linked list in JS and use it in your solution.
