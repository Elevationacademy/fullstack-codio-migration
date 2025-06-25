
We said that we're learning mongoose so that we can access our DB through our server. Let's see how that looks.

  

Take a look at this setup:

```js
// Server setup
const express = require('express')
const app = express()

// Mongoose setup
const mongoose = require('mongoose')
const Schema = mongoose.Schema
mongoose.connect("mongodb://127.0.0.1:27017/peopleDB", {
  useNewUrlParser: true,
}).catch((err)=> console.log(err))
// Schema/model setup
const personSchema = new Schema({
    firstName: { type: String, required: true },
    lastName: String,
    age: Number
})
const Person = mongoose.model("person", personSchema)

//Routes
app.get('/people', function (req, res) {
    Person.find({}).then( function (people) {
        res.send(people)
    })
})

const port = 4200
app.listen(port, function () {
    console.log(`Running on port ${port}`)
})
```
  

Now if you run the above file (node `server.js` assuming you called the file `server.js`) and go to `localhost:4200/people` - you'll receive an array of objects from the database!

  

But in reality what's happening is the client (browser) is going to the `/people` route in the server, the server is querying the DB using mongoose, the DB returns some data, and the server `.sends` the data back to the client. Full Stack!

  

----------

  

Of course the above is a little bloated for a server file, so we would like to separate it to separate files.

In terms of our file hierarchy, it looks like this:

-   /server
-   /models
-   Person.js
-   /routes
-   api.js
-   server.js

And this is how each file would look:

  

**server.js**


```js
// Server setup
const express = require('express')
const app = express()
const api = require('./server/routes/api')

// Mongoose setup
const mongoose = require('mongoose')
mongoose.connect("mongodb://127.0.0.1:27017/peopleDB", {
  useNewUrlParser: true,
}).catch((err)=> console.log(err))

app.use('/', api)

const port = 4200
app.listen(port, function () {
    console.log(`Running on port ${port}`)
})
```
  

----------

  

  

**Person.js** - we will have a separate file for each schema/model, i.e. for each collection.


```js
const mongoose = require('mongoose')
const Schema = mongoose.Schema

const personSchema = new Schema({
    firstName: { type: String, required: true },
    lastName: String,
    age: Number
})

const Person = mongoose.model("person", personSchema)
module.exports = Person
```
  

Notice that ultimately we're **only exporting the model**, as that's what we'll be using for document creation/querying.

----------

  

**api.js** - nothing new here, except that we're importing the `Person` model:


```js
const express = require('express')
const router = express.Router()

const Person = require('../models/Person')

router.get('/people', function (req, res) {
    Person.find({}).then( function (people) {
        res.send(people)
    })
})

module.exports = router
```
