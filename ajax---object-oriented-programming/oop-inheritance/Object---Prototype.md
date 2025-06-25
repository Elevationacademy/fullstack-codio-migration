
This section is a little theory-heavy, so be strong.

There is a class built-in to JS that is the base of all classes.

By default, all classes inherit from this base class behind the scenes.

Some might say it is the Master Class. The One Class to Rule Them All **and in the darkness, bind them**

This class is called `Object`. Yes, the same ``{ }`` you know and love [is actually a class](https://www.youtube.com/watch?v=cphNpqKpKc4).

So when we do something like `let x = { }`, behind the scenes we're really doing `let x = new Object( )``

  

You can see `Object` yourself in the browser's console - open it up and type in `Object( )`, then click on the empty object that appears, you should see this:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/oop-base-object.PNG)

These are all the methods available to Object

  

As for proof that everything inherits from `Object`, go ahead and copy+paste your `Person` class into the console, then type `new Person( )` and you should see this at first:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/oop-person-proto.PNG)

  

See that? All the attributes of `Person` - note that `name` and `startYear` are undefined because we didn't initialize them.

  

But where are the methods? If you open up that `__proto__` property, you should see this:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/oop-person-proto-open.PNG)

  

The `addCourse` method! And the `constructor`! And - another `__proto__`? Open that up and you'll see...

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/oop-person-proto-proto-open.PNG)

  

All the methods of `Object`!

So `Person` has access to all of `Object`'s method because (by default) every object inherits from `Object`, and therefore gets access to its methods.

  

To understand more specifically about `__proto__` you can read [here](https://medium.freecodecamp.org/prototype-in-js-busted-5547ec68872), but the short of it is that whenever any object is created in JS, the JS engine gives it a `__proto__` (short for **prototype**) property, which is itself a _reference_ to another object - it can be confusing to understand, so don't worry about understanding it fully too much right now.

  

What you do need to understand is that **a child object has a reference to all of its inherited methods through its** **prototype**.

  

If the `prototype` doesn't have the method in question, it will go to _its_ prototype, and so forth up the chain until it reaches `Object`'s prototype, at which point it will either find the method or find `null`

  

Let's look at our `TeachingAssitant` class again:
```
class TeachingAssistant extends Teacher {
    constructor(name, startYear, salary) {
        super(name, startYear, salary)
    }
}
const ta1 = new TeachingAssistant("Brandon", 2014, 20000)
ta1.addCourse("General Relativity")
```
  

Notice that `TeachingAssistant` does **not** have an `addCourse` method explicitly defined - but we are able to do `ta1.addCourse..` on the last line.

  

We can do this because JS will search up `ta1`'s **prototype chain** until it reaches `Person`*, which _does_ have an `addCourse` method, and then invoke that.

###### *Assume we _didn't_ override this method in `Teacher`. If we do, then JS would go up the chain only until `Teacher`

  

**Spot check:** copy+paste the `Person`, `Teacher`, and `TeachingAssistant` class in the console, then run the following line:
```
const ta1 = new TeachingAssistant("Brandon", 2014, 20000)
console.log(ta1.toString())
```
  

What do you see, can you explain it? We didn't define a `toString` method in any of our classes - why does this work?

<details><summary>Solution</summary>
  
It works because `toString` is a method of the `Object` class.
  
Because `TeachingAssistant` inherits from `Teacher`, `Teacher` inherits from `Person`, and `Person` inherits from `Object` (by default), and because all inherited methods are passed down through `__proto__`, `TeachingAssistant` has access to `toString`


</details>  

