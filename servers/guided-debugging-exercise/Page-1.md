### The Task
Here is some code that contains bugs.
Your task is to find these bugs and fix them.
Copy the code and run it in your computer so that you can debug.

### Hint
The debugger id your friend!

### Guidance
1. First take a minute to understand what the code is doing
1. Now find the bugs. Specifically try to find the row of where the bug happens
1. Fix the bug, so that the code works fine.

```js
const posts = [
    {
        id: 1,
        text: "Love this product",
        comments: []
    },
    {
        id: 2,
        text: "This is the worst. DON'T BUY!",
        comments: [
            { id: 1, text: "Idiot has no idea" },
            { id: 2, text: "Fool!" },
            { id: 3, text: "I agree!" }
        ]
    },
    {
        id: 3,
        text: "So glad I found this. Bought four already!",
        comments: []
    }
]

const removeComment = function (postId, commentId) {
    for (post in posts) {
        if (post.id === postId) {
            removeCommentFromPost(post, commentId);
        }
    }
}

const removeCommentFromPost = function(post, commentId){
    for (let i =0; i < comments.length; i++) {
        if (post.comments[i].id === commentId) {
            post.comments.remove(comment);
        }
    }
}

removeComment(2, 3)

```