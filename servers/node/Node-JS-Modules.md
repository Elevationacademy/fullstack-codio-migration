
Now it's time to learn about one of Node's best features: modules.

  

Modules in node are similar to regular JS modules we've learned about, but now these work as an actual feature of the environment.

  

By that we mean that **in node, every file you write is automatically wrapped in a module for you** - and this is exciting. As such, we can now say "module" and "file" interchangeably: every file in node is a module.

  

This is exciting because node allows us to **export** and **import** modules from one file to another - this means that we no longer have to rely on our index.html to import everything and allow every piece of our code to be accessible on a global level.

  

As an example, create a circleUtils.js file, and add the following code inside:
```
const title = "Circle Utility";
const pi = 3.14159;

const calcCircleArea = function (radius) {
  return pi * radius * radius;
};

module.exports.pi = pi;
module.exports.calcCircleArea = calcCircleArea;
```
  

Nothing terrible here, we've defined three variables:

1.  A title - which is a simple string
2.  The const pi - which we all know and love
3.  The calcCircleArea function which receives a radius and returns the area of a circle

  

As for the module.exports at the bottom, here's what's going on: **every node file (i.e. module) has a built in** **exports** **object. We can assign new keys to this object in order to export (i.e. expose) them to other files**. Without this, no other module could access this piece of code.

  

To see what this means, go ahead and create another file called shapesApp.js, and add the following code there:
```
const circleUtilities = require('./circleUtils');
console.log(circleUtilities);
```
  

In this separate file, we can **import** the keys that we exported using the require function. This function takes one argument: a string with a path to some file.

  

In this case, the file (i.e. module) in which we're interested is in the same directory, so we preface its filename with ./ - notice also that we **don't have to write out the** **.js** **extension, just the filename is enough**.

  

If you run the above code (of course, using the node shapesApp.js command in your terminal, or by pressing F5 in VS Code), you'll see the following object in the console:

  
```
{ pi: 3.14159, calcCircleArea: [Function] }
```
  

Yes, circleUtilities is now a plain JS object with two keys: pi - a number - and calcCircleArea - a method.

  

However, if you try to run any of these inside of shapesApp.js, you'll get an error:
```
console.log(pi)
console.log(title)
console.log(calcCircleArea)
```
  

You'll see an error because these only exist in the scope of the circleUtilsmodule! To access them from shapesApp.js you have to access their values from the circleUtilities object, like so:

  
```
const circleUtilities = require('./circleUtils')

const r = 4
console.log(`The area of a circle with radius ${r} is ${circleUtilities.calcCircleArea(r)}`)
//^prints "The area of a circle with radius 4 is 50.26544"
```
  

Just plain dot notation to access the calcCircleArea method from the circleUtilities object.

  

**Spot check 1:** the calcCircleArea function uses pi in its calculation - we have not defined pi in the shapesApp.js module - why does the above code still work?

<details><summary>
  Click here to reveal the answer.
</summary>

Closure! Inside the circleUtils file - which again, is a module - the calcCircleArea function accesses pi. Since this is _a function accessing an external function's variables_ - we have closure! The value of pi is kept from within the calcCircleArea function.

</details>

</br>


  

**Spot check 2:** from within the shapesApp module (as it is written above), can you access title?

<details><summary>
  Click here to reveal the answer.
</summary>

Nope, because we did not **export** it from the circleUtils module.

</details>

</br>


  

  

----------

  

If we take a step back to think about **why** we did this, it should be straightforward: **separation of concerns** is key. We have one module, circleUtils which has all the utilities we need for dealing with circles: pi, a function to calculate the area of a circle, and we could add more.

  

But the actual usage of these utilties is in another module: shapesApp - this is the module that needs access to everything, so it imports them. Now each module is responsible for its own, separate concern.

  

So we use module.exports to export, and require to import.

Important note: this **only works in node, this will not work if you try to run it in the browser**.

  

**Spot check:** what happens if you run `console.log(module.exports)` inside of shapesApp.js?

<details><summary>
  Click here to reveal the answer.
</summary>

You should see an empty object, because you haven't assigned anything to it!

</details>

</br>



  

  

----------

  

Of course, since `module.exports` is just an object, there's no reason for us to not be able to just assign it more simply, like so:

  
```
const dbName = "SQL_DB_1102"
const dbPassword = "e3!accT"

module.exports = {
    dbName: dbName,
    dbPassword: dbPassword
}
```
  

In this case we're overwriting the entire exports objects - but since it is empty by default, that doesn't really matter.