
Classes give us the ability to add methods as well. Remember, a method is just a function in an object.

This is similar to what we've done before, but with slightly different syntax:

```js
class Animal {
    constructor(name, numLegs) {
        this.name = name
        this.numLegs = numLegs
    }

    giveBirth(name){
        console.log("Boom. Birthed " + name)
    }
}
```
Note that we cannot define anything (for the most part) outside of the `constructor`, other than methods.

Unlike our work with closure/modules, here we don't need to `return` the function in order to expose it - the `giveBirth` method will intrinsically be part of every `Animal` instance that we create.

So if we let our old Puss go through the holy ritual of birthing...

```js
const cat = new Animal("Puss", 4)
cat.giveBirth("Dolly") // prints "Boom. Birthed Dolly"
```
Let's repeat this again so it's crystal-clear: **a class is just a blueprint for how subsequent objects should be and behave**.

Since the `Animal` class has a `giveBirth` method - every instance of `Animal` will have the ability to give birth.
