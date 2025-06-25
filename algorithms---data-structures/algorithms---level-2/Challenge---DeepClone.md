# DeepClone

Create the deepClone function:
```function deepClone(obj) {}```
The function should receive an object or a primitive type, and duplicate them. Any change to the original object should not affect the cloned object.


**Example:**
```js
let x = {a: "b", a2: ["first", "second"]};
let y = {b: x, b3: ["firtsY", x]};
let z = deepClone(y);
```

**Solution:**
```js
{
    b: {
        a: "b",
        a2: ["first", "second"]
    },
    b3: ["firtsY", {
        a: "b",
        a2: ["first", "second"]
    },
    ]
};
```

