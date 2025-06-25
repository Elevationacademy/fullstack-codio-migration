
In jQuery, $ is just the global "jQuery" variable that gives us jQuery's functionality.

  

Go ahead and console log jQuery (in the project where you've imported jQuery) - you should see a function.

  

Now console log $ - it will print the same thing!

  

Ok, so $ === jQuery - what's jQuery?

  

It's just a function! Check this out:
```
const myQuery = function (selector) {
    if (selector[0] == "#") {
        const elementId = selector.split("#")[1] //will return everything after the # in selector 
    ﻿return document.getElementById(elementId)
        }
    }
```
  

Now, if you add an element with an ID to your HTML, then run this:
```
console.log(myQuery("#yourElementID"))
```
  

You'll see exactly the element you selected using myQuery!

  

Of course, jQuery is much more robust and intricate than myQuery - but it's the same idea: just a function.

  

----------

  

So where does the $ come in? Well, that's just for convenience. JS allows us to store values in some symbols. Check this out:

  
```
const sayHi = function(){
  console.log("Hi!")
}

const $ = sayHi

$() //prints "Hi!"
```
  

In jQuery, somewhere in the source code, the jQuery function gets assigned to the $ symbol, just like we assigned sayHi above.

  

So there you go. No mystery, no magic. Just functions ~

  

To reiterate,

  

-   When you select something with jQuery you are invoking a function and passing in an argument
-   The argument is used to determine what you want to select
-   The result of invoking that function is an array of elements and some special jQuery methods
-   We can use these methods to manipulate the returned array of elements

  

Let's see an example of some methods.