
Handling user events is quite simple in React. In fact, it looks very similar to how we handle events with plain DOM.

  

Say we had a component with a button, and we wanted to invoke some function when the button is clicked. It's as simple as this:

  
```
import React from 'react';

const App = () => {
  const logClick = () => {
    console.log("I was clicked!")
  }

  return (
    <button onClick={logClick}>Click me</button>
  );
}

export default App;

```
  

A few points on syntax:

-   You must camelCase the `onClick` - it's different from the `onclick` in normal DOM
-   You do **not** invoke the method in the `onClick` with parentheses
    -   You only pass the function object, just like we did with `addEventListener`
    -   React will add the event listener for you, and the callback, `logClick` in our case, will be called when the button is clicked. 
-   Of course, because a function call is a JS expression, we need to wrap it in curly braces - JSX