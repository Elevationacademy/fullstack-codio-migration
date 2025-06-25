
Now that you're each done with your respective parts of the project, we'll begin the **merging** process. Unlike when working solo, you won't simply merge back into master. Since you're on a team, **your code needs to be reviewed**!

  

This is where **pull requests** come in. Bitucket defines them as so:

  

> _In their simplest form, pull requests are a mechanism for a developer to notify team members that they have completed a feature. Once their feature branch is ready, the developer files a pull request. This lets everybody involved know that they need to review the code and merge it into the master branch._

>_But, the pull request is more than just a notification—it’s a dedicated forum for discussing the proposed feature. If there are any problems with the changes, teammates can post feedback in the pull request and even tweak the feature by pushing follow-up commits. All of this activity is tracked directly inside of the pull request._

  

So when git see's another branch is ahead of `master`, meaning it has new commits not merged into master, you can make a pull request.

-   This will notify your collaborators that your feature is finished and ready for review
-   It will show them the changes you made, and allow them to comment on the changes
-   When the changes are approved, github will allow you to merge the changes into `master`
-   If there are any conflicts in the merge* it will take you to an interface to determine which changes to take, and commit them
-   It will additionally prompt you to delete your branch, which you should do if you no longer need the branch

*For instance, someone edited master in the same place you made changes in your branch

  

Great words. Let's put it to practice.