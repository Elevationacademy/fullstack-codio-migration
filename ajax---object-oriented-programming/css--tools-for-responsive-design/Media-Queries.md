Now for the coup-de-grace of responsive design: **media queries**.

  

Media queries allow us to load _different_ CSS styling, depending some condition.

Let's take a look at an example:

  
```html
<div class="signup"><input type="text" placeholder="Name"><button>Submit</button>
</div>
```
  

Since both `input`s and `button`s are inline-elements by default, the above will appear side-by-side.

  

On large screens, this should not be a problem. But if we want this to be split (i.e one line after the other) for smaller screens, we need to introduce some logic.

  

A popular rule of thumb is that "small" screens start at a width of `768px`. To add some CSS that is _only_ applied once is the screen becomes `768px` or fewer wide, we would do this:


```css
@media(max-width: 768px){
  input{
    display: block;
  }
}
```
  

The above CSS states the following: once the viewport is `768px` or fewer, the following CSS styling will be applied.

  

Try this out for yourself on [codepen](https://codepen.io/pen/) and see for yourself.

  

  

----------

  

  

Next, check out [this example](https://codepen.io/ElevationPen/pen/LBYRjp) for a more common use case of media queries.

  

You'll note that when you shrink the page too much, the pictures become small and a little out-of-whack.
