
Now let's try this again, this time partner B and Partner A switch roles.

Partner B, you **open up a new repo on your github** this time, and add partner A as a collaborator.

  

But, **Partner A**, when it comes to your turn, you're also going to fill in some boilerplate on the `server.js` because you're impatient.

  

Follow along with the instructions like you did before, **but partner A do not run** **`git pull origin master`** **before you open your pull request this time.**

  

**Partner A**, when you get to your pull request, you'll notice that github says it _cannot automatically merge the changes_ this time. Like the message says, don't worry. You can still open the pull request. **So go ahead and make the pull request**

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/cantmerge.png)

---
  

This time you cannot merge your conflicts right away. **So partner A, you need to click resolve conflicts** to go and resolve your conflicts.

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/resolveConflicts.png)

---

The next screen you'll see is githubs conflict resolving screen. Whether you resolve conflicts on github or in your code editor, most of it looks the same:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/githubResolve.png)

---

For each conflict, you have:

-   The `<<<<<<< your-branch`, followed by the code from your branch
-   Then this: `==========`
-   And then the code that it conflicts with from the branch you are trying to merge into
-   This is followed by `>>>>>>>>>>>>> branch-you're-trying-to-merge-into`

  

In order to resolve the conflict, you simply need to delete all the lines that you do not want.

Since Partner A was impatient, **Partner A delete your lines that are conflicting and keep partner B's lines.**

  

When you're finished, delete the `<<<<<<<`, `=========`, and `>>>>>>>>>` lines. This will tell github you have finished the merge.

  

Now, **click the "resolve" button followed by the "commit merge" button.**You'll now be redirected back to your pull request, where **partner B can now go approve the changes, and merge your changes into the** **`master branch`**. Huzzah!

  

Remember to delete your branches, go back to your local master branch and `pull` from `origin master`.