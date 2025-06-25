In this lesson, you're going to practice the important skill of problem solving, i.e. writing **algorithms**.

  

An **algorithm** may sound like a big word - but all it is is **a set of instructions to complete some task**.

  

Let's consider the classic _find the smallest number in an array_ task:

```
let numbers = [31, 9, 18, 2, 106, 382, 0, 71, 8239, 791, -2321, 2500, 12, 13]
```

As a human, it's pretty easy to look at this and see that - `2321` is the smallest number - but that's because our subconscious mind is quite powerful. Behind the scenes, we're probably following an algorithm that looks like this:

  

1.  Look at the first number
2.  Store it in some place in our memory
3.  Look at the second number
4.  Compare the second number to the number stored in memory
5.  If the second number is smaller, forget the number stored in memory, and store the second number in memory
6.  Look at the third number
7.  If the third number is smaller, forget the number stored in memory...
8.  Repeat until the end

  

Of course, our minds do this blazingly fast so we don't really think of it like that - but that's effectively the process - and that is an excellent example of an algorithm! A very clear set of instructions.

  

----------

  

Now let's translate the above algorithm to code:

```
let smallestNumber //our 'number stored in memory'

for(let num of numbers){ //going over each number

  if(num < smallestNumber){
    smallestNumber = num //forget the number stored in memory and store num instead
  }
}

console.log("Smallest number is " + smallestNumber)
```
  

The above is pretty self-explanatory, but if you run this code you'll find **a logical bug**.

  

To solve this bug, you'll have to **debug the code, maybe also** [**take a look here**](https://stackoverflow.com/a/22134555/3147774) - try to figure this out on your own before looking at the solution.

<details><summary>
  Click here to reveal the answer.
</summary>
  
The problem is that the value of `smallestNumber` is initially `undefined` - we cannot compare greater/less than to `undefined`, so the expression `smallestNumber > num` always returns `false`.

This means we need to define some initial value for `smallestNumber`
</details>

---


Once you've figured out **and fixed** the bug, run your exact same code (without changing anything else) for the following arrays:

```
let numbers = [823412013513, 1381120136324, 82341381745, 181238377131412, 74128377131412, 74128377412] // should find 74128377412

let numbers = [-312, -9123, -112, -812, -7411, -312] //should find -9123

let numbers = [23, 23, 23, 23, 23] //should find 23
```

If you didn't get the correct results - it's because you've made some **assumptions**, and one of the golden rules in writing an algorithm is that you must **be aware of your assumptions**.

  

If, for instance, you initially set `let smallestNumber = 0` - then you couldn't find the smallest number in the first or third array above, because none of those numbers are less than `0`.

  

If, for instance, you initially set `let smallestNumber = 10000` - or some other 'large number', you might not find the smallest number in the first array because you assumed all your numbers would be less than 10000

  

Either way, to guarantee we're not assuming anything about our data, **we can set** `let smallestNumber = numbers[0]` - then we know we'll always get a result relevant to our `numbers` array.

  

And **even now, there's still a problem** - what result do we get for the following array?

```
let numbers = []
```
  

We would see `Smallest number is undefined` - not a very friendly message.

  

In summary, **when we write good algorithms, we need to assume as little as possible, and consider as many edge cases as possible**.