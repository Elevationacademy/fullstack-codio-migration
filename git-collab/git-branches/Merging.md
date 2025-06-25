
Let's go back to the local project on your computer.

  

**Add a "Hello World" to your HTML, and commit again.**

Now, let's say that we've finished development on our new feature.

  

Now that we're done with this feature, **run** **`git checkout master`**  to enter back into our master branch, our main code branch. Now we need to **merge** our feature branch into the `master` branch.

  

Our friends at Bit Bucket tell us: _The_ _`git merge`_ _command lets you take the independent lines of development created by git branch and integrate them into a single branch._

  

When you're done working on a feature branch, you `merge` your commits back into the `master` branch.

  

Merging happens on the branch _you are currently on_.

  

Because we are back in our master branch, we can **run** **`git merge new-feature`** merging our commits from new feature, into our master branch.

  

Visually, you can think of **merging** like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/merging.PNG)

  

Click [here](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/merging.PNG) to embiggen.

  

Check your code again, and you'll see your files and changes from the `new-feature` branch, all together in your `master` branch, completing our **branching workflow**:

-   Branch out
-   Develop feature in new branch
-   Merge changes back into `master`

  

This kind of merge is called a **fast forward merge**

  

**Note:** You only merged your changes into your master branch. This means that any more commits you make from this point forward on master **will not affect** your `new-feature` branch.

  

Good practice says that **you should delete a branch once its changes are merged** in and you are done with it. We'll talk about this more with git collaboration.