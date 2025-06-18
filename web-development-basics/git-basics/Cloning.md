# Cloning

Click [this link](https://github.com/Elevationacademy/git-practice) to navigate to the repo. Click the button in the top right that says "fork"...

  

![.guides/img/PROD_A569-0](.\img\PROD_A569-0.png)


  

Then select your profile.

  
![.guides/img/PROD_A569-1](.\img\PROD_A569-1.png)


  

GitHub has now made a `copy` of our repository on you your profile.

Now click "Clone or download" and copy the URL that is displayed.

  

![.guides/img/github](.\img\github.jpg)

  

Now, open your terminal and navigate to wherever you're storing your code - for example `mycode/week1/day3`.

Type

```bash
 git clone <PasteURLHere> 
```
  

(of course you need to replace "PasteURLHere" with the URL you just copied):

  

For example:

  


![.guides/img/PROD_A569-2](.\img\PROD_A569-2.png)
  

Run the command (press enter). This will create a new folder on your computer. called `git-practice`.

`cd` into that folder like normal and open it in vsCode (or the editor of your choice) to start working with it!

  

**When you clone a github repo it will also set up a remote called "origin"** so there is no need to do the whole `git remote add origin ...` thing :-)

  

By the way, you do **not** always have to fork repositories. If you're working on an existing repository and contributing to it, it's enough to just **clone** it so you have local access to it. Then you make your changes, and push it back to the original repo.

  

Generally we will only fork repos if we want to create something entirely new _based off_ something that exists.