One of the most critical concepts of good software engineering is the ability to develop reusable code. Making code reusable also requires us to allow the code to work with multiple types.

Earlier we got familiarized with type unions, allowing us to define multiple types for a variable. This works well in a single block of code, as we would need to initialize a variable with a value, and therefore its type, but when we use functions and classes, the arguments and return value types are only defined at run-time. This causes TypeScript to throw many compile-time errors. And this is where Generics come to the rescue.

In this lesson we will learn:
1. Why do we need Generics?
1. Using Generics with functions
1. Using Generics with classes