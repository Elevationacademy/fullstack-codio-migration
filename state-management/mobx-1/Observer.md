
It's all well and good to tell MobX we want some properties to be `observable`, but it's no help unless we have something to _observe_ them.

  

So, if you go to your `App.js` file, we'll see just how we can do this.

  

Your `App.js` should have the following code:

```
import React, { Component } from 'react';
import { observer } from 'mobx-react'
import './App.css';
import Item from './components/Item';

class App extends Component {

  constructor() {
    this.state = {
      newItem: ''
    }
  }

  handleChange = (e) => {
    this.setState({
      newItem: e.target.value
    })
  }

  addItem = () => {
    this.props.store.addItem(this.state.newItem)
  }

  render() {
    return (
      <div className="App">
        <input onChange = {this.handleChange} value={this.state.newItem}/>
            <button onClick = {this.addItem}>Add</button>
            
        {/*your code here You should map each grocery item into an Item component */}  
       </div>
    )
  }
}
  
export default observer(App);
```
  

Let's break this down:

-   We're importing `observer` from **mobx-react**
-   We wrap the `App` class with the `observer` Higher Order Component (HOC for short) in the `export` of our class,
    -   This marks our app as an `observer` of our `observable`s.
    -   This way our app will be watching for any changes to `observable`s.
    -   In the meantime, you don't need to exactly understand what a Higher Order Component is, except that you can invoke it as a function and pass a component to it as an argument. If you want to learn a little more about it you can read about it [here](https://reactjs.org/docs/higher-order-components.html).
-   We have an `handleInput` method, for an input we've added in for you.
-   The rest is regular React!
    -   We'll explain about `this.props.store` in the `addItem` later on.

  

In the `Item.js` file (in your components folder) you can see a similar structure. In order to Observe changes, **each child component must also be passed to the `observer` HOC** - it is not inherited!

  

----------

  

With functional components, we can also use `observer` like this (as an alternative to the way learned above):

```
import React, { Component } from 'react';
import { observer } from 'mobx-react'
import './App.css';
import Item from './components/Item';

const App = observer((props) => {
   ...
   ...
   
   return (
      <div className="App">
        <input onChange = {this.handleChange}/>
        <button onClick = {this.addItem}>Add</button>
        ...
      </div>
   )
})

export default App
```
  

In the example above, we:

-   Created a variable called `App` which is the name of our component
-   Assigned the invocation of the `observer` function to `App`
-   Passed our functional component as an argument to the `observer` function
-   This example is identical to the first example, only here we can use hooks (because we are using a functional component)

  

----------

  

As of now, we still aren't seeing any data from our store - so let's add that data in.