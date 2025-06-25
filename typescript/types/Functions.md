We can define what the types the function arguments should be, as well as the return type of the function.

```
// Calculate the circumference of a circle given its diameter
function circumference(diameter: number): string {
  return 'The circumference is ' + Math.PI * diameter;
}

console.log(circumference(10)); // => "The circumference is 31.41592653589793"
```

The same function, using ES6 arrow function.

```
const circumference = (diameter: number): string => {
  return 'The circumference is ' + Math.PI * diameter;
};
```

A function that doesn't return anything can be defined with return type `void`:

```ts
function printHello(name: string): void {
  console.log(`hello ${name}`);
}
```