# Spot Check

## Exercise 1 

Use the HTML below to complete the following exercises. Try not to check the solution until you've tried to solve it. Use either your text editor or [codepen](http://codepen.io/pen/) to solve these.
    
  
<sup> Note, if you do use codepen, only grab the HTML **within** the `body` tag - codepen sets everything else up for you.</sup>
    

```html
    <!DOCTYPE html>
    <html>
    <head>
      ﻿<link rel="stylesheet" type="text/css" href="style.css">
      ﻿<title>Secret Tel Aviv</title>
    ﻿</head>
    <body>
   <nav>
       ﻿<ul>
          ﻿<li>
            ﻿<a href="#food">Food</a>
          ﻿</li>
          ﻿<li>
            ﻿<a href="#night-life">Night Life</a>
          ﻿</li>
          ﻿<li>
            ﻿<a href="#jobs">Jobs</a>
          ﻿</li>
          ﻿<li>
            ﻿<a href="#apartments">Apartments</a>
          ﻿</li>
        ﻿</ul>
      ﻿</nav>
                
      <section class="hero">
        ﻿<img class="hero-image" src="https://images.squarespace-cdn.com/content/v1/6282ec55d5f3c229291fcb47/1674437725718-PQYL45LC1J5G7XX6ZAIM/image-asset.png"></section>
     ﻿</body>
    </html>
 ```  
      
    
Give the body element a background color of #ddd.
        
<details><summary>  
Click here to reveal the answer.  
</summary>

```css
body { 
  background-color: #ddd; 
}
```
</details>

## Exercise 2

Give the nav element a background color of rgb(51, 51, 51).
    
<details><summary>  
Click here to reveal the answer.  
</summary>

```css
nav { 
  background-color: rgb (51, 51, 51); 
}
```
</details>

## Exercise 3
    
Give the "hero-image" element a width of 100%.

<details><summary>  
Click here to reveal the answer.  
</summary>

```css
.hero-image { 
  width: 100%;
}
```
</details>

 ## Exercise 4

    
Using a pseudo selector to make the first "li" background green.
    
<details><summary>  
Click here to reveal the answer.  
</summary>

```css
li:first-child {
  color: green;
}
```
</details>
