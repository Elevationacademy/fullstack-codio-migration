# Indentation and Line Breaks

A very critical criteria of a readable code is Indentation and line breaks. In the industry you will be sharing a lot of the code you write to other colleagues.

Lets look at the following code, Which one of the following is more readable

**Example A:**
```js
function    isPositive(num) {
    if(num>
            0 ){
return true
    }
          return false
}
console.log(isPostive(1))
```

**Example B:**
```js
function isPositive(num) {
    if (num > 0) {
        return true
    }
    return false
}
console.log(isPositive(1))
```

<details><summary>
Click here to reveal the answer.
</summary>

**It should be obvious that its B!**
some of you might say "Oh but it works 😉"
that is correct, however it would take double the time to understand your code.

</details>

---

Follow these rules:
- It is acceptable to use 4 spaces for Indentation in JavaScript
  You can customize it in your idea settings. check [this](https://stackoverflow.com/questions/29972396/how-can-i-customize-the-tab-to-space-conversion-factor) out. 
- Make sure your Block's content is always indented in the Scope of the Block

**Indentation and line breaks** are generally only of use to programmers, compilers and interpreters rarely care how much whitespace is present in between programming statements.



in order to be able to share your code properly you need to make it as readable as possible.
