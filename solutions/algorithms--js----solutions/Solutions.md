## Exercise 1

```
const printStars = function (num) {
	    let ast = ''
	    for (let i = 1; i <= num; i++) {
	        ast += "*"
	        console.log(ast)
	    }
}


```

## Exercise 2

```
const printBackwardsStars = function (num) {
	    let string = ''
	

	    while (num > 0) {
	        if (string.length < num) {
	            string += '*'
	        } else if (string.length === num) {
	            console.log(string)
	            num--
	            string = ''
	        }
	    }
}

```

## Exercise 3

```
const printStarSeries = function (num, count) {
	

	    for (let j = 0; j < count; j++) {
	        for (let i = 1; i <= num; i++) {
	            console.log(i)
	        }
	

	        for (let i = num - 1; i > 0; i--) {
	            console.log(i)
	        }
	    }
	

}

```

## Exercise 4

```
const reverse = function (str) {
	

	    let reversed = ''
	    for (let i = str.length - 1; i >= 0; i--) {
	        reversed += str[i]
	    }
	

	    return reversed
}
```

## Exercise 5

```
const isPalindrom = function (str) {
	    str = str.replace(/\s/g, '').toLowerCase()
	    console.log(str)
	    let r = reverse(str)
	

	    if (r === str) {
	        return true
	    }
	

	    return false
}
```

## Exercise 6

```
const encrypt = function (str) {
	

	    let encryptedStr = ''
	

	    for (let i = 0; i < str.length; i++) {
	        let char = ''
	        str[i] === 'z' ? char = 'a' : char = String.fromCharCode(str.charCodeAt(i) + 1)
	

	        encryptedStr += char
	    }
	

	    return encryptedStr
}
```

## Exercise 7

```
const decrypt = function (str) {
	    let decryptedStr = ''
	

	    for (let i = 0; i < str.length; i++) {
	        let char = ''
	        str[i] === 'a' ? char = 'z' : char = String.fromCharCode(str.charCodeAt(i) - 1)
	        decryptedStr += char
	    }
	

	    return decryptedStr
}
```

## Exercise 8

```
const jumble = function (arr1, arr2) {
	    let jumbledArr = []
	

	    for(let a of arr2) {
	        arr1.push(a)
	    }
	

	    while(arr1.length) {
	        let randomNumber = Math.floor(Math.random() * arr1.length)
	        jumbledArr.push(arr1.splice(randomNumber, 1)[0])
	    }
	

	    return jumbledArr
}
```

## Exercise 9

```
getLetter() {
    const rawDist = {
      A: 60,
      B: 10,
      C: 10,
      D: 20
    }
    let randomNum = Math.floor((Math.random() * 100) + 1)
    const letters = Object.keys(rawDist)
    let currentPercentage = 0
    for (let i = 0; i < letters.length; i++) {
      const letter = letters[i]
      if (rawDist[letter] + currentPercentage >= randomNum) {
        return letter
      } else {
        currentPercentage += rawDist[letter]
      }
    }
}
```

