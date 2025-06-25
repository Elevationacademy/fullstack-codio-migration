When we talk about **time complexity**, we generally **ignore constants**. Look at the `printAll` function from earlier, we can see that the *actual* number of operations is **2n**.

For each element in the array `arr`, we need to:

1.  assign the value of `e` - `let e of...` is an assignment
2.  print out `e` - that's `console.log`

Say we had 40 elements inside of `arr`, then this would take 80 operations. And if **n** is the length of our input (the array), then our time complexity is technically **2n**.

However, when we talk about time complexity we are usually thinking about the **long term** efficiency* of the code. This means that we care about what happens when our *input* grows - in this case, what happens if `arr` grows.

*Think about scale. If your input is 100 or 200, it doesn't matter; it's the same **magnitude**. Likewise, if your input is 10,000 or 20,000 - that **2** isn't going to make a difference.

As such, we can ignore the **2** and just say that the `printAll` function **runs in O( n )** - *O of n*.

This kind of analysis (where we think about the long term and ignore constants like this) is called **asymptotic analysis**.

## Spot check

What is the technical and asymptotic time complexity of the following code?

```
const doSomething = function(arr){
  console.log(arr[0] + arr[37])
}
```
<details><summary>
  Click here to reveal the answer.
</summary>
  
Technically: 4

1.  Accessing the first variable
2.  Accessing the second variable
3.  Summing the variables
4.  Printing the sum
  
Asymptotically: 1, i.e O( 1 )
</details>


---
<br>
**Note**: though we *ignore* constants when talking about time-complexity, **constants are still important** - if the constant is one million, then obviously we need to consider this as it will affect our runtime execution.