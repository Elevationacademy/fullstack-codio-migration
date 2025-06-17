# Intro

CSS can be... a lot. The absolutes, positions, margins - sometimes one attribute messes with another and it's unclear how instead of a few boxes side by side you got this:

  

![.guides/img/badCss](.\img\badCss.PNG)



  

Though, to be honest, if you're able to replicate that - well done.

  

Anyway, sometimes we want to layout our page a certain way without worrying too much about the small details of CSS. Everything from the basic CSS lesson is **still important** and you definitely **will use it more** - but for a more intuitive approach to the layout of our web apps, we want someone else to take care of the heavy lifting.

  

And so we have [CSS Grid](https://cssgrid.io/).

  

----------

  

#### **A GRID**

  

A grid layout is just what you imagine - some columns and rows, with our elements aligned neatly around the page.



![.guides/img/1](.\img\1.png)


Can you think of how you would design something like the above image with just plain CSS? And how would the HTML look? This is one (not very fun) option:

NOTE: if you copying thous line by clicking the "copy" button, it might not work... To fixed that, just select the code and copy/paste it

  
```html
<div class="container"><div class="head"></div><div class="side-nav"></div><div class="main"><div class="inner-content"><div class="content-title"></div><div class="content-image"></div><div class="content-text"></div></div> 
   </div><div class="foot"></div>
</div>
```

```css
.container{
  padding: 10px;
  position: relative;
}

.head{
  height: 70px;
  width: 90%;
  right: 0;
  position: absolute;
  background-color: #a29bfe;
  display:inline-block;

}

.side-nav{
  height: 500px;;
  width: 10%;
  background-color: #6c5ce7;
  display: inline-block;
}

.main{
  position: absolute;
  display: inline-block;
  width: 100%;
}

.inner-content{
  position: absolute;
  top: 70px;
  height: 430px;
  width: 90%;
  background-color:red;
}
```
  

...point is, it becomes pretty involved - and that is a pretty _basic_ layout. What if we wanted something even more complex? _And_ a lot of the values there are **hard-coded**.

  

With CSS Grid, we can simplify this a _whole_ lot. Let's dive right in and see what this is all about.
