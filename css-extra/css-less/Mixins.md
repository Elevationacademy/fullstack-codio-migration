
Using the same `.box` styling from above, we can use **mixins** to take advantage of **parameters** with some "base" CSS.

  

Say we wanted many elements to have the `.box` styling, but instead of all of them being 100 by 100 `px`, we wanted that to be dynamic. With **mixins**, this is trivial:

  
```
.box(@w, @h) {
    width: @w;
    height: @h;
    background-color: #9b59b6;
    box-shadow: 1px 1px 3px #2c3e50;
    border-radius: 4px;
}

.other-container {
    .box(50px, 50px);
    margin-top: 1vmax;
}
```
  

Note what the **compiled CSS** (in the auto-generated `.css` file) looks like:


```
.other-container {
  width: 50px;
  height: 50px;
  background-color: #9b59b6;
  box-shadow: 1px 1px 3px #2c3e50;
  border-radius: 4px;
  margin-top: 1vmax;
}
```
  

There is **no mention of the** **`.box`** **selector** - that is because with **mixins**, we are effectively defining "CSS functions" to be invoked elsewhere in our stylesheet. And of course, functions by themselves are meaningless - it's their invocation that matters.

  
## Spot check
What is the difference between &extend: and **mixins**?
<details><summary>
  Click here to reveal the answer.
</summary>
We use extensions to define some "base" and add on to it. One the other hand, mixins allow us to define dynamic styling based on a template we've defined.
</details>


  

