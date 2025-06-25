
It's time to complete Tweeter!

  

So far we have our module that handles the logic - adding/removing posts and comments.

  

And our rendering module which takes the data from the logic module and renders it.

Now we need to build the part that handles both of these. How do we add posts? When are comments created and removed? Who calls renderPosts?

  

All of these dynamic things happen as a result of user interaction! In our case, clicks.

This, finally, is the **Controller** in our MV**C** architecture - the part that deals with user input.