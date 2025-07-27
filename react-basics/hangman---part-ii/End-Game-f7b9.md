
Once you've completed the previous steps, you should **add an End Game** functionality.

  

You should do this by creating a new component called `EndGame`, which should be displayed when the game is over.

  

The game is over when either:

-   The user guesses the word*
-   Or, the score has reached 0 or below

###### *Since you're keeping track of all the secret words' letters in `letterStatus`, you can validate that the game has ended by checking that all those letters have a status of true

  

If the user guessed the word, you should display a "Congratulations" message.

  

Otherwise, you should display a message that reveals the secret word.