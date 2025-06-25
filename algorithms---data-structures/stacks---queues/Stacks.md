
A stack is a data structure similar to an array, but:

-   You can only ever access the **top** of the stack (i.e the last item that was entered)
-   You can only ever remove the **top** of the stack
-   You cannot modify a stack's items (only add and remove)

  

In other languages, a Stack is built-in, like an `Array` is built into JS. In JS, there is no built-in stack, but we can build one according to the rules of a stack, i.e. the stack's "API".

  

A stack has four methods - these are the rules of how we **interface** with this data structure:

1.  `push(x)`
    - Adds an item to the **top** of the stack
2.  `isEmpty()`
    - Returns `true` if the stack is empty, `false` otherwise
3.  `peek()`
    - Returns the **top** item in the stack
4.  `pop()`
    - Returns the **top** item in the stack **and** removes it

Because we can base a stack off an array, you can think of the **last** item in the array as the **top** of the stack.