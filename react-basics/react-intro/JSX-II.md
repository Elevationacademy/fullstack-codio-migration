
### JSX II

One of the nice things about JSX is that we can **create it anywhere**, and then use it like a normal variable - passing it around from method to method. Take a look at this example:

  

```js
function App() {
  const personContainer = (name, email) => {

    let greatName = `The Great ${name}`
 
    return (
       <div className='person'>
         <h4>{greatName}</h4>
         <p>Contact at: <a href={email}>email</a></p>
       </div>
     )
   }

  return (
    personContainer("Louisa", "l@elo.com")
  );
}
```
  

The `return` section is working like a "manager" - it determines what to render and in what order. However, the actual definition of what we're rendering is being done inside of the `personContainer` method.

  

The above code works fine because `personContainer` returns JSX, and `App` is returning what `personContainer` is returning - very cool.

  

**Important Note**: in the above code, we wrap our `h4` and `p` inside of a `div` - in this case it makes sense, but generally speaking: **you may only return one element in your** **`function component`** - the element may have as many children as you like, but they must all be wrapped in one element.
