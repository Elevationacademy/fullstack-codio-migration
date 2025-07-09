# Solutions

## Exercise 1 - Callbacks
```
const pushPull = function (func) {
	    func()
	}
	
	const push = function () {
	    console.log("pushing it!")
	}
	
	const pull = function () {
	    console.log("pulling it!")
	}
	
	pushPull(push)
	pushPull(pull)
```

## Exercise 2 - Callbacks
```
const getTime = function (func) {
	    const time = new Date()
	    func(time)
}
	
const returnTime = function (time) {
	    alert('The current time is: ' + time)
}
	  
getTime(returnTime)
```

## Exercise 3 - Callbacks
```
const displayData = function (alertDataFunc, logDataFunc, data) {
  alertDataFunc(data)
  logDataFunc(data)
}
	
const logData = function (data) {	    
  console.log(data)
}
	 
displayData(alert, logData, "I like to party")
```

## Exercise 4 - Arrow Functions
```
const getSum = (a, b, c) => a + b + c
	
console.log(getSum(1,2,3))
```

## Exercise 5 - Arrow Functions
```
const capitalize = str => str[0].toUpperCase() + str.slice(1).toLowerCase()
	
const b = capitalize("bOb") // returns Bob
console.log(b)
const t = capitalize("TAYLOR") // returns Taylor
console.log(t)
const f = capitalize("feliSHIA") // returns Felishia
console.log(f)
```

## Exercise 6 - Arrow functions
```
const determineWeather = temp => {
  if (temp > 25) {
    return "hot"
  }
  return "cold"
}
	
const commentOnWeather = temp => `It's ${determineWeather(temp)}`
	
console.log(commentOnWeather(30)) //returns "It's hot"
console.log(commentOnWeather(22)) //returns "It's cold"
```

## Exercise 7
HTML (inside <body> element):


```
<div id="box" style="width: 100vw; height: 100vh;"></div>
```