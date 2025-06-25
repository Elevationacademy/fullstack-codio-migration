Generics is used by declaring that a function handles a specific type, that is defined during the function call. A Generic type is defined using the **<generic_alias>**, where the name of the Generic is defined between the greater-than and less-than symbols.

Once the Generic is defined, we would use this alias anywhere in the code. Notice the `<Type>` piece of code added adjacent to the function name. Notice also that we replaced the union type with the name of the Generic, `Type`.
```
function calc<Type>(num: Type): Type {
    return num;
}

const calc_num = calc(4);
const new_num = calc_num + 4; // No error is thrown.
```
The above example is considered Generic **type inference**. We’ve come across this term before. This means that TypeScript automatically determines the type by the arguments in the function call, and in this example, the compiler sees that we call the function with a *number*, therefore the Generic gets the type *number* at run-time.

### Explicit Generic definition
The more robust way of using Generics is by explicitly defining the type when calling the function. Notice the `<number>` statement adjacent to the *calc* function call.
```
function calc<Type>(num: Type): Type {
    return num;
}

const calc_num = calc<number>(4);
const new_num = calc_num + 4; // No error is thrown.
```
The same would be used for a ‘string’ and any other type.
```
function calc<Type>(num: Type): Type {
    return num;
}

const first_name = calc<string>('John');
const full_name = first_name + ' Sagi'; // No error is thrown.
```
