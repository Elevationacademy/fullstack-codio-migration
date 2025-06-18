# Tracking Files

Now we need some files in the repository.

Let's add one.
  

Create a file in the directory named git-practice

You can do it in the cmd or create the file in your file system, text editor, idea...

  
Here is how you create a file in the cmd:

```bash
 touch hello.txt 
```
  
Let’s add some content to the file:

```bash
echo "Hello World" >> hello.txt
```
  
Alternatively, open the file in a text editor and add the line "Hello world".

  
Now try this command:

```bash
git status
```
  
This command is used to see the current status of your git repository. In other words it will tell you what files you're tracking and if those files have changed.
  

We're not tracking anything yet so you should see a message like this:
  

![.guides/img/PROD_A2401-0](.\img\PROD_A2401-0.png)

  

And let's add another file called file2.txt

```bash
touch file2.txt
```
  
And again, type :

```bash
git status
```
  
You'll see now the other file file2.txt is also untracked:

  

![.guides/img/PROD_A2401-1](.\img\PROD_A2401-1.png)


    

This tells us that we have two "untracked files". In other words, Git knows these files exist but it is currently not looking for any changes within them. We need to tell git to follow the changes we made in these files, meaning we need to manually add the files in order to track them. To do that we can add them one by one like this:
```bash
git add hello.txt
git add file2.txt
```
 
Or, if we want to add all untracked files at once, we can use:

```bash
git add .
```
    

Now, if we again check the status of our repository by typing:

```bash
git status
```
  
You'll now see that the two files that are ready to be "committed". In developer speak, we can say that the files are "staged".

  
![.guides/img/PROD_A2401-2](.\img\PROD_A2401-2.png)

   

You've just let Git know that you want these two files in their current state, to be "saved" in the version control history. Now, to actually do that "save" you need to do a "commit".

  

**Commit**

  
A "commit" is like a snapshot of our project. It is a record of what our files looked like at the time of the "commit". Run the following command to commit the two files.

  
```bash
git commit -m "Add some files"
  ```
  

![.guides/img/PROD_A2401-3](.\img\PROD_A2401-3.png)



You may be prompted to run commands which assign your name and email, go ahead and run these command to finish configuring git.

    

You'll notice we included a message (the string after the -m) flag. This message is saved alongside the commit and is used to record the status of our app when this "snapshot" was taken. The message content is up to you, but it's generally a good idea to use it to briefly describe the changes made between the current and last commits.

  
To look at a log (record) of our all our commits, type:

```bash
git log
```
  
![.guides/img/PROD_A2401-4](.\img\PROD_A2401-4.png)
    
Above we can see that we only have 1 commit. It's represented by a unique ID called a "SHA hash" (mine is ec272cf7fc230d27dca66b0232425fac1a68e7d6). Later, we'll use this ID to reference our commit.

  
Now when continue to work on our project, we'll be safe in the knowledge, that Git version control has a record of the project as it stands. Excellent!

  
While working as a developer you should be committing quite often. Think of version control like this: For each new feature of a project you work on, you may want to revisit those changes at some point in time, or track why those specific changes were made.

  
If you find your commit messages becoming too long and detailing too many changes you made, then you're not committing often enough, and vice-versa.

  
There's a sweet spot you'll find for how frequently you should commit, but to begin, we recommend more often rather than less.