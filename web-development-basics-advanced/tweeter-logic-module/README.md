# Intro

It's time to put what we've learned about closures and modularization to practice. We'll do so by creating our own Tweeter. It is not at all related to the somewhat more popular Twitter, though its basic functionalities will be similar.

  

Eventually, our Tweeter will look like this:

  

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/tweeter-final.PNG)

  

But for now we're only going to implement the data related parts that will be the 'engine' powering this multi-million dollar project.

  

Go ahead and **create a tweeter folder** - you can start by creating a repository on Github, or by doing it locally and then pushing later. Up to you. It should end up on GitHub eventually, though.

  

  

----------

  

  

#### **MODULES IN ACTION**

  

  

We learned about modularization, but it'll only be clear once we start to talk about applications on a higher level.

  

So - what are the components, the building blocks, the _modules_ of Tweeter?

  

-   The module that manages our posts logic
-   Storing all our twits (not the same as tweets)
-   Posting a twit
-   Commenting on twits
-   Removing twits
-   Removing comments
-   A module that manages our **rendering** - displaying things on the page
-   Creating HTML for a twit dynamically
-   Creating HTML for comments dynamically
-   Rendering all our twits and their comments
-   Something that glues both of the above

  

For now, we're only going to deal with the first part - our core _twits_ operations - so we're going to create a Tweeter module.

  

We'll learn about MVC soon, but know that this module is the **Model** in our **M**VC architecture - the part that is responsible for our data.

  

Because we want to keep our modules separate, we're literally going to separate them into different files.

As such, go ahead and **create a** **model.js** **file** - this is where our Tweeter module will be. Add this file to your **tweeter** folder.