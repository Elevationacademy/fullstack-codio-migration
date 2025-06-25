Nothing too impressive for now, but let's add some color in here. For this we of course need the help of CSS. The first thing we need to do is make our HTML file aware of our CSS file. To do this, we will add the following HTML inside of the **head** tag:

```html
<head>
  ﻿<link rel="stylesheet" type="text/css" href="style.css">
  ﻿<title></title>
</head>
```

We've added a `link` tag with three **attributes**: `rel` (relationship), `type` and `href`(hypertext reference). When linking CSS files to our HTML file, the attribute values for `rel` and `type` are always the same, but the value of `href` will always be the filepath from our HTML file to our CSS file.

Since both **index.html** and **style.css** are in the same folder, we can just write **style.css**.

Now add the following CSS inside of **style.css**:

```css
h1 {
  color: red;
}
```

Now, our H1 is red!

![Hello World!](./8.png)