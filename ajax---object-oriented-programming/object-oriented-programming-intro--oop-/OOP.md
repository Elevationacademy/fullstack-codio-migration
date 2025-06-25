
Ultimately, with all the classes and instances and new syntax - an object is just an object. It can be passed to functions just like any other object. Check this:

  


```js
class Zoo {
    constructor() {
        this.animals = []
    }

    addAnimal(animal) {
        this.animals.push(animal)
        console.log("Added " + animal.name + " to the zoo")
    }

    showAnimals() {
        this.animals.forEach(a => console.log(a.name))

    }
}

class Animal {
    constructor(name, numLegs) {
        this.name = name
        this.numLegs = numLegs
    }
}

const cat = new Animal("Puss", 4)
const zoo = new Zoo()

zoo.addAnimal(cat) // prints "Added Puss to the zoo"
zoo.showAnimals() // prints "Puss"
```
  

Notice how when we invoke `addAnimal` we're passing it the `cat` object we instantiated through the `Animal` class!

It's exciting, but shouldn't be surprising. After all, `cat` is just an object ~
