
Often times we find ourselves looking for things in arrays. Maybe it's an array of objects, each of which has an ID, and we need to find something by that ID:

  
```js
let posts = [
    {
        id: 0, text: "I'm not here",
        comments: [{ id: 0, text: "support that" }]
    },
    {
        id: 1, text: "Find me",
        comments: [
            { id: 0, text: "here I am" },
            { id: 1, text: "rock you like a hurricane" },
            { id: 2, text: "dum dum" }]
    },
    {
        id: 2, text: "Where's waldo anyway",
        comments: [
            { id: 0, text: "who's waldo" },
            { id: 1, text: "he's called Effi" }]
    },
    {
        id: 3, text: "Poof",
        comments: [{ id: 0, text: "like magic" }]
    }
]
```
  

To find a post, we might do something like this:

```js
const findById = function (id) {
    for (let post of posts) {
        if (post.id == id) {
            return post
        }
    }
}
```
  

With the `find` method, you can bet it's much shorter:

```js
const findById = id => posts.find(p => p.id === id)
console.log(findById(1)) // prints {id: 1, text: "Find me", comments: Array(3)}
```
  

This may seem like a lot of symbols, but all we've done is:

  

-   Define a function called `findById` just like before
-   We use arrow syntax to have the function receive one parameter, `id`
-   The function returns ( `=>` ) whatever posts.find(...) returns
-   The `find` method receives an anonymous callback
-   The callback iterates over every post, `p`, and finds the one who's ID matches the given `id`

  

Again, like in filter, we need to return some boolean. **The** **`find`** **method will find the first item in the array that matches the filter provided, and return that one item**.

  

----------

  

**Spot check:** write a `findCommentByID(postID, commentID)` function that finds a comment object. You should use the `.find` - certainly do **not** use a for loop.

  

If you do it right, then invoking `findCommentByID(1, 0)` should return `{id: 0, text: "here I am"}`
Check out the solution [here](https://codepen.io/ElevationPen/pen/gNYopd?editors=0010)
