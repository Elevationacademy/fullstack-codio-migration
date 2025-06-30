# Display Grid

We'll work on the main layout for now (without the inner content stuff), so let's simplify the HTML to this:

  
```html
    <div id="container">
        <div class="head"></div>
        <div class="side-nav"></div>
        <div class="main"></div>
        <div class="foot"></div>
    </div>
```
  

Clean.

  

~ Note that we call the parent `div` the **grid container**, and the children are called **grid items** ~ (but this has **nothing to do** with their `class`/`id`s)

  

Now, we know how we _want_ it to look. In fact, let's make some shortcuts and "sketch" out what we want on a grid:

-   **h**: head
-   **s**: side-nav
-   **m**: main
-   **f**: foot

  


Eventually, we'll want something like this:

  
```css
    h h h h h h
    s s m m m m
    s s m m m m
    s s m m m m
    s s f f f f
```
  

Right? Header on top, side-nav on the side, content in the middle, and footer on the bottom - this grid is our very basic _layout_.

  

You know what's crazy? That matrix up there _is_ one of the fundamental ways we create CSS Grid code. We'll see that in a bit.

  

First up, open up a CSS file (make sure it's linked in your HTML), and write the following:

  
```css
#container{
    height: 100vh;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
    grid-template-rows: 1fr 1fr 1fr 1fr 1fr;
}
```
  

**height**: How high, relative to the view (hence the `vh` we want our entire container to be)

  

**display**: This will tell CSS to use CSS Grid

  

**grid-template-columns**: This determines how many columns we'll have, and how much space they take. We could use `px`, `%`, or other units - but `fr` is nice because it is a _fraction_ unit, and it takes up **one part of the available space** - the available space is the width of the page, because `div`s are block elements.

  

**grid-template-rows** - same concept, but for rows, and this time the available space is the `100vh` we decided earlier.
###### We'll soon see to simplify these `template` properties

  

Since we have repeating columns/rows, CSS Grid allows us to simplify the above to this:

  

```css
#container{
    height: 100vh;
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    grid-template-rows: repeat(5, 1fr);
}
```
  

It works as intuitively as it looks: use the `repeat` keyword to tell it how many/column rows you want and what dimension each should have.

Alone, the above code does nothing. But here's where our matrix comes in. **Add this to the above** **`#container`** **selector**

  

```css
    grid-template-areas: 
    "h h h h h h""s s m m m m""s s m m m m""s s m m m m""s s f f f f";
```
  

Notice that each row in the grid is identified by opening and closing quotes, and each _cell_ is one letter. Also, remember the **semicolon** at the end - CSS Grid is great, but CSS is still strict.

  

Of course, CSS doesn't know that `h` means "header" and `m` means "main", so we need to tell it that. Now we'll connect our HTML using the `grid-area` attribute, as such:

  
```js
.head{
    grid-area: h
}

.side-nav{
    grid-area: s
}

.main{
    grid-area: m
}

.foot{
    grid-area: f
}
```
  

A few notes:

-   These selectors are _outside_ of the `container` selector
-   There are **no** quotes around the letters

This is basically our mapping between our HTML classes and our `grid-template-area`

  

So now if you open up your `index.html` page in the browser you'll see... nothing! Or do you?

  

How about that Chrome Developer Tools? (right-click, Inspect on the page)

  

Not only are our elements _there_, but if you hover over any of them you'll see a grid appear on the page!

  


![.guides/img/gridSansFormattingEx](.\img\gridSansFormattingEx.PNG)

  

What we're seeing in the image is the `h` or `.header`'s layout on the page, and it's exactly the way we laid it out in the matrix.

Bam.

  

To make it clearer, let's add some background color to each of our four elements (head, side, main, foot), and voila:

  

![.guides/img/gridColorEx](.\img\gridColorEx.PNG)


  

By the way, you can add `grid-gap: 10px`; to your `grid-container` to actually space the `div`s out and make it look like an actual webpage. Try it out!

  

Now say you don't like how thick the `side-nav` is. The great thing is, we don't have to guess anything to make it thinner. We can just change the matrix to have one s column instead of two, like so:
```css
    "h h h h h h""s m m m m m""s m m m m m""s m m m m m""s f f f f f";
```
  

And kablam! Check it out on your browser and see for yourself ;)

  

Now create the following layouts by _only_ changing the `grid-template-areas` matrix:

  

![.guides/img/gridColorEx3](.\img\gridColorEx3.PNG)


  

![.guides/img/gridColorEx4](.\img\gridColorEx4.PNG)

  

![.guides/img/gridColorEx5](.\img\gridColorEx5.PNG)


  

This next one has a bit of a twist, here's the trick: you can replace the letters with dots to skip cells. Can you figure it out?

  

![.guides/img/gridColorEx6Dots](.\img\gridColorEx6Dots.PNG)
  

Ok, that was the plain-and-simple CSS Grid intro. Let's get a little fancier now.
