
Given this HTML:
```
<div class=feedme>Feed me more</div>
```
  

Complete the JS below to recreate the following (see below):

  

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A2541-0.gif)

  

Starter JS:
```
$(".feedme").on("click", function(){
  let divCopy = //use template literals and $(this)
  
  $("body").append(divCopy)
})
```
  

This one is a little tricky - but think first. You need to access the clicked element's text.. and you need to insert that text into another div - you should do both of these in one line.

  

Check your work with [this solution](https://codepen.io/ElevationPen/pen/GaLeQa?editors=1010) on codepen.