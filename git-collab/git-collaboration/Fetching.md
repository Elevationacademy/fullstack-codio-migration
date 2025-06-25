
Now we're presented with a new scenario - the `master` branch is ahead of Partner A's branch.

  

Or at least our _remote_ `master` branch is.

  

Remember, `origin master` is a different branch than our local `master` branch.

When we `git push origin master`, we are pushing our _local_ changes to the _remote_ branch.

  

So, even though we merged the changes from Partner B into `origin master`, Partner A cannot see them on his or her computer. This is where fetching and pulling come in.

  

Basically, **fetching is a process that downloads all the data on a branch or branches onto your local environment**. It does **not** do anything with that data - only downloads it and makes it available to you.

  

**Both partner A and partner B run** **`git branch -a`** in your terminal.

  

This will show you a list of branches, both local and remote. You should see a list that includes your branch and `master`, as well as each branch with `origin` in front of it, the remotes of your branches, but **your partner's branch is missing**.

  

This is because your partner communicated with the _remote_ repository, but you never downloaded their changes. To have your partner's branch available to you, **both partners run** **`git fetch origin`**.

  

**Now run** **`git branch -a`** and you should see the remote of your partner's branch. You don't have a local version because you have not checked out their branch yet, but the information is there and you have access to it.