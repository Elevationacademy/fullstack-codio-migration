
There are five commands we need to know in order to use git branching on a **solo** project:

-   `git branch`
-   `git checkout -b branch-name`
-   `git push origin branch-name_`
-   `git checkout branch-name`
-   `git merge branch-name`

  

Let's practice these.

  

**Open up a new repository**, and `git init` in it. Now run `git status`.

Notice what the message says - `On branch master` - so we are currently on our main project code branch.

  

Now let's add some boiler plate to our project. Go ahead and make a `server.js` file, install express, and write in some server boilerplate. Once that's ready, **commit your project** (add then commit.)

  

Now that we have a root commit (first commit of the branch) let's run `git branch`

The **`git branch`** **command lists the branches in our project, and the branch we are currently on**. Since we only have one branch, the list should only consist of `master`

  

As we've done before, **open a new repo on github and link it to your local directory**.

Go ahead and **push your code** to this repo.

  

Now we want to create a new feature, so we're going to create a new branch.

  

**Run** **`git checkout -b new-feature`**

  

Let's break this down:

-   `git` - you know this
-   `checkout` - this is the word that means to go into a different branch. You `checkout` the branch you want to see. Think of it like "check-it-out". You want to go to a new branch? Go check(it)out!
-   `-b` - this means "new", a new branch
-   `new-feature` - this is the name of the new branch. Since you generally branch out for a new feature or bug fix, the branch name should be self descriptive
-   _Note: branch names cannot have a space in them and are case sensitive_
-   Generally, a branch would be named something like `bug-fix/db-save` or `feature/handle-multiple-users`
-   Of course, the naming conventions will depend on the team you work with

  

**Run** **`git branch`** **again**. Notice there are two branches now listed, `master` and `new-feature`, and we are in `new-feature`

  

Our new branch, so far, is exactly the same as our previous. **When we make a new branch, it starts as a snapshot of the branch we came from**, i.e. "branched out" from.

  

Visually, we could think of it like this, where each circle is another commit (assume we had other commits in our `master` branch):

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/create-new-branch.PNG)

  

Notice that and `master` (representative names) are at exactly the same place.

  

Now let's **add a** **`dist`** **folder to your project**, and put in it an `index.html`, `style.css` and a `main.js` in it, and add some boilerplate to your `index.html` file.

  

Again, **commit your changes** - notice when you commit, it tells you which branch you're commiting to.

  

Now we can visualize our branch state like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/git/new-breanch-commit.PNG)

  

Now, before we do anything else, let's **run** **`git checkout master`** and checkout master again.

  

Go back into your project folder and **go to your** **`index.html`** **file.**

  

***gasp!* It's not there!**

  

This is because the changes you made were committed to your _feature branch_ - notice in the above image that the latest `feature` commit is **ahead** of the latest `master` one - they're different!

  

Your **branches are like separate work stations**, they now hold **different code** in them. What you did in your `new-feature` branch does not affect your master branch, and visa-versa. If we **now run** **`git checkout new-feature`**. You'll notice your changes have come back.

  

**Important!** You must commit* your changes before checking out to a **new** branch!

###### *or stash, which we won't talk about right now
