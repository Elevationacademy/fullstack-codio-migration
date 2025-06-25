### TypeScript's primitive types
There are seven primitive types in TypeScript and they are immutable (meaning they cannot change after assignment). Out of the seven primitives, there are five which are the most common (the other two primitives are *bigint* and *symbol*, but are rarely used):
- string
- number
- boolean
- undefined
- null
 
### TypeScript's type handling
To core to TypeScript is in its **type** handling. Through its 'compiler', it ensures all variables have a defined type and that their behavior, and restrictions are preserved. If a violation occurred, a compiler error is generated.

Generally, you would define a type for each variable using the following syntax: 
`const/let <var name>: <type> = <value>`   

Below is an example of assigning the type *boolean* to the variable *hasDog*, and when trying to change its value to a *string*, we get an error.
```
let hasDog: boolean = true; // Assigning type 'boolean'
hasDog = 'yes'; // ERROR
```

### The 'any' type
TypeScript also has a type called *any* which basically means, it has no specific type, and will **not** be type-checked. It's not recommended to use this, and should only be used in rare cases during development.