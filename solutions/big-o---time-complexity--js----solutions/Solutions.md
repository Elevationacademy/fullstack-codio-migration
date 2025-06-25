## Exercise 1

```
O(n)
```

## Exercise 2

```
O(log(n))
```

## Exercise 3

```
O(1)
```

## Exercise 4

```
O(NM)
```

## Exercise 5

```
O(n)
```

## Exercise 6

```
const findDuplicates = function (arr) {
	

	    let obj = {}
	

	    for (let i = 0; i < arr.length; i++) {
	        if(obj[arr[i]]) {
	            obj[arr[i]]++
	        } else {
	            obj[arr[i]] = 1
	        }
	    }
	

	    Object.keys(obj).forEach(k => {
	        if(obj[k] > 1) {
	            console.log("There is a duplicate")
	        }
	    })
}

```

## Exercise 7

```
let employees = {
	    ax01: {
	        name: "Ray",
	        age: 28,
	        salary: 1300
	    },
	    qs84: {
	        name: "Lucius",
	        age: 31,
	        salary: 840
	    },
	    bg33: {
	        name: "Taylor",
	        age: 18,
	        salary: 2700
	    }
}

const findEmployeeSalary = function(employeeID) {
	    let salary = employees[employeeID].salary
	    return salary
}
```

## Exercise 8

```
const findIndex = function (numbers, num) {
	    let startIndex = 0
	    let endIndex = numbers.length - 1
	    let middleIndex, index
	    let found = false
	    while(!found) {
	        middleIndex = Math.floor((endIndex - startIndex)/2)
	        index = middleIndex + startIndex
	

	        if(num === numbers[index]) {
	            found = true
	        } else if(numbers[index] > num) {
	            endIndex = middleIndex - 1
	        } else if (numbers[index] < num) {
	            startIndex = middleIndex + startIndex
	        }
	    }
	    
	   return index
}
```