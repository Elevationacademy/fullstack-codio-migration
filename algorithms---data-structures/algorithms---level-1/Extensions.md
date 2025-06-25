### These exercises are not necessarily harder - you may just have to think a little different.

## Extension 1

Write a function called `printInLoop` that receives a single parameter: `words` - an array of strings.
    
The function should print each word in words continually until you stop the program. For instance, the following code:
    
```
printInLoop(["down", "the", "rabbit", "hole"])
```   
    
Would print "down", "the", "rabbit", "hole", then start again and print "down", "the", ... until you stop your code manually (i.e. shut down your terminal if using node.js).
    
## Extension 2
    
Write a function called `findClosest` that receives two parameters: `points` and `point`- an array of `x`, `y` coordinates, and a single `x`, `y` coordinate.
    
The function should find a coordinate in `points` that is closest to the coordinate `point`. For instance:
    
```
let pizzaLocations = [
        { x: 6, y: 12 },
        { x: 3, y: 1 },
        { x: 9, y: 0 },
        { x: 4, y: 10 }
]
    
let homeLocation = { x: 4, y: 2 }
    
findClosest(pizzaLocations, homeLocation) // should return {x: 3, y: 1}
```
    
You should use the [Pythagorean Theorem](https://en.wikipedia.org/wiki/Pythagorean_theorem) to determine how far apart two points are.
    
Target complexity: O(n)


<details><summary>
  Click here to reveal a hint:
</summary>
  
You should calculate the distance between the `homeLocation` and each of the pizza locations.
    
To calculate each distance, you should get the difference in `x`s and difference in `y`s, and use that as your `a` and `b` in the Pythogorean Theorem.
    
Once you have all the distances, you should be able to easily find the smallest one, and then determine which coordinate that matches with.
</details>
    



## Extension 3

Write a better cipher function called `secretEncrypt`
    
Instead of encrypting by shifting one letter to the right, use a _secret_.
    
For example, let's say the word to encrypt is `elephant`, and the _secret_ is `cab`
The result of `secretEncrypt("elephant", "cab")` would be `hmgsicqu`
    
Instead of shifting each letter one to the right, we're always shifting by the next letter in `cab`:
    
-   At first we shift the first `E` by **c**, i.e 3 letters (**c** is the third letter in the alphabet, the first letter of `cab`)
-   Next we shift the `L` by 1 letter (**a** is the first letter in the alphabet, second letter of `cab`)
-   Next we shift the second `E` by 2 (**b** is the second letter in the alphabet, third letter of `cab`)
-   Next we shift the `P` by 3 again, because we're back at **c** in our secret
-   And so on
    
Target complexity: O(n)
    

## Extension 4
    
Naturally, write a `secretDecrypt(encryptedMessage, secret)` function.