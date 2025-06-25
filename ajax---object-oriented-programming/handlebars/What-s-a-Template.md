
When we want to add HTML dynamically, we sometimes get something really ugly in our JS:

  
```
const commentsContainer = '<div class="comments-container">' + 
  '<div class=comments-list></div>' + 
  '<input type="text" class="comment-name">' +
  '<button class="btn btn-primary add-comment">Post Comment</button> </div>';

$('.posts').append('<div class="post">' + 
  '<a href="#" class="remove">remove</a> ' + 
  '<a href="#" class="show-comments">comments</a> ' +       
  post.text +
  commentsContainer + 
  '</div>'
);
```
  

With handlebars, we can re-write the above in our HTML file instead, like this:

  
```
<script id="post-template" type="text/x-handlebars-template">
  <div class="post">
    <a href="#" class="remove">remove</a> 
    <a href="#" class="show-comments">comments</a> 
    {{ post.text }}
    <div class="comments-container">
      <div class="comments-list">
      <input type="text" class="comment-name"/>
      <button class="btn btn-primary add-comment">Post Comment</button> 
    </div>
  </div>
</script>
```
  

Notice that {{ post.text }}? That's a placeholder that our JS will fill in for us.

Using handlebars, we will just invoke a function that fills in anything inside the {{ }}with actual data, so our DOM will end up looking like this:

  
```
<script id="post-template" type="text/x-handlebars-template">
  <div class="post">
    <a href="#" class="remove">remove</a> 
    <a href="#" class="show-comments">comments</a> The first post!
    <div class="comments-container">
      <div class="comments-list">
      <input type="text" class="comment-name">
      <button class="btn btn-primary add-comment">Post Comment</button> 
    </div>
  </div>
</script>
```
  

Check out [this example here](http://codepen.io/amhayslip/pen/JGWdjq) - this is what Handlebars.js (and many other similar templating libraries) can do for us.

  

Let's break it down step by step:

  

1.  We write our HTML normally (inside our .html file), but inside a script tag.

  

-   For each "dynamic" item, we use our "handlebars" {{ }} to mark where we want to insert dynamic content - the thing we put inside the handlebars is a _variable_ - we'll see soon what initializes it.
-   Note that the id attribute we're using ( store-template ) is just a convention, but it makes sense to call it 'something-template'.
-   Also, text/x-handlebars-template is a special type we give the script, but there's no need to delve into this:
-   p.s: it sometimes helps to put the script at the bottom of the page and NOT as a part of the HTML - remember this is HTML that will be _generated_ by Handlebars, **not** _where_ it will be generated

  
```
<script id="store-template" type="text/x-handlebars-template">
  <p>
    <span> {{ item }} </span> - <span>{{ price }} Dollars </span>
  </p>
</script>
```
  

2. Next, we must add a link to the Handlerbars.js script after the jQuery script to our page (similar to the way we've added jQuery):

  
```
 <script src="https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/4.0.4/handlebars.js"></script>
```
  

3. Now, we use jQuery's .html method to select our template and convert it to an HTML string in our javascript:

  
```
const source = $('#store-template').html();
```
  

4. After that, we invoke Handlebars' compile function and pass in source. It returns a new function that we will use to fill our HTML in with our Javascript data.

  
```
const template = Handlebars.compile(source)
``` 

5. Now we invoke our new template function and pass in an object as an argument.

    -   Notice that our object properties match up to the items our template requires inside the {{ }} - this is how our variables get initialized!
    -   This function **returns a string with HTML code** that we had previously written out by hand

  
```
const newHTML = template({item: "bread", price: "15"});
```
  

6. And lastly, we just append it as normal!

  
```
$('.items').append(newHTML);
```
  

Check out [the example](https://codepen.io/project-shift/pen/JGWdjq) again to see the whole code without interruptions.

  

**Important notice**: when you append something - the place to which you are appending (above it's .items, but it can be anything) **must be outside** of the template script.

  

This is logical since inside the script tag it's basically just JS - we can't have raw HTML there, of course, but we can insert placeholder HTML that will then be generated into real HTML for us by Handlebars.

  

----------

  

**Spot check:**

  

Go to [this codepen](http://codepen.io/amhayslip/pen/PZpGZM?editors=1010) and write some javascript that loops through our items array, creates a template for each item and appends it to the .items div.

Note, you do _not_ need get the source and compile each time. Just create a new template and add.

  

See the solution on [this](https://codepen.io/ElevationPen/pen/xoKLwd?editors=1010) codepen.