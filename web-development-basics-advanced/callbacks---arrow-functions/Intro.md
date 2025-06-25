
In this lesson, we're going to learn two _entirely separate_, non-related concepts in JS:

-   Callback Functions
-   Arrow Functions

  

We'll also get to practice functions a little more, because they're funportant.

  

Both of these will come into play more as the course progresses. Enjoy!

  

----------

  

  

**CALLBACK FUNCTIONS**

  

Simply put, a callback is a function that is passed to another function as a variable, and is executed _by_ that function. This may seem trivial, but let's look at this example:

  
```
let users = []

const getData = function () {
    users = [{ name: "Rick" }, { name: "Morty" }]
    console.log("Got users")
}

const displayData = function () {
    console.log("Going to display users")
    for (user of users) {
        console.log(user.name)
    }
}

getData()
displayData()
```

  

The above will work as expected:

-   The getData function will populate the users array, then console log "Got users"
-   The displayData function will console log the array its going to display, then iterates through each user and console log their names

  

See for yourself that this works.

  

The above is called **synchronous code** - that is, code that executes one line at a time, in order, without delays.

  

However, sometimes parts of our code are **asynchronous** - i.e. it might take a while before the code actually finishes executing.

For instance, if getData is retrieving the user data from a database, then it definitely makes sense that it will take longer than normal for that code to run.

  

Let's simulate this by using setTimeout - we can use this to delay what happens inside of getData:

  
```
const getData = function () {
    setTimeout(function () {
        users = [{ name: "Rick" }, { name: "Morty" }]
        console.log("Got users")
    }, 3000)
}

getData()
```

  

**Run the code above** and notice that it takes 3 seconds (3,000 milliseconds) until we see "Got users".

  

Don't worry too much about how setTimeout* works right now - we're just using it for the example to show that sometimes code doesn't always finish executing right away.

###### *Of course, if you are curious, [here](https://www.bitdegree.org/learn/javascript-settimeout/) is a reference

  

Ok, now our entire code looks like this:

  
```
let users = []

const getData = function () {
    setTimeout(function () {
        users = [{ name: "Rick" }, { name: "Morty" }]
        console.log("Got users")
    }, 3000);
}

const displayData = function () {
    console.log("Going to display users")
    for (user of users) {
        console.log(user.name)
    }
}

getData()
displayData()
```
  

Notice that we're still calling getData _before_ displayData - and yet, when we run this code, this is what we see in the console log:

  
```
Going to display users 
```
  

then, three seconds later...

  
```
Got users
```
  

This happens because it takes 3 seconds for getData to actually get the data! That means the users array is empty when displayData gets executed, and therefore there are no users to loop over and display!

  

  

This is the problem we are trying to solve: how do we guarantee one function runs after another, no matter what?

  

The answer is callback functions.