### Definition
Modules should be open for extension, but closed for modification.

Let's look at a concrete example to understand it more.
If we have a collection of animals and we want to print their sounds, we might want to implement this function:

```js
function makeSounds(animals)
```

This function takes a collection of animals, it will probably iterate them and according to the animal type will print the relevant sound.

So we could implement it like this:

```js
function makeSounds(animals){
    for (let animal of animals){
        let sound = ""
        switch (animal.type) {
            case "Cat":
                sound = "Miao"
                break 
            case "Sparrow":
                sound = "tweet tweet"
                break
        }
        console.log(sound);
    }
}
```

In this case an animal is an object with a type property and a sound property, both are strings.

Now, what will happened if we want to add another type of animal, for example, Cow?
In this case we would have to add another case:

```js
function makeSounds(animals){
    for (let animal of animals){
        let sound = ""
        switch (animal.type) {
            case "Cat":
                sound = "Miao"
                break 
            case "Sparrow":
                sound = "tweet tweet"
                break
            case "Cow":
                sound = "Moo"
                break
        }
        console.log(sound);
    }
}
```

We have modified the module (in this case the `makeSounds` function) and violated the open close principle.

In order for us to use extension and not modification we will use the polymorphism principle.

Our code will look like this:
```js
function makeSounds(animals){
    for (let animal of animals){
        animal.makeSound()
    }
}
```

Now each animal should implement it's own `makeSound` method.

We could create an `Animal` base class:
```js
class Animal {
    constructor(type){
        this.type = type
    }

    makeSound(){
        console.log("hello");
    }
}
```

and create animal sub classes like this:
```js
class Cat extends Animal{
    constructor(){
        super("Cat")
    }

    makeSound(){
        console.log('Miao');
    }
}

class Sparrow extends Animal{
    constructor(){
        super("Sparrow")
    }

    makeSound(){
        console.log("tweet tweet");
    }
}
```

Now if we want to add a Cow we can simply **extend** the module by creating another animal subclass that will implement it's own `makeSound` method:
```js
class Cow extends Animal{
    constructor(){
        super("Cow")
    }

    makeSound(){
        console.log("Moo");
    }
}
```

Create some animals and print their sounds:
```js
let cat = new Cat()
let sparrow = new Sparrow()
let cow = new Cow()
makeSounds([cat, sparrow, cow])
```

Note that we did not touch the `makeSounds` function!!