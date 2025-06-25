You'll continue using the `BSNode` class you made during the lesson, so make sure you have your `constructor` and `insertNode` method.


## Exercise 1 

#### FINDING A NODE
    
      
Lets write a `findNode` method for our class that **receives a value parameter** and returns `true` or `false` if that value exists in your tree.
    
You'll need to write this function recursively, similar to the `insertNode` function
    
      
Test your method with the same array from before: `const letters = ["H", "E", "S", "G", "L", "Y", "I"]`
    
```
const bsTree = new BSNode(...)
//insert nodes (same as in lesson)
    
//Use the following to test
bSTree.findNode("H") // should print true
bSTree.findNode("G") // should print true
bSTree.findNode("Z") // should print false
bSTree.findNode("F") // should print false
bSTree.findNode("y") // should print false - we didn't make the tree case sensitive!
```    
      
    
**Hint:** since you only want to `return` the final value's `true` or `false`, you need to `return` each recursive function.
    

## Exercise 2
    
Write a `findCommonParent` method for you class that takes two values that are definitely in your tree, and returns the closest common parent the two nodes have.
    
      
Test your `findCommonParent` method for a BS tree made made from the following array: `["J", "H", "R", "E", "S", "P", "G", "B", "L", "Y", "I"]`
    
```
const bsTree = new BSNode(...)
//insert nodes from array
    
bSTree.findCommonParent("B", "I") //should return "H"
bSTree.findCommonParent("B", "G") //should return "E"
bSTree.findCommonParent("B", "L") //should return "J"
bSTree.findCommonParent("L", "Y") //should return "R"
bSTree.findCommonParent("E", "H") //should return "J"
```    

## Exercise 3
    

This one is trickier. You're going to have a lot of `if` and `if elses`**. Try for at least 20 minutes before looking at the down below**.
    
      
    
Your method will need to do the following:
    
-   Recieve a value **and** parent parameter. We delete a node by removing it from its parent as a reference
    -   This means you should change the parent's child to `null`
-   Look for the value, recursively calling the method on its right or left child, based on if the the value is greater than or less than the node
-   Once the node is found there are one of three scenarios:
    -   If the node has no children, remove it as a reference from its parent
    -   If the node has one child, make the child node the reference of the parent node, effectively removing the current node
    -   If the node has two children, find the maximum value to the left of the node, replace that as the reference of the parent node, and remove the node you just moved
    
      
  
[Here's](https://www.cs.usfca.edu/~galles/visualization/BST.html) a nice tool for visualizing inserting, finding, and deleting a node from a binary search tree.
    
      

To check this, run this code:

```
const numbers = [8, 9, 12, 3, 5, 1, 11, 4];
let nodeWithOneChild = new BSNode();
numbers.forEach(n => nodeWithOneChild.insertNode(n));
console.log(nodeWithOneChild.removeNode(nodeWithOneChild, 9)); // will return tree like the first image (the 9 will be deletied) 
    
let nodeWithTwoChildren = new BSNode();
numbers.forEach(n => nodeWithTwoChildren.insertNode(n));
console.log(nodeWithTwoChildren.removeNode(nodeWithTwoChildren, 8)); // will return tree like the second image (the root will be 5) 
```    
      
<details>
<summary>
Click here to reveal some hints.  
</summary>
  
  <ol>
    <li>Remember the function takes both a node and its parent, but you'll always run it from the root of your tree, which has no parent. So, while you're recursively looking for your node to the in the beginning of your method, pass the recursive function both the <code>value</code>, and <code>this</code> as your parent.</li>
    <li>
      For the deletion of a node with two children, finding the minimum value should be a separate function, which checks to see if there is a <code>leftChild</code>
    </li>
    <li>
      Here is a written out logic for the delete:
      <ul>
        <li>   If the new value is less than the current value, and there is a left child, recursively run the function on the child and pass <code>this</code> as the parent</li>
    <li>  Otherwise if the value is less than the current value, return false - the value does not exist in this tree</li>
    <li>  Otherwise if the new value is greater than the current value, and there is a right child, recursively run the function on the child and pass <code>this</code> as the parent</li>
    <li>   Otherwise if the value is greater than the current value, return false = the value does not exist in this tree</li>
    <li>   
      Otherwise
        <ul>
    <li>   If there is no right child or left child, and this was the parent's right child, set the right child of the parent to <code>null</code></li>
          <li>   Otherwise if there is no right child or left child, and this was the parent's left child, set the left child of the parent to <code>null</code></li>
   <li>   Otherwise if there is right child and no left child, and this was the parent's right child, set the right child of the parent to the right child of the current node</li>
    <li>   Otherwise if there is right child and no left child, and this was the parent's left child, set the left child of the parent to the right child of the current node</li>
    <li>   Otherwise if there is no right child and there is a left child, and this was the parent's right child, set the right child of the parent to the left child of the current node</li>
    <li>   Otherwise if there is no right child and there is a left child, and this was the parent's left child, set the left child of the parent to the left child of the current node</li>
    <li>   Otherwise, set the value of this node to the minimum value of the right child, and then delete the node that is the minimum value of the right child</li>
     </ul>
       </li>
        </ul>
    </li>
  </ol>
</details>

    
      
    
    