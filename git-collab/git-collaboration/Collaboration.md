
The principle of opening a new branch for each new feature in a project extends to git collaboration. So when Cindy and John start working on the landing page, the **first thing they'll do is break off into <ins>separate</ins> branches**.

  

It's recommended that you separate work based on sections of a project - e.g. Cindy works on the server and John works on the client of the landing page. There is inevitably overlap that comes from this, and that leads to merge issues. When collaborating, you'll merge back into master through the pull request system - allowing you to review each other changes before merging, making sure you keep communication through your project

  

Let's explore how this actually happens:

  

----------

  

#### **ADDING A COLLABORATOR**

  

A github repository will only have **one location**. If you're working in a company, this will be on the company's github. If you're making your own repository and working on it with colleagues, then you'll have to open it on your github and add them as collaborators.

  

For this example, we're going to **work in partners**. So pick a "driver", partner A, and a "shotgun", partner B (you'll switch rolls later on.)

  

Let's go to github now. **Partner A, create a new repository** called `git-collaboration`

  

Still Partner A, **create a local repo** with a `dist` folder and an `index.html` file inside it.

**Add in some boiler plate, add, commit, and push to** **`origin master`**

  

Now we want to bring Partner B in, but first we need to add them as a **collaborator**.

  

For that, **Partner A:**

-   Go to your repo on github
-   Go to the settings tab in the top right corner
-   Click on the second item in the navbar, "Manage Access"
-   Put in your partners github user name or email address

And now they're added as a collaborator! Make sure to **give them write or admin access** to the repo.

  

**Partner B**, you should have received an email form Github informing you that you've been added as a collaborator to Partner A's repo. Follow the link to the repo.

  

Now **partner B,** **`clone`** the repository. **Do not fork it!** This is an important distinction.

  

We said that a repo only has one place on Github, but **when you fork a repo, it makes a _copy_** of the repository that now exists on _your_ Github which is **not** connected to the original repo.

  

When you're collaborating you just `clone` the repo to make direct changes to it when you push.