
Do the same, but now only pass down the articles of clothes that are blue from the `Wardrobe2` component.

  

Use `App` to render `Wardrobe2` in the `#spotcheck-5` area.

**Hint**: you're `filter`ing for the blue clothes.

---


<details>
  <summary>
     Solution
  </summary>

```JSX
const Article = (props) => {
  return <div>{props.info.color} {props.info.type}</div>
}

const Wardrobe = () => {
  let wardrobe = [
    { type: "shirt", color: "red", size: "Medium" },
    { type: "shirt", color: "blue", size: "Medium" },
    { type: "pants", color: "blue", size: "Medium" },
    { type: "accessory", color: "sapphire", size: "" },
    { type: "accessory", color: "lilac", size: "" },
  ]

  return wardrobe
    .filter(c => c.color === "blue")
    .map(c => <Article info={c} key={c.color + c.type} />)
}

const App = () => {
  return <Wardrobe />
}

export default App;

```


</details>