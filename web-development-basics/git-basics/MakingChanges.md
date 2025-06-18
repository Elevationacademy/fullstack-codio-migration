# Making Changes

OK, nothing exciting so far. Let's make things more interesting by changing your code.

  

Change the line in your hello.txt to: "hello again"

So your `hello.txt` should now be:

```bash
hello again
```
  

Now if you type:

```bash
git status
```
  

...in your command-line, you will see that Git has noticed there have been changes. To see these changes type:

  

```bash
git diff
```
  
![.guides/img/PROD_A567-0](.\img\PROD_A567-0.png)



  

You can see what was "deleted" and what was added. To exit this screen type **q** (short for quit, or **shift**+ **q**)

Remember in order to commit changes you first need to "stage" them. Let's do that by typing:

  

```bash
git add hello.txt
```
  

Then, if you want, you can check the status again:

  

```bash
git status
```
  

Then finally do a commit:

  

```bash
git commit -m "changed greeting"
  ```

And push again!
  

```bash
git push origin master
```
  

Check Github... Awesome!