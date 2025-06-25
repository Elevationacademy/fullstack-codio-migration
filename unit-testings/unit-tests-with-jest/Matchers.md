
The `expect` and `toBe` are great, and we also have other **matchers** we can use. You can check out [the full docs](https://jestjs.io/docs/en/expect) to see all of them, but let's go over a couple more now.

  

Say we had a class that had a method called `removeBug` that receives an array of code, and returns an array without any bugs:

```
const removeBugs = function (code) {
    return code.map(c => c != "BUG")
}
```
  

Though this is just one line of code (in the function) - it's quite easy to make mistakes with array methods. So we write this test to help us make sure we did it right:

```
const removeBugs = require('./code')

test("should remove all BUGs from list of code", () => {
    let code = ["great code", "good code", "BUG", "async await awesome code", "BUG", "BUG", "general code"]
    let bugFreeCode = removeBugs(code)
    expect(bugFreeCode).not.toContain("BUG")
})
```
  

There are two new things here:

-   `not` - this works similar to `!` in JS
-   The `.toContain` matcher that checks whether something exists in an array

  

So what we're saying above is that we **_expect_** _the array that the_ _`removeBugs`_ _function returns_ **_to not contain_** _any "BUG"_

  

If you run `npm test` with the above, your test will past because indeed, "BUG" is `not` inside of `bugFreeCode` - **however!**

  

If you're sharp, you'll notice we used `map` instead of `filter` in our method. So **even though our test passed, our code is still bad**- the `removeBugs` function actual returns an array of booleans!

  

To fix this, we should modify our test to look like this:

```
test("should remove all BUGs from list of code", () => {
    let code = ["great code", "good code", "BUG", "async await awesome code", "BUG", "BUG", "general code"]
    let bugFreeCode = removeBugs(code)
    
    expect(bugFreeCode).not.toContain("BUG")
    expect(bugFreeCode).toContain("good code") //this is just an example, there are other ways to check
})
```
  

Now we're checking two things: that we've removed all the "BUG"s, _and_ that we kept our good code - this is the importance of writing good tests; they check our code _thoroughly_.

  

Note that **there is no limit to how many** `expect`s **we can have** in a single test - but **all the expects must pass** for the test to pass.

Also note that **when writing tests, you're hard coding data on purpose so your test is as clear as possible**.

  

----------

  

Write a function/method called `clearLowPriority` that receives an array of objects. The objects have two keys:

-   `text` - a simple string
-   `priority` - a string that is either "HIGH" or "LOW"

  

The function should return a new array with only "HIGH" priority items.

  

Then write a test for this function. You should **expect** the `priority` **for each** item in the new array **to be** "HIGH". That's a hint.

  

If you need help, you can check out the solution [here](https://codepen.io/ElevationPen/pen/byoPWL?editors=0010) .

  

----------

  

There are, of course, many ways to test the exact same code. Here is another example:


```
test("should keep only HIGH priority tasks", () => {
    let tasks = [{ text: "dummy", priority: "HIGH" }, { text: "dummy", priority: "LOW" }]
    let filteredTasks = clearLowPriority(tasks)

    expect(filteredTasks.length).toBe(1)
    expect(filteredTasks[0].priority).toBe("HIGH")
})
```
  

The reason this is also an OK test is because _we the developer_ **know** that if our `clearLowPriority` function works correctly, then we _should_ only be left with `1` item in the `filteredTasks` array, and that the first item to should have a priority of "HIGH".

  

You can be very creative with your tests, **but you must consider as much as possible**. In the above, it would not be enough to _only_ test for the length to be `1` - but _both_ of those `expect`s together are a good indicator that our function is behaving appropriately.