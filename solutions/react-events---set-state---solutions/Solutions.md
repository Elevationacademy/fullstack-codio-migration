## Exercise 1
```
 shiftImageBack = () => {
    const currentImg = this.state.currentImg-1
    this.setState({currentImg: currentImg})
  }
  shiftImageForward = () => {
    const currentImg = this.state.currentImg+1
    this.setState({currentImg: currentImg})  }


  render() {
    const {images, currentImg}= this.state
    return (
      <div >
        <button className="back" onClick={this.shiftImageBack}>back</button>
        <img src={images[currentImg]} alt=""/>
        <button className="forward" onClick={this.shiftImageForward}>forward</button>
      </div>
    );
  }
```

## Exercise 2
```
render() {
    return (
      <div >
        {this.state.displayConversation ? <Conversation /> : <List />}
      </div>
    );
  }
```

## Exercise 3
Exercise2.js
```
 render() {
    return (
      <div >
        {this.state.displayConversation ? <Conversation /> : <List contacts={this.state.conversations.map(c => c.with)}/>}
      </div>
    );
  }
```

## Exercise 4
List.js:
```
class List extends Component {
  render() {
    console.log(this.props.contacts);
    return (
      <div >
        {this.props.contacts.map((c, i) => <Contact key={i} name={c} />)}
      </div>
    );
  }
}
```
Contact.js:
```
class Contact extends Component {
  render() {
    return (
      <div >
        <span>{this.props.name}</span>
      </div>
    );
  }
}
```

## Exercise 5
Exercise2.js
```
displayConvo = name => {
    this.setState({displayConversation: name})
  }


  render() {
    return (
      <div >
        {this.state.displayConversation ? <Conversation /> : <List displayConvo={this.displayConvo} contacts={this.state.conversations.map(c => c.with)}/>}
      </div>
    );
  }
```
```
class List extends Component {
  render() {
    console.log(this.props.contacts);
    return (
      <div >
        {this.props.contacts.map((c, i) => <Contact key={i} name={c} displayConvo={this.props.displayConvo}/>)}
      </div>
    );
  }
}

class Contact extends Component {
  displayConvo = () => {
    this.props.displayConvo(this.props.name)
  }
  render() {
    return (
      <div onClick = {this.displayConvo}>
        {this.props.name}
      </div>
    );
  }
}
```

## Exercise 6
```
class Conversation extends Component {
  render() {
    return (
      <div >
        {this.props.convo.map((c, i) => {
          <div key={i}><span className="sender">{c.sender === 'self' ? 'Me' : this.props.sender}:}</span><span>{c.text}</span></div>
        })}
      </div>
    );
  }
}
```
Exercise2.js:
```
  render() {
    const {displayConversation, conversations} = this.state
    return (
      <div >
        {displayConversation ? 
        <Conversation convo={conversations.find(c => c.with === displayConversation).convo} sender={displayConversation}/> : 
        <List displayConvo={this.displayConvo} contacts={conversations.map(c => c.with)}/>}
      </div>
    );
  }
```

## Exercise 7
```
class Conversation extends Component {
  resetConvo = () => {
    this.props.resetConvo()
  }
  
  render() {
    return (
      <div >
        {this.props.convo.map((c, i) => {
          return (<div key={i}><span className="sender">{c.sender === 'self' ? 'Me' : this.props.sender}:</span><span>{c.text}</span></div>)
        })}
        <button className="back" onClick={this.resetConvo}>Back</button></div>
    );
  }
}
```
Exercise2.js:
```
resetConvo = () => {
    this.setState({
      displayConversation: null
    })
  }

  render() {
    const {displayConversation, conversations} = this.state
    console.log(conversations.find(c => c.with === displayConversation));
    return (
      <div >
        {displayConversation ? 
        <Conversation 
        convo={conversations.find(c => c.with === displayConversation).convo}
        sender={displayConversation}
        resetConvo = {this.resetConvo}/> : 
        <List displayConvo={this.displayConvo} contacts={conversations.map(c => c.with)}/>}
      </div>
    );
  }
```







