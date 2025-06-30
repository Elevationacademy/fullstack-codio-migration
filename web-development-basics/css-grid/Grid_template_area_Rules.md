# Grid template area Rules

In the above example, we did not use the `grid-template-areas` (the one where we define a matrix of letters) property, so you might be wondering what is the point of this property. This property is useful when we are certain that we want a very specific layout.

  

However, when working with `template-areas`, there are some rules:

-   The matrix cannot be "tetris" shaped
-   In particular, the cells must create a **single** filled-in rectangle
-   Only **direct descendents** of the grid container (i.e the element that has `display:grid`) are considered **grid items**

  

The advantage of this property is that we can get very granular control of our layout. The disadvantage, of course, is that it is not dynamic. Let's talk about dynamic CSS Grid.