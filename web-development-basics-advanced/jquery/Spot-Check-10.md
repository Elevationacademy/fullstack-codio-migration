
By the way, there's nothing stopping us from combining this all with a loop, too. Check this out:

  
```
const names = ["Alex", "Byron", "Cassandra", "Deandre", "Ellena"]

for(let name of names){
  $("body").append(`<div>${name}</div>`)
}
```
  

That will add a div with the name of each person in the array to the body! Very useful.

  

Given the following array, create a <div class='human'>FIRST_NAME - LAST_NAME</div> for each item, and add it to body

  
```
const names = [
  { first: "Alex", last: "Johnson" },
  { first: "Byron", last: "Loveall" },
  { first: "Cassandra", last: "Wuthers" },
  { first: "Deandre", last: "Rahm" },
  { first: "Ellena", last: "Freeman" }
]
```
  

Here's a [solution](https://codepen.io/ElevationPen/pen/MddQeZ?editors=0010) if you need.