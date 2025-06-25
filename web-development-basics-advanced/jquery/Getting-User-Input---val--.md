
With Vanilla JS, we used an input element's value property to "read" the value of the input. In jQuery, the method we use is quite similar.

  

Let's say we have this input element:
```
<input type="text" id="my-input" placeholder="Some Text!">
```
  

This code would give us the value of the input:
```
$('#my-input').val()
```
  

We can also _set_ or alter the value of an input by passing val an _argument_. There are more details and examples in the [documentation](http://api.jquery.com/val/).