## Exercise 1

Set up a new directory called npm-exercises, and inside create one file called ex.js

  

Create your NPM environment using npm init, then install the [validator](https://www.npmjs.com/package/validator) package.

  

Read its documentation, and then use the package for the following:
```
//Ex. 1
//Check whether "shoobert@dylan" is a valid email (should be false)

//Ex. 2
//Check whether "786-329-9958" is a valid US mobile phone number (should be true) - use the en-US locale

//Ex. 3
//Use the following blacklist
let blacklist = ["!", "?", ".", "@", "~", ",", "'"]
//Along with validator's `blacklist` method to clean this text:
let text = "I'M SO EXCITED!!!~!"
//Ultimately, it should print "im so excited"
```

## Exercise 2

Read the docs for the [faker package](https://www.npmjs.com/package/@faker-js/faker), then do the following in the same ex.js file:

  

Install the package, require it, and create a function called makeHuman

-   The function should receive a number
-   Inside, you should create as many people using faker as the number received
-   Each person should have a name, an image URL (avatar), and a company name

  

Because faker uses random data, your result will be different, but it should be something like this:
```
makeHuman(2) //prints the following:
// Viola, https://s3.amazonaws.com/uifaces/faces/twitter/motionthinks/128.jpg, Donnelly - Feil
// Isaias, https://s3.amazonaws.com/uifaces/faces/twitter/gt/128.jpg, Wilkinson, Hickle and Hoppe
```



## Exercise 3

For a bit of extra practice, go back to an old project (or a few) where you used jQuery, Handlebars, and Font Awesome (or any combination), and use NPM to host these libraries instead of the CDN. Then, of course, push your project to Github again _without_ the node_modules directory.

  

----------

  

#### **npm install done**



