
Let's look at this bit again:

  
```
const m = mathOperations()
```

What we're doing here is - as with any function call - getting whatever the function returns and setting it in a variable. In this case, storing mathOperations' returned object inside of the variable m

  

So now, m has the value of this object that we returned earlier:

  
```
{
    add: add,
    sub: subtract,
    mult: multiply,
    div: divide
}
```
  

Again, m is just a normal JS object. So if we do m.mult, all we're doing is accessing the **value** of the property mult - which in this case happens to be the multiply function!

  

That's why m.mult(3, 4) works - we're simply calling a function.

  

**Modularization** (using modular bits of code) is one of the most popular design patterns in Javascript. In future lessons we'll learn an even _better_ way to modularize our code.

  

Write your own example of a module. If you're still unsure, ask an instructor or a classmate to help clarify.

  

----------

  

  

Let's look at an example of a module with closure:

  
```
const UsersModule = function () {
    const _users = ['Aaron', 'Avi'];

    const addUser = function (user) {
        _users.push(user)
    }

    const listUsers = function () {
        for (let user of _users) {
            console.log(user)
        }
    }

    return {
        addUser: addUser,
        listUsers: listUsers
    }
}

const usersModule = UsersModule()

usersModule.addUser('Narkis')
usersModule.listUsers()
```
  

Copy/paste the above code for this part (you can use [repl.it](https://repl.it/) again)

  

Here we've created a module called **UsersModule***. Inside this module we will keep all of our code related to users:

###### *By convention, we CapitalizeModuleNames, as opposed to our usual camelCase

  

-   A function to add users
-   A function to show (list) all our users
-   A **private*** variable, _users** where we store all our..well, users

###### *We say _private_ because it's not accessible outside of the module

###### **Also, by convention, we preface private variables/functions with an underscore to signify they should not be exposed

  

When UsersModule is invoked, it returns an object with our two module functions. So now outside of our module we can interact with our users, but _only_ to the extent that we've been allowed (with the addUser and listUsers functions)

  

In other words, because of closure, we cannot _directly_ interact with our users, but we can do so indirectly.

  

This is great because if we want to guarantee that adding users only happens in a certain way (say we always want to send an email to a user once they have been added), we know the only way to modify users is through addUser!