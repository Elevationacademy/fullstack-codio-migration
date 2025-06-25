At the bottom of the CSS, add a media query that changes the `width` property of any element with a class `column` to `100%` as soon as the width of the page is fewer than `700px`.
    
      
    
If you've done it right, you'll see the page turn to a single-column display when you shrink it.
    
      
    
Check out [this solution](https://codepen.io/ElevationPen/pen/KLJLGV?editors=0100) to compare.
    
      
    
Of course, you can have **multiple** media queries for multiple sizes, and you can have multiple changes per media query.
    
      
    
Some developers opt to have a whole separate file to handle their smaller-device CSS. Certainly not a bad practice!
