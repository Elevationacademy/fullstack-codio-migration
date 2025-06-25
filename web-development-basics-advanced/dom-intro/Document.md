
### Document

Fork [this repo](https://github.com/Elevationacademy/basic-dom) (make sure not to clone it in a folder that contains a git already - don't clone it in the week-1 folder) and take a look at `index.html`. Make sure the divs make sense to you.

  

We're going to use this code on-and-off throughout the lesson. It's a small game that allows you to move the green ball around using the arrows (of course, it doesn't work now - you'll make it work by the end of the lesson!)

  

Now open up the HTML in the browser, and look at your console - we've console logged `document` in our `main.js` file.

  

If you click on the object (in the console) and start opening up more layers, you'll notice exactly what we said earlier - that **`document`** **is an object representation of our HTML** - everything the user sees on the page, we can access through this object.

  

To show you what that means, go ahead and enter this line _in the console_:

  
```js
document.getElementById("playing-field").style.backgroundColor = "blue"
```
  

And snap. JS has modified our page. Just like that.

You can probably figure out what the above code does by yourself, but we'll explain more in a bit. We need to keep talking about `document` and the DOM first.

  

----------

  

In our first HTML lesson, we talked about how everything in HTML is a **node**.

More generally, we can say that **our entire HTML document is a tree of nodes**.

  

We say it's a tree because effectively, we can think of our HTML (in the project you cloned) like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/HTML+Tree.PNG)

  

In the image, each **node** represents part of the HTML, with the `document` representing the **root node**, i.e the beginning of the tree (it's an upside-down tree with branches going outwards)

  

We can say things like the `down` node is a child of the `arrows` node, or the `container` node is a parent to both `playing-field` and `arrows` - remember, this is just a different representation of our normal HTML.

  

Great - now we understand what we're dealing with. An object that represents HTML nodes.
