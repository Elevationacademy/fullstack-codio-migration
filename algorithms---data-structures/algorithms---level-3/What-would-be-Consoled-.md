# What would be Consoled?

Look at the code, and **without executing the code** decide what will be printed in the console.


```js
(function () {
    console.log(1);
    setTimeout(function () { console.log(2) }, 1000);
    console.log(3);
    setTimeout(function () { console.log(4) }, 0);
    setTimeout(function () { console.log(6) }, 0);
    console.log(5);
})();
```


