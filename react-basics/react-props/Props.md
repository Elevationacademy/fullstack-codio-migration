
The term **props** is short for **properties**, and you can think of them as parameters received in a function - they are **built-in to every React component**, even if they're empty.

  

In this case the **function** is a React component, and the **invoker** of the function is the component's parent.

  

Check this example out:*

  
```
function Company(props) {
	let explodedRevenue = props.revenue * 100

	return (
		<div>
			<p>{props.name} earns {explodedRevenue}</p>
		</div>
	)

}

export function App() {
	let companies = [
		{ name: "Tesla", revenue: 140 },
		{ name: "Microsoft", revenue: 300 },
		{ name: "Google", revenue: 600 }]

	return (
		<Company name={companies[0].name} revenue={companies[0].revenue} />
	)
}
```
  

###### *The two components should be in **separate files**, but for the ease of the example we're using one file.

  

The way we pass data _down_ in React (i.e. from a **parent** to its **children**) is by using `props`

  

So in the above case, the parent component `App` is passing down the values `name` and `revenue` to its child `Company`

  

You'll note the syntax of **sending down props** is quite simple:

  

-   We start with the component's name, as per usual when loading a child component
-   Then we use what looks like HTML attributes to pass down props
-   In the above we wrap each of the values with curly braces because this is JSX!
    -   If we had instead hard-coded some values, we wouldn't need the curly braces

  

In terms of **receiving props from a parent**, it's also straightforward:

  

-   The child component (above: `Company`) always has access to `props` which are passed as the first parameter to the functiondefined as the first p 
-   If the parent has passed something down, then the child can access this data as a normal object
-   You can access `props` in(as we do with `{props.name}`), or directly as a normal object a (as we do with `props.revenue`) - both are legitimate

  

Per the react [docs](https://facebook.github.io/react-native/docs/props),

  

_Most components can be customized when they are created, with different parameters. These creation parameters are called_ **_props_**_._

  

And that's what we saw above. The `name` and `revenue` are **parameters** of any `Company` component we create.