
To start using these packages, we're going to go ahead and create a directory called package-explortation, and add a file there called time.js

  

From your terminal/command line, navigate to package-exploration, and execute the following command:
```
npm init
```
  

You will be prompted to fill several fields in, but you can also skip them all by pressing enter several times.

  

Once you finish (after a final confirmation), you'll see that a file has been created for you: package.json

  

In the beginning, the contents of this file should like something like this:
```
{
  "name": "package-exploration",
  "version": "1.0.0",
  "description": "",
  "main": "time.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}
```
  

For now, the contents of this file are not so interesting. But we'll get back to it in a moment.

  

This file will (soon) hold some info about all the packages we've installed. To see that, let's jump right in and install a package called [Moment.js](https://momentjs.com/) - a handy module for dealing with dates in JavaScript.

  

To install a package, make sure you're in the same package-exploration directory, and run the following command in the terminal:

  
```
npm install moment
```
  

You'll see a loading bar, and eventually you'll see something like this output in your console:
```
+ moment@2.22.2
added 1 package from 6 contributors and audited 1 package in 2.187s
found 0 vulnerabilities
``` 

That's it! We've installed Moment.js - easy as that. Now take a look at your package.json again, and you'll see this bit was added to the file:

  
```
  "dependencies": {
    "moment": "^2.22.2"
  }
```
  

So our package.json keeps track of all the external packages we have in our app - excellent. But wait, there's more!

  

----------

  

Once your moment installation was complete, something else was added - a node_modules directory!

  

If you open that up, you'll see that it has one folder inside of it called moment - and inside _this_ directory is all the code required to use the Moment.js module.

  

The node_modules directory will store _all_ our external packages - this is code we want to use but (typically) not modify. It's there for us to access, so let's get accessing.