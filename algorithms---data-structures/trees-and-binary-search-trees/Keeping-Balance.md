
Remember we mentioned the **height** of a tree and the **depth** of a node?

  

The **height** of the tree is the longest number of **edges** (connection between nodes), and the **depth** of a specific node is the number of **edges** from that node to the **root**

  

**Balance** in trees is used to describe if the number of levels on the tree is even or uneven. If example, The following tree has 4 levels and is perfectly balanced - the **depth** of all the **leaf** nodes is the same:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/balanced-tree.png)

  

In an unbalanced tree, some of the **paths** from the root to a leaf will be much longer than others - like so:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/unbalanced-tree-2.png)

  

Whether a BST is balanced or unbalanced depends on how it's data is input.

  

If you were to insert an array of sorted numbers from smallest to largest into your BST, every new node would be the right child of the previous node.

  

For example, if you have an array of sorted numbers `[1, 2, 3, 4, 5, 6, 7, 8, 9]` and create a BST with each one as a node, in order of the array, the next value will always be larger than the previous, and will always be the right child. Your tree will end up looking like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/unbalanced-tree.png)

  

Searching through this tree is just **O (n)**, and we lose the benefits of having a BST in the first place. In fact, this data structure is now more similar to a [linked list](https://www.geeksforgeeks.org/linked-list-set-1-introduction/) than a Tree.

  

So in a best case scenario (where we have a balanced BST), searching has a complexity of **O( log(n) )**. In the worst case (totally unbalanced) it has a complexity of **O (h)**, where **h** is the height of the tree.

  

There are other types of trees which are **auto-balancing** such as [AVL trees](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/) and [red-black trees](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/). This means that as you insert a node, the tree will automatically adjust itself to maintain the lowest number of levels, the shortest height possible. These are harder to create so we won't go into them.

  

For now, the easiest way to maintain balance is to input a random set of data.