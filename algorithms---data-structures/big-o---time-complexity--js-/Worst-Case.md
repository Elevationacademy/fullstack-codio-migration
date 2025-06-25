Say we had this code:

```
const findPerson = function(people, id){
    for(let p of people){
        if(p.id === id){
            return p
        }
    }
}
```

  

In theory, we could get lucky and find the person with the correct ID in the first item of the `people` array - i.e. the complexity would be **O( 1 )**.

  

But maybe the person is in the middle of the array, then the complexity would be **O( n/2 )** - i.e. we need to go through only _half_ the input to complete our logic.

  

But.. if the person was in the _end_, this would be **O( n )** - and in fact, **we always take the worst case scenario when considering time complexity**.

  

As such, for the `findPerson` function, we say it has a complexity of **O( n )**, because at worst we have to look through all of people (i.e. all **n** operations) to find the person with the specific ID we're looking for.

## Spot check
What is the complexity of this code?
```
const bagpack = {
    food: {
        apple: 2,
        bread: 1,
        cheese: 3
    },
    officeSupplies: {
        pencil: 5,
        ruler: 1
    },
    gadgets: {
        phone: 1,
        laptop: 1
    }
}

const getFromBag = function (category, item) {
    if (bagpack[category]) {
        let foundItem = bagpack[category][item]
        return foundItem ? foundItem : { err: "Item not found" }
    }

    return { err: "Category not found" }
}
```
<details><summary>
  Click here to reveal the answer.
</summary>
It is O( 1 )!

All of the operations are **O( 1 )**, so even if we get the worst case of **O( 3 )**, 3 is a constant, so we just say it's **O( 1 )**.
</details>