# Adapter

An Adapter pattern acts as a connector between two incompatible interfaces that otherwise cannot be connected directly. An Adapter wraps an existing class with a new interface so that it becomes compatible with the client’s interface.

Using this pattern is necessary mostly when using closed classes that cannot be modified.
We can wrap this class using composition, and add the functionality required by the interface.

Lets look at an example (based on geeksforgeeks.org).
In this example, we have `Bird`s, who can `fly()` and `makeSound()`.
We also have a `ToyDuck` which can `squeak()`.

This is the `Bird` interface:
```
interface Bird {
  fly(): void;
  makeSound(): void;
}
```
This is the `Sparrow` class which implements the `Bird` interface:

```
class Sparrow implements Bird {
  fly(): void {
    console.log('Flying');
  }
  makeSound(): void {
    console.log('Chirp Chirp');
  }
}
```
This is the `ToyDuck` interface:
```
interface ToyDuck {
  squeak(): void;
}
```
And a `PlasticDuck` that implements the `ToyDuck` interface:
```
class PlasticDuck implements ToyDuck {
  squeak(): void {
    console.log('Squeak');
  }
}
```
These two interfaces, and the two implementing classes, have nothing to do with each other.
They don't have common methods or any relationship.
But what if, for our own reasons, we wanted to use a `Bird` as a `ToyDuck`?
Well, then we will need an adapter.

```
class BirdAdapter implements ToyDuck {
  private bird: Bird;

  constructor(bird: Bird) {
    this.bird = bird;
  }

  squeak(): void {
    this.bird.makeSound();
  }
}
```
This adapter wraps a `Bird`, and implements `ToyDuck`.
It uses the `Bird`'s `makeSound()` to implement the `ToyDuck` squeak.
Meaning that the client can now use a `Bird` as a `ToyDuck` since it now has the ability to `squeak()`.
For the client to use a `Bird` as a `ToyDuck`, it only needs to wrap it with our `BirdAdapter`:
```
const sparrow: Sparrow  = new Sparrow();
const toyDuck: ToyDuck  = new PlasticDuck();

const birdAdapter: BirdAdapter  = new BirdAdapter(sparrow);

console.log("Sparrow:");
sparrow.fly();
sparrow.makeSound();

console.log("ToyDuck:");
toyDuck.squeak();

console.log("BirdAdapter:");
birdAdapter.squeak();```
This code prints:
```
Sparrow:
Flying
Chirp Chirp
ToyDuck:
Squeak
BirdAdapter:
Chirp Chirp