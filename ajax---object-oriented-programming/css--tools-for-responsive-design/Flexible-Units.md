So far we've really only dealt with the `px` unit, but of courses there are many others. [This guide](https://thecssworkshop.com/lessons/relative-units) is a good _starting_ point, but let's talk about a couple of popular units.

  

**Percents: %**

  

If we give a `div` a `width` of `500px`, it will always be 500 pixels no matter where it is displayed.

  

If, however, we give it a width of `25%`, it will always be one quarter of **its _parent's_ width**.

  

[Check out the difference.](https://codepen.io/ElevationPen/pen/yWZWPe?editors=1100)

###### ***Note that you should be viewing this on a large screen, ironically, to get the full experience**

  

To see this in action, shrink this window and watch how eventually the `px` `div` overflows, where as the percentage one shrinks accordingly.

  

  

----------

  

  

**vw & vh**

  

We can use the `vw` and `vh` units for font-sizing as well as the size of entire elements (i.e. width, height).

  

The `v` stands for "viewport", and the `w`/`h` is "width" or "height".

  

By definition, **`1vw`** **is 1/100th of the viewport width**, and likewise for `vh` and the viewport height.

  

That means that these grow and shrink relative to the _viewport_. Check out the difference between `px` font-size and `vw` font-size with [this codepen](https://codepen.io/ElevationPen/pen/gNWgvM). *Shrink/grow the page again to see how the vw text shrinks and grows accordingly.

  

**Note**: `vw` is only affected by changes in the page's **width**, and `vh` by changes in the page's height.

  

There is also a `vmin` and `vmax` unit.

The `vmin` will equal `1vw` or `1vh`, whichever is smaller (remember, this is a unit based on the viewport)

And `vmax` will equal `1vw` or `1vh`, whichever is larger.

  

It's best to test these out on your own, but this is a [great resource](http://thenewcode.com/1137/MinMaxing-Understanding-vMin-and-vMax-in-CSS) to dive into it.
