# Comments

The main purpose of writing code is so that a computer can interpret it as commands. However, it's also important that the code we write is also easily interpretable by fellow developers.

Have you ever gone back to a project and had difficulty understanding the internal logic? Well that's probably because said project hasn't been commented properly.

However, redundant comments are extremely efficient and tiring. 

Make sure to do the following:
- Do not write comments for code that is self exploratory 
- Avoid adding too many comments.
- Add comments to pieces of codes that might be very unclear.
- the only time we can write a comment some sort of **assumption** on the code. 

<span style="color:red">**Don't**:</span>
```js
//this function sums all even members of the array
function sumEvenNums(arr){
    let total = 0 //a total variable that we save the sum of all elements in
    for(let element of arr){ // a for loop that sums the array elements
        if(element % 2 == 0){ //checks if even
            total += element //adds it to total
        }
    }
    return total
}
```

<span style="color:green">**Do**:</span>
```js
function sumEvenNums(arr){
    let total = 0 
    for(let element of arr){
        if(element % 2 == 0){
            total += element 
        }
    }
    return total
}
```
Yes , just don't add anything! it is pretty self exploratory what the function does. and thats what we aim for in our Bootcamp. for all our code pieces to be self explanatory.



