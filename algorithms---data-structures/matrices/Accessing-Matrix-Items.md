
Say we wanted to access the number `7` in the above matrix.

  

Because our matrix is simply an array within an array, we know we're going to be using indexes. The indexes will be the row and column numbers, one after the other. Take a look at this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/matrix-w-rows-and-cols.PNG)

  

So if we're looking for the number seven, here are the row/column indexes we need to use:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/matrix-w-rows-and-cols-highlighted.PNG)

  

We need to access the matrix at `row 1` and `column 2`, like so:

  
```
let matrix = generateMatrix(3, 4)
console.log(matrix[1][2]) //prints 7
```
  

This should make sense, since `matrix` is just an array with some arrays inside.

-   As such, `matrix[1]` will return the array `[5, 6, 7, 8]`
-   And `matrix[1][2]` is the same as getting the item at index `2` of this array: `[5, 6, 7, 8]` - which is `7`!