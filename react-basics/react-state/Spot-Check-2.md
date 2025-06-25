
Add a new `companies` state in the `App` component. The value of this key should be the following array:

  
```
[
      { name: "Tesla", revenue: 140 },
      { name: "Microsoft", revenue: 300 },
      { name: "Google", revenue: 600 }
]
```
  

You should render a `Company` component for each of the above items, but you should render them from `state`. 


<details>
  <summary>
     Here is our solution 
  </summary>

```js
function App() {

  let companiesData = [
    { name: "Tesla", revenue: 140 },
    { name: "Microsoft", revenue: 300 },
    { name: "Google", revenue: 600 }]
  
  let [companies, setCompanies] = useState(companiesData)

return (
    <div className="ex-space">
      {companies.map(company => <Company name={company.name} revenue={company.revenue}></Company>)}
    </div>
  )
}
```
</details>