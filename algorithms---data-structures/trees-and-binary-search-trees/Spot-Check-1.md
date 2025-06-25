
Using the `insertLeft` and `insertRight` methods, test your class by making the following tree:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/letter-tree.png)

  

Your output should look like this:

```
const H = new Node(...)
//left and right inserts
console.log(H)
//prints:

Node {
  value: 'H',
  leftChild: Node {
     value: 'E',
     leftChild: null,
     rightChild: Node { value: 'G', leftChild: null, rightChild: null } 
   },
  rightChild: Node {
     value: 'S',
     leftChild: Node { value: 'L', leftChild: [Node], rightChild: null },
     rightChild: Node { value: 'Y', leftChild: null, rightChild: null } 
  } 
}
```
  

You can [click here](https://codepen.io/ElevationPen/pen/QXKYaa?editors=0010) check our answer if you're stuck. But make sure to try it yourself first.