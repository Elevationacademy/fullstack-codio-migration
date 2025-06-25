### Definition
A client should never be forced to implement an interface that it doesn’t use.

### In Other Words 
Separate between unrelated functionalities.

Let's look at this innocent class:

```js
class Bird {
    constructor(type){
        this.type = type
    }

    tweet(){
        console.log("tweet tweet");
    }

    fly(){
        console.log("I'm Flying");
    }
}
``` 

What could be wrong with that?
Nothing yet, but what if we want to add a `Penguin` class?
It is reasonable that it will extend the `Bird` class.
So we get:
```js
class Penguin extends Bird{
    constructor(){
        super("Penguin")
    }
}
```

So now we got for free a Penguin that can fly and tweet :)
But wait, penguins don't fly (Yes! it's a fact, check it out!)
So what can we do?

We want to separate the special abilities of birds and use composition instead of inheritance. So the `Penguin` class will inherit from `Bird` it's common properties, like tweeting, and will add the other abilities, such as flying or swimming with composition.

So how can we do it?

First, we will create an object for each ability:
```js
const flier = {
    fly: function(){ 
      console.log(this.type, "is flying")
    }
}

const swimmer = {
    swim: function(){ 
      console.log(this.type, "is swimming")
    }
}
```

And we will leave only the common properties in the Bird class:
```js
class Bird {
    constructor(type){
        this.type = type
    }

    tweet(){
        console.log("tweet tweet");
    }
}
```

Now, the penguin can be a swimming bird:
```js
class Penguin extends Bird{
    constructor(){
        super("Penguin")
        addAbilities(this, swimmer)
    }
}
```

And the Sparrow can be a flying bird:
```js
class Sparrow extends Bird{
    constructor(){
        super("Sparrow")
        addAbilities(this, flier)
    }
}
```

# Spot Check
What is this `addAbilities` function?
Try to implement it!

* To check your answer - keep reading!
<hr>

We can also add a Swan that is a swimmer and a flier:
```js
class Swan extends Bird{
    constructor(){
        super("Swan")
        addAbilities(this, swimmer)
        addAbilities(this, flier)
    }
}
```

What is this `addAbilities` function - you must be wandering?
It simply copies the properties of the abilities to the given object:

```js
function addAbilities(object, abilities){
    Object.assign(object, abilities)
}
```

You can read more about `Object.assign` [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign)

One last thing.
There is some inefficiency in this example.
Can you spot it?


<details>
  <summary>
     Here is the answer
  </summary>
    If we add the abilities in the constructor then this function will ne added to each instance, instead of one time for all the class instances!!!
</details>
</br>
So in order to solve this problem we could implement the composition like this:

```js
class Swan extends Bird{
    constructor(){
        super("Swan")
    }
}
addAbilities(Swan.prototype, flier)
addAbilities(Swan.prototype, swimmer)
```

# Spot Check
1. Add another bird ability - singing. 
2. Now add a song bird, for example Humming Bird. This bird should be able to sing and fly.


<details>
  
  <summary>Solution</summary>    
 
  ```JavaScript
      const singer = {
        sing: function(){ 
          console.log(this.type, "is singing")    
        }
      }

      class HummingBird extends Bird{
          constructor(){
              super("Humming Bird")
          }
      }
      addAbilities(HummingBird.prototype, flier)
      addAbilities(HummingBird.prototype, singer)

      let madona = new HummingBird()
      madona.fly()
      madona.sing()
  ```

</details>
<br>
There you go!