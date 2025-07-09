# Components Overview

Let's think about the components we'll need for our hangman game.

  

-   A component to show the remaining guesses
-   One to show the _ _ _ _ and fill up with letters
-   One for the letters we can choose

  

For now that should be enough.

  

Starting with the last one, we can break it down some more:

  

-   A component to hold all our letters
-   A component that represents a single letter

  

A component for a single letter may seem extreme. In fact, _how small should we make our components?_ is a popular question. Some will say _as small as possible_ - but that's more of a buzz-phrase than concrete guidance.

  

The React docs themselves have a nice [Thinking In React](https://reactjs.org/docs/thinking-in-react.html) section which is worth checking out - but the short of it is that you should make your components small enough so they are maintainable and serve one specific purpose.