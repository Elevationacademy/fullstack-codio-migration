
To get started, create a folder called `mongoose-practice`

  

Then install [mongoose](https://www.npmjs.com/package/mongoose) - a convenient NPM package. Don't forget your `npm init` before `npm install`

  

Now create a file called `person.js`. The first thing we need to do is include `mongoose`, so add this:

  

```js
const mongoose = require('mongoose')
```
  

Then, to connect mongoose to our database we will use the `connect` method:

  

```js
mongoose.connect('mongodb://localhost/peopleDB', { useNewUrlParser: true })
```


|||important
## NodeJS Version

If you are working on a **NodeJS** version that is `^17.0` , please make sure to replace the **mongodb url** to the following:

```js
mongoose.connect("mongodb://127.0.0.1:27017/myDB", {useNewUrlParser: true,});
```
|||


  

This method takes a **connection string** as its first parameter, and in the above we are passing our `local` connection - always easier to work locally for testing. You can read up about the second parameter [here](https://mongoosejs.com/docs/deprecations.html) if you're interested, but it is not so important right now.

  

Also note that we're telling mongoose which DB to connect to - in this case, the `peopleDB` - this will work **even if you haven't created this DB yet - mongoose will create it for you.**

Make sure to also add a `catch` method to catch any possible issues

```js
mongoose.connect("mongodb://127.0.0.1:27017/peopleDB", {
  useNewUrlParser: true,
}).catch((err)=> console.log(err))
```
And that's the setup. You gotta love NPM.
