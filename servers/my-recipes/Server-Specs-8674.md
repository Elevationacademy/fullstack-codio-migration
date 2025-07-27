## Basics


In order to access the **API**, you will have to explore the following [**Recipe API**](https://recipes-goodness-elevation.herokuapp.com).

- Create a route inside the server that gets all recipes from the Recipes API which contains a certain ingredient .
  

|||info
## Note

You can use the **axios** library to make requests to the **API**.
|||


<details><summary>
  Click here to reveal a hint.
</summary>

Notice that when you make a request to this API _from the server_, you're going to receive a very big **string** with some data in it.

You will need to `JSON.parse` this string (remember, you need to **first extract it from the body** of the API's response). The actual data you're interested is an array that is inside.
</details>

</br>

## Filtering

When returning the data to the client, make sure to filter the data in the server, meaning you will be removing all the irrelevant data from the data we are sending back. 



## Static Serving Files

Because we want our **app** to be accessable to everyone accessing the server, our server will serve the entire client files using ``app.use(express.static...)``, but in terms of the **flow of data**, we have a client-server request, then server-externalAPI request, and then of course the data has to flow back: from the NBA API to our server, and from our server back to our client.
