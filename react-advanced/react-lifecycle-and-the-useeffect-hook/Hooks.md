We have seen hooks before, and used them. 
Remember `useState`?
Now we will explain a bit more what it is all about.

**What is a hook?**

  

As the React documentation states:

>"A hook is a special function that lets you 'hook into' React features."

  
**Note:**
Whenever you encounter the term 'class,' it pertains to the old way in React using class components. However, we have now transitioned to using functional components.

React hooks allow us to use React features like state, lifecycle and more while using functional components. This means that we can use all of the React features without needing to write full classes.
Since functions are "stateless" by definition, hooks enable us to make these function components "stateful" just like class components.
  

There are many benefits to this, but just to state a few:

-   It is easier to use functional components with simple Javascript knowledge
-   There is no need to know how classes work in JS to use functional components, specifically:
    -   There is no need to constantly reference `this` when calling methods or accessing state
    -   There is no need to understand how `this` works in JS and bind `this` in every class method (or use arrow functions every time)
-   _If you'd like to read a more in-depth list of benefits you can read about them in the React docs_ [_here_](https://reactjs.org/docs/hooks-intro.html#motivation)_._

  

It is important to note that React has no plans to remove class components but they do believe that in the future hooks will be the primary way to write in React. That being said, you can use both class components and functional components (with hooks) in the same project; there is no problem with using them side by side.

  

----------

  

This lesson will focus on the _useEffect Hook._

  

Ready? Let's hook!