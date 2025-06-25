
There are a few ways to include the jQuery library in your project.

  

-   Download [the latest version](http://jquery.com/download) of jQuery
-   For development purposes we recommend going for the "uncompressed, development version" as it is easier to debug
-   Move the downloaded JS file into your project folder, then add a script tag that points to it - add this tag _before_ your main.js tag
-   Use a CDN (Content Delivery Network)
-   Point your script tag to a file in the cloud. For example: <script src="https://code.jquery.com/jquery-3.3.1.js" crossorigin="anonymous"></script>
-   Use NPM (Node Package Manager)
-   We've not learned about this yet, but in future lessons it will be our preferred method

  

----------

  

Let's jump right in. **Create a new project** and call it something sensible like "jQuery101".

  

Add an index.html and inside it include a jQuery script tag via one of the above methods.

Also include a script tag that point towards a file of your own called main.js

  

Your HTML should look more or less like this for starters:
```
<!DOCTYPE html>
<html><head>
    ﻿<title>jQuery101</title><link rel="stylesheet" href="style.css" /></head><body>
          
     <script src="https://code.jquery.com/jquery-3.3.1.js" crossorigin="anonymous"></script>
     ﻿<script src="main.js"></script></body>
﻿</html>
 ```