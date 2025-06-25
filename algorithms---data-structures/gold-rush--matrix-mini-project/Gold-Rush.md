
You're on your own for this project, but here are some suggestions to make your work more organized:

-   Start by creating a fixed **5x5 board**
-   This board should display Player 1 on the top left corner, and Player 2 on the bottom right corner
-   You should write some methods that, when invoked, will alter the player in that direction

  

You should start your work **only in the console**, like this:

```
const board = new GoldRush()
board.print() //the print method should be defined inside of Matrix
//prints
1       .       .       .       .
.       .       .       .       .
.       .       .       .       .
.       .       .       .       .
.       .       .       .       2

board.movePlayer(1, "down") //this method should be defined inside of GoldRush
board.print()
//prints
.       .       .       .       .
1       .       .       .       .
.       .       .       .       .
.       .       .       .       .
.       .       .       .       2

board.movePlayer(2, "left")
board.print()
//prints
.       .       .       .       .
1       .       .       .       .
.       .       .       .       .
.       .       .       .       .
.       .       .       2       .

```

  

Once that is set up, you should generate a few coins when you generate the board.

-   Again, for starters you can start with a fixed number of coins
-   You should add the coins on random locations in the matrix
-   However, make sure you're not adding them on a player or another coin

  

Now when you load your board, it could look like this:


```
const board = new GoldRush()
board.print() 
//prints
1       .       c       .       .
.       .       .       .       .
.       .       c       c       .
.       .       .       c       .
.       c       .       c       2
```


Of course, the numbers and `c`s are merely representational. Eventually when we display this on the browser we will render something prettier.

  

But the point is this: **our entire game's logic will be inside of this** **`GoldRush`** **class**, and then the only thing that `Renderer` needs to do is to render the `board`'s matrix after each move.

  

----------

  

Once you're generating coins, add some code that increases a player's score each time they move onto a coin.

  

If you're testing along, you should be seeing something like this:


```
const board = new GoldRush()
console.log(board.player1.score) //prints 0
board.print() 
1       .       .       c       .
.       .       .       .       c
c       .       .       c       .
.       c       .       .       .
c       .       .       .       2

board.movePlayer(1, "down")
console.log(board.player1.score) //prints 0
board.print()
.       .       .       c       .
1       .       .       .       c
c       .       .       c       .
.       c       .       .       .
c       .       .       .       2

board.movePlayer(1, "down")
console.log(board.player1.score) //prints 10
board.print()
.       .       .       c       .
.       .       .       .       c
1       .       .       c       .
.       c       .       .       .
c       .       .       .       2

board.movePlayer(1, "down")
console.log(board.player1.score) //prints 10
board.print()
.       .       .       c       .
.       .       .       .       c
.       .       .       c       .
1       c       .       .       .
c       .       .       .       2﻿
```

  

#### **RENDERING**

  

Now you've got something of a game - so go ahead and **start rendering** on the browser - remember, the _only_thing you should render inside of `renderBoard` is the entire matrix. There should be no logic in the `Renderer` class.

  

You should, of course, have a separate `renderScores` method that renders the players' scores.

  

----------

  

#### **CONTROLLER**

  

Once you've got something rendererd that looks reasonable, you're going to translate key-presses into function calls.

  

In other words, when the key `W` is pressed on the keyboard, it should invoke `movePlayer(1, "up")` as we saw earlier.

  

If you're using jQuery, that could look like this:

```
$(document).keypress(function (e) {

      if (e.which == 119) {
            board.movePlayer(1, "up")
      }

}
```

  

Notice that `119` is the number that represents the letter `W` - you can figure out which other numbers you need by pressing them and printing out the value of `e.which` each time.

  

Remember, your controller is the main manager of everything, so the above code (and the code that initializes the initial board) should be in your `main.js`