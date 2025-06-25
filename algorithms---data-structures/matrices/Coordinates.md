Usually when we work with matrices, we think of each location as a "coordinate" or an `x, y` value - as if the matrix were a graph.

  

Whether you call it a coordinate, an `x, y`, an `i, j`, or a `row, col` - visually you can think of any point on the matrix like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/matrix-coordinates.PNG)

  

So if, for instance, we wanted to print all the values of the second column (index 1), we could use the following code:


```
function printColumn(matrix, colNum) {
    for (let i = 0; i < matrix.length; i++) {
        console.log(matrix[i][colNum])
    }
}

printColumn(1) //prints 2, 6, 10 on separate lines
```
  

This code works because the "y" coordinate of the second column will always be `1` (i.e. the `colNum` variable), and the "x" coordinate changes all the time.