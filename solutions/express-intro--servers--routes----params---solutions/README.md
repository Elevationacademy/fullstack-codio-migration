# Solutions

## Exercise 2
```
app.get('/priceCheck/:name', function(request, response) {
	    let name = request.params.name
	    let priceObj = {price: null}
	    for(let obj of store) {
	        if(obj.name === name) {
	            priceObj = {price: obj.price}
	        }
	    }
	

	    response.send(priceObj)
	})
```

## Exercise 3
HTML:
```
 <div id="inputs">
	        <input type="text" placeholder="Enter furniture" id="furniture">
	        <button id="submit">Submit</button>
	    </div><br>
	    <div id="money-container">Money: </div>
```
JS:
```
$("#submit").on("click", function () {
	    const input = $("#furniture").val()
	    $.get(`/priceCheck/${input}`, function (furnData) {
	        $("body").append(`<div>${furnData.price}<div>`)
	    })
	    $("#furniture").val("")
	})﻿
```

## Exercise 4
```
app.get('/buy/:name', function(request, response) {
	    let name = request.params.name
	    for(let obj of store) {
	        if(obj.name === name) {
	            obj.inventory -= 1
	            response.send(`Congrats! You've just bought ${obj.name} for ${obj.price}. There are ${obj.inventory} left in stock.`)
	        }
	    }
	

	    response.end()
	})
```

## Exercise 5
html:
```
 <input type="text" placeholder="What would you like to buy" id="buy-furniture">
	        <button id="buy">Buy</button>
```
js:
```
$("#buy").on("click", function () {
    const input = $("#buy-furniture").val()


    $.get(`/buy/${input}`, function (response) {
        $("body").append(`<div>${response}<div>`)
    })


    $("#buy-furniture").val("")
})
```

## Exercise 6
```
app.get('/sale', function(request, response) {
	    let q = request.query
	    if(q.admin) {
	        for(let obj of store) {
	            if(obj.inventory > 10){
	                obj.price *= 0.5
	

	            }
	            console.log(obj.price)
	        }
	    }
	

	    response.end()
	})
```

## Extension 1 
html:
```
<div id="money-container">Money: </div>
```
js:
```
$("#buy").on("click", function () {
	    const input = $("#buy-furniture").val()
	

	    $.get(`/priceCheck/${input}`, function(priceObj) {
	        if(money >= priceObj.price) {
	            $.get(`/buy/${input}`, function (response) {
	                $("body").append(`<div>${response}<div>`)
	            })
	            money -= priceObj.price
	            fetch()
	        } else {
	            $("#money-container").append(`<div>Not enough money, get a job!</div>`)
	        }
	    })
	

	    $("#buy-furniture").val("")
	})﻿
```

## Extension 2
```
let currentChairPrice
	

	setInterval(function() {
	    $.get(`/priceCheck/chair`, function(priceObj) {
	        if(!currentChairPrice) {
	            currentChairPrice = priceObj.price
	            console.log("set current price")
	        } else if(priceObj.price < currentChairPrice) {
	            $.get('/buy/chair', function(response) {
	                console.log("bought chair for less")
	                currentChairPrice = priceObj.price
	            })
	        } else {
	            console.log("Still waiting for price drop.")
	        }
	    })
	

	}, 3000)
```