# Selectors

With CSS, we "select" certain HTML elements and give them "style" (color, size, position, etc.). Let's review a few ways we can select elements with CSS.

----------
**Element Selectors**

One way to select an HTML element in CSS is by using the element's tag name. For instance, we can style a `div` element like we did earlier, like this:
```css
    div {
      width: 50%;
    }
```
Note that this kind of selection is _very general_ - this will style **all** the divs in our HTML.

The same is true for an `h1` element like this:
```css
    h1 {
      font-family: "Helvetica";
    }
```
Or even a `ul` element, along with any of its children li elements, in this way:
```css
    ul {
      color: red;
    }
```
This works as the `li` elements are children of the `ul`. This is because in CSS a child element inherits some (but not all) of the CSS properties belonging to its parent.

**Class Selectors**

Another way to select an HTML element in CSS is by using the name of an element's "class attribute". For instance, if we had a `div` with the class `nav-bar` like so...

```html
    <div class="nav-bar"></div>
```
...we could style it in CSS this way ( notice how we use a `.` before the class name ):
```css
    .nav-bar {
       position: fixed;
    }
```
_Reminder_ — you can add any class, or classes, to any HTML element, or elements — and you can name those classes any name that you would like ( nav-bar, cat, dog, etc. ). Try to find meaningful names - that will make your code more readable, and it is a good practice!

Here is an example:

 
```html
    <h1 class="heading tomato">Caution!</h1>
        <h3 class="tomato">Never eat these things!</h3>
      
        <ul class="gross-color">
          ﻿<li>pickled pigs feet</li>
          ﻿<li>rotten cheese</li>
          ﻿<li>fried field mouse</li>
        </ul>
              
        <hr/>
              
        <h1 class="heading tomato">Notice!</h1>
              
        <h3 class="tomato">Always eat these things!</h3>
              
        <ul class="nice-color">
          ﻿<li>pickled pigs feet</li>
          ﻿<li>rotten cheese</li>
          ﻿<li>fried field mouse</li>
        </ul>
```
The CSS might look like this:
````css
    .heading {
      font-weight: bold;
      vertical-align: middle;
    }
    
    .tomato {
      color: tomato;
    }
    
    .gross-color {
      color: #a3c010;
    }
    
    .nice-color {
      color: #03bbbb;
    }
````


**ID Selectors**

Another way to select an HTML element in CSS is by using the name of an element's "id attribute". For instance, if we had a `div` with the id `about-me` like so...
```html
    <div id="about-me">I'm really cool.</div>
```
...we could style it in CSS this way ( notice how we use a `#` before the id name ):
```css
    #about-me {
      font-family: sans-serif;
    }
```
_Reminder_ — the big difference between IDs and classes is that **there can only be _one_** **`id`** **per element, and there can only be _one_ occurrence of a specific** **`id`** **per HTML page**

###### Most browsers will allow the same id to effect multiple HTML elements, but this is bad and will mess with us when we get into JavaScript

**Pseudo Selectors**

To give an HTML element a _special state_, we can use pseudo-class selectors in our CSS. For instance, we might want to style an element when a user mouses over ( or hovers over ) it:
```css
    button:hover {
      background-color: blue;
      color: black;
      border: 1px solid black;
    }  
```
Or we might use a pseudo-class to style a specific child element:
```css
    p:nth-child(2) {
      background: red;
    }
```
The above CSS will find any `p` element that is the _second_ child (of anything), and color it red. For instance:
```html
    <div>
      ﻿<p>1</p>
      ﻿<p>2</p>
    ﻿</div>
        
    <ul>
      ﻿<li>Dummy1</li>
      ﻿<li>
        ﻿<p>Some text</p>
        ﻿<p>Red text</p>
      ﻿</li>
      ﻿<li>Dummy3</li>
    ﻿﻿</ul>
```
The number 2 in the above **and** "Red text" would be colored red because they are both the second occurrence of a `p` tag. The first within the `div`, and the second within the `li`.

Check out this example of using [pseudo selectors.](http://codepen.io/amhayslip/pen/OMOzyg) And maybe bookmark this [complete list](https://developer.mozilla.org/en-US/docs/Learn/CSS/Introduction_to_CSS/Pseudo-classes_and_pseudo-elements)

**Combining Selectors**

You can combine CSS selectors to get more granular results. For example:
```css
    /* All p elements that are direct descendants of a div are given green text */
    
        div > p  {
          color: green;
        }
```
This example says that any `p` that is **directly nested** inside of a `div` will get the color green, for instance:
```html
    <div>
      ﻿<p>Some text</p>
      ﻿<p>Also direct</p>
      ﻿<span>
        ﻿<p>More text (no color here)</p>
      ﻿</span>
      ﻿<p>Yup, I'm green too</p>
    ﻿</div>
```
The `p` elements with "Some text", "Also direct", and "Yup, I'm green too" _will_ become green - because they are all **one level deep, i.e. direct children** of the `div`.

However the `p` with "More text (no color here)" will _not_ get the green color because it is nested inside a `span`, hence it is not a direct child of a `div`.
```css
    /* All p elements that within a div are given blue text */
    div p {
      color: blue;
    }
```
Here, _any_ descendant of `div` that is a `p` will receive the color blue.

Test it out yourself ;)
