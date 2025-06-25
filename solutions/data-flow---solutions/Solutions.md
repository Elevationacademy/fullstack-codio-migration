## Recap Exercise
```
const posts = [
	    {
	        name: "Uncle Jerome",
	        text: "Happy birthday kido!"
	    },
	    {
	        name: "BFF Charlene",
	        text: "HEARTS LOVE YOU FOREVER BFF4LYFE HBD"
	    },
	    {
	        name: "Old High School Teacher",
	        text: "Hey ace, have a good one."
	    }
	]
	

	const render = function() {
	    for(let post of posts) {
	        $("#posts").append($(`<div class="post">${post.name}: ${post.text}</div>`))
	    }
	}
	

	render()
	

	$("button").on("click", function () {
	    
	

	    const $name = $("#name")
	    const $text = $("#text")
	

	    const post = {name: $name.val(), text: $text.val()}
	

	    posts.push(post)
	

	    $("#posts").empty()
	    render()
	

	    $name.val("")
	    $text.val("")
	})
```

## Extension
```
$("#posts").on("click", ".post", function () {
	    
	    const $post = $(this)
	    
	    const name = $post.text().substring(0, $post.text().indexOf(":"))
	    
	

	    
	    for(let i in posts) {
	        if(posts[i].name === name) {
	            posts.splice(i, 1)
	        }
	    }
	

	    $("#posts").empty()
	    render()
	})
```