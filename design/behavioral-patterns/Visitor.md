The purpose of the visitor pattern is to allow us to add functionality to a class without major changes to the class itself.
The idea is that this extra functionality can be something not directly related to the core business logic of the class.

Let's take the example of a bakery,
We have a class for every appliance in the store such as the `Oven`, the `FoodProcessor`, the `Microwave` etc..
Each appliance has it's own logic and it's own process to make food and perform its core "business logic".
If we wanted to clean these appliances we could add a `clean()` method to each of them, but this is beside their main logic.
A lot of times we prefer not to alter existing working classes if we don't have to.
Adding a `clean()` method could affect these classes and if we decide that we want to make only minimal changes to these classes we could use a visitor that will be responsible for cleaning.
Moreover, let's say that in a week from now, we will also want to add a `repair()` method.
The visitor pattern allows us to do that easily without adding more logic or code to the classes.
By adding more visitors we can add more functionality without touching the classes themselves.

### Pattern Structure
- **Common element interface** - an interface that has the `visit()` method and is implemented by our appliance classes.
- **Concrete classes** - the actual appliance classes.
- **Visitor interface** - an interface implemented by every visitor.
- **Concrete visitor(s)** - implementation of visitors that add the functionality to the classes.

Let's continue with our bakery example.

### Common interface
This is our common `Appliance` interface.
It has only one method `visit()`, since the rest of the functionality of the classes implementing it is not common to all appliances.
```
interface Appliance {
  accept(visitor: Visitor): void;
}
```
### Concrete classes
Here is our `Oven` implementation.
The other appliances look very similar.
```
class Oven implements Appliance {
  private id: number;

  constructor(id: number) {
    this.id = id;
  }

  bakeBread(): void {
    console.log('Baking bread...');
  }

  accept(visitor: Visitor): void {
    visitor.visitOven(this);
  }

  toString(): string {
    return `Oven{id=${this.id}}`;
  }
}
```
### Visitor interface
Our visitor interface needs to have a method for each type it is going to visit.
```
interface Visitor {
  visitOven(oven: Oven): void;
  visitFoodProcessor(foodProcessor: FoodProcessor): void;
  visitMicrowave(microwave: Microwave): void;
}
```
We cannot simply have one `void visit(Appliance appliance);`, since every appliance gets a different implementation.
### Concrete visitor
In our example, the concrete visitor is a `CleaningVisitor` responsible for cleaning the appliances.
```
class CleaningVisitor implements Visitor {
  visitOven(oven: Oven): void {
    console.log(`Cleaning the oven ${oven}`);
  }
  visitFoodProcessor(foodProcessor: FoodProcessor): void {
    console.log(`Cleaning the food processor ${foodProcessor}`);
  }
  visitMicrowave(microwave: Microwave): void {
    console.log(`Cleaning the food microwave ${microwave}`);
  }
}
```

### Usage (client code)
This is how a client would use our system:
```
    public static void main(String[] args) {
        List<Appliance> appliances = new ArrayList<>();
        appliances.add(new Oven(1));
        appliances.add(new FoodProcessor(2));
        appliances.add(new Microwave(3));

        CleaningVisitor cleaningVisitor = new CleaningVisitor();
        for (Appliance appliance : appliances) {
            appliance.accept(cleaningVisitor);
        }
    }
```
This code will print:
```
const appliances: Appliance[] = [];
appliances.push(new Oven(1));
appliances.push(new FoodProcessor(2));
appliances.push(new Microwave(3));
const cleaningVisitor: CleaningVisitor = new CleaningVisitor();
for (const appliance of appliances) {
  appliance.accept(cleaningVisitor);
}
```
### Summary
It does require some work to implement the visitor pattern, but once implemented for one visitor, it is very easy to add other visitors and more functionality.
This pattern is a good solution for situations where we want minimal changes to existing classes.
### JavaScript
Possible JavaScript code for this pattern:
```
class Oven {
  constructor(id) {
    this.id = id;
  }

  bakeBread() {
    console.log('Baking bread...');
  }

  accept(visitor) {
    visitor.visitOven(this);
  }

  toString() {
    return `Oven{id=${this.id}}`;
  }
}

class Microwave {
  constructor(id) {
    this.id = id;
  }

  accept(visitor) {
    visitor.visitMicrowave(this);
  }

  toString() {
    return `Microwave{id=${this.id}}`;
  }
}

class CleaningVisitor {
  visitOven(oven) {
    console.log(`Cleaning the oven ${oven}`);
  }
  visitMicrowave(microwave) {
    console.log(`Cleaning the food microwave ${microwave}`);
  }
}

const appliances = [];
appliances.push(new Oven(1));
appliances.push(new Microwave(3));
const cleaningVisitor = new CleaningVisitor();
for (const appliance of appliances) {
  appliance.accept(cleaningVisitor);
}
```