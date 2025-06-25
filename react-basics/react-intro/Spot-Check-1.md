
## Instructions

Notice that so far, you've been using your own create-react-app repo. You can continue to work in this repo, or use codepen.
 
***

Check out this App component:

```js
function App() {
  const getStuff = () => {}

  return (
    <div>
      <div className="ex-space">
        <h4 className='ex-title'>Spot-check 1</h4 >
        <div className="exercise" id="spotcheck-1">
          {/* your code here */}
        </div>
      </div>
    </div>
  )
}
```

Inside of `App`  you'll find a method called  getStuff.

  

This method should return some text. Call this method in  the `return` section using a JSX expression to render the text inside an  `h1`  tag.

  

<details>
  <summary>
     See our solution if you're stuck
  </summary>

```
function App() {
  const getStuff = () => "Wild function'ed text"

  return (
    <div>
      <div className="ex-space">
        <h4 className='ex-title'>Spot-check 1</h4 >
        <div className="exercise" id="spotcheck-1">
          <h1>Stuff: {getStuff()}</h1>
        </div>
      </div>
    </div>
  )
}
```
</details>

