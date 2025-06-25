
What will the following return? Think about these before you test them out in code.
```
const s1 = new Student("Ronda", 2017)
const t1 = new Teacher("Cassandra", 2002, 40000)
const p1 = new Person("Anon", 1999)

s1 instanceof Person
t1 instanceof Teacher
t1 instanceof Person
s1 instanceof Teacher
t1 instanceof Student
p1 instanceof Person
p1 instanceof Student
p1 instanceof Teacher

s1 instanceof p1
```
  

Check yourself with [these answers](https://codepen.io/ElevationPen/pen/zVOpLE?editors=0010).

  

Once you complete the above, you might wonder "so is `t1` a `Teacher` or a `Person`?"

  

The answer is both! This is a concept called **polymorphism** - this allows one object to be many types, as we have now.

Indeed, `t1` **IS A** `Teacher`, _and_ `t1` **IS A** `Person` - they are both true.

  

Here is a neat little link to [learn more](https://stackify.com/oop-concept-polymorphism/) about polymorphism*.

###### *Great word to throw out there in an interview, by the way.