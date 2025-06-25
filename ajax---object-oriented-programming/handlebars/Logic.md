
We can also write some of our logic right into our template using some built in **helpers**.

  

**For Loop**

  
```
<script id="menu-template" type="text/x-handlebars-template">
  <ul>
    {{#each menu}}
      <li><a href="{{link}}">{{name}}</a></li>
    {{/each}}
  </ul>
</script>

<div class="menu">
</div>
```
  
```
const menuData = {
  menu: [
    { name: "Google", link: "http://google.com" },
    { name: "Facebook", link: "http://facebook.com" },
    { name: "Instagram", link: "http://nstagram.com" },
    { name: "Twitter", link: "http://twitter.com" },
  ]
};

const source = $('#menu-template').html();
const template = Handlebars.compile(source);
const newHTML = template(menuData);

// append our new html to the page
$('.menu').append(newHTML);
```
  

Some notes on the above code:

  

-   #each and /each are reserved keywords for handlebars.
-   menu is the name of the array over which handlebars will iterate, and must be the same (case sensitive) in both the HTML and JS code.
-   Notice that we can have handlebars within strings - as with the href
-   The reason we wrap menu inside of a menuData object is twofold:

1.  The template function must receive an object as a parameter.
2.  We might want to send more arrays or other objects later, so it's better to encapsulate them like this and send them together rather than have separate handlebars for each (not relevant for now, but just so you know).

  

  

----------

  

**Spot check:** given this object:

  
```
var classData = {
    classmates: [
        {name: "That on gal", description: "Always has the ansswer"},
        {name: "The weird dude", description: "Quick with a smile"},
        {name: "Taylor", description: "Just Taylor"}
    ]
}
```
  

Write some Handlebars (HTML & JS) that displays all the students and their description using the #each syntax.

  

Check out [this codepen](https://codepen.io/ElevationPen/pen/PrYjMd?editors=1010) for the solution.

  

----------

  

**If**

  

We can also use handlebars to _conditionally render_ some of our HTML. Check it:

  
```
<script id="menu-template" type="text/x-handlebars-template">
  <ul>
    {{#each menu}}
      {{#if socialNetwork}}
      <li><a href="{{link}}">{{name}}</a></li>
      {{/if}}
    {{/each}}
  </ul>
</script>

<div class="menu">
</div>
```
  

The only potentially tricky bit here is that you need to make sure that the objects in iteration have a property (in this case socialNetwork) with a value of **true** or **false**.

  

----------

  

**Spot check:** alter the menuData object from earlier so that each item in the menu array has a socialNetwork property with true or false - then see if the above works.

  

Check out [this codepen](https://codepen.io/ElevationPen/pen/RzbZge?editors=1010) for the solution

  

----------

  

**Spot check:** build a template with both a for loop and an if statement. Use [this code pen](http://codepen.io/amhayslip/pen/vGZWOR?editors=1010) (which already has handlebars and jQuery) as your blank canvas. Be creative!