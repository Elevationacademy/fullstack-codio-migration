## Exercise 1
```
$("button").on("click", function () {
	    $("#human-list").append(`<li>${$("input").val()}</li>`)
	    $("input").val("")
	})
```

## Exercise 2
```
$("#human-list").on("click", "li", function() {
	    $(this).remove()
	})
```

## Exercise 3
```
$("body").append("<div class="box"></div>")
$("body").append("<div class="box"></div>")
	
let $boxes = $(".box")
	
$(".box").hover(function () {
  $boxes.css("background-color", "rgb(231, 76, 60)")
  $(this).css("background-color", "rgb(142, 68, 173)")
})
```

## Exercise 4
```
$(".item").click(function () {
	
	    if ($(this).data().instock) {
	        $("#cart").append(`<div class="cart-item">${$(this).text()}</div>`)
	    }
	}) */
```

## Exercise 5
```
const fruits = [
	    { name: "Orange", color: "orange" },
	    { name: "Banana", color: "yellow" },
	    { name: "Coconut", color: "brown" },
	    { name: "Kiwi", color: "brown" },
	    { name: "Lemon", color: "yellow" },
	    { name: "Cucumber", color: "green" },
	    { name: "Persimmon", color: "orange" },
	    { name: "Pumpkin", color: "orange" }
	  ]
	
	  for(let fruit of fruits) {
	      $("#basket").append(`<div class="${fruit.color}">${fruit.name}</div>`)
	  }
```

## Extensions - Color Picker
```
let $spans = $("span")
	
	for(let $span of $spans) {
	  console.log($span)
	  $($span).addClass("picker")
	  $($span).css("background-color", $($span).data().color)
	
	  $($span).on("click", function () {
	      const color = $($span).data().color
	      $(".box").css("background-color", color)
	  })
	}
```

## Extensions - Cart
```
let melonCounter = 1
	let shoeCounter = 1
	

	$(".item").click(function () {
	

	    if ($(this).data().instock) {
	

	        if ($(this).text() === "Shoe") {
	

	            if (shoeCounter === 1) {
	                $("#cart").append(`<div class="cart-item shoe">${$(this).text()}</div>`)
	                shoeCounter++
	            } else {
	                $(".shoe").remove()
	                $("#cart").append(`<div class="cart-item shoe">${$(this).text()} x${shoeCounter}</div>`)
	                shoeCounter++
	            }
	

	        } else if ($(this).text() === "Melon") {
	            if (melonCounter === 1) {
	                $("#cart").append(`<div class="cart-item melon">${$(this).text()}</div>`)
	                melonCounter++
	            } else {
	                $(".melon").remove()
	                $("#cart").append(`<div class="cart-item melon">${$(this).text()} x${melonCounter}</div>`)
	                melonCounter++
	            }
	        }
	

	    }
	})
	

	$("#cart").on("click", ".cart-item", function () {
	    $(this).remove()
	})
```
