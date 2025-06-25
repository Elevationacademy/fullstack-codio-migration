## Exercises
html:
```
  <div>
	        <input type="text" placeholder="simple">
	        <button id="app">Click me</button>
	        <button id="ls-clear">Clear wisdom</button>
	    </div>
	

	    <div id="info"></div>
```
JS
```
﻿let wisdom = []
	let input
	// let texts = localStorage.wisdom || []
	

	let texts = JSON.parse(localStorage.wisdom || "[]")
	

	

	if (texts) {
	    for (let a of texts) {
	        $("#info").append(`<div class="line-delete" data-id="${a.text}"><i class="fas fa-trash delete"></i><span>${a.text}</span></div>`)
	    }
	}
	

	let isInside
	let p
	$("#app").on("click", function () {
	    $("#info").empty()
	    input = $("input").val()
	    $("#info").append(`<div>${input}</div>`)
	    wisdom.push({ "text": input })
	    $("input").val("")
	

	    if (!(wisdom.length % 2)) {
	        if (localStorage.wisdom) {
	            p = JSON.parse(localStorage.wisdom)
	            for (let i in wisdom) {
	                isInside = false
	                for (let j in p) {
	                    if (p[j].text === wisdom[i].text) {
	                        isInside = true
	                    }
	                }
	                if(!isInside){
	                    p.push(wisdom[i])
	                }
	            }
	            localStorage.wisdom = JSON.stringify(p)
	        } else {
	            localStorage.wisdom = JSON.stringify(wisdom)
	        }
	

	    }
	})
	

	$("#ls-clear").on("click", function() {
	    localStorage.removeItem("wisdom")
	    $("#info").empty()
	})
	

	$("#info").on("click", ".delete", function() {
	    $(this).closest(".line-delete").remove()
	

	    let id = $(this).closest(".line-delete").data().id
	

	    let storage = JSON.parse(localStorage.wisdom)
	

	    for(let i in storage) {
	        if(storage[i].text == id){
	            storage.splice(i, 1)
	        }
	    }
	

	    localStorage.wisdom = JSON.stringify(storage)
	})
```
