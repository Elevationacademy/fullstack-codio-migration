# Meaningful Naming

We, developers name everything from variables, functions, classes to files, however many times we focus on solving a problem and we do not worry about readability and best practices while naming.

---

<span style="font-size: 28px"> **Variable & Functions**</span>

Variable and function naming is an important aspect in making your code readable so, you should follow a simple idea: **Create variables that describe their function**.




- Don’t use names that are too short. Simple one-letter names or names that don’t make sense are not a good option when naming variables. **(i in a for loop is an exception )** 


<span style="color:red">**Don't**:</span>
```js
function a(x) {
    if(x > 0){
        return true
    }
    return false
}
```

<span style="color:green">**Do**:</span>
```js
function isPositive(num) {
    if(num > 0){
        return true
    }
    return false
}
```
</br>

- Use more than one word to name your variable. This will ensure your variable name is precise.

<span style="color:red">**Don't**:</span>
```js
function greet(first,last){
  return "Hello ${first} ${last}"
}
```

<span style="color:green">**Do**:</span>
```js
function greet(firstName,lastName){
  return "Hello ${firstName} ${lastName}"
}
```
</br>


- When using more than one word in your variable names, always put the adjective to the left. For example, this is correct: var greenGrass.

<span style="color:red">**Don't**:</span>
```js
numMax = 10
numMin = 1

```

<span style="color:green">**Do**:</span>
```js
maxNum = 10
minNum = 1
```

</br>


- in JavaScript we use camel case, that means we the first word is lowercause however every single word after that their first letter is uppercause


<span style="color:red">**Don't**:</span>
```
function IsPOSTIVE(x) {///}
function is_positive(x) {///}
function ISPOSITIVE(x) {///}
function Is_POSiTIVE(x) {///}
function isPoSTiVe(x) {///}

```

<span style="color:green">**Do**:</span>
```
function isPositive(x) {///}
```

we can tell what the function does with the **Meaningful Naming**

</br>


another Example, try to see whats wrong with it, then try to fix it.

```
function greet_person(x, y){
    if(y = "Female"){
        return "Hello Mrs."+x
    }
    else{
        return "Hello Mr."+x
    }
}
```
<details><summary>
Click here to reveal the answer.
</summary>

- the function name needed to be changed
- the arguments needed meaningful naming
  
```js
function greetPerson(lastName, gender){
    if(gender == "Female"){
        return "Hello Mrs." + lastName
    }
    else{
        return "Hello Mr." + lastName
    }
}
```

</details>

</br>

---

<span style="font-size: 28px"> **File names**</span>

- when we create a file the naming convention is to use all lower case letters seperated with hyphen ``-``.

<span style="color:red">**Don't**:</span>
```js
myCodefile.js
mycodefile.js
my code file.js
my_code_file.js
```

<span style="color:green">**Do**:</span>
```js
my-code-file.js
```
---

<span style="font-size: 28px"> **Constants**</span>

- when we add a Constant in our code we write it in All Caps with underline separation ``_`` 

<span style="color:red">**Don't**:</span>
```js
const myconstant = "const"
const myConstant = "const"
const my-constant = "const"
const MyConstant = "const"
```

<span style="color:green">**Do**:</span>
```js
const MY_CONSTANT = "const"
```






