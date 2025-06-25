## Exercise 1

```
export class Dummy extends Component {
    render() {
        return (<div>
            <input type="text" name="" id="" />
            <button>Submit</button>
        </div>)
    }
}
```


## Exercise 2

Spam.js
```
const Spam =()=> <div>Spam</div>
```

Spamalot.js
```
     const spamArray = [];
        for (let i = 0; i < 500; i++) {
            spamArray.push(<Spam />)
        }
        return (
           <div id="ex-2">{spamArray}</div>
        );
    }
```



## Exercise 4

NavBar.js
```
const NavBar = () => <div>NavBar Component</div>
```

Menu.js
``` 
render() {
        return (
        <div><div>Menu Component</div><Item /></div>


        )
}
```


Item.js
```
const Item = () => <div>Item Component</div>
```

Checkout.js
```
render() {
        return (
       <div>
            <div>Checkout Component</div>
            <Item />
       </div>
        )
}
```