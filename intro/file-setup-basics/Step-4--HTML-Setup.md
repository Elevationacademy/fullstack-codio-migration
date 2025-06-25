Okay, now we're ready to write some code! We'll start with our HTML file.



Most of our projects will have an HTML file named **index.html**. The index file is the main file that gets run in our browser and it's where we connect all our other files (if we have them). Go ahead and copy/paste the following code inside of our **index.html** file:

```html
<!DOCTYPE html>
<html>

  <head>
    ﻿<meta charset="utf-8" />
    ﻿<meta http-equiv="X-UA-Compatible" content="IE=edge">
    ﻿<meta name="viewport" content="width=device-width, initial-scale=1">
    ﻿<title>Page Title</title></head>
                    
  <body>
                    
  </body>
                    
</html>
```

This is our "HTML boilerplate". Boilerplate code is what we call code that we use to set-up our projects.

In VS Code you can start typing out `html`, then choose the second option from the auto-complete (the one with the screen icon), and press enter - it should give you the above boilerplate and more (which we'll cover soon) - note that this will only work if you are in an `___.html file`.

In the first line in the image above, we declare to the browser (the thing that actually runs our code) that we're using HTML. 

The `html` wraps our whole HTML document and inside of it we have our **head** and our **body**. Our **head** is for "logistics", like the title of our page and linking in other files.

The **body** is for the actual content of our page. Go ahead and add the following code inside of the **body**:

```html
<h1>Hello World!</h1>
```

Lastly, open your HTML file in Google Chrome. You can

- Drag the icon from VS Code (side panel) to the top of your browser tabs(if you're using a Mac)
- Open Google Chrome and type **ctrl + O** if you're on a Windows and **command + O** if you're on Mac, then find your html file.
- Double click your HTML file from within the `project` folder
- Type `start chrome index.html` in your command line, if you're in the `project` directory
- Install this VSC (Visual Studio Code) [extension](https://marketplace.visualstudio.com/items?itemName=techer.open-in-browser)

If you like shortcuts then maybe try [this guide](http://michaelcrump.net/getting-sublime-3-to-launch-your-html-page-in-a-browser-with-a-key-combo/).