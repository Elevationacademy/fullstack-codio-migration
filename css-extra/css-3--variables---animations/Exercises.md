
Simple tools go a long way to making our lives easier as developers, and adding a bit of extra spice to our apps.
    
      
    
**Word of warning** about animations: generally when developers first learn about CSS animations, they get excited and animate _everything_ - **do not do this**. In design, always remember that **less is more**. A simple effect is usually much more impressive than a whole page jumping up and down.
    
      
    

    
      
    
## Exercise 1
    
      
    
Using CSS variables and animation, create the following glowing effect:
    
![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/glow-animation.gif)
    
-   The balls halo should increase-decrease alternately, infinitely
-   You should only have one `div` in your HTML
-   The [box-shadow](https://developer.mozilla.org/en-US/docs/Web/CSS/box-shadow) property should be useful
-   Use some pretty [flat UI colors](https://flatuicolors.com/palette/defo)
    
      
This could be used on a page as a nice indication that something is currently active, like a recording or even a loading screen.
    

## Exercise 2
    

Read up about the [transition property](https://www.w3schools.com/css/css3_transitions.asp) and re-create the above effect. However, instead of constant animation, make the glow occur when the mouse `:hover`s over the element.
    
Here's a more [detailed documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Transitions/Using_CSS_transitions%20target=) on `transition` - in general MDN is a more in-depth doc than W3.
    

    
## Exercise 3

The classic _hamburger_ - using a simple `transition`, recreate the following effect:
    
![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/burger-side-nav.gif)
    
Of course, because this works `on-click`... you'll need some JS in there ;)
    
**Hint:** you'll want to use the [overflow-x](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow-x) property to hide the text as the side navigation moves.
    
<details>
<summary>Click here for a more detailed hint.</summary>
  <ul>
    <li>Start by creating the top and side nav bar
      <ul>
        <li>Make sure the top goes all the way across, and the side goes all the way down</li>
        <li>Using CSS Grid might be helpful here</li>
      </ul>
    </li>
    <li>Add the burger icon - it can be from Font Awesome, or your own CSS creation</li>
    <li>The side nav is the part that's being animated
    <ul>
      <li>In particular, its _width_ is changing</li>
      <li>As such, we want the <code>transition</code> for the <code>width</code> to last about a second</li>
      <li>However, you should use jQuery in your JS file to actually change the <code>width property</code>
      <ul>
        <li>You want to use jQuery because you can't tell CSS to change element B when element A is clicked</li>
        </ul>
      </li>
      </ul>
    </li>
  </ul>
</details>      

    

---  
      
    
**Extra challenge:** use some animation to change the "burger" to an "X" when it's clicked, and back to a burger on the next click.
    
    

## Inspiration


If you're really into this stuff, [here is some inspiration](https://cssnewbie.com/15-new-awesome-creative-css-animations/#.XB9dIHQzZPY) to get your mind running with wild ideas. They all connect to some codepen, so you can see all the code for yourself.