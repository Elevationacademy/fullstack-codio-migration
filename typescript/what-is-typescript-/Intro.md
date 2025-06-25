TypeScript is a compiled language that enhances JavaScript. It brings type-checking and syntax-checking superpowers to JavaScript.

By saying TypeScript henhances JavaScript we mean that you write TypeScript code, which is then **transpiles** (being translated) into standard JavaScript code that can be run in any JavaScript-enabled environment. 


|||info
## Compiler vs Transpiler
---
**Compiler** -  translates code from a programming language to Machine language.
**Transpiler** - translates code from one programming language to another programming language
|||

Let’s look at an example. You will see some unfamiliar syntax, that includes types, we will explain it later. 

This TypeScript code:
```
const first_name: string = "John"
let age: number
age = 2
```

Is transpiled to standard JavaScript:
```
"use strict";
const first_name = "John";
let age;
age = 2;
```

Notice the unique type declarations in the TypeScript code that are ‘omitted’ in the JavaScript output. The reason for that, is that we don’t have types in JavaScript.

TypeScript makes sure you write better code which keeps to standards, easily understood by others, improves your application’s robustness, and reduces amounts of defects.

In this lesson we will be covering the differences between JavaScript and TypeScript, what are the benefits of using it, and where can we use it.

### Topics covered:
1. Differences between JS and TS
1. Benefits of TypeScript