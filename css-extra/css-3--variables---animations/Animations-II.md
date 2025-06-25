
We can also have more granular control of our animation instead of just `from` and `to` - we can define what to do at each stage of the animation, like so:

  

**HTML**

```
<div class="loader"><div class="ball"></div>  
</div>
```
  

**CSS**

```
@keyframes morph{
  25%{
    background-color: #e74c3c;
  }
  
  50%{
    background-color:#27ae60;
  }
  
  75%{
    background-color: #2980b9;
  }
  
  100%{
    background-color: #f1c40f;
    margin-left: 200px;
  }
}

.loader {
  width: 220px;
  background-color: #2c3e50;
  padding: 1vmin;
  border-radius: 4px;
}

.ball{
  width: 20px;
  height: 20px;
  background-color: #9b59b6;
  border-radius: 50%;
  
  /*Normal Animation commands*/animation-name: morph;
  animation-duration: 2s;
  
  /*iteration-count tells it how many times to repeat*/animation-iteration-count: infinite;
  
  /*direction is for which way to go (we use alternate to go back and forth)*/animation-direction: alternate;
  
  /*How the animation should "ease" in/out*/animation-timing-function: linear;
}
```
  

You can see the result in [this codepen](https://codepen.io/ElevationPen/pen/wRJbza).

  

The main difference (aside from the extra `animation-X` commands you can read about in the docs), is that we are now explicitly telling the browser what to do at each **keyframe**:

-   At 25% of the animation's duration, make the background color red
-   At 50% of the animation's duration, make the....
-   At 100% of the animation's duration (i.e. at the end), change the color _and_ make the margin `200px` - which is the end of the `.loader`'s width

  

The percents, of course, reference our `animation-duration` property.

  

Of course, **we can add as many or as few keyframes as we want** - you don't have to go by 25% increments.

  

**Also note** that we don't have to indicate `margin-left` at each keyframe - we just need to tell it where it should be by the end.

  

**Also, also note** - you can _mix_ the `from`, `to`, and percents - `from` is always 0, and `to` is always 100%.