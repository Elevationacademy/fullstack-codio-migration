And that's pretty much it for matrices! Again, they're nothing more than nested arrays, but they open up a world of possibilities.

----

## Exercise 1

For starters, let's collect all our bits of code from through this lesson and **create a proper** **`Matrix`** **data structure**.
    
      
Fork [this repo](https://github.com/Elevationacademy/matrices-lesson-exercises), clone it, and run `npm install`. You should write your `Matrix` class in the `Matrix.js` file which can be found in the `src` folder.
    
Your constructor should invoke the `generateMatrix` method, using parameters received from the instance.
    
Use the following to check your work:
    
      
```
let m = new Matrix(3, 4)
m.print()
//prints
/*
1       2       3       4
5       6       7       8
9       10      11      12
*/
    
m.alter(0, 0, m.get(1, 1))
m.printColumn(0) //prints 6, 5, 9 (separate lines)
m.printRow(0) //prints 6, 2, 3, 4 (separate lines)
```    

    
## Exercise 2
    
Add a `findCoordinate` method to your `Matrix` that:
    
-   Receives a `value`
-   <ins>Returns</ins> an object `{x: colNum, y: rowNum}` of the first occurrence of `value`
    
Use the following to test your code:
    
```
let m = new Matrix(3, 4)
console.log(m.findCoordinate(12)) //prints {x: 3, y: 2}
console.log(m.findCoordinate(7)) //prints {x: 2, y: 1}
```
    

## Exercise 3

Navigate to the `EmployeeMatrix.js` file (which is in the `src` folder).
    
Create a new matrix called `EmployeeMatrix` that inherits from `Matrix`  (don't forget to require the Matrix)
    
Add a `loadData` method to `EmployeeMatrix`. The method should:
    
-   Receive an array of objects called `salaryData`
-   Generate a matrix where
    -   Each object represents the next row in the matrix
    -   Each object key represents a column in the matrix
-   Replace the instance's matrix with this new matrix
    
      
**Hint:** don't rush to write a double for-loop for this. You're _receiving_ an _array_ of data. There is a certain _method_ you can use to make your life easier.
    
Use the following to test your code:
    
```
let data = [
        { _id: "e10021", name: "Gillian", department: "Finance", salary: 2000 },
        { _id: "e10725", name: "Tibor", department: "Design", salary: 1200 },
        { _id: "e10041", name: "Anisha", department: "Finance", salary: 2300 },
        { _id: "e10411", name: "Jakub", department: "Design", salary: 1600 },
        { _id: "e11995", name: "Mar", department: "Design", salary: 1300 },
        { _id: "e10732", name: "Nisha", department: "Design", salary: 1200 }
]
    
let m = new EmployeeMatrix()
    
m.loadData(data)
m.print()
//prints
    
e10021  Gillian Finance 2000
e10725  Tibor   Design  1200
e10041  Anisha  Finance 2300
e10411  Jakub   Design  1600
e11995  Mar     Design  1300
e10732  Nisha   Design  1200
```    

    
## Exercise 4

Add a `getEmployees` method to your `EmployeeMatrix` class.
    
This method should receive one parameter, `department` - a string, and it should return an array of all the employee names that work in that department.
    

This method should run in **O( n )**.
    
Use the following to test your code:
    
```
console.log(m.getEmployees("Finance")) //prints [ 'Gillian', 'Anisha' ]
console.log(m.getEmployees("Design")) //prints [ 'Tibor', 'Jakub', 'Mar', 'Nisha' ]
``` 


## Exercise 5
    
Keeping with the `EmployeeMatrix` example, write a method called `getTotalSalary`
    
      
This method should receive one parameter, `department` - a string, and it should return the sum of the salaries _for that department_.
    
      
This method should run in **O( n )**.
    

Use the following to test your code:

```
console.log(m.getTotalSalary("Finance")) //prints 4300
console.log(m.getTotalSalary("Design")) //prints 5300
``` 
    
    
## Exercise 6

Keeping with the `EmployeeMatrix` example, write a method called `findRichest`

The method should return the name of the employee with the highest salary.


This method should run in **O( n )**, and exactly **O( n )*** - that means if you've achieved a complexity of **O(2n)** - you've written redundant code.
    
*You can, of course, ignore **O( 1 )** operations
    
Use the following to test your code:
    

```
console.log(m.findRichest()) //prints Anisha
```    

    
## Exercise 7

Create a new matrix called `TicTacToe` that extends from `Matrix`
    
          
Add a `loadBoard` method that generates a **3x3** matrix of all dots - `.` -, and replaces the original matrix.
    
Use the following to check your code:
    
```
let board = new TicTacToe()
board.loadBoard()
board.print()
//prints
.       .       .
.       .       .
.       .       .
```    


## Exercise 8

Add a `play` method to `TicTacToe`
    
It should receive three parameters: a `rowNum`, a `columnNum`, and a `player` - all of these are numbers.
    
If the `player` is `1`, it should alter the relevant dot to be an `x`, otherwise it should alter it to be an `o`
    
      
**Hint:** **D**on't **R**epeat **Y**ourself.
    
Use the following to check your code:
    
      
```
    let board = new TicTacToe()
    board.loadBoard()
    
    board.play(2, 2, 1)
    board.play(0, 0, 2)
    board.print()
    //prints 
    o       .       .
    .       .       .
    .       .       x
```
 
    
## Exercise 9

Modify your `play` method so that if there is any three-in-a-column of `o`s or `x`s, it prints _Congratulations Player ${num}_
    
Use the following to test your code:
    
```
let board = new TicTacToe()
board.loadBoard()
    
board.play(2, 2, 1)
board.play(0, 0, 2)
board.play(0, 2, 1)
board.play(1, 0, 2)
board.play(1, 2, 1) //prints Congratulations Player 1
    
board.print()
//prints
o       .       x
o       .       x
.       .       x
```