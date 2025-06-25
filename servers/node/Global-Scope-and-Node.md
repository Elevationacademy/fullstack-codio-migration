
Remember that within the browser, any variables in the "global" scope are assigned to the window object. In Node, they are assigned to the module of the file unless you _explicitly_ assign them to the module.exports object.

  

If, for some reason, you forget to declare a variable with a let or const, it will be assigned to the global scope and accessible by any file. **Don't do that!**

  

Try it now. Remove the const from title inside of circleUtils.js and console log it from shapesApp.js. It works, but be warned doing **this can lead to the appearance of bugs which are very hard to find**.

  

----------

  

This has been your soft intro to node. Again, node is **nothing more than a JS runtime environment**. It is **not** a language, a server, or a genie. We can _use it_ to run JS, to create servers, and to work wonders, but in and of itself it only gives us the required foundations.

  

If you'd like to know more about what's going on behind the scenes in node, [here's something](http://www.c-sharpcorner.com/article/node-js-v8-javascript-engine-day-one/) with a little more depth.

  

For now, let's put our knowledge of debugging & modules in node to some practice.