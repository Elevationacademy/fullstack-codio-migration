![](https://4cawmi2va33i3w6dek1d7y1m-wpengine.netdna-ssl.com/wp-content/uploads/2018/07/Computer-science-fundamentals_6.1.png)

  

In this lesson we're going to cover two data structures that are quite popular in the world of programming: **Stacks**, and **Queues**.

  

Both of these data structures are similar to an array, but their uniqueness come from how we _insert_ and _retrieve_ data.

  

In JavaScript, the **call stack** is an excellent example of a stack - it is a data structure that holds all the functions to be executed in the program. The _last_ function to enter the stack is the _first_ one to get out of it. We call this **LIFO - last in, first out**.

  

JS also has an **event queue** - this is (briefly) where asynchronous operations "wait" for the **call stack** to clear before they are added to the stack themselves. These operations come out of the queue in the order that they came in. We call this **FIFO - first in, first out** - and this is how **queues** work in general.

  

We're going to talk about these data structures a bit, and then **you will implement your own stack and queue**. It will be popping.