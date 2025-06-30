# Global vs Local Scope

In the above example, `nextItem` was not available outside of the `if`, however, the `bag` variable _was available_ within the `if`.

  

That is because `bag` exists in the **global scope** - i.e. there is nothing binding the bag into any specific scope.
On the other hand, `nextItem` exists in its own, **local scope** - specifically, the scope of the `if`

  

Generally speaking, **a variable defined in the global scope is accessible from anywhere**.
Conversely, **a variable defined in a local scope is only accessible from its own scope**.

  

Given the following code, what do you expect to see in the console?

```js
let height = 1.73

const grow = function(){
  height += 0.1
}

grow()
console.log(height)
```
  

Because `height` is defined **globally**, then the `grow` function can certainly access `height`. Therefore, we will see `1.83` in the log - try this out yourself.

  

How about this?

```js
const getBaseHeight = function(){
  const height = 1.73  
  return height
}

const grow = function(){
  height += 0.1
}

grow()
```
  

Now we'll get an error again, because `height` is only defined locally within the scope of the `getBaseHeight` function. Therefore, the `grow` function has no idea what height is.
