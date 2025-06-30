# Grids Everywhere

So far our grids have taken up the whole page - but that is definitely not necessary. We can use grid to layout an entire page, or even just a navbar. Let's see how we would re-create the following using CSS Grid:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/grid-nav-bar.PNG)

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/grid-nav-bar.PNG) to embiggen.

  

The first step to using CSS Grid is determining what our containers and items are. In other words, how will our HTML look like?

  

Of course, as is often the case with CSS and programming in general, there are several ways to break this down, but let's look at this for now:

  

```html
<body>
    <div id="nav-container">
        <div class="main-items">
            <div class="nav-item">Home</div>
            <div class="nav-item">About</div>
            <div class="nav-item">Cart</div>
        </div>
        <div class="nav-item logo-container">
            <p>The Company</p>
            <p>We do it best.</p>
        </div>
    </div>
</body>﻿
```
  

Clearly, we have our main container: `nav-container` which will house our entire navbar. So far so good.

  

Next we have two **nested** containers, the `.main-items` and `.logo-container` `div`s. We do this because there are effectively two sections in our navbar:

1.  The main links to navigate our web-app
2.  The company logo/name/tagline area

  

The first section we want to further split into three sub-sections (one for each link), and the second section we want to throw all the way to the right.

  

Within each sub-section, we have the actual content.

Now, before we look at the CSS, let's make something very clear:

  

-   The two sub-sections, `.main-items` and `.logo-container` are **grid items of the** **`#nav-container`** **container**
-   The _Home_, _About_, and _Cart_ divs are **grid items of the** **`main-items`** **container**
-   The two p elements are **grid items of the** **`.logo-container`** **container**

  

Remember, in CSS Grid we have a **grid container** and its **grid items** - and as you can see above, we can certainly **nest** them.

  

  

----------

  

  

Ok, let's look at the CSS from the top going down:

  

```css
#nav-container{
    display: grid;
    background-color: #2c3e50;
    grid-template-columns: repeat(2, 1fr);
    padding-right: 15px;
    padding-left: 15px;
}
```
  

This is our main grid container. It holds the two main sub-sections we discussed before, and it evenly splits them using the template-columns property.

  

This will physically split the two main sub-sections into `[main........................logo]` on our navbar.

  

Notice that

-   We didn't have to define a `template-rows` property, because we only have one row
-   We add a bit of padding only for stylistic effect
-   This is a grid container, so of course it needs the `display: grid` property
-   We **don't** define a height, because we want the content within the navbar to determine that

  

Go ahead and run this code to see the current result.

  

Now let's see our `.main-items` sub-section:

  

```css
.main-items{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
}
```
  

Again, this is its own grid-container, hence the `display: grid`, and here we repeat the columns 3 times, because we have three links.

  

This part is what splits our first sub-section into `[link1.......link2......link3]` - this single-subsection is entirely oblivious to the rest of the world.

  

As for our actual `.nav-item` elements, here is their CSS:

  

```css
.nav-item{
    display: grid;
    align-content: center;
    color: #ecf0f1;
    height: 100%;
}
```
  

In this case, we're using `display: grid` so that we can take advantage of the `align-content` property.

  

We'll talk about `align-content` and `justify-content` in a second, but for now it's enough to understand that it is a simple way to help us center things within a `grid`

  

As for the `height: 100%` - this is to ensure that when we change the background color ( as we do on `:hover` ), it will color the entire section and not just the text.

  

Notice that this code is **only for stylistic effect** - it does not affect the actual layout of our navbar. Try removing this code and look at the result: same layout, just without the styling.

  

Finally, let's look at our `.logo-container` CSS:
  

```css
.logo-container{
    display: grid;
    justify-content: end;
}
```

Once again, we use the `grid` display **purely for stylistics**. In this case, we use it so that we can take advantage of the `justify-content` property which allows us to move things left-right within our elements.



----------

 

Except for some fonts and pointers - that's basically it! This is the power of CSS Grid. Very intuitive, very clean CSS to help us layout our elements.
