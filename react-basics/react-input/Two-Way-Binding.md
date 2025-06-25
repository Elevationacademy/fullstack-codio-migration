
We'll start off simple. Say we have this setup 

```js
const InputTest = () => {
  return (
    <div>
      <input type="text" />
      <button>Alert</button>
    </div>
  )
}

export default InputTest
```

You might be having a flashback to the jQuery days where we would have to traverse the DOM from the button that was clicked to the relevant input - but no worries, we have a more straightforward way with React.

  

We're going to need to do three things for this to work:

1.  Add a `state` for our text value
```
const [text, setText] = useState("")
```
2.  Add a `value` attribute to the `input` tag, and assign it to the `state`'s value
    *  Now the value of the `input` will be **bound** to the value of the `state` : 
      ``` 
      <input type="text" value={text} /> 
      ```
    * Now we can say that the `input` is **bound** to the `text` state -i.e, whatever the value of `text` will be reflected in the input (but not the other way around)

    * Now we need to add the `onChange` that will do the reverse - make the value of `text` state be whatever the user types
  
3. Add an `onChange` listener to the `input` that updates the `state`

    ```
    <input type="text" value={text} onChange={updateText}/>
    ```

**The update method**

```
updateText = (event) => {
    setText(event.target.value);
}
```
Notice that we're using the plain, vanilla-JS `event` - recall that `onChange` fires an event each time the `input` changes. We can capture that `event`* in whichever function we invoke once the change occurs.

*As with all parameter names, the name does not have to be `event` - it can be whatever we want
-  Now the value of the `state` will be **bound** to the value of the `input`

And now we can say that our state is **bound** to our `input` - whenever the latter changes, the state is automatically updated.

Now, because our state updates when the `input` changes, and the value of `input` is bound to the `state`, we have **two-way binding**.

Check it out, here is the entire component:

```
const InputTest = () => {
    const [text, setText] = useState("")

    const updateText = (event) => {
        setText(event.target)
    }

    return (
        <div>
            <input type="text" value={text} onChange={updateText} />
            <button>Alert</button>
        </div>
    )
}

export default InputTest
```
  






  
  


  



  

