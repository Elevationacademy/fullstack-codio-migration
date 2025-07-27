we will be implementing our Client using the **MVC** principles. 

## Basics 

you need to create a basic HTML template with all the relevant elements. 
you can use this picture as reference.

![](https://kernel-files.s3-eu-west-1.amazonaws.com/images/PROD_A601-0.png)


-   Create an `input` for an ingredient, and a `Search!` button
-   When the button is clicked, take the value of the input (with jQuery) and make a request to `/recipes`
    -   The value from the `input` should be your `ingredient` parameter


You should receive an array of recipes from this request. This array should have several objects, each with:

-   An `idMeal`
-   An _array_ of `ingredients`
-   A `title`
-   A `thumbnail` - a URL of a small image
-   An `href` - a link to the recipe video. Note that sometimes this link is invalid.

  

*Make sure that the objects in the array have the above properties **only.** They should look like this:
```
[
  {
    idMeal : "52972"
    ingredients: ['tomato', 'water'],
    title: 'Tomato Soup',
    thumbnail: 'sample.com/image.jpeg',
    href: 'youtube.com/movie'
  }
]
```
  

