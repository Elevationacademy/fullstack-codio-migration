We can define the types that each piece of data should be in a class.

```
class Person {
  name: string;
  isProgrammer: boolean;
  children: number;

  constructor(n: string, c: boolean, p: number) {
    this.name = n;
    this.isProgrammer = c;
    this.children = p;
  }

  sayHello() {
    return `Hi, my name is ${this.name} and I have ${this.children} children`;
  }
}

const person1 = new Person('John', false, 2);
const person2 = new Person('Michael', 'yes', 4); // ERROR, Argument of type 'string' is not assignable to parameter of type 'boolean'.

console.log(person1.sayHello()); // => Hi, my name is John and I have 1 children
```