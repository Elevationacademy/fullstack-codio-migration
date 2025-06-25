
You may have run across the data- attribute in HTML elements:
```
<div data-color="#2980b9">Blue</div>
```
  

We use data-something to add some extra data about the element that we would like to access dynamically, but not show the user.

  

For instance, in the above div, we're showing the user the text "Blue" in the div - but we use the data-color attribute to store information about the div

  

To access the data above, we can use jQuery's data method. Very convenient:
```
const color = $("div").data().color  
console.log(color) //prints #2980b9
```
  

Notice that data( ) will return an **object** - hence the dot notation to extract the color.

  

It returns an object because we can store multiple data-something attributes!

  

We'll put this to practice in an exercise later on, but for now...