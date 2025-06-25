If you haven't run across it yet, JavaScript has a built-in operator called [typeof](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof) which tells us the type of some expression:

```
typeof "hello, world!" //returns 'string'
typeof 1337 //returns 'number'
typeof true //returns 'boolean'
typeof {name: "Frenkel"} //returns 'object'
```
  

However, if you tried `typeof []`, you would **also** see object!

  

That is because **in JS, an array is an object**.

  

In fact, **all data structures in JS are some form of JS object**.

  

This shouldn't be _terribly_ surprising, as you've done things like this in the past:

```
let stuff = ["hat", "iron", "bag", "lamp"]

stuff.push("shoe")
stuff.length
```
  

The `.push` up there looks a lot like a method, and the `.length` access certainly looks like a property - _and that's because they are!_

  

So all arrays are objects, and the `[]` syntax is nothing more than **syntactic sugar** - i.e. a simple way to represent this class.


As such, the following two are exactly the same:

```
let stuff = []
stuff.push("boat")

let stuff = new Array()
stuff.push("boat")
```
  

The `Array` class is **built-in to JS**, but because it is so common, we have access to it through the square-bracket syntax.

  

And if the `new` keyword didn't convince you that an Array is an object, then this example will:

```
class SillyArray {
    constructor() {
        this.sillyStuff = []
        this.sillyLength = 0
    }

    print() {
        console.log(this.sillyStuff)
    }

    push(stuff) {
        this.sillyStuff[this.sillyLength] = stuff
        this.sillyLength++

        this.sillyStuff[this.sillyLength] = stuff
        this.sillyLength++
    }

    annihilate() {
        this.sillyStuff = []
    }
}

let myStuff = new SillyArray()
myStuff.push("Roger")
console.log(myStuff.sillyLength) //prints 2
myStuff.print() //prints ["Roger", "Roger"]
myStuff.push("Rabbit")
console.log(myStuff.sillyLength) //prints 4
myStuff.print() //prints [ 'Roger', 'Roger', 'Rabbit', 'Rabbit' ]
myStuff.annihilate()
myStuff.print() // prints []
```
  

Here we've built our own data structure that behaves similarly to an array, but this `push` inserts _twice_ the amount of elements into the array.

  

The other things that make this data structure unique are the `print` and `annihilate` methods which do not exist in a normal array.

  

To be clear, the above `SillyArray` class is:

-   A **new, custom data structure** that we've just created
-   **Based on an array**, as many data structures are
-   **Not** an array
    -   If you tried to do `myStuff.forEach(...)`, for instance, it would throw an error
-   **Not** a simple object
-   A `SillyArray`

  

Notice that in _our_ `push` method we're not using `sillyStuff`'s built-in `push` - this is a convention when building custom data structures based off arrays: **don't use the array's built-in methods/properties** - usually.