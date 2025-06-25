Instructions
-

This was quite a bit, but make sure you get the fundamentals: the concept of inheritance, `extends`, `super`. If you understand these, everything else will click.

  

----------

  

Create a `Principal` class.

  

It should inherit from `Person`, and have the following additional attributes and methods:

1.  `teachers` - an array of `Teacher` objects
2.  `hireTeacher` - a method that receives a `teacher` and adds it to the `teachers` array

    -   It should also console log "`<principal name> just hired <teacher name>`"

1.  `students` an array of `Student` objects
2.  `recruitStudent` - a method that receives a student and adds it to the `students` array
3.  `expelStudent` - a method that receives a student and removes it from the `students` array (for now, you can just search by name)
4.  `transferStudent` - a method that receives a student and a principal, removes the student from `students` and pushes it to the other principal's `students` array

  

You can test your code with the following:
```
const p1 = new Principal("Martin", 1991)
const p2 = new Principal("Martha", 1990)

const t1 = new Teacher("Cassandra", 2002, 40000)
const t2 = new Teacher("Kevin", 2006, 30000)

const s1 = new Student("Ronda", 2017)
const s2 = new Student("Byron", 2016)

//1 & 2
p1.hireTeacher(t1) //should print "Martin just hired Cassandra"
console.log(p1.teachers) //should print Array(1) [Teacher] - the teacher should be Cassandra

p1.hireTeacher(t2) //should print "Martin just hired Kevin"
console.log(p1.teachers) //should print Array(2) [Teacher, Teacher]

//3 & 4
p1.recruitStudent(s1)
p1.recruitStudent(s2)
console.log(p1.students) //should print Array(2) [Student, Student]

//5
p1.expelStudent(s1)
console.log(p1.students) //should print Array(1) [Student] - the student should be Byron

//6
p1.transferStudent(s2, p2)
console.log(p1.students) //should print Array(0) []
console.log(p2.students) //should print Array(1) [Student] - the student should be Byron
```