# The Box Model

# The Box Model

We know enough now to talk about the Box Model. To understand this, you must first accept the following boggling statement:

_There is more to an element on the page than the element on the page._

And we can explain that visually. Say we have our good old red box, with a `width` and `height` of 100px. Create such an element.

Now right-click the box and select "Inspect". You should see Chrome's developer tools pop up, and there you'll see the HTML that the browser has available:

![.guides/img/DevTools](.\img\DevTools.PNG)

You should be on the **Elements** tab, and in the smaller window you should be on the **Styles** tab. Scroll down the little window until you see this:


![.guides/img/BoxModelPlain](.\img\BoxModelPlain.PNG)

This is the CSS **box model**. What we're seeing here is how the element looks on the page. Right now it's pretty stark - naturally, because we haven't done much.


Notice the 100 x 100 in the middle? Yup, those are the dimensions we gave our element!

##### **Note: the box model will _always show dimensions in pixels_, even if you use percents or other units**

Ok so the above doesn't tell us much we don't know. But let's add a margin-top of 100px as well and see what that does:




![.guides/img/BoxModelMargin](.\img\BoxModelMargin.PNG)
There it is, our box model keeping exact track of the positioning of our element. Of course, you should have seen your element move as well. Now what if we add just `padding: 20px` ?

  

![.guides/img/BoxModelMarginAndPadding](.\img\BoxModelMarginAndPadding.PNG)


Yessir, all around. Just as we would expect. But the really fun part is when you **hover your mouse** over any of the box model's sections.


When you hover over the innermost part, you'll see your div get highlighted on the page - this is _great_ for locating elements when you've got a bunch on the page.
 

When you hover over the margin section, you'll see exactly what the browser is doing with that 100px - the "push", so to speak. You'll _also_ see that the margin highlight extends all the way to the right-most part of the page - why? Because this `div` is a **block** element! Bam.
 

So **whenever elements start disappearing or they don't look the way you expect - inspect them and look at their box model**, that should give you some headway about how to start fixing.

  
Btw, what happens when you hover on the padding section?


You should see the 20px all around that are padding the element. That's what we mean by the `div` being pushed "outside" beyond its original 100 x 100 dimensions.