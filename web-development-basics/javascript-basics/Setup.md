# Setup

In terms of running our JS code, there's no visual output like HTML and CSS, which is why we work with the **console** when dealing with JS.

  

In Chrome (and similar for other browsers), we can access the console by right-clicking on the page, selecting **Inspect**, and entering the "Console" tab.

  
There is also the **Ctrl+Shift+I** shortcut for Windows,or **⌘+option+J** for Mac.
  

Whenever we write `console.log("something")` in our JS code, whatever that _something_ is will output here, in the console.
  

We can also write code directly in the console (it's interactive) - but it's not as comfortable for longer pieces of code.
 

Just to try it out though, write `37 + 5` in the console, and you should see `42` output on the next line.

  
But, for the most part, **we will write JS code in our** **`main.js`** **file** - so go ahead and create that file, and connect it to your HTML file using the following line in the `header` tag in your **index.html** file:
  

```html
<script src="main.js"></script>
```
  
Make sure your files are in the same directory or this won't work!

  
To make sure everything is set up correctly, add this line to your **main.js** file:
  

```js
console.log("Hello, world!")
```
  
Then open up your **index.html** in the browser, and enter the console like we discussed before.

You should see "Hello, world!" in the console - boom, we're set up.

There are two ways to comment out code pieces in JavaScript :
- adding `//` to the begining of a line.
- wrapping a piece of code with `/*` in the beginning, and `*/`

```js
// console.log("Hello, World")

/*
  console.log("Hello, World")
  console.log("Bye, World")
*/
```

----------

There is another way to write/execute JS code, and that is directly inside our HTML, in between two `script` tags, like this:

  
```html
<body>
  ﻿<script>console.log("You will definitely see this")</script>
</body>
```
  

Typically, we do **not** want to write JS like this (inside our HTML), but it is important to understand that **ultimately, our JS will be run where we insert it in the HTML**.

  

In other words, where we place our tag makes a difference: if we place it _before_ our HTML, our JS will execute _before_ any of the HTML gets rendered.

  

Likewise, if we place our tag _after_ our HTML (before the closing `body` tag) then our JS will execute after our HTML gets rendered - this is generally what we prefer to do.
