
[ES6](https://www.makeuseof.com/tag/es6-javascript-programmers-need-know/) gives us the `class` syntax to help us properly modularize our code, _and more_. Check it out:

```js
class Animal {
    constructor(name, numLegs) {
        this.name = name
        this.numLegs = numLegs
    }
}
```
Remember this: **a class is just a blueprint** - it merely tells us what future objects will look like.

Like a function, defining a `class` doesn't do anything by itself. But it does explain the eventual object.

In the above `class`, for instance, we know that each object will have a `name` and a `numLegs` - these are the **class attributes** (a.k.a properties).

We'll talk about `constructor` and `this` in a bit.

For now, to actually create an object from a class, we need to **instantiate** it.

  

----------

#### **INSTANTIATION**

Using the `class` above - which again, is just a blueprint - here is how we **instantiate** an actual object from it:

```js
const cat = new Animal("Puss", 4)
```
Notice the `new` keyword - this is what creates a new **instance** of our `Animal` class.

Of course, an `Animal` expects to have a `name` and `numLegs`, so we must pass those as arguments - similar to a function.

You can think of an **instance** as an actual, "physical" object.

The `Animal` class is just a blueprint, whereas the `cat` instance is an actual object we can use in our code, like this:


```js
console.log(cat.name + " has " + cat.numLegs + " legs") //prints "Puss has 4 legs"
```
Let's look at the `class` definition again:

```js
class Animal {
    constructor(name, numLegs) {
        this.name = name
        this.numLegs = numLegs
    }
}
```
Notice the `constructor`? This is where we assign **class attributes**.

More specifically, the **constructor** is in charge of creating the new objects (each new instance).

It is a _method_ that initializes the attributes of the new objects. Inside the constructor method, we define the properties we want to give to each of the new objects that will be created.

We're using `this` because behind the scenes, a **class** **is just a fancy object.**

As such, in the `constructor`, `this` refers to the new object to be created.

So the above `new Animal` statement would be equivalent (more or less) to doing this:

```js
this = {}
this.name = "Puss"
this.numLegs = 4
const cat = this
```
Good thing JS (the constructor, in this case) does this for us.

Of course, the above is a one-time object where we have to define the properties ( `name` and `numLegs` ) each time.

The `class` allows us to define attributes once, and create as many instances as we want of similar objects.

﻿Now we have a class that is independent of anything else in our code. It is some blueprint that represents our data, regardless of any logical flow in our app.

This is what we mean when we say that OOP puts **data before logic**.
