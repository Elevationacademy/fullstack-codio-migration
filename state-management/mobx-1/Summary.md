
The major advantage MobX is giving us _so far_ is having all of our data, and anything that can affect our data in a single place, our source of truth.

  

-   We mark anything we want MobX to track as `observable`
-   Any component which will render this data as an `observer`
    -   Note - if you have a component which does not interact (render or affect) the App's state in any way, it does not need to be an `observer`
-   Any function which can affect the App state should be a part of our store and be tagged as an `action`.

  

Great, let's get some practice!