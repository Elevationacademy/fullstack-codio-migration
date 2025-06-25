
## Instructions

Check out this App component:

```js
function App() {
  const getMorningGreeting = () => { }
  const getEveningGreeting = () => { }

  return (
    <div>
      <div className="ex-space">
        <h4 className='ex-title'>Spot-check 2</h4 >
        <div className="exercise" id="spotcheck-2">
          {/* your code here */}
        </div>
      </div>
    </div>
  )
}
```
Inside of `App` you'll find a couple of empty methods that you'll need to fill out:

1.  `getMorningGreeting`
2.  `getEveningGreeting`

Both methods should return JSX of a simple string inside of a `div`

  

Inside the `return`, use a [ternary operator](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator)* to return the morning greeting if the hour is before 12, or the evening greeting otherwise.

  

You can use `new Date().getHours()` to determine the current time.

<sup>*Note that you have to use a ternary statement if you want a condition inline in your JSX. If you wanted to use an if-statement, you'd have to do that _outside_ of the `return`

<details>
  <summary>
     See our solution if you're stuck
  </summary>

```
function App() {
  const getMorningGreeting = () => <div>Good Morning</div>
  const getEveningGreeting = () => <div>Good Evening</div>

  let isMorninig = new Date().getHours() < 12
  
  return (
    <div className="ex-space">
      <h4 className='ex-title'>Spot-check 2</h4>
      <div className="exercise" id="spotcheck-2">
        {isMorninig ? getMorningGreeting() : getEveningGreeting()}
      </div>
    </div>
  )
}
```
</details>
 
