
Our applications will often have several objects. Sometimes those objects interact with one another. Sometimes those objects _depend_ on one another.

  

Let's think about an `Animal` class in the context of a Zoo.
An animal may have a `name` attribute, a `type` (which type of animal) attribute - these will be specific to each instance we create.

  

But all animals need to eat. And they need to get their food from somewhere.

  

So we could create a `Feeder` class that has one method, `getFood`.
This method would take an animal type as a parameter, and determine which food to return. Here's an example of such a class:

  


```js
class LuxuryFeeder {
    getFood(animalType) {
        if (animalType == "lion") {
            return "chia seeds"
        }
        if (animalType == "elephant") {
            return "peanuts"
        }

        return "scraps"
    }
}
```
  

**Spot check:** what happens if we run the following code?

  


```js
const feeder = new LuxuryFeeder()
console.log(feeder.getFood("monkey"))
```
  
<details><summary>  
Click here to reveal the answer.  
</summary>
It will print "scraps" since that is the default food.
</details>

-------------


Alright, so every animal needs access to that feeder. To that end, we could do something like this:

```js
const feeder = new LuxuryFeeder()

class Animal {
    constructor(name, type) {
        this.name = name
        this.type = type
    }

    _consume(food) {
        console.log("Just consumed " + food + ". Feels good.")
    }

    eat() {
        const food = feeder.getFood(this.type)
        this._consume(food)
    }
}
```
  

**Spot check:** what would happen if we ran the following code?


```js
const bumdo = new Animal("Bumdo", "elephant")
bumdo.eat()
```
  
<details><summary>  
Click here to reveal the answer.  
</summary>
It would print "Just consumed peanuts. Feels good." - make sure you understand why this is happening before moving on.
</details>
  

The above solution is okay, but problematic.
True, every animal now has access to the `feeder` instance and can access food based on its type, but...
What if we had a different feeder, like this:

  

```js
class CheapFeeder {
    getFood(animalType) {
        return "scraps"
    }
}
```
  

What if the type of feeder needs to change depending on budget or time of day?

  

We could, in theory, modify our eat method in the Animal class to use either CheapFeeder or LuxuryFeeder based on some condition - but this is considered **bad practice**.

In OOP, your code should be **loosely coupled** - this means that each class should have as little (ideally zero) knowledge of other classes as possible.

  

An animal shouldn't have to care or be aware of the fact that there are different feeders - it should only know to _receive_ a feeder, and to _use_ one.

  

As such, we don't want a series of if-else statements in our Animal class that checks which Feeder should be used. That would make our animals **tightly coupled** to our feeders - no bueno.

  

That said, our animals _do_ depend on a feeder - and that's where **dependency injection** comes in. Check this out:


```js
class Animal {
    constructor(name, type, feeder) {
        this.name = name
        this.type = type
        this.feeder = feeder //dependency injection!
    }

    _consume(food) {
        console.log("Just consumed " + food + ". Feels good.")
    }

    eat() {
        const food = this.feeder.getFood(this.type)
        this._consume(food)
    }
}
```
  

Now each time an animal is instantiated, it will receive a feeder as a **dependency** in the constructor.

Said differently, whenever we create an instance of any animal, we will **inject*** a feeder into it - but the animal _doesn't care which feeder comes in!_

###### *Technically, the injection happens on line 2, in the constructor**

###### **Teeeeechnically, the injection happens once we instantiate an object and pass it the feeder

  

So long as the animal receives _some_ feeder, everything will work fine.

That's dependency injection for you.

  

Also, make note of line 13 in the code above - the animal accesses its own feeder via `this` - because `feeder` is now a class attribute!

