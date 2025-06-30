# Going Backwards

You may find yourself wanting to undo your code changes and commits - how do you do that?

  

The way to revert your code back to a previous version depends if you have already pushed to github or not.

  

To be honest you should only push code that you are 100% happy with so ideally you'll never want to revert your pushed code - but we'll talk you through both scenarios.

  

----------

  

## **1) IF YOU DIDN'T PUSH TO GITHUB**

  

If you haven't pushed to github and didn't like the last `commit` (or even the last `add`) you made you can just reset it!

  

We just did a push, so to make this scenario work make some new changes to your code, `add` them, `commit` them (it's good practice!). But now you are going to change your mind (before you push). How do you un-commit and un-stage (reverse the add)?

  

You'll need the SHA hash of the commit that you want to get back to. Remember you can use `git log` to find that.

  

Run the below command, where `YOUR_SHA_HASH` is the hash of **the commit you want to go back to** (that'll be the commit where you wrote "add title").

  
```bash
git reset YOUR_SHA_HASH
```
  

Notice though that the `reset` didn't actually change your code. Try a `git status` and you'll see it's only "uncommitted" and "unstaged" it. Any unwanted changes to your code will still be there.

So two questions: 1) why reset? and 2) how do you reset the code?

  

1) Maybe you committed but forgot to stage a new file or forgot some important changes. It's nice to have a "clean" commit history - where every commit "makes sense" - and `reset` gives you this ability.

  

2) To both blow away the last commit and reset your code back to the way it was, you would type in the same thing, but with a **--hard** flag, like this:

  

```bash
git reset --hard YOUR_SHA_HASH
```
  

Try this and notice your code now changes back. Use this with caution as you've now lost those changes.

  

Lastly, just for your information: there is a final option, `reset --soft` - this only un-commits. It doesn't un-stage. Fun!

[More about reset/soft/hard](https://git-scm.com/docs/git-reset)

  

## **2) IF YOU HAVE PUSHED TO GITHUB**

  

Ideally, you'll never find yourself in this situation. But, if you do then there are at least 2 ways to deal with it:

  

1.  Do a hard reset (as above) and then do a **forced** push: `git push -f origin master`
2.  Revert the commit and re-commit and push again

  

The first option whilst valid is a bit "dodgy" as a forced push will change your github repo's history. This is OK if you are the only person using the github repo. But, if other people have been using it you may find yourself in muddy waters.

  

The second option is far safer and not too difficult to achieve. To revert the last commit, use the command:

  

```bash
git revert HEAD -n
```
  

This reverts the changes that were specified by the last commit (aka "the HEAD" commit).

The `-n` flag stops Git from automatically recommitting the change - if you don't want to make any further changes before committing then you can leave it out.

The code will change back.

If you used `-n` you are now free to make continue making changes before doing an `add`, `commit` and `push`. If you didn't use `-n` then you can simply do a `push`.

  

You can also read about [revert](https://www.atlassian.com/git/tutorials/undoing-changes#git-revert) and [reset](https://www.atlassian.com/git/tutorials/undoing-changes#git-reset) by following the links provided. In general, [atlassian.com](https://www.atlassian.com/git/tutorials/) is an excellent resource for using Git. Feel free to read it in your spare time so you can become a Git Jedi!