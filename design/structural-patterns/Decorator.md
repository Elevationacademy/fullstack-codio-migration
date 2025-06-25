Decorator design pattern enables us to add functionality to an object without any alteration of its class.
Using a decorator is fairly simple yet very useful.

Let's take for example an icecream program.
Our program has the `IceCream` interface that has the `flavor()` method.
```
interface IceCream {
  flavor(): void;
}
```
We have a `Vanilla` class that implements this interface.
```
class Vanilla implements IceCream {
  flavor(): void {
    console.log('Vanilla');
  }
}
```
Now, if we wanted to add functionality to any class implementing `IceCream`, we can introduce a decorator.
First, we need an abstract class to act as the "base" of all decorators.
```
abstract class IceCreamDecorator implements IceCream {
  protected iceCream: IceCream;

  constructor(iceCream: IceCream) {
    this.iceCream = iceCream;
  }

  flavor(): void {
    this.iceCream.flavor();
  }
}
```
This class implements `IceCream` and also wraps an instance of `IceCream` (remember composition?).
Now, lets create a concrete decorator that adds maple syrup to any `IceCream`.
```
class MapleSyrupDecorator extends IceCreamDecorator {
  constructor(iceCream: IceCream) {
    super(iceCream);
  }

  flavor(): void {
    super.flavor();
    this.addMapleSyrup();
  }
  addMapleSyrup(): void {
    console.log('With maple syrup');
  }
}
```
This decorator adds one method `addMapleSyrup()` and uses it inside the `flavor()` method.
It still calls the `super.flavor()` thus "decorating" it but not replacing it.

That's it!

Now, lets look at the client code:
```
console.log("Plain vanilla:");
new Vanilla().flavor();
console.log("Decorated vanilla:");
new MapleSyrupDecorator(new Vanilla()).flavor();
```

This code will print:
```
Plain vanilla:
Vanilla
Decorated vanilla:
Vanilla
With maple syrup
```