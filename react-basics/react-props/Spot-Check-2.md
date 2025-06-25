
Recall that JSX allows us to do the following:

  
```

return (
    <div>
        {[<Company... />,
        <Company... />,
        ...]}
    </div>
);

```
  

P. S. the three dots represents all the rest of the props component call (all the props etc.).

In other words, you can render an array of `Company` components.

  

***

  

Go ahead and create a `generateCompanyTags` method inside of `App` (before the `return`)- it should take `companies` as a parameter, and return an array of `Company` instances. You should create this array by looping through `companies`.

  

[Here's](https://codepen.io/ElevationPen/pen/mgzNrO?editors=0010) one solution you can look at after giving it a go.

  

Once you create this method, you can go back to the `return` in `App` and do this in the relevant Spot Check part.

  
```
  render() {

    let companies = [
      { name: "Tesla", revenue: 140 },
      { name: "Microsoft", revenue: 300 },
      { name: "Google", revenue: 600 }]

    return (
      <div>
        {generateCompanyTags(companies)}
      </div>
    )
  }
```
  

Save and look at your page - all the companies are there!

  

And the crazy part is that we haven't touched our `Company` component since we told it to render using  **props** - that's because it doesn't care about anything except for what it should display. Talk about separation of concerns.

  

In fact, this is an important point: **children components should not be aware of their parents**, in other words, they should receive some props and **it doesn't matter who gives them those props**, as long as the keys match up.