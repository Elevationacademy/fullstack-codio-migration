For all of that, all we really need to do to use a promise is the `then` method, and maybe sometimes a `Promise.all`.

  

To practice, here are a couple of exercises:

  

----------

  

## Exercise 1


  

Using the following [random word API](http://random-word-api.herokuapp.com/home)

  
1.  Make a request to the **API** and get a random word
2.  _Then_ use that word to make a request to the **Google Books API**
3.  You should request a book whose `title` has that random word

  

For your convenience, here is the URL for this API: `https://www.googleapis.com/books/v1/volumes?q=intitle:WORD_HERE`

Nice, you've created a random book generator.

## Exercise 2

Now do the same, except instead of only getting a random book, get a random book _and_ a random [GIF](https://developers.giphy.com/docs/) based off the word that came back from `/randomWords`.

  

When `all` of the data you want comes back, display it on the page. It doesn't have to be anything fancy, you can just add the book title and the GIF directly to the `body`.

Now we're talking.

  

----------

  

#### **DO.then( function(NE){ } )**

  

Well done. We promise you'll get used to using Promises.
