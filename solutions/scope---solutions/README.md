# Solutions

Exercise
-
```js
//Section 1
	

	//Will console log all the distances they ran plus the finished line and then throw an error
	//because distance is local to the if statement and the last console log is trying to access it.
	

	//===================================================================================
	/* const run = true //Global
	
	if (run) {
	    let distance = 8 // local scope to if statement
	    for (var i = 0; i < distance; i++) {
	        console.log("running")
	    }
	    console.log("Finished running " + distance + " miles")
	}
	
	console.log("Damn, you see this gal? She ran " + distance + " miles") */
	

	//===================================================================================
	//Section 2
	

	//Will throw an error because the variable is local to the if and never even get's defined
	//because the else was entered and the iff failed.
	

	//===================================================================================
	/* if (13 == "space") {
	    let cowSound = "moo" // local to the if statement
	}
	else {
	    console.log("Cow says " + cowSound)
	} */
	

	//===================================================================================
	//Section 3
	

	//Will log sentence with all items in the array and then log the sentnce with the full array.
	//No error
	

	//===================================================================================
	/* const serveOrders = function (orders) { //this funtion is global and orders is local to the function
	
	    for (let order of orders) { //order is local to the for
	        let specialOrder = "special " + order //specialOrder is local to the for
	        console.log("Served a " + specialOrder)
	    }
	
	    console.log("Finished serving all the orders: " + orders)
	}
	const allOrders = ["fish", "lettuce plate", "curious cheese"] //global array
	serveOrders(allOrders) */
	

	

	//===================================================================================
	//Section 4
	

	//Will throw an error because seed is local to getSeed and plant cannot see it
	

	//===================================================================================
	/* const pot = "red pot with earth in it" //global variable
	
	const getSeed = function () { // global function
	    const seed = "brown seed" //local to the getSeed function
	}
	
	const plant = function () { //global function
	    getSeed()
	    console.log("Planting the " + seed + " inside a " + pot)
	}
	
	plant() */
	

	//===================================================================================
	//Section 5
	

	//Will throw an error because 'found' variable is local to the if. When the function tries
	//to return it he can't access it.
	

	//===================================================================================
	/* const doesUserExist = function (name) { //name is local to the function
	    const users = [{ name: "Shapira", age: 19 }, { name: "Lucius", age: 23 }] //users is local to the funtion
	    for (let u of users) { //u is local to the for loop
	        if (u.name == name) {
	            const found = true // found is local to the if
	        }
	    }
	    return found
	}
	
	const userExists = doesUserExist("Lucius") //global variable
	if (userExists) {
	    console.log("We found the ragamuffin!")
	}
	else {
	    console.log("No idea where this person is.")
	} */
	

	

	//===================================================================================
	//Section 6
	

	//Will console log "Finally, sheesh" --* Wrong
	//We cannot change the isEnough variable because it is a const. Will thrown an error
	

	//===================================================================================
	const isEnough = false // global variable
	

	const makeEnough = function () { // global function
	    for (let i = 0; i < 10; i++) { //i is local to the for
	        if (i > 5) {
	            isEnough = true
	        }
	    }
	}
	

	makeEnough()
	if (isEnough) {
	    console.log("Finally, sheesh")
	}
	else {
	    console.log("Here we go again...")
	}
```