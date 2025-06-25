
To update the `state` with `event handlers`, you might be tempted to do something like this:

```React
import React from 'react';

const App = () => {
  const importantData = "Shoobert";

  const updateData = () => {
    importantData = "Treboohs";
  }

  return (
    <div>{importantData}</div>
    <button onClick={updateData}>Update</button>
  );
}
```

or define a state with useState but update the state directly, without using the `setImportantData` method

```React
import React from 'react';

const App = () => {
  const [importantData, setImportantData] = useState("Shoobert");

  const updateData = () => {
    importantData = "Treboohs";
  }

  return (
    <div>{importantData}</div>
    <button onClick={updateData}>Update</button>
  );
}
```



---
### **DON'T DO THAT**
---
What we're doing above is not good. We need a `state`. Technically, the above code will work in some cases, but It will not cause the component to rerender, meaning the `App` function will not run again, and neither any of it's children. The proper way to change state is to use React Hooks, specifically the `useState` method.

When we use `useState`, it gives us a stateand a `set` method. (state is a name that can change, for example, data and setData, the update function can too.)

it will look like this:

```React
import React, { useState } from 'react';

const App = () => {
  const [importantData, setImportantData] = useState("Shoobert");

  const updateData = () => {
    setImportantData("Treboohs");
  }

  return (
    <button onClick={updateData}>Update</button>
  );
}
```

We do not mutate directly; we use the set method defined by the hook like this:
  
```js
const [data, setData] = useState({name:"Shoobert"});

setData({name: newValue})
```
  
The `setData` method will receive the new state value. In this case it is a new string.

So for our previous example, we would do the following:


  
```js
  const updateData = () => {
    setImportantData("Treboohs");
  }
```
  

Let's break this down:

-   First, note that we're using **an arrow function** for `updateData`
-   Next, we invoke `setImportantData` - this is the method we mentioned earlier, that we get back from the `useState` hook.
    -   This method receives, for now, one parameter: the updated data (must align with the type of state we defined)
    -   In our case, the only thing we're doing is changing the value of `importantData` to a different string
    -   If the state is an object then we should pass the update function a new object. Usually it is easy to clone the object and then modify the new object.

