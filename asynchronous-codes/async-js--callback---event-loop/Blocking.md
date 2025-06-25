
**_Main point:_** _Javascript is_ **_single-threaded_** _and_ **_blocking_**_. It can only do one thing at a time._

  

Let's look at an example of blocking code. Copy/paste the following into your console:

  

```js
function pause (milliseconds) {
  var date = new Date();
  while ((new Date()) - date <= milliseconds) { 
    /* Do nothing */ 
  }
};

function firstFunc () {
  pause(3000)
  console.log('I have to go first.')
};

function secondFunc () {
  console.log('Then I can go');
};

firstFunc();
secondFunc();
```
  

We created a useless function called `pause` to simulate a function that takes some time to return (such as an HTTP request or database query). Notice that `secondFunc` does not return until `firstFunc` is finished. This is because firstFunc _blocks_ the call stack - `secondFunc` cannot execute until `firstFunc` is finished, which won't return until `pause` is done.
