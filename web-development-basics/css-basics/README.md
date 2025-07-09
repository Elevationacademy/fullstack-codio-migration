# Properties

We use CSS **properties** to define what styling to apply to our elements.

For instance, the following HTML will be "invisible" on our page - that is, we won't see anything:
```html
    <html>
      ﻿<head>...</head>
      ﻿<body>
        ﻿<div></div>
      ﻿</body>
    </html>
```
Try this out for yourself, it's good practice.

But, if we add some CSS to it (again, in our .css file), like this:
```css
    div {
      width: 50px;
      height: 50px;
      background-color: #e74c3c;
    }
```
Then we'll see this box on our page:

![](./img/PROD_A319-0.png)

For the most part, properties are pretty easy to understand from their name - i.e. the width property above gives the div a width of 50px, where px is short for **pixels**, a unit we use when we want to be very precise (there are other units like % or emwe'll learn about later).

The background-color*, as you probably guessed, is what assigns the color, and it can receive several values as well. The above example uses a [hex color](http://www.color-hex.com/) format, but you can use [RGB colors](https://www.w3schools.com/colors/colors_rgb.asp) or some simple text-colors like "red" and "indigo".
###### *Note, there is a different property called color which is for changing the color of _text_ - not the same
[Here is a list](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Properties_Reference) of many CSS properties and how to use them. Note, **you never need to memorize** any of them; you can always search for them.

That said, some good ones to keep in mind for _styling_ (we'll learn about positioning later) are: width, height, background-color, background-image, border, border-radius, box-shadow, font-size, font-family, text-align.

Final note on properties, **each property value* must end with a semi-colon**, or else your CSS will break.
###### *Except the last, but you should put a semicolon there anyway