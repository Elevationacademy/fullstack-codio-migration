## Morse Code



Did you know that Morse code is a binary search tree, based on the inverse frequency of letters in the English language? Take a look!

  

![](https://upload.wikimedia.org/wikipedia/commons/1/19/Morse-code-tree.svg)

  

![](https://hrexach.files.wordpress.com/2015/07/morse.jpg)

  

Every edge to a `leftChild` is a dot, and every edge to a `rightChild` is a dash. So the path to a letter determines the dots and dashes it is made up of! So cool!

  

For this exercise, we've provided a morse code tree for you - [**fork it from here**](https://github.com/Elevationacademy/morse-code-student)

  

Each node here has both a value and a score - since the tree is not built alphabetically, you'll need to use the score to determine if the new value is greater than or less than the score of the current node.

  

You need to **write a method** **`translateWord`** which records the path taken to get to each letter with dots, for `leftChildand` dashes for `rightChild`, to translate words from English to Morse code. **Separate each letter with a space, and each word with a "/"**

  

You need to translate the following phrases to Morse code:

```
morseCode.translateWord("welcome") // should print .-- . .-.. -.-. --- -- . 

morseCode.translateWord("elevation is cool") // should print . .-.. . ...- .- - .. --- -. /.. ... /-.-. --- --- .-.. 
```
  

Then, write a `translateMorse` method which takes Morse code and returns the English words or phrases.

  
```
morseCode.translateMorse("... --- ...")

morseCode.translateMorse("-. .. -.-. . / .--- --- -... / --- -. / - .... . / .-.. . ... ... --- -.")
```
  

![](https://media.giphy.com/media/DJ1r80Q1fyn7O/giphy.gif)