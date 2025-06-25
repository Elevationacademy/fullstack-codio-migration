In the world of programming we need a way to store data. For this purpose, we have what's known as **data structures**.

  

You already know (at least) two data structures by now:

1.  Arrays
2.  Objects

  

When we talk about data structures, we usually consider the **complexity** of:

-   An **insert** into the data structure
-   A **find** from the data structure
-   An **update**
-   A **remove**

  

For instance, say we had this array:

```
let people = []
```
  
The complexity of **insert**ing into an array is **O( 1 )**:

```
let p1 = {
    id: "a0x3",
    name: "Candice",
    age: 23
}

let p2 = {
    id: "q113z",
    name: "Jay",
    age: 16
}

let p3 = {
    id: "kl991",
    name: "Drew",
    age: 31
}

people.push(p1)
people.push(p2)
people.push(p3)
```
  

Since `push` always inserts an item to the _end_ of the array, it's only one operation.

That's pretty simple. However, to **find** something, it's typically* **O( n )**:
*generally we don't know where elements are in the array

```
const findPerson = function (personID) {
    for (let p of people) {
        if (p.id === personID) {
            return p
        }
    }
}
```
  

To **update** an item in an array is also **O( n )**:

```
const updatePerson = function (personID, newName) {
    let person = findPerson(personID)
    person.name = newName
}
```
  
In order to **update** something in an array, we must first **find** it - so even though the update itself is **O( 1 )**, we're forced to use `findPerson` in order to understand _which_ person to update - and that's **O( n )**.

## Spot check
What's the complexity for the **remove** in an array?

<details><summary>
  Click here to reveal the answer.
</summary>
  
Also **O( n )** - first find it (using an index), then use the index to `splice`

See [solution](https://codepen.io/ElevationPen/pen/jjMoYY).
</details> 

