# Solutions

Exercise 1
-
```js
const isEven = function(number) {
    return (number % 2) === 0
}
	
const evenOrOdd = isEven(21)
console.log(evenOrOdd)
```
Exercise 2
-
```js
const printOdds = function (numbers) {
  for(let number of numbers) {
    if(!isEven(number)) {
      console.log(number)
    }
  }
}
	
const numbers = [17, 81, 98, 99, 70, 20, 18, 9, 20, 12, 31, 33]
	
printOdds(numbers)
```
Exercise 3
-
```js
const checkExists = function (ints, num) {
  for(let number of ints) {
    if(number === num) {
      return true
    }
  }
  return false
}
	
const numbers = [17, 81, 98, 99, 70, 20, 18, 9, 20, 12, 31, 33]
	
console.log(checkExists(numbers, 99))
```
Exercise 4
-
```js
const calculator = {
	    add: function (a, b) {
	        return a + b
	    },
	    subtract: function(a, b) {
	        return a - b
	    }
}
	
const result1 = calculator.add(20, 1)
const result2 = calculator.subtract(30, 9)
	
console.log(calculator.add(result1, result2))
```
Exercise 5
-
```js
const makeRegal = function(name) {
  return "His Royal Highness, " + name
}
	
const increaseByNameLength = function(money, name) {
  return name.length * money
}
	
const turnToKing = function(name, money){
  name = name.toUpperCase()
  money = increaseByNameLength(money, name)
  name = makeRegal(name)
  console.log(name + " has " + money + " gold coins")
}
	
turnToKing("martin luther", 100)
```