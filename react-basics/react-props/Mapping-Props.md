
Continuing with the example above (without `SubCompany`), we want to render all the companies. Now, we could do something like this:

  
```
function App() {
  let companies = [
    { name: "Tesla", revenue: 140 },
    { name: "Microsoft", revenue: 300 },
    { name: "Google", revenue: 600 }
  ]

  return (
    <div>
      <Company name={companies[0].name} revenue={companies[0].revenue} />
      <Company name={companies[1].name} revenue={companies[1].revenue} />
      <Company name={companies[2].name} revenue={companies[2].revenue} />
    </div>
  )
}
```
  

But it's just wrong. Please don't do this. Please eat a teaspoon of salt if you ever do this. We're not barbarians.

  

One way we could create the above is to **use a for-loop to generate each of those lines** - remember, we're dealing with **JSX** here - we're allowed to combine JS and "HTML" freely.