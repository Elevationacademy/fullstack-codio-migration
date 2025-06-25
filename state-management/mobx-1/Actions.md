
Now, we want to change what is rendered based on the application state - if we've completed our task, we should render the item with a strike through. In order to do this we need to change our state. This is where `action`s come in.

  

In short, anything that causes some kind of change in your app state (or in other words - an `observable`) is an `action` and should be signified as such in the `makeObservable` function (in the constructor).

  

Since we want to keep anything related to our state in our store, we'll add a method to change our store properties in our store - the `ShoppingList` class. This method will be our `action`.

  

**Go to your** **`ShoppingList.js`** **file and edit your** **`checkItem`** **method to look like this:**

  
```
class ShoppingList {
    //other items
    checkItem = (name) => {
        let item = this.list.find(i => i.name === name)
        item.completed = !item.completed
    } 
  //other methods
}
```
  

And now edit the `makeObservable` function in the constructor to look like this:

```
makeObservable(this, {
    list: observable,
    length: observable,
    checkItem: action
})
```

If you have an error here - make sure you import `action` from MobX!

  

Let's break this down - we've added a method to our class `checkItem`

-   The method takes one parameter, `name`
-   It finds the correct item and updates it's completed field
-   We map the method to an `action` in our constructor to tell MobX that this method can change an `observable`


Now that we have our `action`, let's invoke it `onClick`!

  
**Go back to your** **`Item.js`** **component file. Let's add a** **`checkItem`** **function to our class**, and invoke it **on click for each of our checkbox inputs**.


```
class Item extends Component {
  checkItem = (e) => {
    this.props.store.checkItem(e.target.value)
  }
  //other Methods
  render() {
    let item = this.props.item
    return (
        <div className = {item.completed ? "crossed": null}>
          <input 
            type="checkbox"
            onClick = {this.checkItem} 
            value={item.name}
          /> 
          {item.name} 
        </div>)
  }
}

export default observer(Item)
```
  

Our `checkItem` function runs the store's `checkItem` function, and passes it the name of the item that was clicked - this is similar to how we've used react in the past.

  

The only difference is now the function we are invoking is in our `store` and will edit our store data. Because we passed our store down through `props`, we could call the function in our `Item` component as well!

  

Go ahead and try out your shopping list now! When you check an item, it should cross out, and when you check it again it should come back - remarkable!