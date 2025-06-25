
The more you write in OOP, the more you'll notice that some objects tend to overlap.

If you were writing some classes for a school, for example, you might have a `Teacher` class, and a `Student` class.

  

But both `Teacher` and `Student` will need attributes like `name`, and `startYear` - however, we certainly don't want to be repeating ourselves each time*.

###### In general there is the [DRY](https://medium.com/@olyjoshone/dry-code-vs-wet-code-codementor-4a22ed19e09c) principle, but also what if we later change `startYear` to `startDate`? We'd have to go and change it in two places instead of one.

  

Still, while a `Teacher` may have a `giveGrade` method, a `Student` would not - so we do need to keep them separated.

  

In order to have overlapping but separate classes, we need to introduce the concept of **Inheritance**.

In particular, we're going to talk about

-   Inheritance
-   `extends` & `super`
-   `instanceof` & Polymorphism
-   Overriding
-   Multi-Level Inheritance
-   `Object` and Prototypes

  

----------

  

#### **INHERITANCE**

  

When we talk about inheritance we tend to talk about a **Parent** or **Super Class**, and its **Child Class**(es).

  

Child classes will **inherit** from a parent class in order to have access to the parent's attributes.

  

Much like human children inherit eye color, height, and toe girth from their parents, so too will our classes act in a similar way.

  

To that end, let's create a `Person` class that is general enough for both a student and a teacher:
```
class Person {
    constructor(name, startYear) {
        this.name = name
        this.startYear = startYear
        this.courses = []
    }

    addCourse(course) {
        this.courses.push(course)
    }
}
```
  

While a `Student` may _enroll_ in a course and a `Teacher` may _teach_ one - they will both ultimately have a number of courses.

Therefore, it makes sense for `addCourse` to be a super method to which both will have access.

  

So now that we've created our parent class, let's create one of its children: `Student`
```
class Student extends Person {
    constructor(name, startYear) {
        super(name, startYear)
        this.grades = []
    }

    receiveGrade(courseName, finalGrade) {
        this.grades.push({
            course: courseName,
            grade: finalGrade
        })
    }
}
```
  

There are a few things to break down here, namely the `extends` and `super` keywords. Here we go:

  

You'll notice that in `Student`'s constructor, we **do not** have to do `this.name = name` - because the parent does that for us!

  

But in order for the name to be initialized, we have to invoke `super`*

###### *In fact, you **must** invoke `super` whenever you inherit in JS - you don't have to pass in any parameters, but if you have `extend` without `super()`, JS will throw an error

  

However, we **do not** have to do anything specific to get access to the methods of the parent class. Access to those comes automatically when we use the `extends` keyword.

  

In other words,

-   When a child class **extends** from a parent class, the child gains access to all of its parents' attributes and methods
-   We use **super** to initialize the parent's constructor - i.e. to initialize the common attributes*

###### *Note that `courses` gets initialized as well, even though we didn't pass it to `super`!

  

To see this in action, run the following code:
```
const s1 = new Student("Ronda", 2017)
console.log(s1.name) //prints "Ronda"

s1.addCourse("Algebra II")
console.log(s1.courses) //prints ["Algebra II"]
```
  

See that? The student has its parent's `name` attribute and `addCourse` method - even though we didn't define them explicitly in the `Student` class!

  

You'll also notice that a `Student` has a `grades` attribute, and a `receiveGrade` method - these two are unique and exclusive to `Student`s - the parent doesn't know (or care) about them!