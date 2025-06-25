
Remember the command to push code to github, `git push origin master`?

  

What this command is actually saying is _push my changes to origin, my remote github,_ **_on the master branch_**_._

  

You can push _any_ branch, however, such as `new-feature`.

So if we're working on our `new-feature` branch, we would work as we've previously done - `git add`, `git commit`, `git push origin` **`new-feature`**.

  

Let's do this! **Run** **`git push origin new-feature`** (after add and commit).

Look at the bottom of the push message - * `[new branch] new-feature -> new-feature`

  

You've just made a new _remote_ branch - i.e this branch now also exists in Github!

  

Now **go to the repository in github**.

You'll notice on the top left corner of the repository there is a drop down menu called **branches**.

  

Your new-feature branch is there! Select it and you'll see the files you pushed to `new-feature`

  

Go back to `master` and those files will disappear. This is because those changes are only committed to a specific branch, the branch of your new feature. Amazing.
