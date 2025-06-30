# Operators

Operators in JavaScript are very similar to what many of you already know.


---------- 

## COMPARISON OPERATORS

When we want to compare equality, we have a few choices:
  
```js
console.log(3 < 5) // will output true
console.log(3 > 5) // will output false
console.log(2 >= 2) // will output true
console.log(1 <= -1) // will output  false
console.log("this string" == "that string") // will output false
``` 

Notice that **to compare equality we use two equal signs** - not one! We use one for **_assignment_**.  

Also, when we compare strings, JS compares them _with_ case-sensitivity; "Cat" is **different** from "cat".  

---

There is another way to check for equality, and that is - no joke - the triple equals sign: `===`  

Check this out:

```js
console.log(1 == "1")// prints true
console.log(1 === "1")// prints false 
``` 

**When we check equality with two equal signs JavaScript first converts the two values to a common type** behind the scenes - in the above case, it will convert `"1"`to `1`, and therefore it will be equal.  

However when **we use the triple equals, JavaScript checks for equality in both value and type**, without converting anything. Hence `1` does not equal `"1"`, because the former is a **number** and the latter a **string.**
  

Usually we will use the triple-equal signs. This is not a hard-and-fast rule, though; just good practice. Here's [a good resource](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Equality_comparisons_and_sameness) on equality comparison in JavaScript if you're curious.

---------- 

## **MATHEMATICAL OPERATORS**
  


We have our four standard math operations: plus, minus, multiply, divide. In JS (and most languages) the symbols are `+`, `-`, `*` ,`/`. 

---

**Warning**: if you try to do something illegal like the following:


```js
let num
console.log(3 + num)
```  

Then the console will log a special expressions called **`NaN`** **- short for Not a Number**.

This happens because we didn't initialize `num` with some number, and JS doesn't know how to do `3 + undefined` - it doesn't make sense. 

---------- 

## **MODULO**  

**Modulo** is a special operator that gives us the **remainder** of a division operation. We use the `%` symbol for modulo:

```js
console.log(14 % 5) // will print 4
```
The above outputs 4 because the number 5 can go into 14 twice, with 4 left over.


----------  

## **TRUTHY/FALSEY**  

When something **resolves to true it means that ultimately its value is the boolean** **`true`** - for instance, `3 < 5` resolves to `true`; it is also known as a **truthy expression**.  

Other examples of "truthy expressions" include:

```js
23 == "23"
41 === 41
"this string" == "this string"
972 % 2 == 0
```


There are also, of course, "falsey expressions". **Falsey expressions are those that JavaScript ultimately converts to false**.   

There are also other `falsey` expressions in JS, such as:  

-   `0` - yes, JavasScript sees the number zero as falsey if it's used as a number
-   `""` or `''` - an empty string value is also falsey
-   `undefined`
-   `NaN`
-   null - this is a special expression that we'll talk more about later, but it's a way of saying "no value" that is different from `undefined`
  
----------  

## **LOGICAL OPERATORS**
  

We have three main operators to help us control flow in JavaScript:  

-   `&&` - the **and** operator - both sides must resolve to `true`
-   `||` - the **or** operator - at least one side must resolve to `true`
-   `!` - the **not** operator - flips a boolean from `true` to `false` or the other way around
  


----------

There is a nice trick you can do with the `||` operator when assigning variables. Check out this code:

```js
let startPosition
let newPosition = (startPosition || 0) + 10

console.log(newPosition) //prints 10
```

In other words, **we can use the** **`||`** **(or) operator to assign a value _conditionally_**. This is useful when we have some "starter" value that might or might not be initialized.

**Note:**
The above would not work without the ` || 0` because you cannot add `10` to `startPosition` while it's `undefined`

----------

