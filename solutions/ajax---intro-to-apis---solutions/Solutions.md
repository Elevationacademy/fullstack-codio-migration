## Exercise 1

```
const fetch = function (isbn) {
	    $.ajax({
	        method: "GET",
	        url: `https://www.googleapis.com/books/v1/volumes?q=isbn:${isbn}`,
	        success: function (data) {
	            console.log(data);
	        },
	        error: function (xhr, text, error) {
	            console.log(text);
	        }
	    }); 
}
	
fetch(9782806269171)
```


## Exercise 2

```
const fetch = function (queryType, queryValue) {
	   $.ajax({
	       method: "GET",
	       url: `https://www.googleapis.com/books/v1/volumes?q=${queryType}:${queryValue}`,
	       success: function (data) {
	           console.log(data);
	       },
	       error: function (xhr, text, error) {
	           console.log(text);
	       }
	   }); 
}
	
fetch("title", "The Wise Man's Fears")
fetch("isbn", 9789814561778)
```


## Exercise 3

```
const fetch = function (queryType, queryValue) {
	  $.ajax({
	      method: "GET",
	      url: `https://www.googleapis.com/books/v1/volumes?q=${queryType}:${queryValue}`,
	      success: function (data) {
	          data.items.forEach(b => console.log(`Title: ${b.volumeInfo.title}, Author: ${b.volumeInfo.authors}, ISBN: ${b.volumeInfo.industryIdentifiers[0].identifier}`))
	      },
	      error: function (xhr, text, error) {
	          console.log(text);
	      }
	  }); 
}
	
fetch("title", "The Wise Man's Fears")
```


## Exercise 4

```
const fetch = function () {
	    $.get("http://api.giphy.com/v1/gifs/search?q=cats&api_key=50m5Set06jQuFMy7VNXir7iaNl8ypsEu", function (gifs) {
	        console.log(gifs.data[0].embed_url)
	        $(".gif").append(`<iframe src="${gifs.data[0].embed_url}">`)
	    })
}
	
fetch()
```


## Exercise 5

```
const fetch = function (input) {
	    $.get(`http://api.giphy.com/v1/gifs/search?q=${input}&api_key=50m5Set06jQuFMy7VNXir7iaNl8ypsEu`, function (gifs) {
	        //console.log(gifs.data[0].embed_url)
	        $(".gif").append(`<iframe src="${gifs.data[0].embed_url}">`)
	    })
}
	
	
$("#submit").on("click", function () {
	    let input = $("#yourgif").val()
	    console.log(input)
	    fetch(input)
})
```


## GIF Generator Extension

```
const appendGifs = function (gifs) {
	    
	    const shortGifs = []
	    
	    for(let i = 0; i < 5; i++) {
	        shortGifs.push(gifs.data[i])
	    }
	
	    const urls = shortGifs.map(sg => sg.embed_url)
	
	    const source = $("#gif-template").html()
	    const template = Handlebars.compile(source)
	
	    const newHTML = template({urls})
	    $(".gif").append(newHTML)
}
	
	
$(".gif").on("click", ".add", function () {
	
	    $(".favorite-gifs").append(`<iframe src="${$(this).data().id}"></iframe>`)
	
})
	
	
	
const fetch = function (input) {
	    $.ajax({
	        method: "GET",
	        url: `http://api.giphy.com/v1/gifs/search?q=${input}&api_key=50m5Set06jQuFMy7VNXir7iaNl8ypsEu`,
	        success: appendGifs
	    })
}
	
	
	
$("#submit").on("click", function () {
	
	
	    let input = $("#yourgif").val()
	    console.log(input)
	    fetch(input)
})
```


## Google Books API Extension

```
  let neruoscienceComputerBooks = []
	

	const fetch = function (startIndex) {
	    $.ajax({
	        method: "GET",
	        url: `https://www.googleapis.com/books/v1/volumes?q=intitle:neuroscience&startIndex=${startIndex}&maxResults=40`,
	        success: function (data) {
	            console.log(data)
	            let book
	            for (let j = 0; j < data.items.length; j++) {
	                book = data.items[j]
	                if (book.volumeInfo.categories) {
	                    if (book.volumeInfo.categories.some(c => c === "Computers")) {
	                        neruoscienceComputerBooks.push(book.volumeInfo.title)
	                    }
	                }
	

	            }
	

	            console.log(neruoscienceComputerBooks)
	        },
	        error: function (xhr, text, error) {
	            console.log(text);
	        }
	    });
	}
	

	let startIndexArr = [0, 40, 120]
	for (let i = 0; i < 3; i++) {
	    console.log(i)
	    fetch(startIndexArr[i])
	}
	

	console.log(neruoscienceComputerBooks)
```