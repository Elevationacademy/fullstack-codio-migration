# Var, Let and Const

as we mentioned before there are three identifiers in JavaScript.

theres an important difference to notice between them when it comes to scopes.

---
### Scope of var

Scope essentially means where these variables are available for use. var declarations are globally scoped or function/locally scoped.

The scope is global when a var variable is declared outside a function. This means that any variable that is declared with var outside a function block is available for use in the whole window.

var is function scoped when it is declared within a function. This means that it is available and can be accessed only within that function.

**var variables can be re-declared and updated**
This means that we can do this within the same scope and won't get an error.
```
    var greeter = "hey hi";
    var greeter = "say Hello instead";
```

**Hoisting of var**
Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their scope before code execution. 
So var variables are hoisted to the top of their scope and initialized with a value of undefined.

---
### Scope of let

let is block scoped,So a variable declared in a block with let is only available for use within that block. Let me explain this with an example:

```
   let greeting = "say Hi";
   let times = 4;

   if (times > 3) {
        let hello = "say Hello instead";
        console.log(hello);// "say Hello instead"
    }
   console.log(hello) // hello is not defined
```

We see that using hello outside its block returns an error. This is because let variables are block scoped .

**Hoisting of let**
Just like  var, let declarations are hoisted to the top. Unlike var which is initialized as undefined, the let keyword is not initialized. So if you try to use a let variable before declaration, you'll get a Reference Error.

---

### Const
Variables declared with the const maintain constant values. const declarations share some similarities with let declarations.

**const declarations are block scoped**
Like let declarations, const declarations can only be accessed within the block they were declared.

**const cannot be updated or re-declared**
This means that the value of a variable declared with const remains the same within its scope. It cannot be updated or re-declared.

