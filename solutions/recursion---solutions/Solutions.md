## Exercise 1

```
const findFactorial = function(num, currentPorduct = num) {
	    if(num === 1 || num < 1) { return currentPorduct }
	

	    currentPorduct *= (num - 1)
	    num--
	

	    return findFactorial(num, currentPorduct)
}
```

## Exercise 2

```
const reverseString = function (str, newStr = '') {
	

	    if(str.length === 0) { return newStr }
	

	    newStr += str.slice(str.length - 1)
	    str = str.slice(0, str.length - 1)
	

	    return reverseString(str, newStr)
}
```


## Exercise 3

```
const swap = function(arr1, arr2) {
	    if(arr1.length === 0) { return }
	

	    arr2.push(arr1.splice(0,1)[0])
	

	    return swap(arr1, arr2)
}
```

## Extension

```
class Stack {
  constructor() {
      this.stack = []
      this.length = 0
  }

  push(x) {
      this.stack[this.length] = x
      this.length++
  }

  isEmpty() {
      return !!!this.length
  }

  peek() {
      return this.isEmpty() ? null : this.stack[this.length - 1]
  }

  pop() {
      if (this.isEmpty()) {
          return null
      } else {
        const elem = this.stack[--this.length]
        delete this.stack[this.length]
        return elem
      }
  }

  print() {
      console.log(this.stack)
  }
}


const swapStack = (stack1, stack2, temp = new Stack()) => {
  if(stack1.isEmpty() && temp.isEmpty()) { return }

  if (!stack1.isEmpty()) {
    temp.push(stack1.pop())
  } else {
    stack2.push(temp.pop())
  }

  swapStack(stack1, stack2, temp)
}
```