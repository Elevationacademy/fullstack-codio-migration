What is the complexity of the determineEmployment function?

```
const employers = [{ name: "Microsoft", positions: 3 }, { name: "Tesla", positions: 0 }, { name: "Apple", positions: 14 }]
const removeYouth = (people) => people.filter(p => p.age < 18)
const employ = (person, employer) => {
    person.hasJob = true
    employer.positions -= 1
}

const determineEmployment = function (people) {
    removeYouth(people)
        .forEach(p => {
            employers.forEach(e => {
                console.log(`${p.name} applied for a job at ${e.name}`)
                (e.positions > 0 && !p.hasJob) ? employ(p, e) : null
            })
        })
}
```

  

This is a chunky piece of code. Take your time.


<details><summary>
  Click here to reveal the answer.
</summary>
  
The complexity is **O( mn )**.

Even though we have a `forEach` inside of a `forEach` (a double for loop), the inner one is iterating over `employers` which is a fixed array.

The `removeYouth` function is just a distraction - it's another **n** operation, but remember that **n + n = 2n** - and we ignore constants!
 
The `employ` function is also a distraction - all of that runs in **O( 1 )**, and we can totally ignore that when we're talking about **O( n )** operations.
</details>