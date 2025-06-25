In this exercise you will create your own `Stack` class, implementing the methods above.

  

Firstly, go to [this](https://github.com/Elevationacademy/stacks-queues-lesson-exercises) repo, fork it, clone it, and run `npm install`.

  

In the `src` folder you will find a file called `Stack.js`. Your goal is to create a full functioning `Stack`.

  

*Make sure the name of the class is 'Stack' and that the constructor has two properties: `stack` - an empty array, and `length` - an integer.

  

For the sake of debugging, **add a** `print` **method** that prints the entire stack.

  

Remember that when you create custom data structures based off arrays, you **shouldn't** use built-in array methods/properties. The [delete](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/delete) operator will be helpful.

  

Please give this a good 30-40 minutes before checking the solution, and use the following to check your work:

```
let myStack = new Stack()
console.log(myStack.isEmpty())    //true
myStack.print()                    //[]
myStack.push(2)      
console.log(myStack.isEmpty())     //false
myStack.push(4)      
myStack.print()                    //[2,4]
console.log(myStack.peek())        //4
myStack.pop()
myStack.pop()
console.log(myStack.peek())       //null
console.log(myStack.isEmpty())    //true
```
  

[Click here](https://codepen.io/ElevationPen/pen/mZrNyG?editors=0010) if you need help.