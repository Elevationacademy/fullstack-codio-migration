Today, and probably in the future, screen sizes vary. Sometimes users are on their desktop with a wide-screen, sometimes on a smaller laptop, tablet, or phone - either way, we would like our web-apps to look reasonable on any display.

  

The answer to this conundrum is built up of a few things, but today we will talk about these in particular:

  

-   The Viewport
-   max/min width/height
-   Flexible units (instead of using pixels)
-   Media Queries - _the_ tool for responsive design
-   Emulating other devices on Chrome

It may sound like a lot, but these are pretty small, but useful tools, so let's dive in.

  

  

----------

  

  

#### **THE VIEWPORT**

  

  

The **viewport** is the area of the window in which web content can be seen ([quote](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta)) - that is to say, the visible area of a webpage. Naturally, this changes from device to device. We will be referencing this term throughout the lesson.

  

To accommodate different viewports, we can add this `meta` tag to our root (usually _index_) HTML file:

  

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```
  

The above goes in the `head` tag, usually at the top. You can read all the details about this [here](https://developer.mozilla.org/en-US/docs/Web/CSS/Viewport_concepts), but the gist is that it sets the width of the page to be the width of the _device_.

  

Generally there's not much more to do with the viewport aside from having this `meta` tag in our HTML, so we won't go into more detail about this.
