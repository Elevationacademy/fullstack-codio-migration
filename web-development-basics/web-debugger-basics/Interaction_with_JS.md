# Interaction with JS

We briefly saw in pervious lesson that we can type JavaScript into our DevTools **console** tab. We can also use the console to access the JavaScript written in our files.

Create a boilerplate HTML file with a link to **script.js** at the bottom of the `body`. Create a JS file with that name and in it write the following:

```js
let frontEnd = ['HTML', 'CSS', 'Javascript'];
```
Open your HTML file in Chrome and open the DevTools at the console tab. Type:

```js
frontEnd
```
  

You should see this:

  

![.guides/img/PROD_A1657-0](.\img\PROD_A1657-0.png)

  

Great, we can access our JS file! We can even interact with it. For example, you could add more items to our `frontEnd` array. Try it! 
Just remember that these changes don't change the file itself. You'll find this is a great technique for quickly testing code.

We can go further still and create new variables in our **console** and play around with them. We can also look closer at the objects in our code and see what properties and methods they expose. This may sound like gobbledygook, but in the future you'll love the fact that the DevTools console is kind of like a glorified real-time code editor.
