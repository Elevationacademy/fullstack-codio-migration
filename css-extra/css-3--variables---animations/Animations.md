
Animating anything on our webpage used to be done with Flash or JS only, but now we can do it directly with CSS.

  

The key to animations are the `keyframes` definitions, and then using it on an element, like so:

  

**HTML**

```
<div class="logo">FS</div>
```
  

**CSS**

```
@keyframes slide-from-bottom {
  from {
    margin-top: -10%;
  }
  to {
    margin-top: 0;
  }
}

.logo {
  /* Pretty Design Stuff - not related to animation */position: fixed;
  margin-top: 0%;
  background-color: #27ae60;
  display: inline-block;
  padding: 1vmax;
  color: #f1c40f;
  font-weight: bold;
  font-family: Trebuchet MS;
  font-size: 3vmax;
  border-radius: 5px;

  /* Animation Stuff */animation-name: slide-from-bottom;
  animation-duration: 2s;
}
``` 

You can see this animation in action in [this codepen](https://codepen.io/ElevationPen/pen/ebvoeZ).

  

Here's what's going on in the code above: we use the `@keyframes` keyword to define how our animation will look like, and the `animation-X` properties to use the animation.

  

In this case, it's pretty straightforward:

-   This animation will take the element **from** a state of being at negative `10%` of `margin-top`, **to** a state of being at `0` of `margin-top`
-   The `slide-from-bottom` is a name _we_ have defined
-   We "invoke" the animation inside the element we want to animate (in this case, inside of `.logo`)

  

There are other `animation-x` properties you can read about in [this section of the docs](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations#Making_it_repeat) and onwards - but the main ones are:

-   `animation-name` - which animation do we want to use for this element
-   `animation-duration` - how long should this animation last. The `s` denotes seconds