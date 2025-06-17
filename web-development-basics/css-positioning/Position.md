# Position

The `position` property really is the basics of moving things around correctly in CSS. Using `margin` and `padding` alone is not very useful or scaleable. But first, we need to talk about parents and children.

----------
## **PARENTS, CHILDREN**

We've seen this briefly before, but let's talk about the concept of parents and children.
```html
<div id="parent">
  ﻿<div id="child1"></div>
  ﻿<div id="child2"></div>  
</div>
```
  
The outer `div` _wraps_ the two inner `div`s, and so we say that the outside `div` is the **parent** of the inner ones. The inner `div`s are its **children**, and also **siblings** of one another.

  
Note: we do **not** have to give parents/children any `id` or `class` to create this relationship. The above example is just for clarity, and will help us with our CSS.

  
So create the above layout, give the parent a width+height of 300px, the children 100px each, and give all three different background colors (parent: red, child1: blue, child2: green).

 

Here's an example:


![.guides/img/parent-children-start](.\img\parent-children-start.PNG)



Notice that now the two children are inside the parent, where as usually we saw that divs push each other down.

  This is happening because when we have this parent-child relationship, the parent becomes a (kind of) frame of reference for the children.

  So for now, the children see the parent as the parent sees the entire browser (i.e what we've seen up to now).

  Play around with the margin and padding properties that you know, and see what happens. In particular, you should note that:


- `margin-top` on _child1_ will push the parent `div` down instead of the _child1_`div`
- `margin-top` on _child2_ will push the child2 `div` down from the _child1_ `div`
-   `padding` the children `div`s will cause them to overflow if you give them dimensions bigger than the parent
-   `padding` the parent makes it expand and "pushes" its children "inwards"
-   Adding a `margin` to the parent makes the whole container move

Make sure you experiment until you've experienced all of the above.


Sometimes these results are not what we expect.


In general, when we're building websites **we want to allow room for dynamic content**

This means that we generally don't want to limit our elements (`div`s, etc) to particular dimensions, _especially_ elements that contain children.

  For starters, then, reset your code to only have the parent and its two children, each with their own color. **Remove the dimensions** from the _parent_.

You should see this:
 
![.guides/img/parent-children-no-p-dimensions](.\img\parent-children-no-p-dimensions.PNG)

Woops. If you remember the distinction between `block` and `inline` elements - what's happening should be clear.

  The parent element is a `div`, which is a `block` element, and so takes up the entire width of the page by default. Since we didn't specify any width, it took up 100% of the width.


But we just said we don't want to specify width to allow for dynamic content sizing. Solution? Add this to your parent's CSS:

```
display: inline-block;
```
  
And now! It's gone o_o
  

But that's only because inline elements take up only as much space as they need, which in this case the exactly the dimensions of its children.

  
So now, add the following to your parent:

```
padding: 10px;
```
And voila! Now you have your dynamic parent that resizes according to the content inside.

Modify the **children**'s padding, width, height (and margin, to an extent) - see what happens - no more overflowing content!
  

However, sometimes we _do_ want to limit the parent's dimension - at least its width, because we want it to share the space with other elements. Here's where we start talking about `relative` and `absolute` positioning

  
----------

## **RELATIVE POSITIONING**


Reset the code (or open a new file, or comment out your code, up to you) to the parent (width+height: 300px, red) and its children (width+height: 100px, blue, green)

Now add this to the first child:
```
position: relative;
```
  
  Alone, this doesn't do anything, but what it does is allow us to now use other properties. In particular, `left`, `right`, `top`, `bottom` - note that these are **different** from margin-top etc


Give 200px to the first child's `top` and `left` property - see what happens?


![.guides/img/basicrelativetopleft](.\img\basicrelativetopleft.PNG)
Notice that this time the parent and the second child were not affected at all - only the first child was moved according to the specific instructions we gave it.

Now **that's** power


Effectively, what is happening is that `relative` says to the element: "act as you should act, given your frame of reference (the parent) and the commands you've been given (top, left, etc)". Really "relative" means relative to _itself._
 

In case you want to validate your code, here's the CSS for the above image:

**CSS**:
```
#parent {
background-color: red;
width: 300px;
heightL 300px;
}
.child {
width: 100px;
height: 100px;
}
#child1 {
position: relative;
top: 200px;
left: 200px;
background-color: blue;
}
#child2 {
background-color: green;
}
```
  

**HTML:**
```html
<div id="parent">
  <div id="child1" class="child"></div>
  <div id="child2" class="child"></div>
</div>
```
----------

  

## **ABSOLUTE POSITIONING**

  This is important regarding absolute positioning:

  **Absolute positioning only works if the element's parent is non-static**

  What is static? `position:static` is the default position for any element. (you don't have to define it).

  Thus, if you are going to position anything as `absolute` you must first change its **parent** to either `position: relative` or `position: absolute`


So if this is your child:
```
#child{
  width: 50px; 
  height: 50px;
  position: absolute;
}
```
  
Here are your options for the parent (note the comments that indicate which is an acceptable option and which isn't):

```
/* NO */
#parent{
  width: 100px;
  height: 100px;
  background-color: red;
}

/* Yes */
#parent{
  width: 100px;
  height: 100px;
  background-color: red;
  position: relative;
}

/* Yes */
#parent{
  width: 100px;
  height: 100px;
  background-color: red;
  position: absolute;
}
```
  Now that that's clear...
 

Let's see what happens when we give a child element an `absolute` position. Use the same initial setup from before (parent, two children), but now change the blue child's position to absolute (remember to remove any other top/bottom stuff you had)
  
Hopa! The green child disappeared. Or did it?
Sounds like a good time to open up the developer tools! (right-click on the page, Inspect)

  

![.guides/img/DevTools2](.\img\DevTools2.PNG)

As you can see, the second child is still there, but we aren't seeing it. This is because - and this is important:

**Absolute elements are taken out of the normal flow of the elements on the page.**

Remember that the general flow for **block** elements is to take up the whole row. Any block element thereafter will appear below the first one, because there's "no space" there.

But _absolute elements_ don't adhere to this flow. They ignore it, and are just where they are. This gives us 100% control of every pixel of movement for that element, but it also means that - and this is also important - **other elements ignore absolute elements.**

Because the second child (the green one) is ignoring the first child, it goes to where it would go if the first child didn't exist - **as top left as possible** - and thus ends up behind the first child, making it "disappear" as far as we're concerned.

So what's the added value of `absolute` elements? Add `right: 0` to the first child and see what happens.

  Snap. The second child is up left, and the first child is up-right, 0 pixels away from the edge of its parent.

Remember, children still work in the frame of reference of their parents - **but this only works if the parent's position is either** **relative** **or** **absolute** **(i.e. non-static)**.

So now, using `absolute` positioning, see if you can create this:

![.guides/img/absolutepractice](.\img\absolutepractice.PNG)

If you've tried for at least 8 minutes, check out the solution below - though you should first ask the other students/instructor to understand the concept.

  Check out [this codepen](https://codepen.io/ElevationPen/pen/NVmYQb?editors=1100) for the solution
  
What you'll notice - and this is one of the great things about `absolute` positioning - if we change the dimensions of the parent element, all the children will stay in their respective edges. Try it out and see.

If the above was too easy, trying replicating the following image.

**Hint**: there's a tiny math trick here.

![.guides/img/absolutechallengewithtrick](.\img\absolutechallengewithtrick.PNG)