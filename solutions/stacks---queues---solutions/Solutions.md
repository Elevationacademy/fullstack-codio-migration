## Exercise 1


```
class Queue {
	  constructor() {
	    this.queue = []
	    this.length = 0
	  }
	  enqueue(number) {
	    this.queue.unshift(number)
	    this.length++
	  }
	  isEmpty() {
        return !!!this.queue.length	    
	  }
	  print() {
	    console.log(this.queue)
	  }
	  peek() {
	    return this.queue[this.length - 1] || null
	  }
	  dequeue() {
	    this.queue.pop()
	    this.length--
	  }
}

```


## Exercise 2


```
const Stack = require('./Stack')

class MinStack extends Stack {
  constructor() {
    super()
    this.min = new Stack()
  }

  push(x) {
    if (this.isEmpty()) {
      this.min.push(x)
    } else if (x < this.min.peek()) {
      this.min.push(x)
    }

    super.push(x)
  }

  pop() {
    if (this.isEmpty()) {
      return null
    } else if (this.peek() === this.min.peek()) {
      this.min.pop()
    }

    return super.pop()
  }

  getMin() {
    return this.min.peek()
  }
}
```


## Exercise 3


```
let Queue = require('./Queue')
	class DuoQueue extends Queue {
	  constructor() {
	      super()
	      this.q1 = new Queue()
	      this.q2 = new Queue()
	  }
	

	  _qName(qNum) {
	      return `q${qNum}`
	  }
	

	  enqueue(person, qNum) {
	      this[this._qName(qNum)].enqueue(person)
	  }
	

	  dequeue(qNum) {
	      this[this._qName(qNum)].dequeue()
	  }
	

	  getLongestQueue() {
	      if (this.q1.length === this.q2.lenght) {
	          return "both equal"
	      } else {
	          return this.q1.length > this.q2.length ? this.q1 : this.q2
	      }
	  }
	

	  getShortestQueue() {
	      if (this.q1.length === this.q2.lenght) {
	          return "both equal"
	      } else {
	          return this.q1.length < this.q2.length ? this.q1 : this.q2
	      }
	  }
	

	  balanceQueues() {
	

	      let longestQueue = this.getLongestQueue()
	      let shortestQueue = this.getShortestQueue()
	

	      while ((longestQueue.length - shortestQueue.length) > 1) {
	          shortestQueue.enqueue(longestQueue.peek())
	          longestQueue.dequeue()
	      }
	  }
	

	  print() {
	      console.log("Queue 1: ")
	      this.q1.print()
	      console.log("Queue 2: ")
	      this.q2.print()
	  }
}
```