
There are many different kinds of trees. Going off of the binary tree we previously built, we will now talk about **binary search trees**.

  

A binary search tree is a sorted binary tree - where **every node's left child is smaller than the value of its parent, and its right child is larger**.

  

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Binary_search_tree.svg/2000px-Binary_search_tree.svg.png)

  

Starting with a root node (8), every node we insert will check if it is smaller or bigger than the root node. If the node is smaller, we will check the left child and compare again, if the node is larger, we will check the right child and compare again, going down the tree until we find the right spot for insertion.

  

Let's see a gifical representation of this:

  

![](https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-insertion-animation.gif)

  

Now instead of having an `insertRight` or `insertLeft` function, we'll have an `insertNode` function, which will perform the aforementioned logic.