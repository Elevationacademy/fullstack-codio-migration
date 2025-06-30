# The debbugger word

Our JS code is eventually going to get longer and more complex and we may start having bugs. If this happens, don't worry, DevTools has a `debugger` to help us find and solve the bugs.

Change the code inside of **script.js** to look like this:
```js
let frontEnd = ['HTML', 'CSS', 'Javascript'];
let frontEndLangages = frontEnd;
```
What does the variable **frontEndLangages** point to? Our array. Cool.

Now change it to look like this:
```js
let frontEnd = ['HTML', 'CSS', 'Javascript'];
debugger;
let frontEndLangages = frontEnd;
```
We added the debugger statement to "pause" our code at that point. Go back to Chrome and make sure DevTools is open. Refresh your browser. Now type `frontEndLanguages` into your console, you'll see a response of 
```
Uncaught ReferenceError: frontEndLanguages is not defined.
```
  

![.guides/img/PROD_A1658-0](.\img\PROD_A1658-0.png)


  Why do we see "**not defined**"?
  
<details><summary>
  Click here to reveal the answer.
</summary>
  
The debugger paused our code before the part that declares the frontEndLanguages had been run. Therefore frontEndLanguages is said to be **not**  **defined**
</details>
  
---
In the future, the `debugger` will become one of your best friends.
