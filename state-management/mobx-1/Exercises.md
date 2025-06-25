## Exercise 1

Now that we know we shouldn't directly change our App state without an `action`, create an `addItem` method in your `ShoppingList` class.
    
      
This method should take a `name`, and add a new `Item` to your `items` array.
    
*Don't forget to tag it as an `action`...
    
Notice that we are already using this method in your `App.js`! You should be able to add new Items to your shopping list now.


## Exercise 2
    
Add in a `location` property to your `Item` (store) class. By default, set this property to "Super Sell"
    
Edit your `Item.js` component to render the location next to the item name.
    


## Exercise 3
    
Add in an edit button with a class "`editButton`" for each `Item`.
    

When you click on the edit button, you should be [prompt](https://www.w3schools.com/jsref/met_win_prompt.asp)ed with an input to edit the location of an object.
    

This should call an `editItem` `action` in your store, which finds the item and edits the location of the item in the store.
    
For example your `editItem` function in your store should start like this:
    

```
editItem = (itemName, newLocation) => {
        ....
}
```   


## Exercise 4

Add a delete button per Item.
    
This should be fairly straight forward, the button should call a function which calls an `action` in your store, and removes the `Item` from your list array. **Note**: The `deleteItem` function should receive <ins>one paremeter</ins> (the item name).