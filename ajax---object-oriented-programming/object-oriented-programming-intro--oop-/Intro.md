
Today we step into the world of OOP - Object Oriented Programming. This is an important **design pattern** popular in the programming world.

OOP is popular because a lot of the code we write involves manipulating objects, so we want that to be our focus.

In the past, developers wrote in a style known as [procedural programming](https://en.wikipedia.org/wiki/Procedural_programming) which was more focused on logic* than data. In OOP we put **data before logic**.

###### *This often led to what is known as [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code) which we want to avoid

In other words, our code will focus on the objects of our application - similar to how we worked with modules - in order to keep our code separated and organized.

For this intro lesson, we will cover the following OOP concepts:

-   Classes
-   Attributes, Constructor, & Instantiation
-   Methods
-   Static Methods (extra)
-   Getters & Setters (extra)
-   Unified Modeling Language (UML)

  

----------

#### **UNTIL NOW...**

The way we've created modular code up to now is by wrapping things inside a function, like this:

```js
const someModule = function(){

  const _somethingPrivate = 3const exposePrivates = () => _somethingPrivate

  return 
    {
      exposePrivates: exposePrivates
    }
}
```
Then if we wanted to access that, we'd do something like this:

```js
const m = someModule()
console.log(m.exposePrivates()) //prints 3﻿﻿
```
This is a little limited (we'll see why soon), and it's kind of "hacky" - we're using a function to to **encapsulate*** our code - but that's not really the point of functions.

*[Encapsulation](https://en.wikipedia.org/wiki/Encapsulation_(computer_programming)) is exactly what we've been doing with modules so far - closing off certain pieces of code for modularization and to limit who can access what (i.e. `_private` variables cannot be accessed outside of the module, unless it's through a function)
