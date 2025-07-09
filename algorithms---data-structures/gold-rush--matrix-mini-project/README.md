# Intro & Setup

![](https://s3-us-west-2.amazonaws.com/learn-app/lesson-images/dsa/gold-rush-logo.PNG)

  

#### **INTRO**

Though there are many usecases for matrices (data science, image processsing, graphics, etc) - games are some of the most fun you can have with a Matrix.

In this mini project you will create a game whose entire logic is based on a 2D array (a matrix), and then use your HTML/CSS know-how to make the game playable in the browser.

  

----------

  

#### **SETUP**

  

You'll be creating this project a-la MVC, so go ahead and create the following files:

-   `Matrix.js` - a file to hold your base `Matrix` data structure
    -   Feel free to use a class you've already written in the past
-   `GoldRush.js` - here you'll create your new matrix, it should `extend` from `Matrix`
-   `Renderer.js` - this will have your `Renderer` class with at least one method: `renderBoard`
    -   The `renderBoard` method should receive a matrix, and display it on the screen
-   `main.js` - your controller file: this will load the initial game and react to user input


Then, of course, you'll have your HTML, CSS files, and if you would like to take this up to the cloud, a `server.js` file etc.

  

----------

  

#### **REQUIREMENTS**

  

In this game there should be two players.

  

Player 1 will control their player using the **WASD** keys, and Player 2 should use the **IJKL** keys.

  

A player may not move to a location on the board that has a wall or another player, but they should get 10 points any time they move to a location with a coin on it. In this case, the coin should disappear from the board.