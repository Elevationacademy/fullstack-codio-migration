
#### **QUICK NOTE ABOUT PROTOTYPE**

  

Prototype is Javascript's old way of implementing OOP.

ES6 wrapped the prototype syntax so well that we cannot see any hint of it now. We'll go over these a bit more in our inheritance lesson, but if you like, you can read more about prototypes [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/prototype) or [here](http://prototypejs.org/) and [here](http://prototypejs.org/learn/class-inheritance), but don't let the old syntax confuse you.

If you want to know even more about prototypes, you can read about it [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/proto).

----------

#### **STATIC METHODS (NOT MANDATORY)**

  

Now say we want to know general information about the `Vehicle` class we created before.

For instance, let's say that every instance of a class in my code represents a car that was created physically in the real world.

  

We could, each time a vehicle is instantiated, add a count to some external variable - but this is data that is specifically related to `Vehicle` - the count of `Vehicles` should be a part of this class, but _not_ of each instance.

The solution is something called `static`

  

----------

We can create methods and attributes that are **static** - that means available at the class-level, as opposed to the instance-level.

  

So far, any method/attribute we've had belonged to each specific instance of our class.

With **static**, we can change that:

```js
class Vehicle{
    constructor (x, y, speed) {
      this.x = x;
      this.y = y;
      this.speed = speed;
   }

   static getInfo(){
      console.log("Cars are great");
   }
}
```
  

Notice the `static` keyword before our `getInfo` method. To invoke it, we would do this:

  

```js
Vehicle.getInfo()
```
  

This is _different_ from instantiating a class and calling its method (you could not do `car.getInfo( )` if you had a car instance). This method belongs to the _class_, not a particular instance.

  

  

To make this static method useful, let's change our constructor to look like this:

  
```js
constructor(x, y, speed) {
    this.x = x;
    this.y = y;
    this.speed = speed;
    Vehicle.carsSold++;
}
```

Now whenever we instantiate a specific car object, we will be incrementing the value of `carsSold` by one.

In other words, we are changing a class-level property each time the constructor is called; i.e each time a new Vehicle is created.

  

But what is the initial value of `carsSold`? We have to define that **after the class definition**, like this:


```js
Vehicle.carsSold = 0;
```
  

That is one way we can create static properties for a class.

Finally, we can make `getInfo` a useful method by changing it to this:

```js
static getInfo() {
    console.log("We've sold " + Vehicle.carsSold + " vehicles.");
}
```
Now go ahead and create two instances of a car, then invoke the `getInfo` method - what do you see logged?
<details><summary>  
Click here to reveal the answer.  
</summary>

"We've sold 2 vehicles."
Please ask an instructor if this does not make sense.
</details>
