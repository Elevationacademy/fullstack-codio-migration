
Here are some guidelines to help you out:

  

-   When the user clicks on a letter, (which is being rendered by the `Letter` component) it should **invoke a** **selectLetter** **method in** **App**
-   The method should update the `letterStatus state` 
-   The only thing that should change is _that_ letter's status: it should become true instead of false


Here an internal method of `Letter` is invoking `App`'s `selectLetter` method - this gives us a lot more flexibility if we wanted to do other things before invocation (like maybe check if the user finished the game?)

  

Once you've gotten to this point, you should see this when starting the game:

  

![](.guides/img/toDo-2.png)


Now click a letter, say J - it changed! Look at its class now next to the others:

  

![](.guides/img/toDo-3.png)


Here the styling is simple, text-decoration: line-through - but you could do a lot more.

  

Now for the big finale, what happens when you click on one of the letters in the secret word?

  

![](.guides/img/toDo-4.png)


  

  

Ba-bam, they appear in the `Solution` section, _exactly_ where we want them to.