
Instead of passing the plain company name, use a separate method called `upperCase` to capitalize the name, and invoke that method when you pass the data down.

  ---

<details>
  <summary>
     Solution
  </summary>

```JSX

const App = () => {
  const upperCase = name => name.toUpperCase()

  let companies = [
    { name: "Tesla", revenue: 140 },
    { name: "Microsoft", revenue: 300 },
    { name: "Google", revenue: 600 }]

  return (
    <div>
      {companies.map(c =>
        <Company
          name={upperCase(c.name)}
          revenue={c.revenue}
          upperCase={upperCase}
        />
      )}
    </div>
  )
}

export default App
```


</details>


<br/> 

**Note:** In our solution, we split the `Company` tag just for visual clarity - you can write it either way (one line or many)