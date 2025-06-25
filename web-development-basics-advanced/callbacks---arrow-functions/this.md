
In normal functions, this refers to the object that called the function.

  

But arrow functions do _not_ create their own this context. As such, this keeps its original meaning from its enclosing context.

  

Let's look at this example:

  
```
const suspenseBuilder = {
    name: "El Mysterio",
    displayName: function () {

        console.log("You are going to see the name in 3 seconds...")

        setTimeout(function () { //normal function
            ﻿console.log("The name is: " + this.name)
        }, 3000)

    }
}

suspenseBuilder.displayName()
```
  

The suspenseBuilder object has two keys: a name string and a displayName method.

  

The displayName method has a console log, then sets a timeout to wait 3 seconds before console logging this.name - wild suspense here.

  

However.. With regular functions, this is the object that called the function - but who called that callback function in setTimeout? No one called it o_o

  

Therefore, since "no one" called the function, this will just be the general window object, and this.name will be undefined.

  

Arrow functions save the day. If we rewrite the callback as an arrow function, like this:

  
```
const suspenseBuilder = {
    name: "El Mysterio",
    displayName: function () {

        console.log("You are going to see the name in 3 seconds...")

        setTimeout(() => { //this is the change
            ﻿console.log("The name is: " + this.name)
        }, 3000)

    }
}

suspenseBuilder.displayName()
```  

Then this works as expected!

  

This works because **in arrow functions,** **this** **is determined by lexical scope**. That just means that it doesn't matter _who_ called the function, but rather _where_ it was created - the **context** of the function.

  

In this case, the callback function was called inside suspenseBuilder, and as such this will equal suspenseBuilder!

  

Another way to think of **lexical scope** is simply as the "regular scope". Remember that inner-functions (like the callback) will always have access to the scope of outer functions ( like displayName ). Therefore, whatever this is inside of displayName will apply to the callback as well.

  

  

----------

  

#### **USAGE**

  

  

The question of _when_ to use an arrow function is important. It's not "always".

  

**Do use arrow functions**:

-   When you need this to refer to the context rather than the object
-   In iterator methods such as [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter) and [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map%20target=) (we'll learn about these later)
-   For simple functions, for cleaner syntax

  

**Do not use arrow functions:**

-   In object methods (usually)
-   Just because you can