
A **unit test** is the smallest form of tests we can write. It **tests a single unit/component in a piece of software** - this can be as small as a single function or class method.

  

To practice unit testing, we're going to use [Jest](https://jestjs.io/docs/en/getting-started.html). This **testing framework** has a convenient NPM package, so we're going to focus our efforts on testing in node for now.

  

**Challenge:** if you would like a nice challenge, go ahead and [read the docs](https://jestjs.io/docs/en/getting-started.html) on your own, then skip to the bottom of this lesson for the exercises.

  

----------

  

To get started, open up a new directory called `jesting-around`, and inside of it create two files: `code.js` and `code.test.js`

  

Next, `npm init` and `npm install --save-dev jest` - the `--save-dev` will indicate that this is only for development, and not production - you'll see this in your `package.json` file.

  

Finally, change your `package.json`'s script field to look like this:

  
```
"scripts": {
  "test": "jest"
}
```
  

And that's it, we're set up.

  

Generally, we write our code in `someFile.js`, and then write the _tests_ for that code in `someFile.test.js` - **these names must match**, or Jest won't be able to run the tests.