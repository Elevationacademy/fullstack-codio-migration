# Solutions

## Exercise 1
```
 let validator = require("validator")
	console.log(validator.isEmail("shoobert@dylan"))
	
	console.log(validator.isMobilePhone("786-329-9958","en-US"))
	
	let blacklist = ["!", "?", ".", "@", "~", ",", "'"]
	let text = "I'M SO EXCITED!!!~!"
	
	console.log(validator.blacklist(text, blacklist).toLowerCase())
```

## Exercise 2
```
let faker = require("faker")
	

	const makeHuman = function (num) {
	    for(let i = 0; i < num; i++) {
	

	        console.log(faker.fake("{{name.firstName}}, {{image.avatar}}, {{company.companyName}}"))
	    
	    }
	}
	

	

	makeHuman(4)
```

## Exercise 3
No Solution