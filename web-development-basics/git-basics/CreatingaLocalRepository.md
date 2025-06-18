# Creating a Local Repository

A repository is where our code lives, both on our computer and on a host computer (we will use github later on).

  

We will start by creating the local repository, that is located on our computer.

Starting in a dedicated directory on your computer, create an empty directory named "git-practice" then

  
```bash
mkdir git-practice
cd git-practice
```
  

So we created a directory (not yet a repository) and navigated to it.

  

We need to make this folder a Git repository. Remember, as we said earlier, a repository is just a storage space where Git can keep track of all the files inside it. To turn the folder into a repository run the following command:

  

```bash
git init
```
  

You should see a message that says something like "Initialized empty Git repository in..."

  

![.guides/img/PROD_A2399-0](.\img\PROD_A2399-0.png)


  

Now we have a git repository.

An empty git repository :(

  

Remember, we only need to create the repository once.

Now we can add files, update them and update the remote repository.