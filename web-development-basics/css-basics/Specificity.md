# Specificity

There are several levels of "specificity" in CSS. Specificity is the means by which browsers decide which CSS property values are the most relevant to an element and therefore will be applied. Specificity is based on the matching rules which are composed of CSS selectors of different sorts.

  

Here are the levels of specificity starting at the least specific:

  

**1. Element Selectors (least specific)**

  

If we select an element without being specific to its "class", "id" or other attributes, this is the least specific. This selector will be easily overriden.
```css
    div {
      width: 200px;
      height: 200px;
      background-color: red;
      border: 5px solid magenta;
    }
```
**2. Class and Attribute Selectors**

If we were styling the `div` above, this `class` selector would override its styles because it's more specific.
```css
    .songs-container {
      background-color: green;
      border: 25px solid red;
    }
```
**3. ID Selectors**

If the same `div` had an id, the following would override **both** of the stylings above. This is because id's must be unique and are therefore more specific.
```css
    #rock-songs {
      background-color: orange;
      border: 10px solid blue;
    }

```
**4. Chained selectors**

Note: Combining CSS selectors also affects the specificity of a property. For example, a property with both ID and attribute selectors has more specificity than a property with just an ID selector.
```css
    .panel #rock-songs {
      background-color: gray;
    }
    
    #rock-songs {
      background-color: orange;
      border: 10px solid blue;
   }
```
In this case the background will be gray. The first selector ".panel #rock-songs" contains 2 levels, while the "#rock-songs" contains only 1.

**5. Inline Stlyes**

This is where you use the HTML "style" attribute to add CSS. The following would override the background color for our div example:
```html
    <div style="background-color: pink;" id="rock-songs" class="songs-container">
      
    </div>
  ``` 
Generally, **we avoid writing CSS directly inside the HTML** - but know that it is possible.


**6. Using !important (most specific)**

Using the keyword "!important" in your CSS overrides all styles regardless. This should be used very sparingly if at all. The following would override the background color for our previous styles:
```css
    div {
      width: 200px;
      height: 200px;
      background-color: red !important;
      border: 5px solid magenta;
    }
```
*** Bottom of the File**

  

Lastly, when two conflicting style rules have the same specificity, the one that's defined lower down in your CSS file takes precedent. Take a look at [this example](http://codepen.io/amhayslip/pen/ZWEqrp) here. Notice that the div is blue because that is the style that is defined further down in the file.

This rule also applies across multiple files. If you link several CSS files to your HTML page the `links` further down the page will be more important.

**Example**:

Take a look [here](http://codepen.io/amhayslip/pen/MyWBxX) to see an example in action. Play around with it - for example, remove the `!important`, change the order, just be curious and try things - you're not going to break the internet!

