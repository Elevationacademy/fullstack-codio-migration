
Great, now we have two classes inheriting from `Person` - they each have access to the general attributes `name` and `startYear`, and the method `addCourse`

Separately, each has its own unique attributes and methods.

  

This kind of inheritance, where multiple classes inherit from a single class is called **Hierarchical Inheritance**, and it looks like this:

$~~~~~~~~~~~$A
$~~~~~~~~~$↙↘
$~~~~~~~$B$~~~~~~$C

  

Where, in our case, **A** is the `Person` class, and **B** and **C** are the `Student` and `Teacher` classes.

  

----------

  

#### **PAUSE**

  

So far we've learned about the concept of inheritance, and the `extends` and `super` keywords.

  

These are the most fundamental parts of inheritance. Make sure you understand them before moving on.

  

#### **PLAY**

  

----------

  

#### **INSTANCEOF & POLYMORPHISM**

  

When talking about class hierarchy, we can say things like "a Teacher **IS A** Person", or "a student **IS A** Person" - that is both conceptually and programmatically true.

  

We can check whether objects belong to a certain class using JavaScript's `instanceof` operator, like this:
```
const s1 = new Student("Ronda", 2017)
console.log(s1 instanceof Student) //prints true
```
  

This may look strange, but if you think of `instanceof` as an operator just like `++` or `==` then it shouldn't be too weird.

  

The operator checks whether the left-hand side is an **instance** of the right-hand side. Since `s1` _is_ a `Student`, the above returns `true`