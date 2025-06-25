
Create an `enrollStudent` function. This function should

-   Accept a student name and teacher name as parameters
-   Find the student and teacher's IDs with a simple `SELECT` query
-   Add the student-teacher IDs to the `student_teacher` table

  

**Hint:** remember that any query operation is **asynchronous**, so you'll either have to deal with promises or maybe pull out some [Async/Await](https://javascript.info/async-await).

  

**Hint 2:** you can assume that each student and teacher name is unique, for now.

  

**Note:** this function should only work for students and teachers that already exist in the DB.

  

Check your work by running `enrollStudent("Leonidis", "Yoda")` - then validate with your `student_teacher` table.

  

If you need, check [this solution](https://codepen.io/ElevationPen/pen/byoeYj?editors=0010).