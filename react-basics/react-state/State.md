
In the previous examples/exercises, all our data has been stored inside the Component.

  

This is not how we really do it. Typically we store a component's data in something called `state`

  

From [Thinkster](https://thinkster.io/tutorials/understanding-react-state),

  

_State is an object that determines how [a] component* renders & behaves_.

###### *and, possibly, its children

- hold on to this definition for now; we'll see what it means as we go along.

Let's begin with a simple example. `Example` is a simple component that renders the current page number and allows us to add to it.  

We **define** **state** **in a component**, like so:

```
import React, { useState } from 'react';


function Example() {
  const pageState = useState(1)

  const pageNumber = pageState[0]
  const setPageNumber = pageState[1]

  const addPage = () => setPageNumber(pageNumber + 1)

  return (
    <div>
      <p>You are on page number {pageNumber}</p>
      <button onClick={addPage}>Next page</button>
    </div>
  )
}
```
Now let's take a look at exactly what's happening in our example above:


First, we import the `useState` hook from React 
```
import React, { useState } from 'react';
```

We will talk all about hooks soon, for now all you need to know is that it is a special React function

At the top of our component we add: 
```
const pageState = useState(1)
```
The `pageState` variable we declared will hold whatever the `useState` function returns.
`useState` returns a pair of values in the form of an array with two indices:
-   The first index of the array always holds the value of the state
-   The second index of the array always holds a function that can update/change the state (a setter function)

```
const pageState = useState(1)

const pageNumber = pageState[0]
const setPageNumber = pageState[1]
```

Instead of accessing the index of the array every time we want to use one of the values

```
<p>You are on page number {pageState[0]}</p>
```
we can create two variables that hold the values
```
const pageNumber = pageState[0]
const setPageNumber = pageState[1]
```
-   `pageNumber` - will hold the value of index 0 which is the state itself (the page number the user is on)
-   `setPageNumber` - will hold the value of index 1 which is the function that can change the state variable

By convention, we call the function that modifies state with 'set' and then the name of the state variable. For example, if the state variable was called `password` the function that changes it would be called `setPassword`

We then invoke `useState`, we passed it an argument with the value of `1`:
```
const pageState = useState(1)
```

This is the initial value of the state - this is the value that state will begin with (in our case it's 1)

**Notice** that the state does can be strings, booleans, objects or anything you want (we'll see later how this works with objects & arrays)
        
              
**Note**: we don't need to write any implementation for the function that modifies state (`setPageNumber`), React does that automatically (we'll see this below)


When we want to use the state variable we can just reference the variable name - `pageNumber` 
You can see this in the `<p>` element

```js
<p>You are on page number {pageNumber}</p>
```

If we want to update the state we can just invoke the function we created - `setPageNumber` 
It can be:
```js
<button onClick={() => setPageNumber(pageNumber + 1)}>
  Next page
</button>
```
Or wrapped in a function, like `addPage` in the example above.
We still did not talk about events, but just to you the motivation. The events will be fully covered in the next lesson.

The state setter function always receives one argument - the new value of the state.

