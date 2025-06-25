
The way we've created classes so far, we could access each instance's attributes directly. Like this:

  


```js
const car = new Vehicle()
car.x = 3
car.y = 1
car.speed = 5

console.log(car.x) //prints 3
console.log(car.y) //prints 1
console.log(car.speed) //prints 5
```
Yes, we _should_ be using the constructor, but bear with us for this example.

  

When we initialize the values (3, 1, 5) of `car`, we are **setting** its properties.
When we console log its properties, we are **getting** its values.

  

We can set and get properties directly, and generally this is OK.

  

However, we sometimes want to employ some conditions on a set or get operation.
For instance, we might want to dis-allow setting a negative value to the `speed` attribute.

  

We can do this by creating a method with they keyword `set`, like this:

```js
class Vehicle {
    constructor(x, y, speed) {
        this.x = x;
        this.y = y;
        this._speed = speed;
    }

     set speed(speed) {
        if (speed < 0) {
            return console.log("Speed must be positive")
        }
        this._speed = speed
    }
}
```
We've made a couple of changes:

1.  We've changed the `speed` attribute to `_speed` to indicate it should be private
2.  i.e, it shouldn't be directly accessed
3.  We've added a `speed` method that accepts one parameter, `speed` - and we've prefixed this method with the `set` keyword

  

  

Inside our `set speed` method we've defined some logic that will only set the class's `speed` if it is greater or equal to 0 (positive).

  

Check this out, and **try it out yourself** as well:

  
```js
const c = new Vehicle()
c.x = 3
c.y = 1
c.speed = -2 // at this point, we'll get the console log saying speed needs to be positive
console.log(c.speed) // prints undefined
```
So now we've limited the values that are allowed in any instance! This can be very useful.

  

You'll notice, however, that if we do this:


```js
c.speed = 10
console.log(c.speed)
```
We still get `undefined`, but no error message.

This is because `Vehicle` no longer has a `speed` property which we can get! It only has `_speed`

  

Of course, we don't want to write `c._speed` - that's a lot of work for the fingers. So that's where the `get` syntax comes in:

  


```js
get speed(){
    return this._speed
}
```

  

If you add that to your `Vehicle` class, then you'll be able to do `c.speed` and get its value instead of `undefined`

  

----------

**Common pitfall**: if a class attribute has the same name as the `set`'s method name, you will be faced with an infinite loop:

  

```js
set x(value) {
  this.x = value
} 
```
  

The above will cause an infinite loop because `this.x` will _invoke_ the `x` method (because it has the `set` prefix), which will try to run `this.x` which will _invoke_ the `x` method (because it has the `set` prefix), which will try to run... you get it.

  

Don't fall for this trap. Use private variables ~
