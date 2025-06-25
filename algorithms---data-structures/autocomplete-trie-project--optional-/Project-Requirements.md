
For this project you'll need to create an `AutoCompleteTrie` class. Your class should have the following:

  

-   Properties
    -   A `value`
    -   A `children` **object**
    -   an `endOfWord` flag
-   Methods
    -   An `addWord` method
        -   This method should receive a word
        -   The method should make a node of each letter in the word as a child of the previous letter in the word
        -   If the word or combination of letters already exists, it should add onto the word
        -   For example, if you insert the word "running" into your tree and then insert the word "run", no new nodes will be created, but the first "n" node's `endOfWord` `flag` will be true
        -   Additionally, if you add "runs" to your trie, only an "s" node will be added.
    -   A `findWord` method
        -   This method receives a word
        -   This method should check if a word exists in the trie and return `true` or `false` accordingly
    -   A `predictWord` method
        -   This method should receive the beginning of a word
        -   The method should first find the last spot on the trie
        -   Then, the method should collect all possible word prefixes
        -   Finally, it will add them to the word prefix, and return an array of the possible autocompleted words
    -   Any other helper methods you want to make

  

#### **PROJECT (AUTO)COMPLETED!**