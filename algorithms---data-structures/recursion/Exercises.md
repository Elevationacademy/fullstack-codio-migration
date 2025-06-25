For now, we're going to practice pure recursion, just so we get used to this mode of working. It's good algorithmic practice as well, but also important since it does appear every now and again.
    
      
    
Please fork and clone [this starter repo](https://github.com/Elevationacademy/recursion-lesson-exercises), and run `npm install`. You will write all your solutions in the `app.js` file which can be found in the `src` folder.

----------


## Exercise 1
    
In mathematics, there is a concept known as **factorials**. We represent this concept with an exclamation mark, like so: `5!`
    
      
A factorial says that we should multiply a number by smaller versions of itself, until we reach one. In other words, `5! = 5 × 4 × 3 × 2 × 1`
    
      
We call the above "5 factorial", and it equals 120.
    
      
Likewise, if we wanted to find `8!`, we would do `8 × 7 × 6 × 5 × 4 × 3 × 2 × 1`, which equals `40,320`.
    

Your job is to **write a recursive function that calculates a factorial** of a given number. Remember to start with your **base case**, then recurse accordingly.
    
Please write your code within the `findFactorial` function. Add the parameters needed for the function but do not change the name.
    

## Exercise 2
    
Reverse a string using recursion (no loops, of course).

Please write your code within the `reverseString` function. Add the parameters needed for the function but do not change the name.
    

## Exercise 3

Given the following two arrays:

```
const arr1 = [1, 2, 3]
const arr2 = []
``` 
      
    
Add code to the `swap` function. It should be recursive function that removes all the elements from `arr1` and inserts them into `arr2`.
    
Use the following to check your code:
    

```
swap(arr1, arr2)
console.log(arr1) //[]
console.log(arr2) //[1, 2, 3]
```