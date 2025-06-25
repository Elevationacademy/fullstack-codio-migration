
You'll get plenty of data structure practice as you keep coding, so for now complete this exercise, then keep learning.

  

----------

Create a data structure called `UniqueArray`

It should have four methods:

1.  `add(item)`
    - Stores the item _only if_ it hasn't been added already
2.  `showAll()`
    - Shows all the added items
3.  `exists(item)`
    - Returns `true` if the `item` has been added, `false` otherwise
    - This should run in **O( 1 )**
4.  `get(index)`
     - Returns the item at index `index`, or `-1` if it doesn't exit

  

Effectively, this data structure works like a normal array (for the most part), but:

-   It only works for [primitive types](https://developer.mozilla.org/en-US/docs/Glossary/Primitive)
-   It only allows you to add _unique_ items to it

  

To test your data structure, use the following code:

```
const uniqueStuff = new UniqueArray()
uniqueStuff.add("toy")
uniqueStuff.showAll() //prints ["toy"]
uniqueStuff.add("toy")
uniqueStuff.showAll() //prints ["toy"]
uniqueStuff.exists("toy") //returns true
uniqueStuff.add("poster")
uniqueStuff.add("hydrogen")
console.log(uniqueStuff.get(2)) //prints "hydrogen"
```
  

Once you're done, and only once you're done, **check** [**this**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set) **out**.