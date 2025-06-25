
Getting the data from the API is half the job. Usually, we get our data in some big JSON, and then we need to extract the interesting information - that's the second half of working with APIs. Luckily, you already have quite a bit of practice with this. Remember, JSON is just a special kind of JavaScript object.

  

So whenever you use a new API, you should **first scan through the data, then understand what the properties of interest are and where they are nested**.

  

For instance, if we make a request to this simple [user generator API](https://jsonplaceholder.typicode.com/users), we can extract a user's `geo` data like this:


```js
//request the data with a GET request
$.get("https://jsonplaceholder.typicode.com/users", function(users){
  //extract the geo data of the first user

  let lat = users[0].address.geo.lat
  let long = users[0].address.geo.lng
  
  //log the data
  console.log(`${lat}, ${long}`) //prints -37.3159, 81.1496
})
```
  

**Spot check:** using the same API, how would you extract the `catchPhrase` of the last user's company?

  
<details><summary>  
Click here to reveal the answer.  
</summary>

 
```users[users.length - 1].company.catchPhrase```
</details>
