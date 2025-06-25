We are all familiar with this syntax, where we use JavaScript to ‘select’ a DOM element to query it and perform operations on it.

Let’s assume we have an HTML input element with class ‘foo’ and we would like to query it so we can print out its typed value.
```
const someElement = document.querySelector(".foo");
console.log("someElement", someElement.value);
```
Now this would work fine with vanilla JavaScript, but once we switch to TypeScript, we will get an error “Property 'value' does not exist on type 'EventTarget'” on the second line.

What happens is that any DOM element is derived from a base interface called ‘EventTarget’. Now, this interface, or type if you will, is generic and doesn’t include the specific attributes and functions that exist for an HTML input field. We there need to ‘cast’ the class to its specific type.

See the class inheritance below to understand this concept. Note that ‘EventTarget’ and ‘Node’ are interfaces, and all the rest are classes. You can read more about this here.

![alt text](./chrome_7fYXd9pYGt.png)

### Casting a DOM element in TypeScript
In the above example, we would need to cast the element to HTMLInputElement, which is the correct type for this particular case. Casting is done by adding `as {casted_type}` right after the variable that needs casting.

```
const someElement = document.querySelector(".foo") as HTMLInputElement;
console.log("someElement", someElement.value);
```
This would now work as a TypeScript script.
