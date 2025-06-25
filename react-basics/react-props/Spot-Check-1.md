
Before starting this lesson's spot checks and exercises, create a new react project.

  

----------

  

In the components directory, create a component called `Company` and one called `SubCompany`. The latter should be a child of `Company`. Therefore, the component tree in this case is:

  

`App` → `Company` → `SubCompany`

  

The `App` component (using the code from the previous section) should pass a `name` to `Company`, and `Company` should pass that same `name` down to `SubCompany`.

  

Finally, `SubCompany` should render the received `name` in an `h4`.

  

If you did it right, you should see **Tesla** on your page.


<details>
  <summary>
     Here is our solution 
  </summary>

```jsx
function Company(props) {
	return <SubCompany name={props.name} />
}

function SubCompany(props) {
	return <h4>{props.name}</h4>
}

function App() {
	let companies = [
		{ name: "Tesla", revenue: 140 },
		{ name: "Microsoft", revenue: 300 },
		{ name: "Google", revenue: 600 }]

	return (
		<Company name={companies[0].name} revenue={companies[0].revenue} />
	)
}
```
</details>

 
