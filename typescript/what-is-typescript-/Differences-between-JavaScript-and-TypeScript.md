JavaScript is a **dynamically-typed** language, a forgiving language, allowing you to make mistakes and ultimately write a more free syntax, which is then hard to maintain and could cause defects.

The easiest way to explain dynamically-typed, is the fact that variables in JavaScript can change their type in run-time.

As an example, the following code works fine in JavaScript:
```js
let id = 0
id = "Tomer"
id = true
```

As you can see, the type is ‘dynamic’, meaning we can change the type of the variable from number to string to boolean. As you can also imagine, this could easily cause problems in your application. Enter TypeScript.

TypeScript is a **statically-typed** language, forcing you to write strict syntax and avoiding issues related to type errors.

If we try and run the above:
```js
let id = 0
id = "Tomer"
id = true
```

We will get a compile-time error in line 2 saying 
```console
Type 'string' is not assignable to type 'number'.
``` 
In addition to type-checking, TypeScript also provides extensive and configurable syntax-checking, which we’ll cover later in this course.
