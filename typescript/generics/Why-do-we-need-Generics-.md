Until now, we’ve learnt that supporting multiple types in TypeScript is based on using union types, and the below code would work great in this scenario.
```ts
let calc_num: string | number = 3;
const new_num = calc_num + 4; // No exception as in the previous line we initialized the type to be number
```
And this would also work fine with a string initialization.
```ts
let calc_num: string | number = "John";
const new_num = calc_num + "Smith"; // No exception as in the previous line we initialized the type to be string

```
But when we use functions, its parameters’ and return types are only defined during run-time. In this instance, TypeScript will throw compile-time errors as the returned type is ‘undefined’.

### Run-time type setting problem using unions
If we use unions with functions, an error will be thrown “Operator '+' cannot be applied to types 'string | number' and 'number'”. This basically means that TypeScript can’t determine, during compile-time, what type will be returned.
```ts
function calc(num: string | number): string | number {
    return num;
}

const calc_num = calc(4);
const new_num = calc_num + 4; // ERROR: Supposed to be a 'number' type, but throws an error
```
