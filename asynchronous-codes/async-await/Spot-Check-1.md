
How would you rewrite the below DB Operation with async/await?

  

```js
const fetchData = function (surname) {
    Person.find({ lastName: surname }, function (err, people) {
        console.log(people)
    })
}
```
  

You can check your work [here](https://codepen.io/ElevationPen/pen/vqKqBZ?editors=0010).
