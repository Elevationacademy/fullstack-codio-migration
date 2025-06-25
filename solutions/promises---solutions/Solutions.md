## Exercise 1
```
$.get('/randomWord')
    .then(function(word) {
        console.log(word)
        return $.get(`https://www.googleapis.com/books/v1/volumes?q=intitle:${word}`)
    })
    .then(function(book) {
        console.log(book);
    })
```

## Exercise 2
```
$.get('/randomWord')
	    .then(function(word) {
	        console.log(word)
	        let randomBook = $.get(`https://www.googleapis.com/books/v1/volumes?q=title:${word}`)
	        let randomGif = $.get(`http://api.giphy.com/v1/gifs/search?q=${word}&api_key=50m5Set06jQuFMy7VNXir7iaNl8ypsEu`)
	        Promise.all([randomBook, randomGif])
	            .then(function(result) {
	                $("body").append(`<div>${result[0].items[0].volumeInfo.title}</div>`)
	                $("body").append(`<iframe src="${result[1].data[0].embed_url}">`)
	            })
	    })
```


