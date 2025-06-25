
A binary search tree is important because of the way we can "search" for a node within it.

  

Wikipedia defines a BST as:

  

_“A Binary Search Tree is sometimes called ordered or sorted binary trees, and it keeps its values in sorted order, so that lookup and other operations can use the principle of binary search” _

  

**A quick recap on binary search:** In binary search, **each iteration cuts the remaining input size by half** - just as with the array above where we always went to the _middle_ of the sub-array, then ignored an entire half of it.

  

In terms of **time complexity** _binary search runs in_ **O( log(n) )** - this means that given an input of length **n**, we can complete all our work in **log(n)** operations.

  

Since a binary search tree is built on this principle, finding, inserting, and deleting a value in a binary search tree has the same complexity. Let's see a gifical representation of this:

  

![](https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-sorted-array-animation.gif)

  

With each operation we do, we go either on to either the right child or left child and split the size of numbers we are looking through by **roughly** half, giving us the **O( log(n) )** complexity!

  

We say "roughly" because this depends how well balanced the tree is. Let's talk about this.