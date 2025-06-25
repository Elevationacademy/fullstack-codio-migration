
The premise of the game is that there are some things on the screen - say frogs - and each time the user clicks one, it disappears. Simple enough.

  

But, when all the frogs disappear, the game goes to the next level - there should be _more_ frogs on the screen now.

  

To make it challenging, there's a timer! The user should only have a set amount of time for each level. You can use [setTimeout](https://www.w3schools.com/jsref/met_win_settimeout.asp) for that.

  

So without further ado, here are the instructions:

  

-   Start by creating a few simple `div`s on the screen
	-   Make sure you're generating these dynamically
-   Add a listener to the `div`s that removes them on click
	-   Can you think of a way to do this with MVC?
-   Start a timer
	-   If there are still boxes on the screen when the timer ends*, `alert` the user they lost
	-   Otherwise, add more `div`s to the screen
	-   There should be as many boxes as the level number (Level 1: 1 box, Level 2: 2 boxes, etc)
	-   Each level should add one more second to the timer

###### *Your logic does not have to flow like this. You could check the frog count after each click, or when the timer ends, or every second - you decide on your logic.

  

----------

  

This is the most basic version of the game. Once you're done with the basics, and only once you're done, here are features you should add to the game:

  

-   Use [font-awesome](https://fontawesome.com/) to show an icon instead of a `div`
-   Position each icon randomly instead of one after the other
-   Give each icon a random color
-   Start the game with a button instead of automatically
-   Show a countdown on the top of the screen
	-   Use [setInterval](https://www.w3schools.com/jsref/met_win_setinterval.asp) for that
-   Show the current level
-   Show an updated count of frogs left
-   Instead of alerting a loss, show a message in the middle of the screen
-   Flash the timer yellow each time a new level is reached
-   Flash the timer red when there are 3 or fewer seconds left
-   Change the text on the start button once the game begins
-   Change the size of the frogs depending on how high up they are
	-   Frogs closer to the top of the screen should be smaller
	-   This gives the illusion of depth

  

Note that these are _not_ extensions. These are features you should be able to implement. Just take your time.
