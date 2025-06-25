
Fetching only downloads the data for us, but it doesn't do anything with that data.

  

Git gives us another command called `pull` which essentially fetches the data from our remote, and then merges it into our branch.

  

We always want our branches to be following along with the `master` branch. You may work on a feature for a week, and in that time 5 other features may have been merged into the master branch. To avoid as many conflicts as possible you want your branch to stay up to date with all the changes that are being merged into your master branch. So on a regular basis, you'll run `git pull origin master` quite often.

  

`git pull origin master` downloads the data from repo's remote master branch, where all changes are being merged, and then merges the changes into the local branch you're currently working on.

  

Since you should review the changes made **before** you merge them into your working branch, you're going to checkout `master` and pull from `origin master` into `master`. Then, after review, you'll checkout your feature branch, and `merge master` into it.

  

So, **partner A,** **`checkout`** **your** **`master`** **branch and run** **`git pull origin master`** **now and review the new changes. Then,** **`checkout`** **your** **`front-end`** **branch and run** **`git merge master`**  . There should be no merge conflicts, and you should now have an updated local `master` branch with partner Bs changes, _and_ have those changes in your `front-end` branch.

  

----------

  

#### **ANOTHER PULL REQUEST**

  

Now that you're all up to date **Partner A, it's your turn to make a pull request**. Make sure you commit and git `push origin front-end`

  

Follow the instructions above, go to your github repo and open a pull request.

  

**Partner B, this time you approve the pull request and merge in the results**. Maybe add in a comment on partner A's changes in the pull request interface while you're at it.