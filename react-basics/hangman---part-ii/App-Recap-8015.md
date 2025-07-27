
Here's an overall recap of the app:

  

-   We have one `letterStatus` object in `App`'s `state`
    -   Each letter is initially mapped to a value of false, representing that it has **not** been selected
    -   Both `Letters` and `Solution` use this object to display their letters/underscores/crossed-out-letters according to their status
-   The `Letter` component calls `selectLetter` when a letter is pressed
-   The `selectLetter` method changes the status of the selected letter to true
    -   This change occurs through the `update` function, the second parameter of `useState`
-   Both `Letters` and `Solution` get updated automatically because the `update` function was called
    -   Now, whichever letter is mapped to true will be displayed differently

  

Huzzah for React's DOM re-rendering!

**Huzzah for useState!**

**Huzzah for re-usable components and separation of concerns!**

  

![](.guides/img/lesson-3.png)