Exercise 1
-
```js
for(let i in names) {
  people.push({name: names[i], age: ages[i]})
}
console.log(people)
```

Exercise 2
-

```js
for(let i in people) {
  console.log(people[i].name + " is " + people[i].age + " years old")
}
```

Exercise 3
-
```js
for(let i in posts) {
  if (posts[i].id == 2){
    posts.splice(i, 1)
  }
}
	
console.log(posts)
```

Exercise 4
-
```js
const obj = {}
	 
for(let i in posts) {
  obj = posts[i]
	  
  if(obj.id == 2) {
    for(let f in obj.comments){
      if(obj.comments[f].id == 3){
        obj.comments.splice(f, 1)
      }
    }
  }
}
	
console.log(posts)
```
Extension
-
```js
const properties = Object.keys(dictionary)
const currArr = []

for (let property of properties) {
  currArr = dictionary[property]
  console.log("Words that begin with " + property + ":")
  for (let word of currArr) {
    console.log("\t" + word)
  }
}
```

