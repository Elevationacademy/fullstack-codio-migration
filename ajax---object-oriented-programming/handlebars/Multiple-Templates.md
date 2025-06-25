
Note that you are **not** limited to one ``<script id="..." type="text/x-handlebars-template">`` in your HTML - you can have one any time you want to add some templating!

  

Take the following for example:

  
```
<script id="first-template" type="text/x-handlebars-template">   
  My text: {{text}}
</script>

<div id="normal">Regular HTML Stuff</div>

<script id="second-template" type="text/x-handlebars-template">   
My HB text: {{moreText}}
</script>

<p id="special"></p>
```
  
```
const renderFirst = function(){
  const source = $('#first-template').html();
  const template = Handlebars.compile(source);
  let newHTML = template({ text: "This gets rendered" });
  $('body').append(newHTML);  
}

const renderSecond = function(){
  const source = $('#second-template').html();
  const template = Handlebars.compile(source);
  let newHTML = template({ moreText: "This also gets rendered" });
  $('#special').append(newHTML);  
}

renderFirst()
renderSecond()
```
  

That works just fine, and in fact is a great way to work! We don't always have one object that holds all our data - sometimes we do - and sometimes we just want to separate our HTML - so all is well, we can have multiple templates.

  

**Spot check:** given these two arrays, load them to separate templates using #each:

  
```
const animals = ["Rabbit", "Giraffe", "Kangaroo", "Whale", "Seagull", "Caterpie"]

const languages = ["French", "Spanish", "Togolese", "Javascript", "Uruk"]
```
  

See how these are just strings, and not objects? Here is [a resource](https://stackoverflow.com/questions/20773464/rendering-a-string-array-with-handlebars) that will help you render plain strings in handlebars.