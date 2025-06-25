Create a `Teacher` class which also inherits from `Person`

-   A `Teacher` should also have a `salary` attribute
    -   The value of `salary` should come in from the constructor
-   As well, `Teacher` should have a method called `giveGrade`
    -   The method should receive a student*, a course name, and a grade, and invoke the student's `receiveGrade` method

###### *Remember a student is just an object!

  

The `giveGrade` method might be a little tricky conceptually, but think for a few minutes before you check the answer, and use this code to test your work first:
```
const s1 = new Student("Ronda", 2017)
const t1 = new Teacher("Cassandra", 2002, 40000)

t1.giveGrade(s1, "Algebra II", 82)
const firstGrade = s1.grades[0]

console.log(`${s1.name} received an ${firstGrade.grade} in ${firstGrade.course}`)
//above should print "Ronda received an 82 in Algebra II"﻿
```
  

If you're stuck, you can check out [this solution](https://codepen.io/ElevationPen/pen/qzWpmV?editors=0010).