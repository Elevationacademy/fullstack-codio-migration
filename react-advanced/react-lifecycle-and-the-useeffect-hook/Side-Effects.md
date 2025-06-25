We saw how to use the `useState` hook. 
Now we are going to meet another hook called - useEffect. 

This hook will help us update the component before and after it renders.

Let's see how it works:

<div style="position: relative; padding-bottom: 56.111111111111114%; height: 0;"><iframe src="https://www.loom.com/embed/2930969cebda4b1bac7a2e751bda7e6b" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Here is the `App` code for you to play with and debug:
```
import { useState, useEffect } from 'react'


function App() {
  const [titleIndex, setTitleIndex] = useState(0)

  const updateTitle = () => {
    console.log("update index", titleIndex+ 1);
    setTitleIndex(titleIndex + 1);
  }

  useEffect(() => {
    setTimeout(updateTitle, 1000)
  })

  return (
    <div>
      <div className="box">{titleIndex}</div>
    </div>
  );
}

export default App;
```

We recommend that you run this code and make sure you understand how it works.