The facade pattern's purpose is to simplify the usage of a complex inner system or module.

When we have a process that requires many internal actions we can group them by functionality inside a facade class.
This will allow us to use the facade class instead of performing all our actions separately.
Let's look at an example.

I want to make coffee!
My program has a `Cow` that gives `Milk`, a coffee machine that makes `Foam` from `Milk`, my coffee machine also makes `Coffee` from `CoffeeBeans` and a `Storage` that has `Cup`s in it.
To make a cappuccino, I need to operate a complex process which looks like this:
```
const milk: Milk = new Cow().getMilk();
const coffeeMachine: CoffeeMachine = new CoffeeMachine();
const foam: Foam = coffeeMachine.makeFoam(milk);
const coffee: Coffee = coffeeMachine.makeCoffee(new CoffeeBean(2));
const storage: Storage = new Storage();
const cup: Cup = storage.getCup();
cup.add(coffee);
cup.add(foam);
```
This is where the facade comes in!
A facade is a class that wraps this code into one method.
It makes the same logic easier to use.

This is how our `BaristaFacade` is implemented:
```
class BaristaFacade {
  private cow: Cow = new Cow();
  private coffeeMachine: CoffeeMachine = new CoffeeMachine();
  private storage: Storage = new Storage();

  makeCappuccino(): Cup {
    const milk: Milk = this.cow.getMilk();
    const foam: Foam = this.coffeeMachine.makeFoam(milk);
    const coffee: Coffee = this.coffeeMachine.makeCoffee(new CoffeeBean(2));
    const cup: Cup = storage.getCup();
    cup.add(coffee);
    cup.add(foam);
    return cup;
  }
}
```
And the client ca use it like this:
```
const baristaFacade: BaristaFacade = new BaristaFacade();
const cup: Cup = baristaFacade.makeCappuccino();
```

Now, the client can get the cappuccino without going through all the steps one by one.
Of course, the steps are performed exactly as before, but now, our `BaristaFacade` performs it instead.

### Drawbacks
Facade is a very useful pattern, still, it has it's drawbacks.
It forces us to maintain another abstraction layer.
Since the facade does a lot of work internally, it is harder for this layer to provide flexibility.
What if I want cappuccino with extra foam?
What if I want no foam at all? etc...
Of course we can implement overloads and other methods in the facade. We just need to make sure we keep it useful.