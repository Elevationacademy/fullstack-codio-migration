
A quick reminder, the **Virtual DOM** is one of the core benefits of React and worth knowing about.

  

-   Whenever a component `renders` , an object that is a copy of the current DOM is created
    -   React does all of its manipulations on this _virtual_ DOM first
-   Then, React will compare the updated virtual DOM with a previous snapshot of the virtual DOM that was taken right before the update - this process is called **reconciliation**
-   Finally, React will only update nodes in the physical DOM that are _different_ from its virtual DOM

  

After these updates to the physical DOM, then the `useEffect` callbacks are called, if their dependencies have changed.

  

You can read more about the Virtual DOM [here](https://programmingwithmosh.com/react/react-virtual-dom-explained/) - very interesting stuff.

  

#### **useEffect( ()=> {**

 

A short and sweet lesson on React's lifecycle. 
Final note:

With the exception of making API calls, you generally shouldn't be interacting with `useEffect` unless you have a good reason to (usually for improving performance). In other words, don't piggy-back on this hook to fix things that aren't working.

  

That's all - a bit of under the hood for you!

  

#### **, []}**