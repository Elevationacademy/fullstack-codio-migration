
## Instructions

Another cool thing that JSX allows us to do is return an **array of JSX expressions**.

  

Using the same two methods from before, return an array of:

-   The morning greeting
-   The evening greeting
-   A simple `p` element with "some text" in it


<details>
  <summary>
     See our solution if you're stuck
  </summary>

```
function App() {
  const getMorningGreeting = () => <div>Good Morning</div>
  const getEveningGreeting = () => <div>Good Evening</div>

  return [
    getMorningGreeting(),
    getEveningGreeting(),
    <p>some text</p>
  ]
}
```
</details>

<br/>  

Very powerful stuff.
