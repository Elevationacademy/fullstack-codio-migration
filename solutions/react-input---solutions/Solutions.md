## Exercise 1

```
class Exercise1 extends Component {


    constructor() {
        super()
        this.state = {
            name: "",
            age: ""
        }
    }


    showAlert = () => {
        alert(`Come in ${this.state.name}, you're ${this.state.age} - that's good enough`)
    }


    handleInputChange = event => {
        const {value, name} = event.target;    
        this.setState({
          [name]: value
        });
    }


    render() {
        return (
            <div>
                <input id="name-input" name="name" onChange={this.handleInputChange}/>
                <input id="age-input" name="age" onChange={this.handleInputChange}/>
                <button onClick={this.showAlert}>Go to Bar</button>
            </div>
        );
    }
}
```

## Exercise 2

```
class Exercise2 extends Component {


    constructor() {
        super()
        this.state = {
            name: "",
            fruit: ""
        }
    }


    handleSelect = event => {
        const {value, name} = event.target;    
        this.setState({[name]: value}, () => {
            console.log(`${this.state.name} selected ${this.state.fruit}`);
        })
    }


    render() {
        return (
            <div>
                <input id="name-input" name="name" value={this.state.name} onChange={this.handleSelect} />
                <select id="select-input" name="fruit" value={this.state.fruit} onChange={this.handleSelect}>
                <option value=""></option>
                    <option value="orange">Orange</option>
                    <option value="apple">Apple</option>
                    <option value="lemon">Lemon</option>
                </select>
            </div>
        );
    }
}
```