# Margin & Padding

Let's start with a simple `div`. Create one (remember, HTML goes in the `index.html` file and CSS in the `style.css` file), and give it a width and height of 100px, and a background color of red.

Quick refresher if you're mind has slipped:

**index.html**
```html
    <div id="example"></div>
```
  **style.css**

```css
#example{
  width: 100px;
  height: 100px;
  background-color: red;
}
```
Now say I want to move this div to the right. What I can do is add the CSS property `margin-left`, like this:
``
    margin-left: 100px;
``
If I'm moving it _right_ why do I want margin-_left_? Because I'm pushing it 100px _away_ from the left.

Test it out and see the result.

Now use `margin` to push it _down_ (the opposite of down in CSS is `top`) 100px. D'you get it?

```
margin-top: 100px;
```

You can explore the others (`margin-right`, `margin-bottom`) - but you'll note that if you only have one div on the page, those properties won't affect it because **by default,** **`div`****s are positioned as top and left as possible** - of course, these properties will come in handy later when we have more than just one element.

Note: if you want to push your div from all sides at once, you can just do `margin: 100px`. Try it out and see what happens.

  ----------


## **MORE THAN ONE ELEMENT**
Just one `div` is not very interesting, so let's play with two for a second.

Add another `div`, again with 100px for width and height, and give this one a background color of blue.

Reset any margin settings you have. You should see this:



![.guides/img/twodivsstacked](.\img\twodivsstacked.PNG)

Now play around with the margin properties you know and watch how the divs move around. What have you learned?  

----------

Padding is pretty similar to `margin`, but instead of making the outside push the `div` in certain directions, it pushes the div _inside_.

To understand what this means, experiment for yourself.

If you get it, you should be able to create the following with **only** two `div`s that have a height and width of 100px, and play with the padding:

![.guides/img/twodivsstackedpaddingex](.\img\twodivsstackedpaddingex.PNG)

To be clear, create the above **without** changing the `width` or `height` properties of the `div`s