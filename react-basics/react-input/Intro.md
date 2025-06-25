
In this quick lesson we'll go over how to capture user input.

  

The "problem" with getting user input in React is that we want our `state` to be our **single source of truth** - that is, any information about or generated in a component should be kept in its state.

  

However, DOM elements such as `input`, `text-area`, and `select` have their own form of "state" where they keep the current value of their input inside the element (remember `event.target.value`?)

  

To make sure that we only work with `state`, we will bind the value of the element to `state`, as well as update the `state` each time the value of the element changes.

  

This is called **two-way binding**, and we'll see it in code in a second.

  

For this lesson, you must have a good understanding of:

-   Components
-   The `useState` hook
-   The `useState` set method