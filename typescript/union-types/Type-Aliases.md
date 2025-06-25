You could take unions a step further and create an *alias* or an *interface* of a type, allowing you to 're-use' the same union definition in many places in the code using a simpler *alias* variable.

You would need to use the `type` keyword, following by the type alias, and the union.

```
type ID = number | string; // Type alias 'ID'

let returnedId: ID = 8; // OK
let newId: ID = '9'; // OK
```

We can also use interfaces - but we will cover it later.