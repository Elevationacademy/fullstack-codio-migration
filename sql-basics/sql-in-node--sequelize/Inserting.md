
For the most part, we really only want to spread a `SELECT` command.

  

For other cases, like `INSERT`ing data, we can use a simple promise, like so:

  
```
sequelize
    .query("INSERT INTO company VALUES(null, 'Google', 'Tech', 10000)")
    .then(function ([result]) {
        console.log(result)
    }) 
```
  

In this case, the result is the new `ID` that was generating for the `INSERT` - this is _if_ an `ID` is generated. Again, we used the `[]` to deconstruct the result.

  

----------

  

Make sure you have the following tables set up:

-   A `student` table with the fields
    -   `s_id` - int, PK
    -   `s_name` - string
    -   `is_brilliant` - bool
-   A `teacher` table with the fields
    -   `t_id` - int, PK
    -   `t_name` - string
    -   `is_tenured` - bool
-   A `student_teacher` table with the fields
    -   `student_id` - int, FK
    -   `teacher_id` - int, FK

  

Now, **create two functions:**

-   `addStudent`
-   `addTeacher`

  

Each function should take the relevant parameters as input, and then `INSERT` a new student or teacher into the database.

  

Each function should also **return the ID** of the new row.

  

Check your work by running `addStudent("Leonidis", 1)` and `addTeacher("Yoda", 0)` - then do a `SELECT * ...` to check each table.

  

If you're stuck, check [this](https://codepen.io/ElevationPen/pen/LozZLZ?editors=0010).