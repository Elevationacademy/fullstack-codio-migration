
Currently your `UniqueArray` only knows to handle primitive types.

  

Modify it so that it can work with any type of data.

  

How you do it depends on how you built `UniqueArray` in the first place, but likely you will have to:

-   Modify how your `exists` method works
    -   In particular, you'll have to determine how to compare objects to find a match
    -   **Hint:** `{x: 3} === {x: 3}` returns `false`
-   Modify your `add` method