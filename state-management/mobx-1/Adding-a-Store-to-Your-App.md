
For now, we'll add a store to our App just like we have done any other props in the past.

  

**Go to your** **`index.js`** **file**:

  

-   You can start by commenting in the first 3 commented out lines. This makes an instance of an `Item`, an instance of our `ShoppingList` (`groceryList`), and pushes our `Item`, `potato`, into the list of our `groceryList`
-   Add `groceryList` as a `prop` "`store`" to your `App`

  

When you're done, your index.js file should look like this:

```
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { Item } from '../src/stores/Item'
import { ShoppingList } from '../src/stores/ShoppingList'

let potatoes = new Item("Potatoes")
let groceryList = new ShoppingList()
groceryList.list.push(potatoes)

// Use the prop store for your store
ReactDOM.render(<App store={groceryList} />, document.getElementById('root'));
```
  

Now, our `groceryList` is a property of our `App` and can be passed down as the `prop` "`store`" wherever we need it! So now inside the app component we can access our store like this: `this.props.store`