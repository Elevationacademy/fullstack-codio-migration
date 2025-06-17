# Java Script this

Before we get into what `this` is in JS, let's refresh two concepts: Objects and Methods
```js
const person = {
  username: "Felicia",
  introduce: function(){
    console.log("Hi, I'm Felicia")
  }
}

person.introduce() //prints "Hi, I'm Felicia"
```
  

In the above, we've create an object with two properties: a `username`, which is a string, and `introduce`, which is a function. We call the latter a **method** because it's inside an object.

  

Isn't it repetitive to have "Felicia" both in the `username` property, and inside the method's console log?

  

But if we try something like this:

```js
const person = {
  username: "Felicia",
  introduce: function(){
    console.log("Hi, I'm " + username)
  }
}

person.introduce() //throws an error
```
  

We get an error because inside the `introduce` function, `username` does not exist! The "global"* scope of `username` doesn't apply in this context.

###### *Not really global, but relative to the function it is

To be able to reference/access an object's own properties from within its methods, we need `this`
