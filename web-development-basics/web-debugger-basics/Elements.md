# Elements

Let's talk about the first tab in DevTools - the **Elements** tab. The Elements tab shows all the elements as they have been rendered on our page and lets us play with the CSS on the page. Let's step through a demonstration:

-   Open DevTools and make sure the element panel is selected
-   Click on any element in the left side of the panel. Notice that its CSS properties will appear on the right hand side. Cool, ye? We can even change these CSS properties to dynamically change the styling of our page
-   Try it. Click on the element that represents this text. Now change the font size to 30px
-   Amazing, although everything is now a bit big so change it back!

In all seriousness, if we play around with CSS properties in this way we can learn what each property does. We can also tick and untick the boxes next to each property to find out why our page does not look how we want it to look.

Read this Article: 

  

[Chrome animation](https://developer.chrome.com/docs/devtools/css/animations/)

  

We want you to see that you can even change an element's type - see how they changed an `h3` title to an `h1` title. Take that Harry Potter, we're also wizards!

Remember "The Box Model" diagram? You won't be surprised to find out that we can also change (by double clicking) the numbers that represent an element's padding, margin, border and size (elements with non-static [position](https://developer.mozilla.org/en/docs/Web/CSS/position) even allow you to change their position on the screen, like in the diagram below).

  
![.\img\PROD_A1656-0.png](.\img\PROD_A1656-0.png)

**Please note**: modifications you make on the elements tab do not affect your original code. They are also not permanent, meaning that when you reload the page all your changes are lost. If you want to make your changes stick after a page refresh, then set up [persistent authoring](https://developers.google.com/web/tools/setup/setup-workflow) (but remember your source code never changes).

We'll be looking at the elements tab in more detail in a future lesson called "The DOM".
