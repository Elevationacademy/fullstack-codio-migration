Like any good technology, CSS has evolved over time. Things that used to be painful are now simpler. You may have already run across some CSS3 features without noticing - after all, all major browser can interpret CSS3 natively, but in this lesson we'll look at a couple of especially useful features. Specifically, we will cover:

-   Variables
-   Animations

  

You read right. _Variables_, in CSS!

  

----------

  

#### **VARIABLES**

  

Often times we find ourselves repeating CSS properties over an over - especially when it comes to things like colors.

  

Because we practice good visual design principles, we recognize that **in general, there should be no more than 4 colors on a page** - then our code may end up looking like this:

```
.results{
    padding: 1vmax;
    color: #ecf0f1;
}

input{
    color: #ecf0f1;
    border-bottom: 0.5px solid #ecf0f1;
    font-size: 1em;
}

::placeholder { 
    color: #ecf0f1;
}

.fa-search{
    color: #ecf0f1;
    padding-left: 5vmax;
}
```
  

Notice how many times we're **r**epeating the color `#ecf0f1`? That is not DRY at all.

  

If we wanted to change that to a different color, we'd have search-and-replace in all our files. Not fun.

  

**CSS3 allows us to define variables**, and use them in other elements like so:

```
:root {
    --primary-color: #ecf0f1;
}

.results {
    padding: 1vmax;
    color: var(--primary-color);
}

input {
    color: var(--primary-color);
    border-bottom: 0.5px solid var(--primary-color);
    font-size: 1em;
}

::placeholder {
    color: var(--primary-color);
}

.fa-search {
    color: var(--primary-color);
    padding-left: 5vmax;
}
```
  

We've done three things here:

1.  Targeted the `root` element - this will give all elements access to the variable
2.  Defined the `--primary-color` variable, and given it the value of `#ecf0f1`
3.  Accessed the variable everywhere that's relevant using the `var` keyword

  

Note that we do **not** have to define all variables in the `root` - we can define under any selector that makes sense; the CSS hierarchy will work the same.

  

However, we **do have to** prefix our CSS variables with the double dash `--` - otherwise the browser will think `primary-color` is a CSS property (which it is not, it is our own custom property.)

  

Finally, the **convention** for CSS variable names is two-fold:

1.  We use skewer-case (separated-by-dashes), as is common in CSS
2.  We name the variable something **representational**, as opposed to something like `--pretty-white`

  

The reason we usually don't want to name our variable `--pretty-white` is because we might change our entire color-palette one day, and then the "white" won't be relevant anymore - but we will always have a primary color.