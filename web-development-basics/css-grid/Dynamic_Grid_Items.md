# Dynamic Grid Items

So far we've dealt with CSS Grid in a fairly static way. An entire page's layout, a single navbar that doesn't change.

  

But a lot of our content will be dynamic, and so we need to learn how to dynamically add CSS Grid-styled elements.

  

For instance, say we wanted to create a simple search-and-display part of our webapp, that looks something like this:

  
![search-results-css-grid-example](.\img\search-results-css-grid-example.PNG)



Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/search-results-css-grid-example.PNG) to embiggen.

  

The amount of display items is **dynamic** - so we can't know ahead of time how many rows we want.

  

That said, we can make a decision that we don't want to display more than 3 items per row. In other words, we only want three _columns_.

  

Again, the first part of any work with CSS Grid is the HTML. Here is one way to do this:
```html
<body>
    <div id="search-container">
        <input type="text" placeholder="What are you looking for?">
        <div class="search-btn">Search</div>
    </div>
    <div id="results-container">
        <div class="result">First thing</div>
        <div class="result">Second thing</div>
        <div class="result">Third thing</div>
        <div class="result">Fourth thing</div>
    </div>
</body>
```
  

Notice that in this case we're going to have **two, separate main grid containers** - one of the search area, one for the results. This is _totally fine_.

To be clear, we will **not** give the `body` element a `display: grid`, even though it is wrapping all of our elements.

  

You can figure out the `#search-container` `div` on your own, but let's talk about the `#results-container`:

  

```css
#results-container{
    display: grid;
    grid-gap: 10px;
    grid-template-columns: repeat(3, 1fr);
}
```
  

That is it. Nothing special. We're stating that we want to limit our columns to having 3 items, with a gap of `10px` between each column.

  

Now, no matter how many children we have inside of `results-container`, they will take up only 1/3 of the available space, until they can't fit on the same row, then go down to the next one. Excellent.

  

**Try out the code up to this point** for yourself to see that in action.

  

As for the `.result` elements themselves, once again we're going to use `grid` for nothing more than stylistic flairs, not actual layout:

```css
.result{
    display: grid;
    height: 100px;
    background-color: #16a085;
    text-align: center;
    align-content: center;
    border-radius: 4px;
}
```