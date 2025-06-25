**Start by making a new class for nodes in a Binary Search Tree** - let's call it `BSNode`.

```
class BSNode {
    constructor(value) {
        this.value = value;
        this.leftChild;
        this.rightChild;
    }
}
```


Our constructor is roughly the same as before. A binary search tree is still a binary tree, only the value and two children: one `leftChild`, one `rightChild`

  

Our logic to insert a node should take the following steps:

1.  Check if there is a value to the current node
2.  See if the new value is greater than or less than the current node
3.  If there are children, go to the appropriate child, and compare again
4.  If there is no child in the right or left respectively, insert the node

  

Let's look a this method:

```
    insertNode(newVal) {
        if (!this.value) {
            this.value = newVal
        }
        else if (newVal > this.value && this.rightChild) {
            this.rightChild.insertNode(newVal)
        }
        else if(newVal <= this.value && this.leftChild) {
            this.leftChild.insertNode(newVal)
        }
        else if (newVal <= this.value) {
            this.leftChild = new BSNode(newVal)
        }
        else {
            this.rightChild = new BSNode(newVal)
        }
    }
```
  

Taking it section by section the code says the following:

1.  If the node doesn't have a value, make this the value
    - For instance, if the root node is made without a value
    - Since inserting a node will always start from our root node, **this** is referring to the root node first, and then subsequent nodes down the tree
2.  Otherwise, if the new value is greater than the value of the node **and** the node has a right child, let's **recursively** run this function on the right child
3.  Otherwise, if the new value is less than **or equal to*** the value of the node **and** there is a left child, let's recursively run this function on the left child
4.  Otherwise is the value is less than or equal to the value of the node (and there is no left child) let's **add a new node with the new value as the left child of this node**
5.  Otherwise, since we know the new value must be greater than the current node and there is no right child, we **add a new node with the new value as the right cild of this node**

  

*We are using `<=`, less than or equal to. If we insert a value that is already in our tree, it is added as a left child, the same behavior if it were less than.

  

Take a look at this gif again and make sure the above points make sense:

  

![](https://www.mathwarehouse.com/programming/images/binary-search-tree/binary-search-tree-insertion-animation.gif)

  

To understand how the recursion works here, take a look at the following visual representation:

  

Say we have this tree set up, and we’re about to insert a new node with the value of 2.

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/tree-recursion-base.png)

  

Starting at the root node (as we always do), we test whether the new value should go to the left or right of the node (the root). Because` 2 < 3`, we go left – this is where the recursion happens. When inserting into a BST, we keep going down the tree (taking a left or right) until we reach a node with no children.

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/tree-recursion-1.png)

  

Now we’ve reached the next node and we run the same check: do we go left or right? Since `2 > 1`, we’ll go right.

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/tree-recursion-2.png)

  

Finally, we’ve reached a node with **no children**, and we can **assign a new** **`rightChild`** **- this is where our recursion stops.**

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/tree-recursion-done.png)