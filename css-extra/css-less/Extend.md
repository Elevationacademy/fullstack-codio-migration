
Often in CSS we find ourselves repeating similar blocks of styling several times. CSS3 variables won't help us here, because we're talking about something like this:

```
.box{
    width: 100px;
    height: 100px;
    background-color: #9b59b6;
    box-shadow: 1px 1px 3px #2c3e50;
    border-radius: 4px;
}
```


If we wanted other elements to have these properties, we would have to give each of them the `.box` class - this might be problematic and cause conflicts in some cases, and this is where CSS Less' `&:extend` comes in:

  
```
.box {
    width: 100px;
    height: 100px;
    background-color: #9b59b6;
    box-shadow: 1px 1px 3px #2c3e50;
    border-radius: 4px;
}

.other-container {
    &:extend(.box);
    margin-top: 1vmax;
}
```
  

In the above, we're saying that we want elements with the `other-container` class to have _all_ of `.box`'s style, _plus_ a `margin-top` of `1vmax`.

  

Again, if you take a look at the compiled CSS, you'll notice that the above doesn't necessarily save us a lot of code, but it is certainly clearer that `.other-container` will mostly look like `.box` just from looking at the `.less` file.