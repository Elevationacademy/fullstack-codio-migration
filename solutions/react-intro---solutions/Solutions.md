## Exercise 1

```
showCompany(name, revenue) {
    return (
      <div id={name}>{name} makes {revenue} every year</div>
    )
  }

render() {
return   (<div className="ex-space"><h4 className='ex-title'>Exercise 1</h4><div className="exercise" id="ex-1">
            {companies.map(c => this.showCompany(c.name, c.revenue))}
          </div></div>)
}
```

## Exercise 2

App.js
```
getClassName(temperature) {
    if(temperature < 15) {  
      return "freezing"
    } else if(temperature >= 15 && temperature < 30) {
      return "fair"      
    } else {
      return "hell-scape"
    } 
  }

render() {
 return (
 <div className="ex-space">
          <h4 className='ex-title'>Exercise 2</h4>
          <div className="exercise" id="ex-2">
          <div id="weatherBox" class={this.getClassName(10)}></div>
          <div id="weatherBox" class={this.getClassName(15)}></div>
          <div id="weatherBox" class={this.getClassName(35)}></div>


          </div>
        </div>)
  
}

```

App.css
```
#weatherBox{
    width: 300px;
    height: 300px;
}


.freezing{
    background-color: aqua;
}
.fair{
    background-color: orange;
}
.hell-scape{
    background-color: red;
}
```