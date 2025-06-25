<span/>
When working with Github they will need to authenticate your credentials, meaning they will need to make sure you are the owner of the account, or have the appropriate permissions. By default you will be asked to login, putting you username and password. 

**With SSH key you can connect to GitHub without giving your username and password each time.**


|||info
Read more about it [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh)

|||
## How is it working? 

First, we will generate an ssh key.

cd to your ssh folder:

```bash
$ cd ~/.ssh/ 
```

Generate a new ssh key:
```bash
$ ssh-keygen -t ed25519 -C "your_email@example.com" 
```

* Make sure to change your_email@example.com to your actual email address.
* you can press ENTER for all the questions presented to you, leaving an empty password.

Now, let's make sure it worked.
Print the new SSH key to the console. It should be stored in a file called `id_ed25519.pub`

You can `ls` to see which files exist in the folder.

Now, let's print the content of the file, which is your public key:
```bash
$ cat id_ed25519.pub 
```

You should get something like:
```
ssh-ed25519 AAAAV3VzaC1lZDI1NTE5AAAAIDu5rqczhUykMnrZHg075YUryUwk0sUJN/gGJSfVA6Gy lotem.@gmail.com
```

where `lotem.@gmail.com` is your email.

You can also use the cmd command
```bash
$ pbcopy < ~/.ssh/id_ed25519.pub
```

Now copy the content and let's add it to your github account!

**You can also follow github's instructions [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account)**

1. In the upper-right corner of any page, click your profile photo, then click Settings.

2. In the "Access" section of the sidebar, click  SSH and GPG keys.

3. Click New SSH key or Add SSH key.

4. In the "Title" field, add a descriptive label for the new key. For example, if you're using a personal Mac, you might call this key "Personal MacBook Air".

5. Paste your key into the "Key" field.


6. Click Add SSH key.


7. If prompted, confirm your GitHub password.

Now, let's make sure it works!
In your cmd type:
```bash
$ ssh -T git@github.com
```

you should get a message:
```bash
"Hi <username>! You've successfully authenticated, but GitHub does not provide shell access."
```

And that's it!