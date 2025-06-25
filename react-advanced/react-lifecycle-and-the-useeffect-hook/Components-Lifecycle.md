
Whenever React renders any component to the page, the component goes through a whole **lifecycle** of stages.

  

Much like a human life, there is birth, life, and ultimately death.


There are **three main phases**:
1.  Mounting
2.  Updating
3.  Unmounting

  

We say a component **mounts** onto the DOM when it is added to the DOM, and we (humans) can physically see it on the page*. A component **unmounts** when it is removed from the DOM.

  
\* Not necessarily all components are visible, but we can for sure see them in the DOM via the Elements tab in the dev tools

## Unmount Example
What does it mean that a component is unmounted, or removed from the DOM?

Let's look at an example:

```jsx
import { useState } from 'react'
import Red from './Red';
import Blue from './Blue';


function App() {
  const [color, setColor] = useState("blue")

  const toggleColor = () => {setColor(color === "blue" ? "red" : "blue")}

  return (
    <div>
      <div> Current Color {color} </div>
      <button onClick={toggleColor}> Toggle color </button>
      {color === "blue" ? <Blue/> : <Red/>}
    </div>
  );
}

export default App;
```
** You cam assume the `Red` and `Blue` components are simple divs with the color name.
  
In this example we render each time a different component according to the color state.

At first the color is `blue` so the blue component will be rendered and will appear in the DOM.

But what happens when we click the button?

## Answer
Well, the `Red` component appears on the screen.
But, what happens to the blue component?

It doesn't appear on the screen and it also does not appear in the DOM.

Go ahead and open the elements tab in the dev tools and check it out.
You will see only the `Red` component.

This is what we call `unmount`.
First the `Blue` component appeared in the DOM, and then it was removed from the DOM.