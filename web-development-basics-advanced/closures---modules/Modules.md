
Modules are a way for us to compartmentalize our code into separate, independent blocks. They keep our code clean and allow for re-usability. They can have closures in them, **but don't have to**.

  

For a simple example of a module without closure, let's revisit our mathOperations function from before, but let's add some more operations to it:

  
```
const mathOperations = function () {
    const add = function (x, y) {
        return x + y;
    }

    const subtract = function (x, y) {
        return x - y;
    }

    const multiply = function (x, y) {
        return x * y;
    }

    const divide = function (x, y) {
        return x / y;
    }
}
```
 

The above code really is useless, because it has no return and so we can never access any of those functions.

  

So how do we return everything in one go? Simple enough, we can use an object:

  
```
return {
    add: add,
    sub: subtract,
    mult: multiply,
    div: divide
}
```
  

A few things:

-   The return must, of course, be at the _end_ of the mathOperations function
-   We're using short hand (sub instead of subtract, etc) just for convenience
-   As usual, the property names don't mean anything - we can call them whatever
-   Again, we're not _calling_ the functions we return - we're only returning the function itself

  

These are some of the benefits of what we've done, and modules in general:

1.  All our math operations are organized in one **module**
2.  We can save this module in its own file, and then use it in any other JS file

-   We need to make sure we have proper imports, though

3. Because all our math operations are in one place, it helps our code stay _separated_

  

So now try out the module yourself. Write out the above module [here](https://repl.it/) (a nice place to play around with JS), and then try some of the math operations.

  

Remember, you first have to call the mathOperations module yourself. Something like const m = mathOperations()

  

And _then_ you can do m.add(3, 4), for example.