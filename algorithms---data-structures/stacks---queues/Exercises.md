
## Exercise 1

In this exercise you will implement a `Queue` class - for this one, you can use some array methods; it should be quite trivial.
    
      
    
In the `src` folder there is a file called `Queue.js`.
    
*Please make sure the name of the class is 'Queue' and the constructor has two properties: `queue` - an empty array, and `length` - an integer.
    
      
** Note, you **can** use the _typical_ array methods in this question (splice, unshift, push, etc..).
    
      
Use the following to check your code:
    
```
let q = new Queue()
console.log(q.isEmpty())    //true
q.print()                   //[]
q.enqueue(2)
console.log(q.isEmpty())    //false
q.enqueue(4)
q.print()                   //[2, 4]
console.log(q.peek())       //2
q.dequeue()
q.dequeue()
console.log(q.peek())       //null
console.log(q.isEmpty())    //true
``` 

## Exercise 2

Now you will implement a `MinStack` class.
    
This class should work the same as a `Stack`, but it **should also have a** `getMin( )` **method**.
    
      
This method should **return the minimum value of the** `MinStack`, no matter where the value is in the stack.
    
Furthermore, the `getMin( )` method **must have a time complexity of O( 1 ).**
    
Yes, this is tricky. Yes, you have to think creatively. Maybe even out of the box.
    
Create the class in a file called `MinStack.js` (located in the `src` folder)
    
Use this code to help check your work:
    
```
let ms = new MinStack()
ms.push(17)
ms.push(12)
ms.push(31)
console.log(ms.getMin())    //12
ms.pop()
ms.pop()
ms.pop()
console.log(ms.getMin())    //null
ms.push(19)
ms.push(21)
console.log(ms.getMin())    //19
ms.push(3)
console.log(ms.getMin())    //3
ms.pop()
ms.pop()
console.log(ms.getMin())    //19
```
      

<details><summary>
  If you've tried for at least an hour, and still haven't figured it out, use the following hint:
</summary>
  
Inside of `MinStack`'s constructor, initialize a property called `minValues` which is an empty `Stack`. Use this stack to help you track what the minimum value is at any given time.
  
<details><summary>
  If you're still stumped, here's another, more detailed hint:
</summary>
  
  ```
- Inside `MinStack` constructor, initialize a normal `Stack` called `minValues`
    - This is a "private" stack and will be used to store minimum values
  
- Every time there is a `push`, check (in other words, `peek` at) the `minValues` stack to see what the top value is
  
- If the value being pushed is smaller than the current minimum value (the top of `minValues`), then also `push` the new value to `minValues`
  
- Now create the `getMin( )` method
    - This is a simple function that returns `null` if the stack is empty, or the `peek`s of `minValues` otherwise
  
- The last thing we need to think about is `pop`
    - First of all, make sure to return `null` if our stack `isEmpty`
    - When we `pop` a value, if that value is also the current minimum we also have to `pop` the `minValues`
    - If it is not the current minimum, we can just pop normally
```
</details>
</details>
    

## Exercise 3
    
Create a data structure that will help you manage a grocery store with two checkout aisles.
    
It will be based off two `Queue`s, and as such you should called it `DuoQueue`.
    
You can write your `DuoQueue` in the `DuoQueue.js` file which can be found in the `src` folder.
    
Your `DuoQueue` should:
    
-   Have access to two `Queue`s
-   Have an `enqueue(person, qNum)` method that adds the person to the `qNumth` queue
-   Have a `dequeue(qNum)` method that dequeues from the `qNumth` queue
-   Have a `getLongestQueue( )` method that returns the longest queue
-   Have a `getShortestQueue( )` method that returns the shortest queue
-   Have a `balanceQueues( )` method that moves people from the longest queues to the shortest ones
    -   This movement should happen until the difference between the longest and shortest queue is 1 or less
    
      
*Please make sure the name of your class is `DuoQueue` and that the names of the methods are exactly as show above.
    
To make your life easier, you **may** hard-code `q1` and `q2` directly in `DuoQueue`'s constructor, if you wish.
    
      
Note that **all the methods must have a complexity of O( 1 )**, except for the `balanceQueues` method where you may use a while loop - **but you cannot access queue indexes**.
    
In other words, you cannot do something like `queue[3]` - queues have no indexes.
    
Use the following to check your code:
    
```
let dq = new DuoQueue()
    
//first set
dq.enqueue(1, 1)
dq.enqueue(1, 1)
dq.enqueue(1, 1)
dq.enqueue(2, 2)
dq.enqueue(2, 2)
dq.dequeue(1)
dq.dequeue(1)
    
console.log(dq.getLongestQueue()) //Queue { queue: [ 2, 2 ] }
console.log(dq.getShortestQueue()) //Queue { queue: [ 1 ] }
    
//second set
dq.enqueue(1, 1)
dq.enqueue(1, 1)
dq.enqueue(1, 1)
dq.enqueue(1, 1)
dq.enqueue(1, 1)
dq.enqueue(1, 1)
    
console.log(dq.getLongestQueue()) //Queue { queue: [ 1, 1, 1, 1, 1, 1, 1 ] }
console.log(dq.getShortestQueue()) //Queue { queue: [ 2, 2 ] }
    
//balance queues
dq.balanceQueues()
console.log(dq.getLongestQueue()) //Queue { queue: [ 1, 1, 1, 1, 1 ] }
console.log(dq.getShortestQueue()) //Queue { queue: [ 1, 1, 2, 2 ] }
```