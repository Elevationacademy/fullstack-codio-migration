
Queues are similar to stacks, but "backwards". Instead of LIFO, we use FIFO: the first item in the queue is the first to get out.

  

In an actual application, you might use a queue to determine which order customer tickets come in - first one in, first one to get handled by your customer support team.

  

The rules of a queue, its methods, are as follow:

1.  `enqueue(x)`
    - Adds an item to the queue
3.  `isEmpty()`
    - Returns `true` if the queue is empty, `false` otherwise
5.  `peek()`
    - Returns the **front** item in the queue
7.  `dequeue()`
    -   Returns the **front** item in the queue **and** removes it

  

Because we can base a queue off an array, you can think of the **first** item in the array as the **front** of the queue.

  

----------

  

That's it for stacks and queues, excepting the practice you're about to work on. So let's get to work.