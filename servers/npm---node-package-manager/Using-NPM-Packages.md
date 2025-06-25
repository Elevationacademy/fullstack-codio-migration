
We've finished our install, and now want to start formatting some dates.

  

Go into your time.js file and add this line of code:
```
let timeNow = new Date()
console.log(timeNow)
```
  

If you run the above (directly in VS Code or through the command line), you'll see this output:
```
2017-01-03T12:31:43.981Z
```
  

Which is great if you're a machine, but we're humans damn it.

  

We can format it with built-in JS functions, as offered [here](https://stackoverflow.com/a/3552493/3147774) - but that tends to be a hassle, and somebody spent some good time building Moment.js for us.

  

In order to use this package, we must first import it, like so:
```
const moment = require('moment')
```
  

You'll notice that **when we require external packages, there is no need to preface with a path**. In other words, **if you require a package just with a name, node will assume it's in the** **node_modules** **directory and try to read it from there**.

  

Now we have access to the moment object, and can use it like so:
```
let formattedTimeNow = moment().format("MMMM Do, YYYY")
console.log(formattedTimeNow) //January 3rd, 2017
```
  

And that really is just lovely.

  

----------

  

#### **MORE ON package.json, node_modules**

  

The more you code, the more you'll realize how useful NPM packages are. And there are [so](https://www.npmjs.com/package/pokemon), [so many](https://www.npmjs.com/package/text-cleaner%22), even some [unexpectedly specific](https://www.npmjs.com/package/fitsjs) or [random](https://www.npmjs.com/package/philosophers-names) ones.

  

And the more you use these packages (and you will), the bigger your node_modules directory will get.

  

Of course, we're responsible developers and we push everything to Github... but we don't want to pollute our Github with a ton of code that's already stored somewhere else, and is not even our actual code.

  

To deal with this, **whenever you're using NPM packages** (basically always from now on), **make sure you create a** **.gitignore** **file in the same directory where your** **node_modules** **folder is**.

  

Then write node_modules in the .gitignore file - this will make sure that when you commit, git will simply ignore the entire node_modules directory.

  

All in all, your setup should look something like this now:

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/npm-setup-w-gitignore.PNG)

###### You don't have to worry about the package-lock.json file for now

  

----------

  

But now we're in a pickle: if we don't push our node_modules, other developers that want to work on our code are going to have to install everything all over again - and that can be a lot when you're using dozens of external packages.

  

To see what the solution to this is, go ahead and **delete your** **node_modules****folder** right now. When people initially clone a project from Github, it usualy looks like this: lots of code, no node_modules directory.

  

If you try to run your code now (node time.js in the terminal), you'll see an error:
```
Error: Cannot find module 'moment'
```

Which should make sense, because your code is trying to read the momentmodule from your node_modules which doesn't exist. But instead of doing npm install moment, now you can run this command instead:

  
```
npm install
```
  

Simply put, **running** **npm install** **will go to your** **package.json****, read the** **dependencies** **object, and install all the packages from there** - and that's how we share projects among developers. That is to say, if you're cloning an existing project that already has a package.json with all the dependencies - it is enough for you to execute this command to get going.

  

The command will re-create your node_modules folder if it doesn't exist.