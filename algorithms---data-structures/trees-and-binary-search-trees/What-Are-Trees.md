
Trees are a non-linear data structure that organize their data hierarchically. Rather than having a simple start, end, and middle like an array, trees are arranged by **parent child relationships** - hierarchically.

  

Think of a Family Tree. Each spot on the tree has some sort of value and relationship (its parents and children).

  

This is **no right answer here**, because a tree is not organized linearly. For each spot on the tree, you can only tell what it is (the name), and if it has a relationship to other spots. E.g. Chronus + Rhea are:

-   The parents of Poseidon
-   The grandparents of Athena
-   The children of Uranus + Gaia

  

In Web Development, a tree you constantly work with is [**the DOM**](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction), your interaction with the HTML through JS. Each element consists of its parents, children, and siblings. This data structure allows us to traverse the DOM.

  

![](https://tuftsdev.github.io/WebProgramming/notes/dom_tree.gif)