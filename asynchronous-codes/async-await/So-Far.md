
Let's take a couple of examples of async code we've dealt with in the past.

  

**API Requests** (client-side):

  

```js
const API_URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:0439023521"

const fetchData = function(){
    $.get(API_URL, function(res){
        console.log(res.items[0])
    })
}
```
  

**DB Operations** (server-side):

  

```js
const fetchData = function (surname) {
    Person.find({ lastName: surname }, function (err, people) {
        console.log(people)
    })
}
```
  

Both of these use **callbacks**. Of course, we could use **promises** to clean that up a bit - but we still eventually have to have a callback.

  

Now, **there is nothing wrong with callbacks** - but sometimes, don't you wish you could just avoid them?

Your **a**wait is over!
