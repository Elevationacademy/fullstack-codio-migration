
A classic many-to-many example is the students-teachers relationship. Each student can have many teachers, and each teacher can have many students.

  

If you can think of a way to design tables to store this kind of data differently from what we are about to explain,

-   Without being redundant
-   Efficiently

  

Then let us know and we'll escort you to the patent office.

  

Otherwise, the common solution is to use a third **join table**, and it looks like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/sqlManyToManyVisual.PNG)

  

Now we have a _third_ (on the left in the image above) table that only has two fields: the `student_id` and the `teacher_id` - this table manages our **many-to-many** relationship perfectly.

  

It will do exactly what we want: give us one table where we can see which student has which teachers and vice versa, and the query should be really simple!

  

Ultimately, the join table will look like this:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/sqlManyToManyTable.PNG)

  

But what it's telling us is that

-   The `Student` with `s_id` 1 has two teachers:
    -   The `Teacher` with `t_id` 1
    -   The `Teacher` with `t_id` 2
-   But the `Teacher` with `t_id` 1, for example, has _three_ students, with `s_id`s 1, 2, and 3

  

Hence, **many-to-many**, also denoted as **M : N.**
(We call it M : N because saying _M : M_ would suggest there is an exact match between the amounts of items in the tables, which is not the case. For instance, one student could have 4 teachers, while that teacher has 23 students; so it's still many-to-many, we just don't assume each "many" is the same on both ends)