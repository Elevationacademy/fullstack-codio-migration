
In order to do the exercises for this lesson please create a new react project.

Incase you forgot, heres the command for it
```console
 npx create-react-app my-app
```

For each spotcheck we will be creating a component.


Now do the following:
- Create a Button.
- add a **functionality** where if you **hover over** the button it will prints `"I was hovered!"`.

<details>
<summary>See this Solution</summary>
<div> 

```React
import React from 'react';

const SpotCheck1 = () => {

  const logHover = () => {
    console.log("I was hovered!")
  }

  return (
    <button onMouseEnter={logHover}>Click me</button>
  );
}

```
</div>
</details>
