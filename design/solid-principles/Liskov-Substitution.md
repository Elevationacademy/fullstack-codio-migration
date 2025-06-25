### Definition
if S is a subtype of T, then objects of type T in a program may be replaced with objects of type S without altering any of the desirable properties of that program

### Definition 2
A superclass object should be replaceable with a subclass object without breaking the functionality of the software

Let's look at an example.

Here is a square class:

```js
class Rectangle {
    constructor(width, height){
    
    }

    setWidth(width){}

    setHeight(height){}
}
```

if we want to add a Square class, how should we go about it?

We could inherit from the `Rectangle` class:
```
class Square extends Rectangle {
    //...
}
```

After all a Square is a Rectangle 

But what are the consequences?
If we look closely we will see that the square has now 2 properties width and height which are redundant in a square case, because it can have only one edge property.
It will also have a strange behavior for `setHeight` method, it will probably have to update the width also. 

So in this case we can't really use the square as a Rectangle. The Liskov Substitution principle is violated!!
