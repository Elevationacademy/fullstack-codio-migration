
There is a concept in the tech world known as TDD - Test Driven Development.

  

This is a principle that states that to improve the chances of our writing good code, and to keep our code safe, **we should write tests before we write code**.

  

Take this example: say we've received an assignment from our Dev Lead to write a method called `manipulate` in our `ArrayManipulator` class.

-   The method should receive two arrays of strings
    -   If the arrays are not the same length, the method should return a message saying so
-   The method should use the two arrays to create a single object
-   The object's keys and values should be based off the values in the first and second array
-   The method should return this object

  

For instance, if we receive these arrays:

```
let x = ["food", "item", "location"]
let y = ["cherry", "lightbulb", "Tazmania"]
```
  

We should receive this object:

```
{
  food: "cherry",
  item: "lightbulb",
  location: "Tazmania"
}
```
  

So TDD says: **write these tests first**, then use the tests to assist you in writing the code.

  

How would these tests look? **Try to write the tests now - not the code**. Remember, there's a test for the normal case, and a test for when the array lengths don't match.

  

**Hint:** you should use [toEqual](https://jestjs.io/docs/en/expect#toequalvalue) to compare objects.

Check out how to do it [here](https://codepen.io/ElevationPen/pen/PvJraE?editors=0010).

  

----------

  

Once we have our test - _then_ we can start writing code - and we'll know we're done once the tests pass!

  

So, does this method do the job? Let the test help you figure that out - read the output carefully!

  
```
class ArrayManipulator {
    manipulate(arr1, arr2) {
        let obj = {}
        for (let i in arr1) {
            obj[i] = arr2[i]
        }
        return obj
    }
}

module.exports = ArrayManipulator
```