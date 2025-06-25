
Sometimes a child class will require some attributes/methods from a parent, but not all of them.

  

Let's say we want to preface each teacher's name with "Professor", so that instead of "Cassandra" it would say "Professor Cassandra".

  

To "ignore" an attribute from a parent (the `name` attribute in this case), we can simply _not_ pass it into `super`, and define it for `Teacher` explicitly:
```
class Teacher extends Person {
    constructor(name, startYear, salary) {
        super(null, startYear)
        this.salary = salary
        this.name = "Professor " + name
    }
}
```
  

We pass `null` into `super` as a sort of placeholder, so that `startYear` gets initialized to the correct parameter inside `Person`'s constructor.

  

Now if you write the following:
```
const t1 = new Teacher("Cassandra", 2002, 40000)
console.log(t1.name)
```
  

You will see "Professor Cassandra" - because we've defined what `this.name` is explicitly instead of initializing it through `super`

  

Ignoring class attributes is straightforward. But if we want a different functionality from an inherited _method_...