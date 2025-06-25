
In the OOP Intro lesson we learned the basics - classes, attributes, methods, and instances. In this lesson we'll learn a couple of cool **design patterns** popular in OOP:

1.  The Singleton Pattern
2.  Dependency Injection (DI)

  

We never strictly "need" to use either of these, nor do they require any new syntax.

  

Singletons and DI are merely ways of working which have become common due to the benefits they add to our code.

  

This will be a relatively theory-heavy lesson, so get comfortable.

  

----------

  

#### **SINGLETON**

  

The Singleton Pattern is "a design pattern that restricts the instantiation of a class to one object".

###### 1Quoted from [here](https://en.wikipedia.org/wiki/Singleton_pattern)

In other words, instead of created several `new ...` instances of some class, we only ever create **one** instance.

  

A great use-case for this is a `DataManager` class that handles all our data - storing, retrieving, etc. In other lessons we talk about storing data in LocalStorage and Databases, but for now you can imagine a class that looks something like this:

  

```js
class DataManger{
    constructor(){
        this.data = this.getFromDB()
    }

    getFromDB(){
        // some code that gets data from the DB
    }

    addData(data){
        // code that saves the new piece of data to the DB
    }
}
```
######   

###### **Side note:** notice how the constructor is accessing a method of the class? Perfectly legal.

  

We really should only have **one** data manager - that is, one object that handles our Database data.

  

If we had several instances of the above `DataManager`, then our data might not be in sync throughout our application. But if we decide that `DataManager` is a singleton, then there will only be one instance of it, and no sync issues.

  

How can we guarantee no sync issues? Because there is only ever one object that handles anything to do with data. Because it's a singleton.

  

**Spot check:** say you were building an app to manage a zoo.

What classes would you have?

What would each class be responsible for?

How many instances of each would there be?

Think about these questions before looking at the (one of possibly many) answer.

  
<details><summary>  
Click here to reveal the answer.  
</summary>
One way to do it would be to have three main classes:

-   A `Zoo` class - this would be a singleton and would hold all our animals + be in charge of adding/removing them
-   An `Animal` class - there would be as many instances of this as we have animals in the zoo
-   A `Worker` class - an instance for each person working at the zoo

There could, of course, be more classes or different configurations - but in all likelihood you would have at least one singleton `Zoo` class. Please ask an instructor if this doesn't make sense
</details>
