# Objects

Now we're going to cover the second extremely popular and fundamental **data structure**: Objects.

Objects work just like a dictionary you could find in the library

An object is a **key-value** store.

That means that unlike an **array** that holds items in a position (index 0, index 1...), in objects we have a unique **key** that is referencing some **value**.


---
Let's look at a simple example:

```js
let person = {
  name: "Mariah",
  occupation: "Gangster"
}
```

The syntax of an object, as you can see, is straightforward:

-   Declare a variable
-   Give it a name
-   Wrap it in **curly braces**
-   Add **key**-**value** pairs
-   Keys don't have to have quotes around them (unless you have special characters)
-   Values do (if they are strings)

In the above example, our **keys** are `name` and `occupation`, and their corresponding values are `Mariah` and `Gangster`

So if we wanted to access `person`'s `occupation`, we would do:
```js
console.log(person.occupation) // prints "Gangster"
``` 


---

Note that the **value** of any key can be _anything_. Strings, numbers, booleans, _arrays_, _other objects_, even functions*!

---

## Dot Notation vs. Bracket Notation

There are a couple of way to **access object properties** (properties are the same as keys):

What we saw up to now is called **dot notation** - that is using the variable `name`, `person`, a dot, and then the property we want.

So to get "Mariah" we just do `person.name`

The other way is similar, but with different syntax: `person["name"]`

The result is exactly the same, but don't worry too much about which to use when right now.

----------

Whether you use dot or bracket notation, if you try to access a key that doesn't exist in the object, then you will get `undefined`

This is similar to trying to access an index that doesn't exist in an array - it's not yet defined!

----------

## ADDING VALUES
To add values to an existing object, there is no special method like with arrays. See this example:
```js
const animalCounts = {
  lion: 2,
  zebra: 11,
  ostrich: 1,
  tortoise: 4
}

//Suddenly the zoo acquired two dozen eagles

animalCounts.eagle = 24
//or
animalCounts["eagle"] = 24
```
The reason we must have quotes in the second version is because otherwise JS would think that `eagles` is a variable, which it isn't. So this is one case where bracket notation is required.

Generally speaking, **we don't usually add key-values to an existing object**.

---
As opposed to **strings**, **numbers**, and **booleans** which are all primitive types, **arrays and objects are reference types**.
**JS does not create a new space in memory for reference types. Instead, it references an existing space, if possible.**

