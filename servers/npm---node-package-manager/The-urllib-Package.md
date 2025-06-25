
Sometimes, GET requests from a browser don't work. Generally this has to do with security issues - we won't dive into this right now - but often making the same request from node will work.

  

So far we've made GET requests using jQuery's $.get or $.ajax methods - but of course jQuery won't work in node because jQuery only works in the browser.

  

Luckily, there is a package called request which allows us to make HTTP requests in node [very simply.](https://www.npmjs.com/package/request), check github docs if it doesnt appear

  

To see this package in action, we'll first have to npm install request (do this in your package-exploration folder for simplicity), and then run the following (in your time.js file):

  
```
const request = require('request');

request('https://ele-people-api-8eb0b1bd9b96.herokuapp.com/people', function (error, response, body) {
  console.log(body); 
});
```
  

You'll notice that the syntax is slightly different. We still provide the API URL first, and then use a callback function - but the parameters of the callback are: an error object, and then the response we've received.

  

The request function makes a GET request the same way $.get or the browser does, but it forces us to add an err parameter to our callback. We don't have to do anything with it, but it has to be the first parameter (of course, you could call it error or derp or whatever).

  

Anyway, now the above request works! If you look at your console log, you should see a massive JSON with a bunch of NBA player data - note that this JSON is a string, we always have to call the function toString() to convert the response from Buffer to string (for now, we didn't learn about buffer, but you can read more about it [here](https://www.freecodecamp.org/news/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8/)). Now, you have a stringified JSON - but you know how to handle this ;)

  

**Spot check:** make an API request to the [free movies API](http://www.omdbapi.com/) - you'll have to get an API key ([free and quick](http://www.omdbapi.com/apikey.aspx)), and then build your URL like this:

  
```
http://www.omdbapi.com/?apikey=YOUR_KEY&t=MOVIE_TITLE
```
  

Do this request in **node**, of course, using the request package.

  

Once that's done, console log the Released property for the movie "The Lion King" - it should be "24 Jun 1994".

  

----------

####   

Alright, this lesson may have been a bit heavy on the text - but that's because there's a lot to understand when working with NPM. Good job on getting here.

  

As with everything in programming that uses something external (APIs, packages), you're going to have to **read the documentation** to understand how some things work - this is a fundamental part of being a developer.