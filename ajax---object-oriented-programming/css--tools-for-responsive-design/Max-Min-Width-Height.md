With all the dynamic content on our page, we sometimes need to set some limits. For instance, we might want to allow users to post some feedback on our page.

  

However, we cannot predict how much text the user will write. It can vary from something as short as "awesome", to a long rant about how their grandmother could do it better.

  

As such, we can give our elements the CSS properties of `max-width`, `max-height`, `min-width`, `min-height` - these will give upper/lower bounds to how wide/tall our elements should be.

  

Say we had the following HTML and CSS:

  
```html
<div class="feedback"><p class="text">Awesome</p><p class="text">When my grandmother was in Vietnam she made the same product while under fire, walking uphill both ways, and it was *still* better than this piece of garbage.</p>
</div>
```
  

```css
.text{
  background-color: #f39c12;
}
```
  

Check this codepen to see that result is a bit of a [mess](https://codepen.io/ElevationPen/pen/EzrMpO?editors=1100):

  

Instead, we could give our `.text` class a minimum height and maximum width, like so:

  
```css
.text{
  background-color: #f39c12;
  max-width:500px;
  min-height: 50px;
}
```
  

Which gives us a [nicer, more consistent result](https://codepen.io/ElevationPen/pen/MdLxzG?editors=1100):

###### ***Note that you should be viewing this on a large screen, ironically, to get the full experience**

  

Now we can guarantee that all of our feedback will be at least a certain height, and at most a certain width.
