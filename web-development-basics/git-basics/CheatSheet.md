# Cheat Sheet

**Create git repo Flow**

  

Create empty directory: `mkdir <name>`
Navigate to directory: `cd <path>`
Create a git repo in the current folder: `git init`
Add a remote repository called origin with a link to your github repo: `git remote add origin <link to remote repo>`

  

----------

  

**Git Commit and Push**

  

First we have to add: `git add .`
Commit: `git commit –m "this is my commit message"`
Git pull: `git pull origin master`
Git push: `git push origin master`

----------

**Basic Commands**

  

Working directory status: `git status`
See list of commits: `git log`

  

----------

**Undo**

  

Revert unstaged changes: `git checkout -- <file name>`
Revert staged changes: `git reset -- <file name>`
Revert last commit: `git revert HEAD --no–edit`
