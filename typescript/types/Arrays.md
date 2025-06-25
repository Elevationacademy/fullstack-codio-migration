In TypeScript, you can define what type of data an array can contain. You do that by adding opening and closing square brackets next to the variable type.


```ts
let ids: number[] = [1, 2, 3, 4, 5]; // array of type 'number'
let names: string[] = ['Danny', 'Anna', 'Bazza']; // array of type 'string'
let options: boolean[] = [true, false, false]; // array of type 'boolean'

ids.push(6); // OK
ids.push('7'); // ERROR: Argument of type 'string' is not assignable to parameter of type 'number'.
```