
Getting items is just as easy as setting them. Remember: localStorage is just an object, so there's nothing preventing us from accessing our data as we would from a normal object:

  
```
localStorage.name
//'Shoobert'
```
  

But, because localStorage is a special object with extra methods, we can also use getItem:

  
```
localStorage.getItem('name')
//'Shoobert'
```
  

**Spot check:** it's important to note that localStorage is an object that is _built-in_ to JS. To that end, **open up some JS file that's connected to an HTML file**. Then:

-   In your JS file, save some item to Local Storage
-   Open up your HTML in the browser, and check the Console to see that your item is there
-   Back in your JS file, write some code that gets the item's value from Local Storage, and console.log it