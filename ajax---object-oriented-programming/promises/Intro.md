
In this short lesson, we're technically not learning anything new. We're going to learn a _different_ way to work with asynchronous code.

  

At a different point in the course we learn _another_ way to work with async code, each has their advantages. Today is about **promises.**

  

----------

  

#### **DEFINITION**

  

As per the [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise), **a promise is an object representing the _eventual_ completion or failure of an asynchronous operation**.

  

We'll see exactly what that means soon, but generally we use promises to help us avoid using too many **callbacks.**

  

Now, to be clear, **a promise still uses a callback** eventually - but it helps us avoid what's known as **callback hell**.