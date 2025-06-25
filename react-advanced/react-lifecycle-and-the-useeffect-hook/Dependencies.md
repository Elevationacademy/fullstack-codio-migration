In this section we will see how to make the useEffect callback run only when the relevant state changes. 

<div style="position: relative; padding-bottom: 56.074766355140184%; height: 0;"><iframe src="https://www.loom.com/embed/3246beaf3268407fbf05ef5f6efcbf93" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Here is the code:

```

function App() {
  const [titleIndex, setTitleIndex] = useState(0)
  const [size, setSize] = useState(100)

  const updateTitle = () => {
    console.log("update index", titleIndex+ 1);
    setTitleIndex(titleIndex + 1);
  }

  const updateSize = () => {
    setSize(size + 20);
  }

  useEffect(() => {
    setTimeout(updateTitle, 1000)
  }, [titleIndex])

  return (
    <div>
      <button onClick={updateSize}>Change Size</button>
      <div className="box" style={{width: size, height: size}}>{titleIndex}</div>
    </div>
  );
}
```

## To Summerize
### No Params
```
useEffect(() => {
  ...
})
```
Runs after every render
<hr/>

### Empty array
```jsx
useEffect(() => {
  ...
}, [])
```
Run after the first render only

<hr/>

### Dependencies Array
```jsx
useEffect(() => {
  ...
}, [isActive])
```
Runs after the first render and then after each time the dependencies change 