
Now that we have a basic idea of a tree, let's build a basic tree!

  

We'll build a **binary tree**. Essentially a binary tree is one where each node has no more than two children.

  

Since there will never be more than two children, they are called the **left child** and **right child** of the node.

  

Since a Tree is a new data structure based off nodes, **let's create a node* class**.
*This might not be intuitive, but it will make sense as we go.

```
class Node {
    constructor(value){
        this.value = value;
        this.leftChild = null;
        this.rightChild = null;
    }
}
```
  

Each node should have its own `value`, a `leftChild`, and a `rightChild`. When creating an instance of a node, we don't know the relationship to other nodes yet, so the children are initially `null`

  

**Let's create an instance of our class**, our **root** node of the tree.

```
const root = new Node(3)
```
  

Now if we console log our `root` instance the console should show us the following:

```
Node { value: 3, leftChild: null, rightChild: null }
```
  

Because we only have one node on our tree, and node children, the current graph of our tree would look like this:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/root-node.png)

  

The instance of the class will hold our references to any children it has. So if our tree looked like this:

```
Node {
  value: 3,
  leftChild: Node { value: 1,
                    leftChild: null, 
                    rightChild: null 
                  },
  rightChild: Node { value: 5, 
                     leftChild: null, 
                     rightChild: null 
                   }
 }
```
  

Then the above code is the same as this visual representation of our Tree hierarchy, because the `leftChild` of the **root** node is `1`, and the `rightChild` is `5`:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/3-1-5-tree.png)

----------

  

Let's insert these nodes ourselves and add a method to our class that inserts a left child to a node:

```
insertLeft(value) {
        if (!this.leftChild) {
            this.leftChild = new Node(value);
        } else {
            let newNode = new Node(value);
            newNode.leftChild = this.leftChild;
            this.leftChild = newNode
        }
}
```
  

This method says the following:

-   If this node does not have a left child
    -   Make a new node as the left child with the new `value`
-   Otherwise:
    -   Make a new node with the new `value`
    -   Make the `leftChild` of the current (`this`) node the `leftChild` of the `newNode`
    -   Finally, make the new node the `leftChild` of the original node

  

To see this in action, let's create an instance of our tree, then insert a child:

```
class Node {
      constructor(value) {
            this.value = value;
            this.leftChild = null;
            this.rightChild = null;
      }
      insertLeft(value) {
            if (!this.leftChild) {
                  this.leftChild = new Node(value);
            } else {
                  let newNode = new Node(value);
                  newNode.leftChild = this.leftChild;
                  this.leftChild = newNode
            }
      }
}

//initial setup
let tree = new Node(3)
tree.insertLeft(1)
tree.insertRight(5)

//adding a new node to the tree
tree.insertLeft(2)
```
  

In the above we start by creating a new instance of a node with the value of 3.

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/root-node.png)


```
Node { value: 3, leftChild: null, rightChild: null }
```
  

Then we added new node (1) as the child of our root node (3).

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/two-nodes.png)


```
Node {
  value: 3,
  leftChild: Node { value: 1, leftChild: null, rightChild: null },
  rightChild: null 
}
```

Then we added a new node (5) as the child of our root node (3).

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/3-1-5-tree.png)


```
Node {
  value: 3,
  leftChild: Node { value: 1,
                    leftChild: null, 
                    rightChild: null 
                  },
  rightChild: Node { value: 5, 
                     leftChild: null, 
                     rightChild: null 
                   }
}
```

  

Then we insert a new node with a value of 2 as the `leftChild` of our root node (3). Since three already has a `leftChild`, we set the current left child (1) as the left child of our new node (2). Then we set our new node(2) as the child of our root node (3)

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/3-2-1-5-tree.png)


```
Node {
  value: 3,
  leftChild: Node {
     value: 2,
     leftChild: Node {value: 1, leftChild: null, rightChild: null },
     rightChild: null 
  },
  rightChild: Node { 
      value: 5, leftChild: null, rightChild: null 
  } 
}
```
  

Since `3.leftChild` no longer references 1, it is no longer the `leftChild` of 3. Now 2 is the `leftChild` of 3, and and 1 is the `leftChild` of 2.

  

We can add a similar function for `insertRight` and our class should look like the following:


```
class Node {
    constructor(value){
        this.value = value;
        this.leftChild = null;
        this.rightChild = null;
    }
    insertLeft(value) {
        if (!this.leftChild) {
            this.leftChild = new Node(value);
        } else {
            let newNode = new Node(value);
            newNode.leftChild = this.leftChild;
            this.leftChild = newNode
        }
    }

    insertRight(value) {
        if (!this.rightChild) {
            this.rightChild = new Node(value);
        } else {
            let newNode = new Node(value);
            newNode.rightChild = this.rightChild;
            this.rightChild = newNode
        }
    }
}
```