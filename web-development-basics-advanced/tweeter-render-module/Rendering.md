<br>

We want our **Tweeter** to be built in a **modular way**, Which means we want a **module** that **receives** the **posts array** and simply renders it.
<span style="color:red">**You must only pass an array of posts!**</span>


This **module** shouldn't care about anything else. It doesn't care if we add or remove posts, comments, whatever.

In other words, this module is the **View** in our M**V**C architecture.


---
<br>
To that end, go ahead and **create another file,** **render.js** - add this to your **tweeter** folder as well, Inside of it you should **create a module called** **Renderer** (Render**er**)

  

The only function this module should **expose (return)** is a **renderPosts** function. Here are some guidelines, though again you're mostly on your own:

  

-   The renderPosts function should receive one parameter: posts
-   This parameter is the array of post objects that comes from your Tweetermodule (the one you created in tweeter logic)
-   The function should first empty the #posts element
-   It should loop through each post in the posts array and append some HTML to #posts
-   Use jQuery to create and add the elements
-   Functions are your friends
-   Notice that each post has its own text, as well as the text of its comments
-   You need to generate the HTML for both
-   **Make sure you're adding each post and comment's ID in a data-id attribute**
-   Use the CSS below for styling - you should be able to figure out which elements receive which class
-   We highly encourage you to use [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals)

  

Check your work throughout, of course, but you can use the following to test that your rendering is working in the browser when you open your index.html

---

**Create a** **main.js** **file** (again, add to your **tweeter** folder) and add this code in it:
```
const tweeter = Tweeter()
const renderer = Renderer()

renderer.renderPosts(tweeter.getPosts())
```
  

Do you understand this beautiful work of modules? Our Tweeter module gives us the data, and the Renderer renders it.

Our main.js is the glue that brings the logic and the visuals together, leaving our concerns nicely separated.

We'll add more to this file later, but for now this is enough.

  

----------

<details>
<summary>You can use this CSS for Styling if you do not wish to make your own 😊</summary>

```CSS
body{
    background-color: #ecf0f1;
    font-family: 'Balthazar', serif;
}

#container{
    display: grid;
    grid-gap: 20px;
    padding-left: 25px;
    padding-right: 25px;
    grid-template-columns: 3fr 1fr;
    grid-template-areas: 
    "h .""i b""p p"
}

#header{
    grid-area: h;
    color: #3498db;
}

#input{
    grid-area: i;
    padding: 10px;
    font-size: 1.5vw;
}

#posts{
    grid-area: p;
}

#post{
    grid-area: b;
    padding: 10px;
    background-color: #3498db;
    border: 1px solid #2980b9;
    box-shadow: 1px 1px 5px #2c3e50;
    cursor: pointer;
    display: flex;
    justify-content: center;
    font-size: 2.5vw;
}

.post{
    box-shadow: 1px 1px 3px;
    margin: 10px;
    border-radius: 5px;
    padding: 10px;
}

#post:active{
    background-color: #2980b9
}

.post-text{
    font-weight: bold;
}

.comments{
    margin-left: 10px;
    margin: 10px;
}

.delete{
    cursor: pointer;
    color: #ecf0f1;
    background-color: #e74c3c;
    display: inline-block;
    padding: 5px;
    border-radius: 3px;
    font-size: 0.8em;
}

.delete-comment{
    cursor: pointer;
    color: #e74c3c;
}
```

</details>



----------

# Summary
  
in summary you need to create the renderer module.
the module receives posts and renderers to the HTML the posts

---

# **BEAUTIFUL**

The renderer lives, and we won't have to worry about rendering anymore! Now any change that happens (adding posts, adding comments, etc) will only happen in the Tweeter module, and then we'll just re-render using Renderer!

  

To get all the dynamic stuff to work, though, we'll need to learn a bit more jQuery...