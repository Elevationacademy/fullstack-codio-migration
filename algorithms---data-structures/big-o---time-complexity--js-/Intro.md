Developers have to think about many aspects when they write code:

-   The app's architecture
-   Design
-   Which (if any) APIs to use
-   Servers
-   DBs
-   Frameworks/libraries

...and so on.

But another thing we need to consider is **efficiency** - how good our code is in terms of **number of operations**.

Generally, in the field of Computer Science this is known as considerations of **Time Complexity**. However, we do not measure *time* exactly, but rather we measure **operations**. An operation can be any one of the following:

-   An assignment - let x = 3
-   A mathematical operation - +, /, etc
-   A comparison - x >= 4
-   An access - people[0], p.name, etc
-   A write - console.log
-   A read - accessing a file/DB

When measuring the complexity of our code we don't care about the actual *count* of operations, but rather **how many operations will our code require <ins>relative to the given input</ins>**.

For instance, if we had this code:

```
const printAll = function(arr){
  for(let e of arr){
    console.log(e)
  }
}
```

Then we say that this would take **n operations**, where **n** is the length of the array `arr` - i.e. the number of operations grows as the input grows, one for one.

On the other hand, with this code:

```
const printFirst = function(arr){
  console.log(arr[0])
}
```

No matter *what* the length of `arr` is, this function will always take **1 operation** - whether `arr` has 10 or 10,000 elements inside of it, our **time complexity is O( 1 )*** i.e. it is in the **O**rder of *1* to complete execution.

*We say this as *O of 1*