If you really want a mental workout, say goodbye to your `DuoQueue` and create a general purpose `MultiQueue` data structure.

  

This data structure has all the same methods as before, but instead of a hard-coded _two_ queues, it manages any _n_ number of queues - this should be decided in the constructor, like so:

```
let mq = new MultiQueue(4)
console.log(mq.queues) 
/*
[  
  Queue { queue: [] },
  Queue { queue: [] },
  Queue { queue: [] },
  Queue { queue: [] } 
]
*/
```