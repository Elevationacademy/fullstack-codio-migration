
Bitbucket says: _"Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes. This makes it harder for unstable code to get merged into the main code base"_

  

So, when we want to create a new feature, we **branch out**: create a new branch (a snapshot of where the project currently is) and I start working from there.

  

We continue working and commiting as normal _to that branch_.

  

Finally, when we're done working on the new feature, we **merge**: bring all the changes from the feature branch back into our `master` branch. `Master` then moves forward, one completed feature at a time.

  

![](https://www.atlassian.com/dam/jcr:4cd777cc-24d1-4502-b8a9-8646b15c2d6b/08.svg)

  

Here, each circle represents another commit. We see a new branch "Some Feature", that is created and has a couple commits. It's changes are then merged back into master, in a new commit.

  

Note that **all the work done on feature branches is invisible to our users** - they will only ever see what is in the `master` branch.
