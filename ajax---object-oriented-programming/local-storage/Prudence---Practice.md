
For this section, you have two options:

-   Add Local Storage functionality to an old project that you've already completed
-   Complete the exercise below

###### Of course, you're welcome to do both ;)

  

Either way, you should be aware of the following concept: we cannot 100% trust that our data is always in Local Storage. The user _can_ delete it, inadverntently or otherwise. **Regardless, Local Storage works per browser**, so it's enough that our user switched computers, and our LS won't be consistent.

  

As such, when retrieving data from LS, we always want to guarantee that we have a failsafe. Here is a simple example:
```
let data = JSON.parse(localStorage.dataThatIsImportant || "[]")

data.forEach(d => /*something with data*/)
```
  

Here our application assumes that data is some array. It could be user preferences, or some items in a shopping cart - whatever, but if the user deleted dataThatIsImportant, or changed computers, then **localStorage.dataThatIsImportant** **is undefined!**

  

And of course, we cannot do undefined.forEach...

  

So we use the something || [ ] 'trick' to say _give us something,_ **_or_** _if that thing is somehow falsy, give us an empty array_.

  

Of course, you could also do ... || { }, or any other default you like - but make sure you have a failsafe when working with Local Storage!