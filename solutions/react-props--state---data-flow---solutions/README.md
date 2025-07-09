# Solutions

## Exercise 1
```
class Hudini extends Component {
    constructor() {
        super()
        this.state = {
            show: false
        }
    }
    render() {
        return (
        <div>{this.state.show ? "Now you see me" : "Now you don't"}</div>
        )


    }
}
```

## Exercise 2
App.js:
```
 <div className="ex-space"><h4 className="ex-title">Exercise 2</h4><div className="exercise" id="ex-2"><Home items={this.state.store} />
<Landing user={this.state.user} item={this.state.store.find(s => s.hottest)}/>          </div></div>
```
Home.js:
```
 render() {
        return this.props.items.map((item, index) => <Item key={index} item={item} />)


    }
Item.js: 

render() {
    return <div>{this.props.item.item}: ${this.props.item.price}</div>
    }
Landing.js:

 render() {
    return <div>Welcome, {this.props.user}. The hottest item is {this.props.item.item} for ${this.props.item.price}</div>


    }
```

## Exercise 3
```
{this.state.currentPage === 'Landing' ? 
              <Landing user={this.state.user} item={this.state.store[2]}/>:
              <Home items={this.state.store} />
            }
```

## Exercise 4
App.js:
```
            <Home items={this.state.store} shouldDiscount={this.state.shouldDiscount}/>
```
Home.js:
```
 render() {
        return this.props.items.map((item, index) => {
            return  <Item key={index} item={item} shouldDiscount={this.props.shouldDiscount}/>
        }
       )
    }
```
Item.js:
```
 render() {
        const {price, discount, item} = this.props.item
        return <div>{item}: ${this.props.shouldDiscount ? price * (1 - discount) : price}</div>
    }
```