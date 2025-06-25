
You've got a basic game setup, now it's time to take it all the way to being production-ready.

  

----------

  

**Extension 1**

  

You should make sure that players are not moving `out of bounds` - i.e., if a player tries to move left when they're already on the left-most column of the matrix, your logic should prevent that.

  

----------

  

**Extension 2**

  

Add obstacles to your board. Specifically, you should randomly generate some walls (similar to how you generated the coins).

  

A player may not move through these walls, and coins may not appear on these walls (but they can, in theory, be trapped in between them).

  

----------

  

**Extension 3**

  

Make your game more dynamic. Instead of always being **5x5**, allow the user to input the dimensions they want to play in.

Given this change, you will need some form of `Start` button that initializes the game based on the desired dimensions.

  

----------

  

**Extension 4**

  

Add an ending to your game. For simplicity's sake (because coins can become trapped within walls for now), your game should end when a player reaches some arbitrary score.

  

----------

  

**Extension 5**

  

This one is tricky: add some validation to your wall generation that makes sure walls aren't totally blocking a coin/a path to the other side of the board.