
For the eagle-eyed, you will have noticed that though the `map` code from before works great, we get the following **warning in our console**:

  

**Warning: Each child in an array or iterator should have a unique "key" prop.**

  

We could be reckless and ignore the warning, but that might bite us in the butt eventually.

  

What the warning is telling us is that when we pass "an array or iterator*" to a child (to `Company` in our case), we should somehow make it unique. And it even tells us to make it unique by using a `key` props.

###### *iterators are just data structures that can be iterated over

  

Just like we passed `name = { c.name }` before, we can do the same thing with `key`:

  
```
    return (
      <div>
        {companies.map(c =>
          <Company name={c.name} revenue={c.revenue} key={c.name} />)}
      </div>
    )
```  

We've separated the above to separate lines for clarity, but that `key={c.name}` field is what takes care of the warning.

  

Generally, the **key should be unique** - but in this case we can assume that each company has a unique name.