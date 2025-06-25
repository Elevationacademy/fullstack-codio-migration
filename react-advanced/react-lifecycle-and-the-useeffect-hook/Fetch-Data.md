In this section we will show how to make the useEffect happen only once in the mounting phase.

Check it out:

<div style="position: relative; padding-bottom: 56.074766355140184%; height: 0;"><iframe src="https://www.loom.com/embed/20663e1203304b29a81d01c31f0c7009" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

Here is the code:

```
function App() {
  const [titleIndex, setTitleIndex] = useState(0)
  const [titles, setTitles] = useState([])

  const updateTitle = () => {
    setTitleIndex(titleIndex + 1);
  }

  useEffect(()=>{
    getColors().then((colors)=>{
      setTitles(colors)
    })
  }, [])

  useEffect(() => {
    setTimeout(updateTitle, 1000)
  }, [titleIndex])

  return (
    <div>
      <div className="box">{titles[titleIndex]}</div>
    </div>
  );
}
```

The getColors method in it's sync version:

```
function getColors() {
  return ["green", "blue", "pink", "purple", "gold", "white"]
}
```
and async version:
```
function getColors() {
  return Promise.resolve()
    .then(() => ["green", "blue", "pink", "purple", "gold", "white"])
}
```

# Important note
In this example we fetch the data on the first render. But it is not always the case. In other scenarios we might want to fetch data in the update phase. 

# Async Await
In the previous example we have used promises to handle async code. Check out the next video to see how we can use async await with the `useEffect` hook:

<div style="position: relative; padding-bottom: 62.5%; height: 0;"><iframe src="https://www.loom.com/embed/5709a1cb46d24daaacaf534f9db0b71f" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe></div>

# Spot Check
Try to change the above code to work with async await as was explained in the video.


<details>
  <summary>
     Solution
  </summary>
  
```
useEffect(() => {
    const getData = async function (){
      let colors = await getColors()
      setTitles(colors)
    }
    getData()
  }, [])
```
  
</details>