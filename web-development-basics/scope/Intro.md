# Scope

When we talked about if statements, loops, and functions, we kept referencing this notion of a **code block**.

  

Generally, anything between curly braces, 
```
    {
      this stuff
    }
```
 
is said to be its own block, and therefore have its own **scope**.

Scope refers to the **"visibility"** of a variable - i.e. which parts of the code can see and access the variable. Let's dive into this to see what we mean.

## If

Check out the following code:

```js
const bag = ["flashlight", "medicine"]
const moreItems = ["tent", "water bottle", "knife", "rope"]

if(bag.length < 3){
  const nextItem = moreItems[0]
  bag.push(nextItem)
}

console.log(bag)
console.log("Added " + nextItem)
```
  
We expect the code above to push `"tent"` into `bag`, because the length of `bag` is 2 at first.

Then we expect to see the new `bag` in the console, as well as `"Added tent"`, since that is what we added.

  

When you run this code, you should see two logs:
  

    ["flashlight", "medicine", "tent"]
*Uncaught ReferenceError: nextItem is not defined

  

So the code _does enter_ the if, and it _does push_ `nextItem` in the `bag` - and yet we get an error that says that `nextItem` is not defined.

  

That is exactly **scope** in action.

The variable `nextItem` is only defined within the _scope_ of the `if` - i.e. within the `if`'s curly braces.

  

More generally, **any variable is only accessible in the scope in which it was defined**
