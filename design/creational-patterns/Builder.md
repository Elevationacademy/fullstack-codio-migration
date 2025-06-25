The builder pattern is a very common pattern that allows us to build an object gradually in a step-by-step fashion.
It is very useful when an object requires complex initialization and/or many parameters.
The builder is an alternative to having a huge parameter list at the constructor.

Let's look at a simple example.
```
class Person {
    private id: number;
    private firstName: string;
    private lastName: string;
    private phone: string;
    private address: string;
    private height: number;
    private weight: number;
    private age: number;
}
```
This is a `Person` class that has 8 fields.
We could simple use an 8 parameter constructor but it would not be very user friendly.

Using a builder we can provide default values, easily express mandatory vs. optional properties and give the user an easy way to instantiate our class.

Example with builder:
```
class Person {
  private id: number;
  private firstName: string;
  private lastName: string;
  private phone: string;
  private address: string;
  private height: number;
  private weight: number;
  private age: number;

  public static Builder = class {
    //Required Parameters
    private id: number;
    private firstName: string;
    private lastName: string;

    //Optional Parameters (with defaults)
    private phone: string = '123-456-789';
    private address: string = 'Street 1, City';
    private height: number = 1.7;
    private weight: number = 75.5;
    private age: number = 30;

    constructor(id: number, firstName: string, lastName: string) {
      this.id = id;
      this.firstName = firstName;
      this.lastName = lastName;
    }

    setPhone(phone: string) {
      this.phone = phone;
      return this;
    }

    setAddress(address: string) {
      this.address = address;
      return this;
    }

    setHeight(height: number) {
      this.height = height;
      return this;
    }

    setWeight(weight: number) {
      this.weight = weight;
      return this;
    }

    setAge(age: number) {
      this.age = age;
      return this;
    }

    build(): Person {
      return new Person(this);
    }
  };

  private constructor(builder) {
    this.id = builder.id;
    this.firstName = builder.firstName;
    this.lastName = builder.lastName;
    this.address = builder.address;
    this.phone = builder.phone;
    this.height = builder.height;
    this.weight = builder.weight;
    this.age = builder.age;
  }
}
```
Here is an example of using the builder.
```
const mosheCohen = new Person.Builder(12345, 'Moshe', 'Cohen')
  .setAddress('Rambam 12, Givatayim')
  .setAge(40)
  .build();
```
You can see that not all of `Person` fields are used in this case, some of them will get default values as provided in the class.

Let's talk about the builder implementation:
- It has a constructor containing the required parameters.
Since we cannot instantiate `Person` without `firstName`,`lastName`, and `id`, these parameters are required in the builder constructor.
```
    constructor(id: number, firstName: string, lastName: string) {
      this.id = id;
      this.firstName = firstName;
      this.lastName = lastName;
    }
```
- The non-required parameters are assigned default values
```
    private phone: string = '123-456-789';
    private address: string = 'Street 1, City';
    private height: number = 1.7;
    private weight: number = 75.5;
    private age: number = 30;
```
- Every optional parameter has a setter method, but this is not your usual setter method.
The setter method returns `this` which is the instance of the builder.
That's how we can chain methods together while using the same instance.
```
    setWeight(weight: number) {
      this.weight = weight;
      return this;
    }
```
- Finally we have the `build()` method which will return the actual instance ofter constructing it using a private constructor of the `Person` class.
```
    build(): Person {
      return new Person(this);
    }
```
- The private constructor is not a part of the `Builder` class but still a part of its implementation.
It accepts the builder and initializes a new instance using parameters from the builder.
```
  private constructor(builder) {
    this.id = builder.id;
    this.firstName = builder.firstName;
    this.lastName = builder.lastName;
    this.address = builder.address;
    this.phone = builder.phone;
    this.height = builder.height;
    this.weight = builder.weight;
    this.age = builder.age;
  }
```
Notice that this constructor is private because we only want to use it via the `build()` method of the builder and not enable users to access it directly in the client code.

If you are curious, a possible JavaScript implementation for this pattern could be:
```
class Person {
  constructor(builder) {
    this.id = builder.id;
    this.firstName = builder.firstName;
    this.lastName = builder.lastName;
    this.address = builder.address;
    this.phone = builder.phone;
    this.height = builder.height;
    this.weight = builder.weight;
    this.age = builder.age;
  }
}

Person.Builder = class {
  constructor(id, firstName, lastName) {
    // Required Parameters
    this.id = id;
    this.firstName = firstName;
    this.lastName = lastName;

    // Optional Parameters (with defaults)
    this.phone = '123-456-789';
    this.address = 'Street 1, City';
    this.height = 1.7;
    this.weight = 75.5;
    this.age = 30;
  }

  setPhone(phone) {
    this.phone = phone;
    return this;
  }

  setAddress(address) {
    this.address = address;
    return this;
  }

  setHeight(height) {
    this.height = height;
    return this;
  }

  setWeight(weight) {
    this.weight = weight;
    return this;
  }

  setAge(age) {
    this.age = age;
    return this;
  }

  build() {
    return new Person(this);
  }
};

```