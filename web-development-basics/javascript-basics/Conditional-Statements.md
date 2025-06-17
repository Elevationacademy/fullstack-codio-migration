# Conditional Statements
In this lesson we're going to talk about basic control flow in JS. 


**Conditional Statements**:
-   `if`
-   `else if`
-   `else`

This is how it's done in  JS:
```js
if (x > 100){
  console.log("big")
} else if (x < 10) {
  console.log("small")
} else {
  console.log("x between 10 and 100")
}
```

---

## Prompt

Before we dive into the exercise, it may help to know about the `prompt` command that is built-in to JS.

  

This command allows us to receive some input from the user through JS, like this:

  
```js
let username = prompt("What is your username?")
```
  

If you run the above code, you'll see a popup with an input. Whatever you (the user) types into that input will be the **value** of the `username` variable.
