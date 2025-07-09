# Client Vs  Server Packages

Though NPM literally has **Node** as the first part of its acronym, we're not limited to node when we use NPM packages. We can also take advantage of NPM (depending on the package) in the browser.

  

For example, we've hitherto imported jQuery, Handlebars, and font-awesome like this:
```
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU"crossorigin="anonymous">

<script src="https://code.jquery.com/jquery-3.3.1.js" integrity="sha256-2Kok7MbOyxpgUVvAk/HJ2jigOSYS2auK4Pfzbm7uH60="crossorigin="anonymous"></script>

<script src="https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.12/handlebars.amd.js"></script>
```
  

Which is a pain, because we'd always have to go and find those CDNs - but no more! Now you can run the following command:

  
```
npm install jquery handlebars font-awesome
```
  

Yes, you can install multiple packages at once - just separate them with a space.

And then add them to our HTML like this:

  
```
<!-- Before, our `href` and `src` were external links - now it's just our `node_modules` folder -->

<link rel="stylesheet" href="./node_modules/font-awesome/css/font-awesome.css" >
<script src="./node_modules/jquery/dist/jquery.js"></script>
<script src="./node_modules/handlebars/dist/handlebars.js"></script>
```
  

Which is much, much cleaner, more straightforward, and definitely more reliable.

  

Of course, the code in these packages is the exact same as what you get from the old way (using the CDN) - and it will still only work in JS that you run in the browser, but **NPM is a package manager for any JS code, not just code that runs in node**.

  

This might be confusing, but if you realize that humans called this **Node**Package Manager because at first it was just for Node, and you realize that humans don't always think ahead, then you should be able to sleep at night.

  

----------

  

**Spot check:** Create a directory called npm-jquery-run, and inside of it create two files: index.html and main.js

-   Use NPM to install jQuery
-   Import jQuery in your HTML from node_modules
-   Create a small div in your HTML - give it some dimensions and a background color
-   In your JS file, use jQuery to add a listener to the div - when you click it, it should change to the color "#f39c12"

  

Once that works, in your JS file make a GET request to the following API, and console log the results:
```
https://ele-people-api-8eb0b1bd9b96.herokuapp.com/people
```
  

Unfortunately, the above GET request won't work (but still do it so you see the error). Let's fix that.