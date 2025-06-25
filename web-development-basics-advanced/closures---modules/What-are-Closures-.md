Richard Bovell sums up what a closure is nicely: A closure is an inner function that has access to the outer (enclosing) function’s variables.



So when we talk about closures we're just talking about regular functions that are nested inside some outer function. What makes them special is their persistent access to variables from the outer function, even when that function has finished executing.



When a function is finished executing, JavaScript's "garbage collection" cleans up the function and removes any variables inside of it. This is to save memory. However, if those variables are being accessed outside the function's scope somewhere else, they will stay around. This is closure. Let's look at an example:


```
const foo = function () {
  const x = 1

  const bar = function () {
    console.log(x) //notice this inner function using the outer function's variable
  }

  return bar
}

const baz = foo() //out here, x doesn't exist
baz() //but when we invoke baz, we're printing x!
```

Run this code, then try to console.log(x) - it's not defined, but baz is using it! Here's what's going on:



After compilation is done, the JS engine is ready to execute. 

It starts by setting the variable baz to the result of calling the function foo
The function foo gets called, initializing the variable x and the function bar (in its scope)
Finally, foo returns the function bar back to baz


Now baz is referencing the function bar 

When baz (bar) gets invoked, since it uses the variable x, foo's scope sticks around even though normally it would disappear. 

The number 1 is logged. Closure observed.



Let's look at another example. Copy/paste the following into your dev console - this will be an interactive example.


```
 const setCounter = function (num) {
  let counter = 0

  const count = function () {
    counter += num;
    console.log(counter)
  }

  return count
}

const increment = setCounter(2)
increment()
```

2 will be logged, that makes sense. Try to invoke the increment() function again. This time 4 is printed. The counter variable has been remembered via the closure.



Now in the console, type counter and press enter. What happens? Again, you get an error because counter is only available inside the setCounter scope except through our closure.