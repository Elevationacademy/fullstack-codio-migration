# Grid Areas vs Columns Rows

Let's take a second to highlight the difference between the `grid-template-areas` and `grid-template-columns/rows`. If you think about it, our code above was a little redundant. We defined the dimensions in two places.

  

Look at the following:

  



![.guides/img/css-grid-fr](.\img\css-grid-fr.PNG)
  

The template-areas should be this:

  
```css
"s m"
"f f";
```
  

Yes, that's it. Why? Because we should use the `template-columns` and `template-rows` for **dimensions**, and the `template-area` for the **layout**.

  

So we see that the main (purple) is 3 times as large as the side (green), and the top section (green+purple) is 3 times as large as the bottom (yellow). _That's_ where dimensions come in. So all in all, it should look like this:

```css
grid-template-columns: 1fr 3fr;
grid-template-rows: 3fr 1fr;
grid-template-areas: 
"s m"
"f f";
```
  

**Columns:** a 1:3 ratio, side to main (green to purple)

**Rows**: a 3:1 ratio, top section to bottom (green+purple to yellow)

  

Of course, you could also do this:

```css
grid-template-columns: repeat(4, 1fr);
grid-template-rows: repeat(4, 1fr);
grid-template-areas: 
"s m m m"
"s m m m"
"s m m m"
"f f f f";
```
  

They will have the **exact same** result - but you can see which one is easier to work with ;)
