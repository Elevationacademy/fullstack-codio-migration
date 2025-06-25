
#### **GOOGLE FONTS**

  

There is also the question of what font to use. Please forget the days of _Times New Roman_ or, nature-forbid, _Comic Sans_ - in modern times we use modern fonts that are more fitting for the web.

  

Using [Google Fonts](https://fonts.google.com/?sort=popularity&subset=latin), find something that fits the style of your site. If it's something serious you might like _Montserrat_, if it's a little more whimsical, then _Indie Flower_ might be more fitting.

  

These fonts are not built-in to CSS, so again we have to **import** them by adding a link to the `head` of our root HTML, like so:


```html
<link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
```
  

And then normal CSS, like so:

  
```css
font-family: 'Montserrat', sans-serif;
```
  

Note that you can copy both of the above directly from the Google Fonts website.
