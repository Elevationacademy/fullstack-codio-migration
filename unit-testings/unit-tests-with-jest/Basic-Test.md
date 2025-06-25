In your `code.js` file, go ahead and add this code:

  
```
const add = function(a, b){
    return a + b
}

module.exports = add
```
  

Now in your `code.test.js` file add this:

```
const add = require('./code')

test("add should return sum of a + b", () => {
    let sum = add(1, 2)
    expect(sum).toBe(3)
})
```
  

Here's what's going on:

1.  We start by requiring the code we're testing - normal module work in node
    - In this case, we are importing the actual `add` function to be tested
2.  We invoke the `test` function - we have access to this function directly from Jest
3.  This function takes two parameters
    - A test name: a simple string that **describes what is being tested**
        - The more specific this name is, the easier it will be for you and future developers to understand your code
    - A callback function that will includes the test
        - It does **not** matter if this is an arrow or normal function
4.  Inside the callback, we are **invoking the function to be tested**
5.  Finally, we run our test: `expect(...).toBe(...)` - this is one of the most basic tests you can run

  

The `expect` method is also given to us by Jest. This function receives some value, and allows us to invoke the `toBe` method on this value.

  

In the above code we are **_expect_**_ing the sum from the function_ **_to be_** _3_ - we _know_ it _should_ be three because we are passing in the parameters `1` and `2`.

  

Now **to actually run the test, in your terminal execute** **`npm test`.**

  

You should see the following output:

```
 PASS  ./code.test.js
  √ add should return sum of a + b (8ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        1.95s, estimated 2s
Ran all test suites.
```

The code and feedback in Jest is generally quite legible in this regard.

  

Now, just to see what a failed test looks like, **change your** **`add`** **function to return** **`a - b`** **instead**. Then run your test again, you should see longer message explaining the error and where it's happening:

  
```
 FAIL  ./code.test.js
  × add should return sum of a + b (25ms)

  ● add should return sum of a + b

    expect(received).toBe(expected) // Object.is equality

    Expected: 3 
    Received: -1

      4 | test("add should return sum of a + b", () => {
      5 |     let sum = add(1, 2)
    > 6 |     expect(sum).toBe(3)
        |                 ^
      7 | })

      at Object.toBe (code.test.js:6:17)

Test Suites: 1 failed, 1 total
Tests:       1 failed, 1 total
Snapshots:   0 total
Time:        2.187s
Ran all test suites.
npm ERR! Test failed.  See above for more details.
```
  

It's a lot of output, but if you read it it's pretty clear: the test **_expect_**_ed_ the result to be `3`, but instead it was `-1` - that means that the developer wrote bad code (assuming our test is good;)!

  

----------

**Important**: for the rest of this lesson, you'll be writing a few more tests. You can either **comment out old tests/imports/exports** and start fresh for each test, or be clever and use classes and methods ;)

----------

  

Try to write another function in `code.js` called `calculateHyp`

-   The function should receive two numbers
-   It should return the square root of the sum of the numbers' squares - a la [Pythagoreas](https://en.wikipedia.org/wiki/Pythagorean_theorem)
-   You should use `Math.sqrt` to calculate the square root

  

If you've forgotten your favorite theorem, it's: `a^2 + b^2 = c^2`

  

Then, in `code.test.js`, write a test that makes sure `calculateHyp` works as expected.

  

You can use the values `3`, `4`, and `5` to validate that it worked: `3^2 + 4^2 = 5^2` - don't forget your export/import!

  

Check out the solution [here](https://codepen.io/ElevationPen/pen/dEVBGY?editors=0010).