
If you got fed up with document.createElement and then adding endless attributes/classes.. jQuery's got a great shortcut for you. Check this out:

  
```
const aDynamicDiv = "<div class='mine'>Oh yes</div>"
const elem = $(aDynamicDiv)
console.log(elem)
```
  

What you see in the console is a exactly an element.

That's right - you can write your own bona fide, straight up HTML inside quotes, then just wrap it with the $ symbol and boom - it's an element.

  

Notice that we also defined the new div's class right in the string!

  

As for adding that element to the page, jQuery hooks us up with an append method, which works just like document....appendChild:

  
```
$("body").append(elem)
```
  

If you add some styling to .mine in your CSS file - you should see that element you created appear on the page.

  

Of course, we can use jQuery to add anything to existing elements, as well:

  

**HTML:**
```
<div class="fruits"></div>
```
  

**JS:**
```
$('.fruits').append('<p class="red">Raspberry</p>')
$('.fruits').append('<p class="brown">Kiwi</p>')
```
  

Try out the above, then inspect your elements - you should see a couple p tags with the classes as indicated above!

  

Check out the [docs](http://api.jquery.com/append/) for more details and examples about append

  

Of course, we're not limited to just strings - we can always concat:
```
const text = "Banana"
const item = $("<div class=fruit>" + text + "</div>")

console.log(item) //prints <div class=fruit>Banana</div> as a jQuery object - this is what we created!
```
  

Because all the concatenation can get a little annoying with the pluses and quotes, we suggest using [template literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) to concat - a nice feature from **ES6**:

  
```
const text = "Banana"
const item = $(`<div class=fruit>${text}</div>`)

console.log(item) //the same
```