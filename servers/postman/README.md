# Basic Usage

When you finish installing and logging in, you should see a screen more or less like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-starter.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-starter.PNG) to emibggen.

  

Now, say you're making a GET request to our favorite [user api](https://jsonplaceholder.typicode.com/users) - we can make this request via the browser, or with a `$.get` request - and now we can also make it with Postman. Just enter this URL into the input, press send, and you should soon enough see the result:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-first-get.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-first-get.PNG) to emibggen.

  

It knows to make a GET request because of the GET on the side - but we can change that, it's a drop-down!

  

----------

  

To test other request types, go ahead **create a** `dummy-server.js` **file** with the following code, then **run** `node dummy-server.js`:

  
```
const express = require('express')
const bodyParser = require('body-parser')

const app = express()
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: false }))

app.get('/test/:data', function (req, res) {
    console.log("Someone is getting!")
    console.log(req.params.data)
    res.send("Thanks for the get, here's a potato.")
})

app.post('/test', function (req, res) {
    console.log("Someone is posting!")
    res.send("Thanks for the post, here's a potatoe.")
})

app.post('/testData', function (req, res) {
    console.log(req.body)
    res.end()
})

const port = 4349
app.listen(port, function () {
    console.log(`Server running on ${port}`)
})
```
  

We can use Postman to make a GET request to this `get` route as well - we just have to give it the whole path: `http://localhost:4349/test/something`:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-get-to-custom-api.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-get-to-custom-api.PNG) to emibggen.

  

And of course, we can also use Postman to make a request to our `post` route, we just need to select POST from the dropdown:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-post-to-custom-api.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/postman-post-to-custom-api.PNG) to emibggen.