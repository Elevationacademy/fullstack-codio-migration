
In this lesson we covered the following ideas:

-   How to handle user events (clicks, etc)
-   How to update state using the hook set method
      -   We noted that each change of state will **re-render** our DOM
      -   We also noted that we had to use the spread operator ... when modifying reference types from `state`
-   The asynchronicity of the hook `set method`.

  

Before beginning, remember the rules of working with React components:

-   If a component receives `props`, its parent must pass those `props` down
-   You can pass anything down through `props`: strings, numbers, arrays, objects, _methods_
-   Anything accessed from props must be accessed by adding props in the functions paramters.
-   Do **not** mutate state directly