Exercise 1
-
```js
const p1 = {
  name: "Robert",
  age: 25,
  city: "Jerusalem"
}
	
const p2 = {
  name: "Jill",
  age: 25,
  city: "Jerusalem"
}
	
if(p1.age == p2.age){
  if(p1.city == p2.city) {
      console.log(p2.name + " wanted to date " + p1.name)
  } else {
      console.log(p2.name + " wanted to date " + p1.name + ", but couldn't")
  }
}
```


Exercise 2
-
```js
const library = {
  books: [
    {title: "Lawyering", author: "John Doe"}, 
    {title: "Accounting", author: "Master Udi"}, 
    {title: "Computing", author: "Guru Oz"}
  ]
}
```

Exercise 3
-
```js
const reservations = {
  Bob: { claimed: false },
  Ted: { claimed: true }
}

const name = prompt('Please enter the name for your reservation');
	
if(reservations[name] && !reservations[name].claimed) {
  alert("Welcome in, " + name)
} else if (reservations[name] && reservations[name].claimed){
  alert("Hmm, someone already claimed this reservation")
} else if (!reservations[name]) {
  alert("You have no reservation")
}	
console.log(reservations)
  ```
Exercise 3.1

```js
if(reservations[name] && !reservations[name].claimed) {
  alert("Welcome in, " + name)
} else if (reservations[name] && reservations[name].claimed){
  alert("Hmm, someone already claimed this reservation")
} else if (!reservations[name]) {
  alert("You have no reservation")
  reservations[name] = {claimed: true} //exercise 3.1
}	
console.log(reservations)
```
Exercise 3.2
-
```js
const reservations = {
  Bob: { claimed: false },
  Ted: { claimed: true }
}

const name = prompt('Please enter the name for your reservation');
	
const lowerCaseName = name.toLowerCase()
	
const editedName = lowerCaseName.charAt(0).toUpperCase() + lowerCaseName.slice(1)
if(reservations[editedName] && !reservations[editedName].claimed) {
  alert("Welcome in, " + editedName)
} else if (reservations[editedName] && reservations[editedName].claimed){
  alert("Hmm, someone already claimed this reservation")
} else if (!reservations[editedName]) {
  alert("You have no reservation")
}	
console.log(reservations)
```
Extensions

```js
const hasOven = kitchen.hasOven
const doesFridgeWork = kitchen.fridge.works
const name = kitchen.owner

if(hasOven && doesFridgeWork) {
  console.log(name + 
	        "'s " + kitchen.fridge.items[1].name + 
	        " expired " + (date - kitchen.fridge.items[1].expiryDate) + 
	        " day ago. Weird, considering her fridge works. Luckily, she has an oven to cook the " 
	        + kitchen.fridge.items[1].name + " in.")
} else if (hasOven && !doesFridgeWork) {
    console.log(name + 
	        "'s " + kitchen.fridge.items[1].name + 
	        " expired " + (date - kitchen.fridge.items[1].expiryDate) + 
	        " day ago. Probably because her fridge doesn't work. Luckily, she has an oven to cook the " 
	        + kitchen.fridge.items[1].name + " in. And she'll have to pay " 
	        + (kitchen.fridge.price / 2) + " to fix the fridge.")
} else if (!hasOven && doesFridgeWork) {
    console.log(name + 
	        "'s " + kitchen.fridge.items[1].name + 
	        " expired " + (date - kitchen.fridge.items[1].expiryDate) + 
	        " day ago. Weird, considering her fridge works. Too bad she doesn't have an oven to cook the " 
	        + kitchen.fridge.items[1].name + " in.") 
} else {
    console.log(name + 
	        "'s " + kitchen.fridge.items[1].name + 
	        " expired " + (date - kitchen.fridge.items[1].expiryDate) + 
	        " day ago. Probably because her fridge doesn't work. Too bad she doesn't have an oven to cook the " 
	        + kitchen.fridge.items[1].name + " in. And she'll have to pay " 
	        + (kitchen.fridge.price / 2) + " to fix the fridge.")
}
```
  
