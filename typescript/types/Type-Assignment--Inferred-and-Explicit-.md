

### By-inference type assignment
Variables that are assigned values will automatically receive a type from the TypeScript complier, namely *inferred*.

```
let id = 5; // Inferred as 'number'
let firstname = 'danny'; // Inferred as 'string'
let hasDog = true; // Inferred as 'boolean'
```

### Explicit assignment
Most often, and what is recommended best-practice, is to explicitly assign a type to each variable.

```
let id: number = 5;
let firstname: string = 'danny';
let hasDog: boolean = true;
```