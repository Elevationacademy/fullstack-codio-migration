As coders, we have hundreds of files, full of thousands of lines of code in extremely complex folder systems. We are constantly going into these files and making changes, usually improving the code. But we need some way to keep track of it! With complex code, it's not enough to simply have a saved file on your computer. You need to know what was worked on when, be able to differentiate work on one feature from another feature, work with coworkers, and so on.

  

What do you do if you want to undo something you did in those files and folders? Or maybe you want to create two versions of the same feature for [A/B testing](https://vwo.com/ab-testing/). Or perhaps you are in a team that is simultaneously working on an app and you want to monitor everyone's changes, making sure they don't conflict with someone else’s changes.

  

All of these situations can get tricky, but luckily for us, some really smart people created "version control". This makes your life as a developer much more manageable!

  

----------

  

### _What is Version Control?_

Version Control does exactly what it sounds like: it allows us to keep control of different “versions” of code and projects. There are different tools to assist with version control, we'll use **Git** as it is the most popular and best suited to your needs. Git keeps track of changes to your files and it provides mechanisms for sharing that content with others. Sounds great, so how will we use it?

  

**Git** is software that we'll install on our computers (aka we'll be installing it locally). Once installed we can start to use it for local version control ("local" meaning for the files on your computer). Local Version control will track the changes you make on your computer. But that's just half the story. We'll need somewhere to share the code so that many people can work on it at the same time.

  

Along with the local software, we'll use remote hosting site called [Github](https://github.com/) to help us in all our version control endeavors. It provides online storage for your files and it is based on Git so transferring files from your local Git repository to your remote repository on GitHub, or vice versa is really easy. Try not to confuse Git and Github.

  

-   **Git** is a free and open-source version control system. It exists on your computer (once you add it) and is primarily operated via the command-line.
-   **Github** is a company that provides a service. They use Git to provide cloud-based version control. More than that, they are a community that provides a bunch of useful tools and mechanisms to aid development work.

  

And if you were wondering, [alternatives](https://blog.idrsolutions.com/2014/03/top-5-free-hosted-version-control-sites-compared/) to Github do exist, but remember Github is used more than almost all of them.

  

You'll hear the word **repository** ("repo" for short) used a lot. When using Git/Gihub each project, is kept in a "repository". A repository is simply the directory or storage space where your projects live for version control purposes.


