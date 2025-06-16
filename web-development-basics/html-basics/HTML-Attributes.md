# Attributes

HTML elements may be given "attributes". Here is an example of an attribute.

```html
<p id="title">The Weather</p>
```

The **element** is the `p`, and `id` is the **attribute** - we can assign each element its own ID (short for identifier). This attribute in particular does not actually change anything about the element, but some attributes can have different effects or add functionality to elements. Some elements even *require* certain attributes.

Remember, **attributes go inside the *opening tag* of an element** - right after the `p`, for example, but before the first closing bracket: `>`

See [this page](https://www.w3schools.com/html/html_attributes.asp) for more attributes and how to use them. Some interesting ones might be `style`, `title`, `disabled` - though many others won't be practical until we learn JS.

## id & class

You'll use `id` and `class` a lot - they are particularly common attributes used for identifying elements. All HTML elements can be given both "class" and/or "id". For example:

```html
<div class="container">
</div>

<div id="top-section">
</div>

<div class="container" id="bottom-section">
</div>
```

We use Classes and IDs to "find and select" elements on a page. We'll see in the next lesson how we can use `class` and `id` in order to apply CSS styling to elements.
The rules of HTML dictate that **many elements on the page can have the same class. But IDs must be unique** - in other words, no two elements on the same page can have the same ID.

Also, any element can have multiple classes (but only one ID). To give an element more than one `class`, just separate them with a space, like so:

```html
<p class="box large"></p>
```

Again, IDs and classes are pretty useless without CSS or Javascript, but we'll get to that later.

## Element Specific Attributes

As we said some elements require specific attributes. Below is an `img` element (used for images) and it requires a `src` attribute with a value that points to the image to display.

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_March_2010-1.jpg"/>
```

Notice that this element doesn't need a closing `/img` tag - some elements are cool like this!
If we place the above in our index.html file, then the following picture will render on the page:
![](./img/4.jpg)
***
An `a` tag is used for an anchor element. It is commonly used to create a link to another webpage. To do so you use an `href` attribute as follows:

```html
<a href="http://www.google.com">Click Here for Google!</a>
```
This [right here](https://www.google.com/) is an `a` tag with an `href` attribute in action.

Or you can use it to "scroll to" an element with a particular id on your page. For example:
```html
<a href="#topofpage">Back To Top</a>
```
Will make the browser locate the element with the `id=topofpage` - what pure joy!
Try this one out yourself ;)

<sub> Note, this will only work if your page has somewhere to scroll - if it's a small page, there's no scrolling necessary!</sub>






















