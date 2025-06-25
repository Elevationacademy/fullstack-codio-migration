
JavaScript is a language that employs **garbage collection**.

Garbage collection helps developers manage memory by releasing unused variables and objects from memory automatically.

  

When a function is invoked, it takes up place in memory. Once the function is over, all the variables declared in the function are no longer relevant, so they are set free by the garbage collector.

  

That's "normal" JS behavior. On the other hand, **closures prevent the memory from setting variables free**.

You should be very careful when returning a function from a function. Memory leaks in javascript is a very sensitive subject.

  

You can read more about closures and memory [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Memory_Management) and about memory leaks in general [here](https://medium.com/preezma/memory-leaks-in-javascript-and-how-to-avoid-them-63916a02f68).