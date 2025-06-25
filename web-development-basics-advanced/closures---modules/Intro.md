
In this lesson we will go over:

  

-   Closures
-   The Module Design Pattern

  

These concepts are an introduction to good coding principles related to **separation of concerns** and **single responsibility.**

  

  

----------

  

  

#### **QUICK FUNCTION RECAP**

  

Let's recall some important things about functions for a second before we dive into closures:

  

-   Functions can take in some value
-   Functions do something
-   Anything defined inside a function (i.e. in its _scope_) is not accessible outside of the function
-   Functions can return anything, including other functions

  

Let's highlight the last two. First, scope:

  
```
const createPerson = function(name, age){
    const person = {
        personName: name, 
        personAge: age
    }

    return person
}

createPerson("Elon", 42)
console.log(person)
```
  

What do you expect to see in the console.log? Think about this first, then verify:

  

Nothing! Particularly, you should see an error, ReferenceError: person is not defined.

Even though we created a person inside the createPerson function, and **even though** we _called_ the createPerson function - we never took person out of the function's scope!

  

The fix, of course, is to create a new variable like this, _outside_ of the function:

const person = createPerson("Elon", 42) - note that the variable names (person inside and outside of the function) do **not** have to match.

  

That's scope, now let's see a function returning a function. Sounds strange, but not unreasonable. Check it:

  
```
const mathOperations = function(){
    const add = function(x, y){
        return x + y
    }
    return add
}
```  

Inside the mathOperations functions we have defined an add function (which takes two parameters), and then we return it - note that we're **not** calling add in the return.

  

To actually use the above, we would do something like this:

  
```
const math = mathOperations()
console.log(math(1,2))
```
  

Because mathOperations returns the add _function_, then our math variable _is_ that function! So we can invoke it the same way we do with normal functions.

  

If you're thinking "that seems useless and redundant" - you're absolutely right. Right now we're just showing that this works. Please try it out for yourself and see that the console log is what you expect.

  

#### Ok, now that we have that quick recap done, let's move to closures.