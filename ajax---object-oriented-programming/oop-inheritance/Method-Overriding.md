
We said that both teachers and students need an ability to add a course. That's why their parent, `Person` class has that method.

  

But the school has now been running for a few years has realized that students sometimes register for the same class more than once by mistake. As the developers of this school's app, we need to make sure that doesn't happen.

  

Recall how `Person` **implements*** the `addCourse` method (and therefore, how students add courses when they invoke the method)

Implementation means how exactly we do something.

As a simple example, if we had a function that takes a number and doubles it, here are two different _implementations_ for the function:

  

**const** double1 = **function**(x) => x *= **2**

**const** double2 = **function**(x) => x = x * **2**

In this case the methods to the same thing, but different implementation can also mean different logic

  

The `addCourse` super-method simply receives a course and pushes it directly to `courses`:
```
addCourse(course) {
    this.courses.push(course)
}
```
  

When a student or teacher inherits this method, they inherit exactly that.

  

But for students we want to invoke this method only if the course hasn't been added yet. That means that we want to run the method slightly differently. This notion of tweaking an inherited method's implementation is called **method overriding**.

  

To **override** a method, we just have to define it ourselves in the child class.

So in `Student` we would do something like this:
```
class Student extends Person {
    constructor(name, startYear) {
        super(name, startYear)
        this.grades = []
    }

    //method overriding!
    addCourse(course) {
        if (this.courses.indexOf(course) == -1) {
            super.addCourse(course)
        }
    }
}
```  

Notice a couple of things:

1.  We literally write-over the method; i.e we define it in the class again (as opposed to just getting it from the parent)
2.  However, we don't have to define the inherited functionality - the part that actually adds a course to the `courses` array
    -   Instead, we use `super` again to invoke the inherited method - but _only if_ the course is not in `courses`

  

Note that **we could also override the method entirely**, and not use `super` at all inside the overridden method - that depends on how different we want our implementation to be.