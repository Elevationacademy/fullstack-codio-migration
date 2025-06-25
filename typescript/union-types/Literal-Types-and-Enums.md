### Literal types (soft-typed)

You can also define literal type unions, allowing you to restrict variables to specific values. The below example shows you how to restrict a variable to specific values. You can also include multiple types using this definition.

This method of literal types is considered softly-typed, as the restriction is value-based. The ‘enum’ directive allows you to define a hard-typed list of possible type assignments. Keep reading for more information.

```
let favouriteColor: 'red' | 'blue' | true | 12;

favouriteColor = 'blue';
favouriteColor = 'crimson'; // ERROR, Type "crimson" is not assignable to type 'red' | 'blue' | true | 12.
```

### Literal types (hard-typed) / enum
Using the ‘enum’ directive, you can define hard-typed types, making sure the code is clearer and that types are syntax-based and not value-based. Enums are often used with incremental numbers, allowing you just to define the starting number, and TypeScript will fill-in the remaining numbers sequentially.

```
enum Direction {
  Up = 1,
  Down,
  Left,
  Right,
}

console.log(Direction.Down); // => 2
```
It’s also possible to define other enum types such as strings.
```
enum Direction {
  Up = "UP",
  Down = "DOWN",
  Left = "LEFT",
  Right = "RIGHT",
}

console.log(Direction.Up); // => UP
```
