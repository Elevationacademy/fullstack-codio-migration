
So far our work with git has been pretty plain:

  

```bash
git add .
git commit -m "great code"
git push origin master
```
  

The major downside here is that any code we `push` goes directly to `master` - i.e. directly to our users, and _everyone_ working on this project is pushing directly to `master`

  

If something goes wrong, it would be hard to tell where it originated since everyone is just pushing everything to `master`!

Branching allows us to **separate our work**.

  

We separate our work so that we can have our clean code, ready if needed in our `master` branch and we **branch out** for each new **feature** or bug that we work on.

  

A **feature** is any new "thing" we add to our app, like the ability to save a user, an API request, some design changes, etc.

  

Once our work on the feature branch is complete, we `merge` our work back into the `master` branch. This allows us to keep our work separate, but allow us to work in parallel on multiple different features at the same time - essential for working in a team.
