# Solutions

## Exercise 1

```
addItem = (name) => {
        const item = new Item(name)
        this.list.push(item)
}
```

Your constructor should now look like this:
```
constructor() {
    this.list = []
    this.length

    makeObservable(this, {
        list: observable,
        length: observable,
        checkItem: action,
        addItem: action
    })
}
```

## Exercise 2

```
export class Item {
    constructor(name) {
        this.name = name
        this.completed = falsethis.location = "Super Sell"

        makeObservable(this, {
            name: observable,
            completed: observable,
            location: observable
        })
    }
}
```

```
class Item extends Component {

    checkItem = (e) => {
      this.props.store.checkItem(e.target.value)
    }
  render() {
    let item = this.props.item
    return (
        <div className = {item.completed ? "crossed": null}>
          <input 
            type="checkbox" 
            onClick = {this.checkItem} 
            value={item.name}
          /> 
          {item.name}, {item.location}
        </div>
     )
  }
}
```

## Exercise 3

```
class Item extends Component {

  editItem = () => {
    const newLocation = prompt("Please enter a new location")
    this.props.store.editItem(this.props.item.name, newLocation)
  }
 
  render() {
    let item = this.props.item
    return (
        <div className = {item.completed ? "crossed": null}>
          <input 
            type="checkbox" 
            onClick = {this.checkItem} 
            value={item.name}
          /> 
          {item.name}, {item.location}
          <button className="editButton" onClick={this.editItem}>edit</button>
        </div>
     )
  }
}
```

```
export class ShoppingList {
    constructor(){
        //...
        makeObservable(this, {
            list: observable,
            length: observable,
            checkItem: action,
            addItem: action,
            editItem: action
        })
    }

    editItem = (itemName, newLocation) => {
        const item = this.list.find(l => l.name === itemName)
        item.location = newLocation
    }
}
```


## Exercise 4

```
export class ShoppingList {
    constructor() {
        //...
        makeObservable(this, {
            list: observable,
            length: observable,
            checkItem: action,
            addItem: action,
            editItem: action,
            deleteItem: action
        })
    }
    
    deleteItem = (itemName) => {
        const index = this.list.findIndex(l => l.name === itemName)
        this.list.splice(index, 1)
    } 
}

class Item extends Component {
 render() {
    let item = this.props.item
    return (
        <div className = {item.completed ? "crossed": null}>
          <input 
            type="checkbox" 
            onClick = {this.checkItem} 
            value={item.name}
          /> 
          {item.name}, {item.location}
          <button className="editButton" onClick={this.editItem}>edit</button>
          <button onClick={this.deleteItem}>Delete</button>
        </div>
    )
  }
}
```