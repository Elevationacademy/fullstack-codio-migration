# Display

Remember the difference between **block** and **inline** elements?

Say we had a simple `div` in our HTML, and this was the styling we used:

```css
    div {
      height: 50px;
      background-color: #8e44ad;
    }
```
  
The result would be the following:

![.guides/img/PROD_A323-0](./img/PROD_A323-0.png)

Because we didn't specify any `width`, and because `div` elements are **block** by default, the element will take up the entire width available to it.  

On the other hand, if we had a `span` element with nothing inside, with the following CSS (where we _do_ specify the width):
```css
    span {
      height: 50px;
      width: 50px;
      background-color: #8e44ad;
    }
```
Then we wouldn't see _anything_ - and that's because `span` elements are **inline** by default - that means their size is only affected by the content inside of them.

We can use the `display` property like this:
```css
    span {
      height: 50px;
      width: 50px;
      background-color: #8e44ad;
      display: inline-block;
    }
```
And then we _would_ see the `span`, like this:


![.guides/img/PROD_A323-1](./img/PROD_A323-1.png)

Elements that are **inline-block** will still only take up exactly the space they need, and no more. The difference with **inline** elements is that these are _only_ affected by their content, and not by other CSS properties. 

There are [other display values](https://www.w3schools.com/cssref/pr_class_display.asp) you can explore.
