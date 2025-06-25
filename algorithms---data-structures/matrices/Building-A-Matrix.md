We can create matrices manually as we saw in the intro, but that is not always practical.



Generally (but not always), we would use a **
We can create matrices manually as we saw in the intro, but that is not always practical.

  

Generally (but not always), we would use a **double for loop** to create a matrix, where the first iterator represents the **rows** in the matrix, and the second iterator represents the **columns**, like so:

  
```
function generateMatrix(numRows, numColumns) {
    let matrix = []
    let num = 1
    
    for (let r = 0; r < numRows; r++) {
        matrix.push([])
        for (let c = 0; c < numColumns; c++) {
            matrix[r].push(num++)
        }
    }
    return matrix
}
```

  

Now if we invoke `generateMatrix(3, 4)`, it would generate a **3 x 4** (_three by four_) matrix with the numbers 1-12.

  

If you now `console.log(generateMatrix(3, 4))`, you will see something like this:

```
[ [ 1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ] ]
```
  

Which is not so intuitive, but it does show three inner arrays, each with four numbers - still, it's hard to tell what the columns are.

  

We'd like to see our matrix like this:

```
1       2       3       4
5       6       7       8
9       10      11      12
```
  

But to do that we need to learn how to access items in a matrix.