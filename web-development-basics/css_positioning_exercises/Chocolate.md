# Chocolate

Create this partly eaten chocolate bar using [`float`](https://www.w3schools.com/css/css_float.asp) [and](https://www.w3schools.com/css/css_float.asp) [`clear`](https://www.w3schools.com/css/css_float.asp) for the positioning. Yes, this is a bonus challenge. We don't really like to use floats anymore. But it's good practice. You can also do this without floats, of course =]

  


![.guides/img/chocolate-float-ex](.\img\chocolate-float-ex.PNG)
  

We used `#66320E` for the dark brown of each piece,

`darkred` for the strip in the middle,

`black` for the background color.

  

The only other hint is to use `display: inline-block` in the parent - but you may be able to do this without that.
    

<details><summary>  
Click here to reveal the answer.  
</summary>

HTML (inside the `<body>` tag):

```html
<div id="chocolate"><div class="block" id="block-1"></div><div class="block" id="block-2"></div><div class="block" id="block-3"></div><div class="block" id="block-4"></div><div id="middle"></div><div class="block" id="block-5"></div><div class="block" id="block-6"></div><div class="block" id="block-7"></div>
</div>
```
  

CSS:

  
```css
#chocolate {
  background-color: black;
  display: inline-block;
  padding: 4px;
}
#middle {
  background-color: darkred;
  height: 5px;
  width: 385px;
  margin-top: 6px;
  margin-bottom: 4px;
}
.block {
  background-color: #66320E;
  width: 90px;
  height: 90px;
  margin: 3px;
}
#block-1 {
  float: right;
}
#block-2 {
  float: right;
}
#block-3 {
  float: right;
}
#block-5 {
  float: left;
}
#block-6 {
  float: left;
}
#block-7 {
  float: left;
}
```
</details>
