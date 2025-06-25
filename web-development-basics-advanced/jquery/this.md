
The use of this in jQuery is similar to what we learned in Vanilla JS. It's still the object that called the function. So in the following code, what do you expect this to be?

  
```
$("#b1").hover(function () {
    console.log($(this))
})
```
  

The function is hover, the object that called the function is $("#b1") - so this is the element with an ID of b1!

  

The only (minor) difference is that we want to wrap this with a $ so that we can execute jQuery methods with it.

  

There's really not much more to be said. It works as expected =]