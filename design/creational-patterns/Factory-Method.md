The factory design pattern is used when we have a superclass with multiple sub-classes and based on input, we need to return one of the sub-class. This pattern takes out the responsibility of the instantiation of a class from the client program to the factory class.

Let's look at an example.
Say we have a shopping mall, this shopping mall can host a number of stores and they can be of different types.
Let's say we have 3 types of stores:
- Clothing Store
- Toy Store
- Furniture Store
Each store can have different construction logic and process.
Using the factory pattern we can leave the logic to the factory, and let the mall use the factory to get new stores of any type.
First, we need all the stores to have a common base, this can be an abstract class or an interface.
In this example we will use an interface.
```
interface Store {
  sell(): void;
}
```
So we have a `Store` interface that has one `sell()` method.
Great.
Now, let's create three implementations of this interface.
```
class ClothingStore implements Store {
  sell(): void {
    console.log('Selling clothes');
  }
}

class ToyStore implements Store {
  sell(): void {
    console.log('Selling toys');
  }
}

class FurnitureStore implements Store {
  sell(): void {
    console.log('Selling furniture');
  }
}
```
Now, we need to create our factory that will be able to generate stores for us.
```
enum StoreType {
  Cloths,
  Toys,
  Furnitures,
}

class StoreFactory {
  createStore(type: StoreType): Store {
    switch (type) {
      case StoreType.Cloths:
        return new ClothingStore();
      case StoreType.Toys:
        return new ToyStore();
      case StoreType.Furnitures:
        return new FurnitureStore();
    }
  }
}
```
The `createStore()` method will return an instance of the requested store.
Since this method returns an interface (or an abstract class, if we choose a different implementation), the user will be able to use it the same way for every type of store.
```
  const storeFactory = new StoreFactory();
  const store1: Store = storeFactory.createStore(StoreType.Toys);
  const store2: Store = storeFactory.createStore(StoreType.Cloths);
  store1.sell();
  store2.sell();
```
Here is our `Mall` code.
It creates a `StoreFactory` and uses it to instantiate 2 stores of different types.

### Main advantages
There are a few advantages to using this patters.
- It decouples the implementation of a specific type from the general usage of the interface.
Frequent changes to the implementation of any specific store will not affect the client code at all.
- Hiding the creation logic.
If we do not want to expose the logic of creating a new store to the user, the factory does that, and returns the final object, no questions asked.
- Extensibility.
It is very easy to add new types of stores, we just need them to implement the `Store` interface and add them to our factory method.