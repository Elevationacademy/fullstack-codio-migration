
Override the `addCourse` method and `courses` attribute in the `Teacher` class.

-   Instead of `courses` being an array, it should be an object
-   The object should track the amount of times the teacher adds the course
-   Instead of `addCourse` pushing to an array (which now doesn't exist), it should update the course count in `courses`

  

Use the following code to see if you did it right before looking at the answer:
```
const t1 = new Teacher("Cassandra", 2002, 40000)
t1.addCourse("Algebra II")
t1.addCourse("Algebra II")
t1.addCourse("Trigonometry")
console.log(t1.courses) //should print {Algebra II: 2, Trigonometry: 1}
```
  

[Solution](https://codepen.io/ElevationPen/pen/gNYoqN?editors=0010)